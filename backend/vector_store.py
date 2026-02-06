from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/agri_data.txt", "r", encoding="utf-8") as f:
    docs = f.readlines()

embeddings = model.encode(docs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

def search(query):
    q_emb = model.encode([query])
    _, idx = index.search(q_emb, 1)
    return docs[idx[0][0]]
