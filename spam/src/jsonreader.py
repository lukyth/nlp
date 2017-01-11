import json
import parse
import re
from collections import Counter

def listMail():
	s = open('../trec07p/partial/index','r').read()
	s = s.split('\n')
	check = []
	for i in s:
		if re.match('^[S,s].*',i):
			check.append('spam')
		if re.match('^[H,h].*',i):
			check.append('ham')
	return check

def create_header():
	print ("@relation Spamham")

	print ("@attribute \"Class\" {'spam', 'ham'}")

	print ("@data")

create_header()

check = listMail()
cnt = Counter()
all_spam = 0
all_ham = 0

for i in range(1,2):

	path = '../JSON/inmail.'+str(i)+'.json'
	with open(path) as textj_file:
		textj = json.load(textj_file)
	try:
		textj['html'] = re.sub('<[B,b][R,r]>' , ' ', textj['html'])
		cnt,all_ham,all_spam = parse.lem_parse(textj['html'],cnt,check[i-1],all_ham,all_spam)
		print (cnt)
	except KeyError:
		textj['html'] = re.sub('<[B,b][R,r]>' , ' ', textj['html'])
		cnt,all_ham,all_spam = parse.lem_parse(textj['html'],cnt,check[i-1],all_ham,all_spam)
	finally:
		pass

