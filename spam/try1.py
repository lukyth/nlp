import json
import parse
import re
from collections import Counter

def listMail():
	s = open('C:/NLP/3mail/trec07p/partial/index','r').read()
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

for i in range(13,14):

	path = 'C:/NLP/3mail/trec07p/json/JSON/inmail.'+str(i)+'.json'
	with open(path) as textj_file:
		textj = json.load(textj_file)
	try:
		# print (textj['from'][0]['address']+',\"'+check[i-1]+'\"')
		print (1)
	except KeyError:
		# print (textj['from'][0]['address']+',\"'+check[i-1]+'\"')
		print (2)
	finally:
		pass

