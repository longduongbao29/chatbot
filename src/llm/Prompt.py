from langchain_core.prompts import ChatPromptTemplate
default_prompt = """
You are a helpful assistant. 
Reply user input.
Input: {input}"""

DEFAULT = ChatPromptTemplate.from_template(
        template=default_prompt,
    )