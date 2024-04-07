import streamlit as st
import ollama
import sys
import chromadb
from utilities import getconfig
import os

os.environ["OLLAMA_HOST"] = "192.168.178.39"

# Lade Konfigurationen
embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]

# Verbindung zu ChromaDB herstellen
chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection("buildragwithpython")

# Streamlit
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Wie kann ich helfen ?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Eingabeaufforderung anzeigen und verarbeiten
if prompt := st.chat_input("Wie kann ich helfen ?"):
    # Skript für Fragestellung und Antwortgenerierung
    queryembed = ollama.embeddings(model=embedmodel, prompt=prompt)['embedding']
    relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)["documents"][0]
    docs = "\n\n".join(relevantdocs)
    modelquery = f"{prompt} - Beantworte die Frage nur auf deutsch nutze den folgenden Text als eine Quelle {docs}"
    stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)

    # Antworten anzeigen
    #for chunk in stream:
    #    print(chunk)
    #    if chunk["response"]:
    #        result = chunk['response']
    st.chat_message("assistant").write(stream)
    

    
    # Eingabe der Benutzer hinzufügen
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)