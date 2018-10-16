import nltk

def seperate_hashtags(hashtag_list, word_list):
    for tag in hashtag_list:
        s = ''
        result = maxmatch(tag, word_list)
        for token in result:
            s += token + ' '
        print ('{} -> {}'.format(tag, s))

def maxmatch(tag, wordlist):
    start = 0
    words = []
    while(start < len(tag)):
        match = False
        for i in range(len(tag), start,-1):
            if tag[start : i] in wordlist:
                match = True
                words.append(tag[start: i])
                start = i
                break
        if not match:
            words.append(tag[start])
            start += 1
    return words

hashtag_list = ['#computerscience', '#bigbangtheroy', '#thethe', '#breakingbad', '#governmentshutdown', '#gameofthrones']
NLTKdict = nltk.corpus.words.words()
word_list = []
with open('./word_list.txt') as f:
    data = f.read()
    word_list = data.split('\n')
with open('/usr/share/dict/words') as file:
    linux_dict = file.read().split('\n')
print('---------------Using NLTK words--------')
seperate_hashtags(hashtag_list, NLTKdict)
print('---------------Using lexicon from a company--------')
seperate_hashtags(hashtag_list, word_list)
print('---------------Using Linux Dict----------')
seperate_hashtags(hashtag_list, linux_dict)
