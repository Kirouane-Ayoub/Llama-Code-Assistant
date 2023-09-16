from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain import PromptTemplate

#load the model
llm = CTransformers(
    model = "codellama-34b-instruct.Q4_K_M.gguf",
    config={'max_new_tokens':1024,"temperature":0.4}
)

#create template
prompt_template = """
You are an Expert AI Coding Assistant tasked with solving coding problems 
and providing code snippets based on the user's query.
Query: {query}

Here's a helpful code snippet:
"""
prompt = PromptTemplate(template=prompt_template,input_variables=['query'])
chain = LLMChain(prompt=prompt ,llm=llm)

def run(query) : 
    return chain.run({'query':query})