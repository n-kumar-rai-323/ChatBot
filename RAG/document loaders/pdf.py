from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

loader = PyPDFLoader(
    r"C:\Users\DevOps\Desktop\AI\RAG\document loaders\document.pdf"
)

docs = loader.load()

print(f"Total Pages: {len(docs)}")

for page in docs:
    print(page.page_content[:500])