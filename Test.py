import NumericalFeatureExtractor as nfe
import PosTagging as pt
from LinearRegression import LinearRegression 

x = nfe.getAvgWrdLength()
y = nfe.vocabError()
z = nfe.getWordCount()

r = x+y+z

lr = LinearRegression()
mat = lr.buildFeatureMatrix(r)
print mat
