#! /usr/bin/python3
# Nate Levy, Alan Sato
# Sentence Probablility Finder 


def preprocess(str):
    str = str.lower()
    words = str.split()
    
    u = get_unigrams(words)
    b = get_bigrams(words)

    return u, b

def get_unigrams(words):
    print("Creating unigrams...")
    total_uni = 0
    unigrams = {}
    
    for w in words:
        total_uni += 1
        if w in unigrams.keys:
            unigrams[w] += 1
        else: 
            unigrams[w] = 1
            
    #convert from count to probability 
    for u in unigrams:
        u.value = u.value/total_uni
    
    return unigrams
    
def get_bigrams(words):
    print("Creating bigrams...")
    total_bi = 0
    bigram_dump = {}
    prev_word = "<s>"
    for w in words:
        total_bi += 1
        bigram_dump[prev_word].append(w)
        prev_word = w
        
    #convert this bigram dump to a matrix of words, with bigram prob stored
    w1 = []
    for i in bigram_dump:
        bigram_mtx.append[i]
        
    return bigram_dump

def main():
    print("Welcome to the Uni-Bigram creaotr!")
    og_text = input("Enter file name")
    grams = preprocess(og_text)
    
main()