import os
class Config():
    
    #ELASTIC
    ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY","")
    ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT","https://es01:9200")
    ELASTIC_CERT_PATH = os.getenv("ELASTIC_CERT_PATH","")
    ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME","elastic")
    ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD","")
    
    #MILVUS
    MILVUS_URI = os.getenv("MILVUS_URI","http://localhost:19530")
    MILVUS_TOKEN = os.getenv("MILVUS_TOKEN","root:Milvus")
    MILVUS_DB_NAME = os.getenv("MILVUS_DB_NAME","chatbot_db")
    
    #GROQ
    GROQ_API_KEY = os.getenv("GROQ_API_KEY","")
    GROQ_MODEL_NAME = os.getenv("MODEL_NAME","llama-3.3-70b-versatile")
    GROQ_TEMPERATURE = os.getenv("TEMPERATURE",0.5)
    
    #EMBEDDING
    EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME","sentence-transformers/all-mpnet-base-v2")

    #OPENAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")
    OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME","gpt-4o-mini")
    OPENAI_MODEL_TEMPERATURE = os.getenv("OPENAI_MODEL_TEMPERATURE",0.7)
    OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

    EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", 768))
config = Config()