import pickle
import pth
import pan_util as pu
import pan_dict as pd
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


def create_feature1(p1, p2, p3, p4):
  # feature 1 refers to the simple word based feature
  # computed based on simple distance measures
  # -- probably next we can try better features.
  # parameter 1 = .01 --- see how the classification goes.
  #p1 = .01
  # parameter 2 = 200 -- number of words .. from the sorted list..
  #p2 = 200

  f1 = open(pth.ExpDict,'r')
  f2 = open(pth.NonexpDict,'r')

  ExpDict   =pickle.load(f1)
  NonexpDict=pickle.load(f2)

  exp= ExpDict.keys()
  nexp= NonexpDict.keys()
  # work in the script level .. and come back here.
  
  expdiff =[(e,(ExpDict.freq(e)-NonexpDict.freq(e))/(ExpDict.freq(e)+p1)) for e in exp]
  nonexpdiff = [ (n, NonexpDict.freq(n)) for n in nexp ]

  #nonexpdiff= [(n,(NonexpDict.freq(n)-ExpDict.freq(n))/(NonexpDict.freq(n)+p2)) for n in nexp]
  
  expfeat= sorted(expdiff, key=lambda freq: freq[1], reverse=True)
  nonexpfeat= sorted(nonexpdiff, key=lambda freq: freq[1], reverse=True)

  pos = []
  for item in expfeat[:p3]:
    pos.append(item[0])
  
  neg=[]
  for item in nonexpfeat[:p4]:
    neg.append(item[0])
 
  # still one more processing need to be done here.
  return pos, neg

def naive_bayes_classifier(pos , neg):
  #result = False # false ~ non exploiter
  confidence=1
  #f1 = open(pth.ExpDict,'r')
  #f2 = open(pth.NonexpDict,'r')
  #ExpDict   =pickle.load(f1)
  #NonexpDict=pickle.load(f2)
  #exp= ExpDict.keys()[:1000]
  #nexp= NonexpDict.keys()[:1000]
  #msgs = pu.get_msgs_in(conv_id)
  #words = []
  #for msg in msgs:
  #  words+= msg.split()
  #TestFeat = dict([(word,True) for word in words])
  #for word in exp:
  #  PosFeat= (dict((word,True)),'pos')
  #for word in nexp:
  #  NegFeat= (dict((word,True)),'neg')

  PosFeat = [({word :True}, 'pos') for word in pos]
  NegFeat = [({word :True},'neg')for word in neg]

  #print 'feature construction done. off to bayes classf'
  classifier = NaiveBayesClassifier.train( PosFeat + NegFeat )
  
  #result= classifier.classify(TestFeat)
  
  return classifier

def test1(classifier,ls1 , ls2):
  #classifier= naive_bayes_classifier()
  #ls=pu.convs_list_exp()
  
  for i in range(0,20):
    ft = pu.get_words_featureset(ls1[i])
    pb =classifier.prob_classify(ft)
    print pb.prob('pos'), pb.prob('neg')
  #ls2=pu.convs_list_nexp()
  for i in range(0,20):
    ft = pu.get_words_featureset(ls2[i])
    pb=classifier.prob_classify(ft)
    print pb.prob('pos'), pb.prob('neg')

def eval_set(classifier, pos_conv_id, neg_conv_id):
  poscount=0
  for i in range(0,len(pos_conv_id)):
    ft=pu.get_words_featureset(pos_conv_id[i])
    pb=classifier.classify(ft)
    if pb == 'pos':
      poscount+=1
  
  negcount=0
  for i in range(0,len(neg_conv_id)):
    ft=pu.get_words_featureset(neg_conv_id[i])
    pb= classifier.classify(ft)
    if pb == 'neg':
      negcount+=1

  print poscount, len(pos_conv_id)
  print negcount, len(neg_conv_id)



def main():
  # print 'wtf r u doing :P'
  # to update .. from the scrpt .. :)
  
  ls1 = pu.convs_list_exp()
  ls2 = pu.convs_list_nonexp()
  pos, neg = create_feature1(.01,.01,500,500)
  classifier = naive_bayes_classifier(pos,neg)
  eval_set(classifier, ls1 , ls2)
  
if __name__ == '__main__':
  main()
  
