from fastapi import FastAPI

app = FastAPI()

from langchain_community.document_loaders import SeleniumURLLoader
urls = ["https://www.churchofjesuschrist.org/study/manual/general-handbook/"]

loader = SeleniumURLLoader(urls=urls)

data = loader.load()
print (data)
#urls = ["https://www.centrayasa.com"]
#loader = AsyncChromiumLoader(urls)
#docs = loader.load()
#print(docs[0].page_content[0:100])


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI 8!"}