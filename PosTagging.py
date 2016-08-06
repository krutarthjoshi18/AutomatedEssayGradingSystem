import nltk
import xlrd
import collections

def getEssays():
    print "Getting Essays..."
    workbook = xlrd.open_workbook("training_set_rel3.xls","rU")
    essays = []
    sheet = workbook.sheet_by_name("training_set")
    entry = sheet.col_values(2, start_rowx = 2,end_rowx = 50)
    for i in range(len(entry)):
        tempString = ""
        tempString = entry[i].encode("ascii","ignore")
        essays.append(tempString)
    return essays


def makeTokens(essay):
    tokens = nltk.wordpunct_tokenize(essay)
    return tokens


def tokenizedEssays():
    print "Tokenizing Essays..."
    essays = getEssays()
    tokenizedEssays = [None]*len(essays)
    for i in range(len(essays)-1):
        tokenizedEssays[i] = makeTokens(essays[i])

    return tokenizedEssays

def postag():
    print "postagging"
    tokens= tokenizedEssays()
    posTagged = [None]*len(tokens)
    for i in range(len(tokens)-1):
        print"done"
        posTagged[i] = nltk.pos_tag(tokens[i])

    return posTagged

def getCounts():
    posTaggedWords = postag()
    nounCount = []
    adjectiveCount = []
    adverbCount = []
    verbCount = []
    otherCount = []
    for i in range(len(posTaggedWords)-1):
        aC, nC, adC, vC, oC = [0]*5
        for j in range(len(posTaggedWords[i])-1):            
            if (posTaggedWords[i][j][1] in ["JJ","JJR","JJS"]):
                print posTaggedWords[i][j][1]
                aC+=1
            elif (posTaggedWords[i][j][1] in ["NN","NNS","NNP","NNPS"]):
                nC +=1
            elif (posTaggedWords[i][j][1] in ["RB","RBR","RBS"]):
                adC +=1
            elif (posTaggedWords[i][j][1] in ["VB","VBD","VBG","VBN","VBP","VBZ"]):
                vC +=1
            elif (posTaggedWords[i][j][1] in ["FW"]):
                oC +=1
        adjectiveCount.append(aC)
        nounCount.append(nC)
        adverbCount.append(adC)
        verbCount.append(vC)
        otherCount.append(oC)
        
    return adjectiveCount,nounCount,adverbCount,verbCount,otherCount

##def getCount():
##    from collections import Counter
##    posTaggedWords = postag()
##    print len(posTaggedWords)
##    for i in range(len(posTaggedWords)-1):
##        counts = Counter(tag for word,tag in posTaggedWords[i])
##    print len(counts)
##    print type(counts)
##    return counts
##
countSet = getCounts()
