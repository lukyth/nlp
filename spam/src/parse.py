import lemma
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
	return TAG_RE.sub('', text)
# def lem_parse(data):
# 	pass
def lem_parse(text,cnt,check,all_ham,all_spam):
	content = remove_tags(text)
	x,all_ham,all_spam =  lemma.data(content,cnt,check,all_ham,all_spam)
	return (x,all_ham,all_spam)