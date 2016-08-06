import nltk

string = 'He said,"something!" and ran away'
m = nltk.wordpunct_tokenize(string)
print m
r=[]
punctList = [".",",",":",";","/","?","[","]","{","}","!","@","#","$","%","^","*","(",")",',"','?"','."','"']
r =[w for w in m if w.lower() not in punctList]
