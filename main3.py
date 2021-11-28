import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
f = open("computer-science.txt", encoding="mbcs")
r = open("result.txt", "a")

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
    tagged = nltk.pos_tag(tokens)
    n1 = 0
    v = 0
    n2 = 0
    for i in tagged:
        if i[1] in ["NN", "NNS", "NNP", "NNPS"]:
            if n1 == 0:
                n1 = 1
            else:
                if v == 1:
                    n2 = 1
        else:
            if i[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"] and n1 == 1:
                v = 1
    if tokens != [] and n1 == 1 and v == 1 and n2 == 1:
        r.write(s + "\n")