import glob
from operator import itemgetter, attrgetter 
files = glob.glob("docs/*.txt")
docs = []
Posting_list = {}

#Step 1
def ReadFiles():	
	global docs 
	for x in xrange(0,len(files)):
		file = open(files[x], 'r')
		line = file.read().split('\t')
		for y in range(0,len(line)):
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

def GetMatchedDoc(PostingDict):
	temp = []
	for index in PostingDict:
		temp.append(PostingDict[index])
	my_sets = map(set, temp)
	common_items = set.intersection(*my_sets)
	matched = list(common_items)
	for doc in matched:
		print "File number " + str(doc) + " Is matched doc whic is located at " + files[doc]


def HandelQuery(query):
	result = {}
	MatchedDocs = []
	for x in xrange(0,len(query)):
		query[x] = query[x].lower()
		result[query[x]] = GetPostingList(query[x])
	print result
	GetMatchedDoc(result)
	
def StartProgram():
	ReadFiles()
	HandleTokens()
	PostingList()
	query = raw_input("Enter Your Query: ")
	query = query.split(' ')
	HandelQuery(query)

StartProgram()