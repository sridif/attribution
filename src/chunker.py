import elementtree.ElementTree as ET
import pickle

DATA_PATH= '/NOBACKUP/elango/attribution/data/pan_train/'
convs = ET.parse(DATA_PATH +'sexual-predator-identification-pan12-train-2012-05-01.xml')
'''
file=open(Convs.pkl,'r')
pickle.load('Convs.pkl')
file.close()
'''
convsRT = convs.getroot()

file = open(DATA_PATH+ 'sexual-predator-identification-pan12-train-predators-2012-05-01.txt','r')
#file=open('small_data','r');
predator=[]
for line in file:
  predator.append(line)
file.close()
conv_dict={}
count = 0
for conv in convsRT:
  count += 1
  if count == 10:
    break
  safe=1
  authors = []
  state= False
  for msg in conv:
    author=msg[0].text
    if author not in authors:
      authors.append(author)
    
    if predator.count(author)>0 :
      state=True
  conv_dict[conv.get('id')] = [authors, state] 
  
output = open('conv_dict.pkl', 'wb')
pickle.dump(conv_dict, output)

'''   
    if(predator.count(author)>0):
      msg[0].set('exploiter','true')
      safe=0
    else:
      msg[0].set('exploiter','false')
    name=conv.get('id');
    if(safe==1):
      name+='_noexp.xml'
    else:
      name+='_exp.xml'	
  ET.ElementTree(conv).write(name)
	
#convs.write('out.xml')i
'''
