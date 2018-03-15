# Migos Adlib Injector - Nate Levy
# Input: a string
# Output: a string broken into bars with Mighos-style adlibs interspersed
import random

# vibe_list is a set of ways migos noises can be.
# since I don't know how to be more specific with it, they're chars.
vibe_list = ['$', '?', '!', '/', '~', ';']
#   $ - having money.  
#       sounds: "[sound of a thing reflecting light]", "bands", "[expensive category of object]" 

#   ? - questions.
#       sounds: "where?", "what way?", "who?"

#   ! - action.        
#       sounds: "ya!", "fssshew[fast noise]", "skrrt", "hey!", "swoosh", "[impact noises]", "that way!"

#   / - agression.     
#       sounds: "BITCH!", "[gun noise]", "[cutting word]"

#   ~ - drugs.       
#       sounds: ""white!", "[cigarillo brand]", "[drug name]", "[adjective that can be used to mean high]"

#   ; - bullshit. 
#       sounds: "drip", "splash", "tater-tot", "[bird noise]", "swooce!", "bitch"(infinitive)", "mama"

def migos(str):
    global main_vibes 
    main_vibes = get_vibes(str)
    yell_line = 1 - 0.5 * main_vibes["!"] 
    bars = str_to_bars(str)
    out = ""
    for b in bars:
        adlib = exclaim(b)
        b.lyrics.append(" ({0}".format(adlib))
        #are we gonna shout it?
        if b.vibes['!'] > yell_line:        
            b.lyrics.append("!)")
        else:
            b.lyrics.append(")")
        out.append(b.lyrics()+"\n")
    return out

def str_to_bars(str):
    bars = []
    #run through the string, looking for complete statements, append each to bars as bar object
    return bars

def get_vibes(str):
    vibes = {}
    for v in vibe_list:
        mod = 1
        #analyze the text's correspondance to the vibe, mod +/- depending on score
        vibes[v] = mod
    return vibes

def exclaim(b):
    words = b.split()
    word_vibes = {}
    # 2 possible routes: 
    # #1. check words for sounds, then getvibe(sound)
       
    # #2.   get vibes of each word, generate a sound for top few contenders,
    #       then pick sounds based on vibe relation. this is for ad-libs
    #       generated from words that correlate to the message: ad-libs that 
    #       while more "normal", 
    for w in words:
        
        word_vibes[w] = get_vibes(w)
        max_affinity = 0
        significant_word = "wrow"
        
    for v in word_vibes:
        
        bar_affinity = correlate(word_vibes[v], b.vibes)
        
        if bar_affinity > max_affinity:
            max_affinity = bar_affinity
            significant_word = v
            
    exclamation = associate(significant_word)
    return exclamation
def main():
    ogstr = input()
    culture = migos(ogstr)
    print(culture)
    
class bar:
    def __init__(self, line):
        self.lyrics = line
        self.vibes = get_vibes(self.line)
        
