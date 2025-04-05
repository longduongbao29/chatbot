from re import search
from injector import inject
from langchain_core.tools.base import BaseTool
from src.utils.Document import Document
from src.database.DbManager import DbManager
from src.rag.strategy.retrieval.Types import SearchStrategy
from src.rag.strategy.retrieval.VectorSearch import VectorSearch

class ElasticVectorSearch(VectorSearch):
    """
    Elastic vector search strategy for document retrieval.
    """
    @inject
    def __init__(self, db_manager:DbManager):
        self.db_manager = db_manager
    
    def get_documents(self, doc_dict:list[dict])-> list[Document]:
        """
        Convert a list of dictionaries to a list of Document objects.
        """
        docs = []
        for doc in doc_dict:
            docs.append(Document(id=doc["_source"]["id"], content=doc["_source"]["content"], score=doc["_score"]))
        return docs
    def retrieve(self, index:str, query:str, search_type: SearchStrategy = SearchStrategy.HYBRID, num_results:int=5)-> list[Document]:
        """
        Retrieve documents based on the query.
        """
        # Implement the retrieval logic using Elasticsearch
        if search_type == SearchStrategy.FULL_TEXT:
            search_results = self.db_manager.fulltext_search(index,query)
            docs_results = []
            for doc in search_results:
                docs_results.append(Document(id=doc["_source"]["id"], content=doc["_source"]["content"], score=doc["_score"]))
            return docs_results
        elif search_type == SearchStrategy.SEMANTIC:
            search_results = self.db_manager.semantic_search(index,query)
            docs_results = []
            for doc in search_results:
                docs_results.append(Document(id=doc["_source"]["id"], content=doc["_source"]["content"], score=doc["_score"]))
            return docs_results
        elif search_type == SearchStrategy.HYBRID:
            # Implement hybrid search logic
            fulltext_results = self.get_documents(self.db_manager.fulltext_search(index,query))
            semantic_results = self.get_documents(self.db_manager.semantic_search(index,query))
            # Combine results from both searches
            docs_results = self.rerank([fulltext_results, semantic_results])

            return docs_results[:num_results]
    
        
class ElasticSearchTool(BaseTool):
    
    name:str = "elastic_search"
    description:str = "Search information from Elastic database"
    elastic_vector_search:ElasticVectorSearch = None
    @inject
    def __init__(self, elastic_vector_serach: ElasticVectorSearch):
        super().__init__()
        self.elastic_vector_search = elastic_vector_serach
    def _run(self, **args):
        index = args["index"]
        query: str = args["query"]
        translated_queries:list = args["translated_queries"]
        search_type = args.get("search_type", SearchStrategy.HYBRID)
        num_results = args.get("num_results", 5)
        
        queries:list = [query] + translated_queries
        docs_retrieved = []
        for q in queries:
            docs_retrieved.append(self.elastic_vector_search.retrieve(index=index,
                             query=q,
                             search_type=search_type,
                             num_results=num_results))
        rerank_docs = self.elastic_vector_search.rerank(docs_retrieved)[:num_results]
        context = "\n".join([doc.content for doc in rerank_docs])
        return context