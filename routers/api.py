from langchain_ollama import ChatOllama
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/invoke")
async def invoke(prompt: str, temperature: float = 0, model: str = "llama3.1:70b"):
    llm = ChatOllama(
        model=model,
        temperature=temperature
    )
    try:
        return llm.invoke(prompt).content
    except Exception as e:
        HTTPException(500, f"{e}")