#! /usr/bin/python3
# Nate Levy, Alan Sato
# Sentence Probablility Finder

def preprocess(str):
    str = str.lower()
    words = str.split()
    words.append("</s>")

    print("Creating unigrams...")
    total_uni = 0
    unigrams = {}
    unigrams["<s>"] = 1

    for w in words:
        total_uni += 1
        if w in unigrams:
            unigrams[w] += 1
        else:
            unigrams[w] = 1
    unigrams["</s>"] = 1

    for u in unigrams: #convert from count to probability
        unigrams[u] = unigrams[u]/total_uni

    print("Creating bigrams...")
    total_bi = 0
    bigs = {}
    prev_word = "<s>"

    for w in words:
        total_bi += 1
        if (prev_word, w) in bigs: #if this is an identified bigram already
            bigs[prev_word, w] += 1
        else:
            bigs[prev_word, w] = 1
        prev_word = w
    bigs[w, "</s>"] = 1

    for b in bigs:
        bigs[b] = bigs[b] / total_bi
        bigs[b] = bigs[b] / unigrams[b[0]]

    return unigrams, bigs

def main():
    print("Welcome to the Uni-Bigram creator!")
    og_text = input("Enter file name: ")
    grams = preprocess(og_text)
    print("pick an option:\n\t1. Search for unigram\n\t2. Search for bigram\n\t3. Sentence Probablility\n\t4. Exit\n")
    op = input()

    while op < 4:
        if op not in range(1,4):
            print("error! Error! ERROR!1 EEEEEERRRRRRROOOOOORRRRRR!!!!\n\tthat's not an option.")
        elif op == 1:
            uni_query = input("Enter a unigram to search")
            unigram_search(uni_query, grams[0])
        elif op == 2:
            bi_query = input("Enter a bigram to search")
            bigram_search(bi_query, grams[1])
        elif op == 3:
            sent_query = input("Enter a sentence to search")

main()
