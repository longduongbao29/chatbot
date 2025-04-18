import os
class Config():
    
    #ELASTIC
    ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY","")
    ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT","https://es01:9200")
    ELASTIC_CERT_PATH = os.getenv("ELASTIC_CERT_PATH","")
    ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME","elastic")
    ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD","")
    
    #GROQ
    GROQ_API_KEY = os.getenv("GROQ_API_KEY","")
    MODEL_NAME = os.getenv("MODEL_NAME","llama-3.3-70b-versatile")
    TEMPERATURE = os.getenv("TEMPERATURE",0.5)
    
    #EMBEDDING
    EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME","sentence-transformers/all-mpnet-base-v2")

config = Config()