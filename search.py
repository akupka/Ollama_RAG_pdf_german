import ollama 
import sys, chromadb
from utilities import getconfig
from langchain_community.llms import Ollama

embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]

chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection("buildragwithpython")

query = " ".join(sys.argv[1:])
queryembed = ollama.embeddings(model=embedmodel, prompt=query)['embedding']


relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)["documents"][0]
docs = "\n\n".join(relevantdocs)
modelquery = f"{query} - Beantworte die Frage nur auf deutsch nutze den folgenden Text als eine Quelle {docs}"

stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)

for chunk in stream:
  if chunk["response"]:
    print(chunk['response'], end='', flush=True)