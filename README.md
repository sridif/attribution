attribution
===========

For anydoubt 

Source folder - 

pth.py : holds the path to training and test files. 
         The git only stores tokenized dictionaries.
         Not the entire xml files given in the website.


pan_util.py: 
         contains utilities to mine the xml train files.
         for example - given a conversation id get all the conversations

pan_alg.py:
         creates a self designed feature set with 4 parameters.
         these parameters were crossvalidated and hard coded in it.
         These features are then used to train a naive bayes classifier.


Results folder - 

         The best result so far is 93 % true positive
                                   25 % true negative


         Scope for improvement - making the features taking into account the frequency when the bayes classifier is being constructed.






