from langchain_ollama import ChatOllama
import requests
import json

llm = ChatOllama(
    model="llama2",
    temperature=0
)

print(llm.invoke("hi").content)