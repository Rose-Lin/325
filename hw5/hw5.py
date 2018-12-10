import nltk
from nltk.corpus import brown

def CFG(sentences):
    brown_tagged = brown.tagged_words( tagset='universal')
    grammar1 = nltk.CFG.fromstring(
    """
    S -> NP VP| VP | Aux NP VP |VP NP NP
    NP -> N | Det N | Det N PP | "I" | PRON | PRT NP 
    VP -> V | V NP | V NP PP | V ADJ
    PP -> P NP
    V -> "saw" | "ate" |"is"|"has"|"swims"|"flies"|"are"|"have"|"bite"|"fly"|"walks"|"walk"|"bites"|"does"| "Is"|"swim"
    Aux -> "Does"
    Det -> "a" | "the" | "an" |"A" | "This"
    N -> "man" | "dog" |"telescope" | "park" | "fish" | "animal"|"bird"|"gills"|"animals"|"Mammals"|"mammals"|"Humans"|"human"|"Socrates"|"Deepak"|"Dogs"|"dogs"|"Collies"|"collie"|"Rover"|"Beagles"|"beagle"|"Snoopy"|"Birds"|"Canaries"|"Tweety"|"canary" |"Parrots"|"Polly"|"parrot"|"hair"|"birds"|"canines"|"feathers"|"bites"
    P -> "in" | "under" | "with"
    ADJ -> "biped"
    PRON -> "Who"|"What"|"who"|"what"
    PRT -> "all"
    """)
    for sentence in sentences:
        sent = nltk.word_tokenize(sentence[:-1])
        parser = nltk.RecursiveDescentParser(grammar1)
        for p in parser.parse_all(sent):
            print(p)

with open('sen.txt') as file:
    sentences = file.read().strip().split('\n')

CFG(sentences)
