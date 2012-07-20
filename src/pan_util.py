import elementtree.ElementTree as ET
import pth
import os

def get_predators():
  # reads the text file provided by pan.webis.de and saves it to python list.
  pred_file = open(pth.PredFile,'r')
  predators = []
  for line in pred_file:
    cr = line.rstrip('\n')
    predators.append(cr)
  pred_file.close()
  return predators

def make_smaller_test():
  #Break the large conversation into multiple smaller files-.
  convs = ET.parse(pth.XML_TEST)
  convsRT = convs.getroot()
  for conv in convsRT:
    name_id = conv.get('id')
    name = pth.TEST + name_id + '.xml'
    ET.ElementTree(conv).write(name)

def make_smaller_train():
  #Break the large file into multiple smaller files.
  convs = ET.parse(pth.XML_TRAIN)
  convsRT = convs.getroot()
  for conv in convsRT:
    name_id = conv.get('id')
    name = pth.TRAIN + name_id + '.xml'
    ET.ElementTree(conv).write(name)

  #print 'booyay !'

def is_predator( author):
  # booleajn function .. indicating weather an author is a predator or not.
  predators = get_predators()
  if author in predators:
    return True
  else:
    return False

def get_train_authors_in( conv_id ):
  # break into smaller files.. then come here
  predators = get_predators()
  id_xml = pth.TRAIN + conv_id + '.xml'
  conv = ET.parse(id_xml)
  convRT = conv.getroot()
  authors= []
  for msg in convRT:
    author = msg[0].text
    if author not in authors:
      authors.append(author)
  return authors

def get_test_authors_in( conv_id ):
  # break into smaller files.. then come here
  predators = get_predators()
  id_xml = pth.TEST + conv_id + '.xml'
  conv = ET.parse(id_xml)
  convRT = conv.getroot()
  authors= []
  for msg in convRT:
    author = msg[0].text
    if author not in authors:
      authors.append(author)
  return authors

def get_num_lines(conv_id):
  id_xml = pth.TRAIN + conv_id + '.xml'
  conv= ET.parse(id_xml)
  convRT = conv.getroot()
  return len(convRT)
    

  


def get_conv_len_train(conv_id):
  # given a conversation id ... get the length of the conversation 
  length =0
  id_xml = pth.TRAIN + conv_id + '.xml'
  conv = ET.parse(id_xml)
  convRT = conv.getroot()
  return len(convRT)

def get_conv_len_test(conv_id):
  length =0
  id_xml = pth.TEST + conv_id + '.xml'
  conv = ET.parse(id_xml)
  convRT = conv.getroot()
  return len(convRT)

def convs_list_test():
  test_dir = os.listdir(pth.TEST)
  conv_ids=[]
  for name in test_dir:
    if 'xml' in name:
      spt = name.split('.')
      conv_ids.append(spt[0])
  return conv_ids   
  
def convs_list_train():
  train_dir = os.listdir(pth.TRAIN)
  conv_ids=[]
  for name in train_dir:
    if 'xml' in name:
      spt = name.split('.')
      conv_ids.append(spt[0])
  return conv_ids

def convs_list_exp():
  convs = convs_list_train()
  exps = []
  predators=get_predators()
  for conv in convs:
    authors = get_train_authors_in(conv)
    ex = False
    for author in authors:
      if author in predators: 
        ex = True
        break
    if ex:
      exps.append(conv)
  return exps


def convs_list_nonexp():
  # also available in pth -EXP_LIST
  # pth.ExpConvs
  # pth.NonexpConvs 
  convs = convs_list_train()
  exps = convs_list_exp()
  nonexps= []
  for conv in convs:
    if conv not in exps:
      nonexps.append(conv)
  return nonexps

def get_msgs_in(conv_id):
  msgs = []
  fl = open(pth.TRAIN + conv_id +'.xml')
  conv = ET.parse(fl)
  convRT = conv.getroot()
  
  for msg in convRT:
    msgs.append(msg[2].text)
    
  return msgs  


def get_words_featureset(conv_id):
  words={}
  fl = open(pth.TEST + conv_id +'.xml')
  conv = ET.parse(fl)
  convRT = conv.getroot()
  
  for msg in convRT:
    text= msg[2].text
    if text is not None:
      ls = text.split()
      for word in ls:   
        words[word]=True
  return words

def get_msg_featureset(msg_line, conv_id):
  words={}
  fl= open(pth.TEST + conv_id + '.xml')
  conv= ET.parse(fl)
  convRT=conv.getroot()
  
  msg= convRT[msg_line]
  text= msg[2].text
  if text is not None:
    ls= text.split()
    for word in ls:
      words[word] = True
  return words

def get_author_in(msg_line, conv_id):
  
  fl= open(pth.TEST + conv_id + '.xml')
  conv=ET.parse(fl)
  convRT = conv.getroot()
  msg = convRT[msg_line]
  author = msg[0].text # change it to attribute extraction and not value
  return author
  
  

def get_msg_tag(msg_line,conv_id):
  fl=open(pth.TEST + conv_id + '.xml')
  conv= ET.parse(fl)
  convRT = conv.getroot()
  msg= convRT[msg_line]
  return msg


def exp(): 
  fl=open(pth.TRAIN + 'd0dfab93d7b5e33eccdb58238d2b08d0' + '.xml')
  fl2= open(pth.TEMP + 'element_tree_test')
  conv= ET.parse(fl)
  convRT = conv.getroot()
  fl2.write(ET.dump(convRT))


  #def get_msg_tag(msg_line,conv_id):
