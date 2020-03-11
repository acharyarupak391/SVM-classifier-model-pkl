#you might need to install the packages before importing them

#pip install pickle
import pickle    
import re
import os
import sys

arg = str(' '.join(sys.argv[1:]))

# pip install nltk
'''
 >> the steps below only need to be implemented
    only if you are working locally (for the first time)
    not for google collab or in kaggle
           - import nltk
           - then run nltk.download_shell()
           - run -> d stopwords
           - run -> d punkt
'''
from nltk.stem import SnowballStemmer    
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

file_path = os.path.dirname(os.path.realpath(__file__))
svm_pkl_path = os.path.join(file_path, 'pkl', 'svm.pkl')
tfidf_pkl_path = os.path.join(file_path, 'pkl', 'tfidf.pkl')

def isnum(string):
    pattern = re.compile('\d')
    matches = []
    for match in pattern.finditer(string):
        matches.append(match.group())
    return matches

def text_preprocess(text):
    rem_mention = ' '.join([word for word in text.split() if '@' not in word])
    rem_punc = ''.join([char.lower() for char in rem_mention if char not in punctuation])
    tokenize = [word for word in word_tokenize(rem_punc) if word not in stopwords.words('english') and len(isnum(word))==0 and len(word)>1]
    sb = SnowballStemmer('english')  
    stem = ' '.join([sb.stem(word) for word in tokenize])
    return stem


with open(svm_pkl_path, 'rb') as f:
    svm_pkl = pickle.load(f)
with open(tfidf_pkl_path, 'rb') as f:
    tfidf_vc_pkl = pickle.load(f)

def run_model(arg=''):
    if(arg==''):
        new_test = str(input('Enter your review: \n'))
    else:
        new_test = arg
        
    new_test = text_preprocess(new_test)
    new_test_tfidf = tfidf_vc_pkl.transform([new_test])
    ans_svm = svm_pkl.predict(new_test_tfidf)[0]
    if(arg != ''):
        print(f'Your review: {arg}\n') 
    print('\n**********************\n')
    if(ans_svm==0):
        print(f'It seems like a bad review.')
    else:
        print(f'looks like a good one!')
    print('\n**********************\n')
    if(arg == ''):
        command = str(input("Press 'r' to enter review again: "))
        if(command.lower()=='r'):
            run_model(arg)
    

run_model(arg)
