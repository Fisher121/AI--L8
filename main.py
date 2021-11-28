import nltk
import lightrdf

doc = lightrdf.RDFDocument("./CSO.3.3.owl")
f = open("result.txt", encoding="mbcs")
sentences = []
cond = 1
while cond == 1:
    l = f.readline()
    if l == '':
        cond = 0
    l = l.replace("\n", "")
    if l != '' and l !=" ":
        sentences += l.split(".")

for s in sentences:
    tokens = nltk.word_tokenize(s)
    count = 0
    for word in tokens:
        for triple in doc.search_triples("https://cso.kmi.open.ac.uk/topics/" + word,None, None):
            count += 1
            break
        if count != 0:
            print(s)
            break
