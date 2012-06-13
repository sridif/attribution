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
  PosFeat = [({word :True}, 'pos') for word in pos]
  NegFeat = [({word :True},'neg')for word in neg]

  #print 'feature construction done. off to bayes classf'
  classifier = NaiveBayesClassifier.train( PosFeat + NegFeat )
  
  #result= classifier.classify(TestFeat)
  
  return classifier


def create_feature2():
  print '-- under construciton --' 
  
def positive_bayes_classifier(feat2):
  print '-- under construction --'


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

'''
def classify_senti(conv_id)
  if pos send distance to the mail machine ..
  
  
  
'''
def result(classifier, conv_ids):
  for i in range(0,len(conv_ids)):
    ft= pu.get_words_featureset(conv_ids[i])
    pb=classifier.classify(ft)
    if pb == 'pos':
      handle_conv(classifier, conv_ids[i])
    


def handle_conv(classifier, conv_id):
  print conv_id
  # get number of lines in conv
  num_lines= pu.get_num_lines(conv_id)
  for i in range(0,num_lines):
    # message 1 is the problem.
    msg= pu.get_msg_featureset(i,conv_id)
    pt= classifier.classify(msg)
    if pt== 'pos':
      handle_msg(1,conv_id)


def handle_msg(msg_line, conv_id):
  author= pu.get_author_in(msg_line, conv_id)
  out_author(author)
  msg= pu.get_msg_tag(msg_line, conv_id)
  out_msg(msg)

  #handle_msg(msg_line,)
  #psuedo -
  #pos_conv_id.xml -> retrieve messages .. -> bayesian.. poisitve sent to output.


authors_file= open(pth.TEMP+'/authors.txt', 'w')
messages_file= open(pth.TEMP+'/messages.txt', 'w')
def out_author(author):
  print author
  authors_file.write(author)

def out_msg(msg):
  #temp = open(pth.TEMP + 'temp.xml',w)
  #save_temp_xml(msg)
  # read tis temp xml file.
  #
  out= pu.ET.dump(msg)
  if out is not None:
    messages_file.write(out)
  print 'booyay'

def init_out_msg():
  #print 'booyay'
  authors_file.write('er .. testing')
  

def end_out_msg():
  #print 'booyay'
  authors_file.close()
  messages_file.close()


def create_classifier_dump():
  ls1 = pu.convs_list_exp()
  ls2 = pu.convs_list_nonexp()
  pos, neg = create_feature1(.01,.01,500,500)
  classifier = naive_bayes_classifier(pos,neg)
  class_file = open(pth.TEMP + '/classifier','w') 
  pickle.dump(classifier, class_file)
  class_file.close()


def june_eleven():
  class_file = open(pth.TEMP + '/classifier','r')
  classifier=pickle.load(class_file)
  ls=pu.convs_list_exp()
  result(classifier,ls[:10])
  
def main():
  #print 
  # to update .. from the scrpt .. 
  #ls1 = pu.convs_list_exp()
  #ls2 = pu.convs_list_nonexp()
  #pos, neg = create_feature1(.01,.01,500,500)
  #classifier = naive_bayes_classifier(pos,neg)
  
  #eval_set(classifier, ls1 ,ls2)
  #result(classifier,ls1)
  print '<conversations>'
  june_eleven()
  print '</conversations>' 
 

if __name__ == '__main__':
  main()
  
