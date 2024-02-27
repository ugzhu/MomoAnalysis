import pysenti

def get_senti_score(text):
    r = pysenti.classify(text)
    return r['score']


