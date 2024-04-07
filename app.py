import streamlit as st
import ollama
import chromadb
from utilities import getconfig
import os

os.environ["OLLAMA_HOST"] = "192.168.178.39"

# Lade Konfigurationen
embedmodel = getconfig()["embedmodel"]
#mainmodel = getconfig()["mainmodel"]

# Verbindung zu ChromaDB herstellen
chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection("buildragwithpython")

st.title("💬 llama2 (7B) Chatbot")
st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["name"] for model in ollama.list()["models"]])
mainmodel=st.session_state.selected_model

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Wie kann ich helfen ?"}]

### Write Message History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

## Generator for Streaming Tokens
def generate_response():
    response = ollama.chat(model=mainmodel, stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input("Wie kann ich helfen ?"):
    queryembed = ollama.embeddings(model=embedmodel, prompt=prompt)['embedding']
    relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)
    doc1 = relevantdocs["documents"][0]
    metadata = relevantdocs["metadatas"][0]
    filename_with_newline = metadata[0]['source'].split('/')[-1]
    filename = filename_with_newline.strip()
    docs = "\n\n".join(doc1)
    modelquery = f"{prompt} - Beantworte die Frage nur auf deutsch nutze den folgenden Text als einzige Quelle {docs} wenn du die Frage nicht beantworten kannst schreibe keine Ahnung"
    #stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)
 

    st.session_state.messages.append({"role": "user", "content": modelquery})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
    st.chat_message("assistant", avatar="🤖").write(f" (Quelle: {filename})")
    st.session_state.messages = [{"role": "assistant", "content": "Wie kann ich helfen?"}]
 