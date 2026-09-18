from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_chunks(folder:Path):
 chunks=[]
 for path in sorted(folder.glob('*.md')):
  for i,p in enumerate(x.strip() for x in path.read_text(encoding='utf-8').split('\n\n') if x.strip()): chunks.append({'source':path.name,'chunk_id':i,'text':p})
 return chunks
class Retriever:
 def __init__(self,folder:Path):
  self.chunks=load_chunks(folder); self.vectorizer=TfidfVectorizer(ngram_range=(1,2),sublinear_tf=True); self.matrix=self.vectorizer.fit_transform([c['text'] for c in self.chunks])
 def search(self,query,top_k=3):
  scores=cosine_similarity(self.vectorizer.transform([query]),self.matrix)[0]; order=scores.argsort()[::-1][:top_k]
  return [{**self.chunks[i],'score':round(float(scores[i]),4)} for i in order if scores[i]>.01]
