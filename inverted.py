import glob
from operator import itemgetter, attrgetter 
files = glob.glob("docs/*.txt")
docs = []
Posting_list = {}
constatnts = ['and' , 'or' , 'not' , ')' , '(']
#Step 1
def ReadFiles():	
	global docs 
	for x in xrange(0,len(files)):
		file = open(files[x], 'r')
		line = file.read().split('\t')
		for y in range(0,len(line)):
			if not (x+1 , line[y].lower()) in docs:
				docs.append((x+1 , line[y].lower()))
			

#Step 2
def HandleTokens():
	global docs
	docs = sorted(docs , key=lambda element: (element[1]))

#Step 3
def PostingList():
	global docs
	for x in xrange(0,len(docs)):
		if docs[x][1] not in Posting_list:
			Posting_list[docs[x][1]] = []
			Posting_list[docs[x][1]].append(docs[x][0])
		if (x + 1) < len(docs):
			if docs[x][1] == docs[x + 1][1]:
				Posting_list[docs[x][1]].append(docs[x + 1][0])		

def GetPostingList(token):
	if token in Posting_list:
		return Posting_list[token]
	return 'Not Found'

def GetFrequency(token):
	if token in Posting_list:
		return len(Posting_list[token])
	return 0

def GetMatchedDoc(query):
	command = ''
	for term in query:
		if term.lower() in constatnts:
			command = command + ' ' + term.lower()
		if term.lower() in Posting_list:
			command = command + ' ' + str(Posting_list[term])
	print eval(command)
	

def HandelQuery(query):
	global constatnts
	result = {}
	MatchedDocs = []
	for x in xrange(0,len(query)):
		if query[x].lower() not in constatnts:
			query[x] = query[x].lower()
			result[query[x]] = GetPostingList(query[x])
	print result
	GetMatchedDoc(query)

def ShowTermsDocument():
	for term in docs:
		for i in Posting_list[term]:
			print Posting_list[i] , i

def StartProgram():
	ReadFiles()
	HandleTokens()
	PostingList()
	#ShowTermsDocument()
	query = raw_input("Enter Your Query: ")
	query = query.split(' ')

	HandelQuery(query)

StartProgram()