from gensim.models import word2vec
from gensim.models import Word2Vec

sentences = word2vec.Text8Corpus("result.txt")
model = Word2Vec(sentences, size=200)
model.save("modle")