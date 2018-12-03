print("    ")
import gensim
#print (dir(gensim))

import io

#file = open('Pranay-Sadarangani-Resume.txt', 'r', encoding = "ISO-8859-1")

file = io.open("Pranay-Sadarangani-Resume.txt", 'r', encoding = "ISO-8859-1")

raw_documents = file.readlines()
file.close()

#raw_documents = [
#                    "PKI/Encryption: PKI, encryption, certificate authentication, LDAP, Active Directory, Open Auth- IDP",
#                    "Identity Access Management (IAM): authN/authZ, identity management, access management"                   
#                ]
              
              
print("Number of documents:",len(raw_documents))

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
#print(dictionary[5])
#print(dictionary.token2id['india'])

print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
    
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)

tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity(  '/Users/pranaysadarangani/test/',
                                        tf_idf[corpus],
                                        num_features=len(dictionary)
)

print(sims)
print(type(sims))


file = io.open("SalesForceJD.txt", 'r', encoding = "ISO-8859-1")
raw_documents = file.readlines()
file.close()


#query_doc = [w.lower() for w in word_tokenize("Proficiency in at least one of the following programming languages: Golang, Java, C++, Python, C# Mastery of OOO concepts and programmingDemonstrated understanding of general Unix/Linux systems (e.g., CentOS, RHEL, Solaris, or similar) DevOps mindset and strong ownership over owned code (test, monitor, deploy, maintain) M.Sc/M.Eng in Computer Science/Engineering or B.A/B.Sc. in same disciplines with the equivalent years of experience.")]


query_doc = [w.lower() for w in word_tokenize(raw_documents.__str__())]

print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
print(query_doc_tf_idf)

sims[query_doc_tf_idf]











    
