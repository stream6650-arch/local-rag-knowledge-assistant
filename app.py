from pathlib import Path
import streamlit as st
from src.retriever import Retriever
st.set_page_config(page_title='Local RAG Demo',page_icon='🔎',layout='wide'); st.title('Local RAG Knowledge Assistant'); st.caption('Document → Retrieve → Grounded Answer | No API key')
@st.cache_resource
def load(): return Retriever(Path(__file__).parent/'knowledge')
r=load(); top_k=st.sidebar.slider('Top-k',1,5,3); q=st.text_input('Ask a question:','What is idempotency in a data pipeline?')
if q:
 hits=r.search(q,top_k)
 if not hits: st.warning('No sufficiently relevant context found. The demo does not guess.')
 else:
  st.subheader('Grounded Answer'); st.write(hits[0]['text']); st.caption(f"Source: {hits[0]['source']} · score {hits[0]['score']}")
  for i,h in enumerate(hits,1):
   with st.expander(f"#{i} {h['source']} · {h['score']}"): st.write(h['text'])
