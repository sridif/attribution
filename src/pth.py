import os

PTH=os.getcwd()
#print PTH
TRAIN = PTH + '/../data/pan_train/'
#print TRAIN
TEST = PTH + '/../data/pan_test/'
TEMP = PTH + '/../data/temp/'
XML_TRAIN = TRAIN + 'sexual-predator-identification-pan12-train-2012-05-01.xlm'
XML_TEST  = TEST  + 'sexual-predator-identification-pan12-test-2012-05-17.xlm'
PredFile = TRAIN + 'sexual-predator-identification-pan12-train-predators-2012-05-01.txt' 
ExpConvs = TRAIN + 'exploiter_list'
NonexpConvs = TRAIN + 'nonexploiter_list'

# depricated dictionries--
#ExpDict = TRAIN + 'expoliter_dictionary'
#NonexpDict = TRAIN + 'nonexploiter_dictionary' 

# new dictionaries ---
# 1. to lower
# 2. one count per document
ExpDict = TRAIN + 'expoliter_dictionary'
NonexpDict = TRAIN + 'nonexploiter_dictionary'
