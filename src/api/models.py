from pydantic import BaseModel, Field

# Model cho tài liệu
class Document(BaseModel):
    title: str
    content: str

# Model cho câu hỏi
class Question(BaseModel):
    query: str

class ModelParams(BaseModel):
    model_name: str
    temperature: float
    
class Record(BaseModel):
    messages: list = Field(
        ...,
        example=[
            {"role": "user", "message": "Hello, how are you?"},
            {"role": "AI", "message": "I'm good, thank you! How can I assist you today?"}
        ]
    )