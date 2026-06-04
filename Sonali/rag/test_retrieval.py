from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# same embedding model used in ingest.py
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# load saved FAISS index
vectorstore = FAISS.load_local(
    "Sonali/vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

# 🔍 similarity search
query = "SOC2 compliance"

results = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc.page_content)