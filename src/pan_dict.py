import pth
import os
import pan_util as pu
import nltk
import pickle

# For experiments like
# 1. chi2 .
# 2. mood .
# 3. The template .
# 4. Distance .
# 5. Pronoun .
# 6. Calcualting chi2 after segmenting per author.
# Other experiments that are non - lang tech
# 10. how many time does an author start conv.
# 11. Number of long conversation ...

def mk_exp_wordfreq():
  #convs= pu.convs_list_train()
  fl = open(pth.ExpConvs,'r')
  exps= pickle.load(fl)

  ExpFreq = nltk.FreqDist()
  
  for conv in exps:
    msgs= pu.get_msgs_in(conv)
    tally=[]
    for msg in msgs:
      #print msg
      if msg is not None:
        words = msg.split()
        for word in words:
          lw= word.lower()
          if lw not in tally:
            tally.append(lw)
            ExpFreq.inc(lw)
  fl = open(pth.ExpDict,'w')
  pickle.dump(ExpFreq,fl)
  # get_all_text --
  #for conv in convs:
  #print 'booyay'

def mk_nonexp_wordfreq():
  #convs= pu.convs_list_train()
  fl = open(pth.NonexpConvs,'r')
  nexps= pu.convs_list_nonexp()
  NonexpFreq = nltk.FreqDist()
  #count = 0
  for conv in nexps:
    msgs= pu.get_msgs_in(conv)
    tally=[]
    for msg in msgs:
      #print msg
      #count +=1
      #if count >3:
      #  break 
      if msg is not None:
        words = msg.split()
        for word in words:
          lw= word.lower()
          if lw not in tally:
            tally.append(lw)
            NonexpFreq.inc(lw)
         
  fl = open(pth.NonexpDict,'w')
  pickle.dump(NonexpFreq,fl)

def mk_train_nonexp_dump():
  print 'er'
  print 'booyay'


def word_freq_exp_conv():
  print 'booyay'   

def word_freq_nonexp_conv():
  print 'booyay'


