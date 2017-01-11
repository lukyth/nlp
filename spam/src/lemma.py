from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import string


def get_wordnet_pos(treebank_tag):
	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	elif treebank_tag.startswith('R'):
		return wordnet.ADV
	else:
		return "no"

def data(data,cnt,check,all_ham,all_spam):
	wordnet_lemmatizer = WordNetLemmatizer()
	tokenizer = RegexpTokenizer(r'\w+')
	text = data
	tokens = tokenizer.tokenize(text)
	tagged = pos_tag(tokens)

	for word,pos in tagged:
		if get_wordnet_pos(pos) != "no":
			real_word = wordnet_lemmatizer.lemmatize(word,get_wordnet_pos(pos))
			real_word = real_word.lower()
			if real_word not in cnt:
				cnt[real_word] = {'ham': 0,'spam':0}
			cnt[real_word][check] +=1

			if check == 'spam':
				all_spam += 1
			if check == 'ham':
				all_ham += 1

	return (cnt,all_ham,all_spam)

