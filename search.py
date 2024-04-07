import ollama 
import sys, chromadb
from utilities import getconfig
#from langchain_community.llms import Ollama

embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]

chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection("buildragwithpython")

query = " ".join(sys.argv[1:])
queryembed = ollama.embeddings(model=embedmodel, prompt=query)['embedding']


relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5,  include=["metadatas","documents"])

doc1 = relevantdocs["documents"][0]
metadata = relevantdocs["metadatas"][0]  # Gehe davon aus, dass Metadaten in der gleichen Reihenfolge zurückgegeben werden

# Zugriff auf den Dateinamen aus den Metadaten
filename_with_newline = metadata[0]['source'].split('/')[-1]
filename = filename_with_newline.strip()

# Nutze `document` und `filename` wie benötigt
#print(doc1)
print(filename)

docs = "\n\n".join(doc1)
modelquery = f"{query} - Beantworte die Frage nur auf deutsch nutze den folgenden Text als eine Quelle {docs}"
print(relevantdocs)
print(filename)
stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)

for chunk in stream:
  if chunk["response"]:
    print(chunk['response'], end='', flush=True)