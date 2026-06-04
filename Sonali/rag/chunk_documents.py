from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_chunks():

    loader = DirectoryLoader(
        "Sonali/company_docs",
        glob="*.txt"
    )

    documents = loader.load()

    print(f"Documents Loaded: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Total Chunks: {len(chunks)}")

    return chunks