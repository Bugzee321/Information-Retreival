from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob

files = glob.glob("docs/*.txt")
documents = []
for x in xrange(0,len(files)):
		file = open(files[x], 'r')
		line = file.read().replace('\t' , ' ')
		documents.append(line)

query = raw_input("Enter Your Query: ")
documents.append(query)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print (tfidf_matrix)

pair = tfidf_matrix.shape
sec = pair[1]

print ("cosine" ,cosine_similarity(tfidf_matrix[-1], tfidf_matrix))
l = len(documents) -1


li =[]
def sim (Doc ) :
    for D in range (0,Doc) :
        n=0.0
        for m in range (0,sec) :
            n += tfidf_matrix[D,m]  *  tfidf_matrix[l,m]
        li.append(n)
    return li

print("sim  ",sim(pair[0]))



    