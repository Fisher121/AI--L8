import lightrdf


parser = lightrdf.Parser()

doc = lightrdf.RDFDocument("./CSO.3.3.owl")

word = input()
for triple in doc.search_triples("https://cso.kmi.open.ac.uk/topics/" + word, "http://cso.kmi.open.ac.uk/schema/cso#superTopicOf", None):
    print(triple)