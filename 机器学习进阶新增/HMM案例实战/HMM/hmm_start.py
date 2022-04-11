#coding=utf-8
print(__doc__)

import numpy as np
import warnings
warnings.filterwarnings("ignore")
#import matplotlib.pyplot as plt

from hmmlearn import hmm
import get_hmm_param as pa

from hmmlearn.hmm import MultinomialHMM as mhmm
startprob=np.array(pa.get_startprob())
print("startprob is ",startprob)
transmat=np.array(pa.get_transmat())
print("transmat is ",transmat)
emissionprob=np.array(pa.get_emissionprob())
print("emmissionprob is ",emissionprob)
mul_hmm=mhmm(n_components=4)

mul_hmm.startprob_=startprob

mul_hmm.transmat_=transmat

mul_hmm.emissionprob_=emissionprob

phase=u"我要吃饭谢天谢地"

X=np.array(pa.get_array_from_phase(phase))
X=X.reshape(len(phase),1)
print("X is ",X)

Y=mul_hmm.predict(X)
print("Y is ",Y)
#{B（词开头），M（词中），E（词尾），S（独字词）} {0,1,2,3}