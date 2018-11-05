import nltk
from nltk.corpus import brown
from nltk.tag import hmm

# What are the 8 most frequent tags?
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
most_common = tag_fd.most_common()[:8]

def find_most_frequent(freqdist, tagname, count):
    result = []
    for word, tag in brown_news_tagged:
        if tag == tagname:
            if word+"/"+tag in ntable.keys():
                freqdist[word+"/"+tag] += 1
            else:
                freqdist[word+"/"+tag] = 1
    for (word_tag, num) in freqdist.most_common()[:count]:
        result.append((num, word_tag))
    return result

# print(brown_news_tagged[0:20])
# What are the 15 most frequent nouns?
# What are the 15 most frequent verbs?
# What are the 15 most frequent adjectives?
# What are the 15 most frequent adverbs?
ntable = nltk.FreqDist()
vtable = nltk.FreqDist()
adjtable = nltk.FreqDist()
advtable = nltk.FreqDist()

freq_noun = find_most_frequent(ntable, 'NOUN', 15)
freq_verb = find_most_frequent(vtable, 'VERB', 15)
freq_adj = find_most_frequent(adjtable, 'ADJ', 15)
freq_adv = find_most_frequent(advtable, 'ADV', 15)
print("15 most frequent nouns: {}\n".format(freq_noun))
print("15 most frequent verbs: {}\n".format(freq_verb))
print("15 most frequent adj: {}\n".format(freq_adj))
print("15 most frequent adv: {}\n".format(freq_adv))
print("----------------------------------")

def tagging_system(text):
    bts = brown.tagged_sents(categories="news", tagset="universal")
    hmmTagr = hmm.HiddenMarkovModelTagger.train(bts)
    tsent = nltk.word_tokenize(text)
    tagged_sent = hmmTagr.tag(tsent)
    print(hmmTagr.evaluate(bts))
    print(tagged_sent)

with open("./text1.txt") as f:
    data = f.read()
tagging_system(data)

# extra credit
patterns = [
    (r'[\.,:;?!]$', '.'), # punctuation
    (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'), # cardinal numbers
    (r'(The|the|A|a|An|an|no|No)$', 'DET'), # articles
    (r'(some|Some|most|Most|every|Every|which|Which)$','DET'),
    (r'(At|at|On|on|Out|out|Over|over|Per|per|That|that|Up|up|Down|down|Into|into|Under|under|By|by|With|with)$', 'PRT'), # articles
    (r'.*able$', 'ADJ'), # adjectives
    (r'(now|Now)$', 'ADJ'),
    (r'.*ous$', 'ADJ'), 
    (r'.*ly$', 'ADV'), # adverbs
    (r'(and|And|or|Or|but|But|if|If|while|While|although|Although)$', 'CONJ'),
    (r'(many|Many|much|Much|such|Such)$', 'ADV'),
    (r'.*ing$', 'VERB'), # gerund
    (r'.*ed$', 'VERB'), # simple past
    (r'.*es$', 'VERB'), # 3rd person singular present
    (r'.*ould$', 'VERB'), # modal
    (r'.*\'s$', 'NOUN'), # possessive noun
    (r'.*$', 'NOUN'), # noun default
    (r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
    (r'.*s$', 'NOUN'), # plural noun
    (r'.*ness$', 'NOUN'), # nouns from adjectives
]
reTagr = nltk.RegexpTagger(patterns)
test_sent = brown.sents(categories='news')[0]
tsent = nltk.word_tokenize(data)
print('-------')
tag_sent = reTagr.tag(tsent)
print(tag_sent)
