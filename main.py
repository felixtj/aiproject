from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    from langchain_community.document_loaders import AsyncChromiumLoader

    urls = ["https://www.centrayasa.com"]
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    print(docs[0].page_content[0:100])
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI 8!"}