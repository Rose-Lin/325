import nltk
from nltk.corpus import brown
from nltk.tag import hmm

# What are the 8 most frequent tags?
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
most_common = tag_fd.most_common()[:8]
print("8 most frequent tags are: {}".format(most_common))


# What are the 15 most frequent nouns?
# What are the 15 most frequent verbs?
# What are the 15 most frequent adjectives?
# What are the 15 most frequent adverbs?=
def find_most_frequent(freqdist, tagname, count):
    result = []
    for (word, tag) in brown_news_tagged:
        if tag == tagname:
            if tag == tagname:   
                freqdist[word+"/"+tag] += 1
    for (word_tag, num) in freqdist.most_common()[:count]:
        result.append((num, word_tag))
    return result

ntable = nltk.FreqDist()
vtable = nltk.FreqDist()
adjtable = nltk.FreqDist()
advtable = nltk.FreqDist()

freq_noun = find_most_frequent(ntable, 'NOUN', 15)
freq_verb = find_most_frequent(vtable, 'VERB', 15)
freq_adj = find_most_frequent(adjtable, 'ADJ', 15)
freq_adv = find_most_frequent(advtable, 'ADV', 15)
print("15 most frequent nouns:")
for pair in freq_noun:
    print('{} appears {} times'.format(pair[1], pair[0]))
print("----------------------------------")
print("15 most frequent verbs: ")
for vpair in freq_verb:
    print('{} appears {} times'.format(vpair[1],vpair[0]))
print("----------------------------------")
print("15 most frequent adj: ")
for pair in freq_adj:
    print('{} appears {} times'.format(pair[1],pair[0]))
print("----------------------------------")
print("15 most frequent adv: ")
for pair in freq_adv:
    print('{} appears {} times'.format(pair[1],pair[0]))
print("----------------------------------")

# Tagging system
def tagging_system(text, name):
    bts = brown.tagged_sents(categories="news", tagset="universal")
    # train hmmtagr on all bts and use hmmtagger to evaluate the result of unigramTagger
    hmmTagr = hmm.HiddenMarkovModelTagger.train(bts)
    uTagr = nltk.UnigramTagger(bts)
    tsent = nltk.word_tokenize(text)
    tagged_sent = [uTagr.tag(tsent)]
    # print out the accuracy and the tagged text
    if name == 'my_test.txt' or name == 'my_test1.txt':
        print("the accuracy of {} is :{}".format(name,hmmTagr.evaluate(tagged_sent)))
    print("------Below is the outcome of UnigramTagging of text: {}------".format(name))
    print(tagged_sent[0])

with open("./text1.txt") as f:
    data1 = f.read()
with open("./text2.txt") as f:
    data2 = f.read()
with open("./my_test.txt") as f:
    my_data1 = f.read()
with open('./my_test1.txt') as f:
    my_data2 = f.read()
tagging_system(data1, 'text1.txt')
tagging_system(data2, 'text2.txt')
tagging_system(my_data1, 'my_test.txt')
tagging_system(my_data2, 'my_test1.txt')

# extra credit
patterns = [
    (r'[\.,:;?!]$', '.'), # punctuation
    (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'), # cardinal numbers
    (r'(The|the|A|a|An|an|no|No)$', 'DET'), # articles
    (r'(some|Some|most|Most|every|Every|which|Which|who|Who)$','DET'),
    (r'(onto|Onto|At|at|On|on|Out|out|Over|over|Up|up|Down|down|Into|into|Under|under|By|by|With|with)$', 'PRT'), # articles
    (r'(Per|per|That|that)$', 'PRT'),
    (r'(of|Of|from|From)$', 'ADP'),
    (r'.*able$', 'ADJ'), # adjectives
    (r'(now|Now|still|Still|biped)$', 'ADJ'),
    (r'(Polly)$', 'NOUN'),
    (r'.*ous$', 'ADJ'), 
    (r'(and|And|or|Or|but|But|if|If|while|While|although|Although)$', 'CONJ'),
    (r'(many|Many|much|Much|such|Such)$', 'ADV'),
    (r'(engineering)$','NOUN'),
    (r'(is|was|were|are|Is|Was|Were|Are|have|Have|has|Has|had|Had)$', 'VERB'),
    (r'(play|Play|transcend|swims|bite|fly|walk|walks)$','VERB'), 
    (r'(Socrates|Collies|Beagles|Canaries)$', 'NOUN'),
    (r'.*ly$', 'ADV'), # adverbs
    (r'.*es$', 'VERB'), # 3rd person singular present
    (r'.*ould$', 'VERB'), # modal
    (r'.*ing$', 'VERB'), # gerund
    (r'.*ed$', 'VERB'), # simple past
    (r'.*\'s$', 'NOUN'), # possessive noun
    (r'(He|he|His|his|She|she|Her|her|It|it|its|Its|I|me|Me|my|My|You|you|your|Your|Our|our|us|Us|We|we|they|They|their|Their|them|Them)$', 'PRON'), # pronouns
    (r',*ary$', 'ADJ'),
    (r'.*s$', 'NOUN'), # plural noun
    (r'.*ness$', 'NOUN'), # nouns from adjectives
    (r'.*$', 'NOUN'), # noun default
]
reTagr = nltk.RegexpTagger(patterns)
test_sent = brown.sents(categories='news')[0]
tsent = nltk.word_tokenize(data1)
print('---------Extra credit--------')
tag_sent = reTagr.tag(tsent)
print("------Below is the outcome of regular expression tagger of text: {}------".format('text1.txt'))
print(tag_sent)
tsent = nltk.word_tokenize(data2)
tag_sent = reTagr.tag(tsent)
print("------Below is the outcome of regular expression tagger of text: {}------".format('text2.txt'))
print(tag_sent)