import nltk
import matplotlib.pyplot as plt

def minimum_edit_distance(source, target):
    n = len(source)+1
    m = len(target)+1
    matrix = [[0 for x in range(m)] for y in range(n)]
    for i in range(1, n, 1):
        matrix[i][0] = matrix[i-1][0] + 1
    for j in range(1, m, 1):
        matrix[0][j] = matrix[0][j-1] + 1
    for i in range(1, n, 1):
        for j in range(1, m, 1):
            del_cost = 0
            matrix[i][j] = min((matrix[i-1][j] + 1), (matrix[i][j-1] + 1))
            if not source[i-1] == target[j-1]:
                del_cost = 2
            matrix[i][j] = min((del_cost + matrix[i-1][j-1]), matrix[i][j])
    return matrix[n-1][m-1]

def calculate_WER(distance, correct_length):
    return distance/correct_length

def seperate_hashtags(hashtag_list, word_list, rows, correct_answers):
    WER_list = []
    for tag in hashtag_list:
        s = ''
        maxmatch_result = maxmatch(tag, word_list)
        for token in maxmatch_result:
            s += token + ' '
        rows['#{}'.format(tag)].append(s.strip())
        distance = minimum_edit_distance(s.strip(), correct_answers[tag])
        length = len(correct_answers[tag])
        WER = calculate_WER(distance, length)
        rows['#{}'.format(tag)].append(WER)
        WER_list.append(WER)
    return rows, WER_list

def maxmatch(tag, wordlist):
    """ Maxmatch algorithm"""
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

rows = {}
NLTKdict = nltk.corpus.words.words()
word_list = []
correct_answers = {}
hashtag_list = []

# Extracint words list from NLTK words, Lexicon of a company and Linux Dictionary
with open('testHashtags.txt') as tests:
    hashtag_list = [x.strip() for x in tests.read().strip().split('\n')]
    for hashtag in hashtag_list:
        rows['#{}'.format(hashtag.strip())] = []
with open('./word_list.txt') as f:
    data = f.read()
    word_list = data.lower().split('\n')
with open('/usr/share/dict/words') as file:
    linux_dict = file.read().lower().split('\n')
with open('testWithAnswers.txt') as file:
    data = file.read().strip()
    for line in data.split('\n'):
        seperated_part = line.split(',')[1].strip()
        tag = line.split(',')[0].strip()
        correct_answers[tag] = seperated_part

#Segment the hashtags
WER_lists = []
table = []
id = 1
NLTK_WERs = seperate_hashtags(hashtag_list, NLTKdict, rows, correct_answers)[1]
Company_WERs = seperate_hashtags(hashtag_list, word_list, rows, correct_answers)[1]
Linux_WERs = seperate_hashtags(hashtag_list, linux_dict, rows, correct_answers)[1]
WER_lists.append(NLTK_WERs)
WER_lists.append(Company_WERs)
WER_lists.append(Linux_WERs)

# Constructing the table to be printed out
header = ['id', 'hashtag', 'NLTK words', 'WER', 'Lexicon from a company', 'WER', 'Linux Dictionary', 'WER']
for key, values in rows.items():
    new_row = [key]
    for v in values:
        new_row.append(v)
    table.append(new_row)
for i in range( len(header)):
    if i == 0:
        print("{:2s} ".format(header[i]), end = "")
    elif i == 1 or (i%2 == 0):
        print ("{:30s}".format(header[i]), end = "")
    else:
        print ("{:12s}".format(header[i]), end = "")
print ("\n", end = "")
for line in table:
    print("{:2d} ".format(id), end = "")
    id += 1
    for i in range(len(line)):
        if (not i %2 == 0) or i == 0:
            print ("{:30s}".format(line[i]), end = "")
        else:
            print("{:5.2f}\t".format(float(line[i])), end = "")
    print("\n", end = "")

#calculate the average WER
average_nums = []
for WERS in WER_lists:
    s = sum(WERS)
    average = s/len(WERS)
    average_nums.append(average)
i = 2
for num in average_nums:
    print("Average WER for {} is: {}".format(header[i], num))
    i += 2

#START PLOTTING
X = [i for i  in range(1,len(table)+1)]
plt.plot(X, WER_lists[0], 'ro', X, WER_lists[1], 'bs', X,  WER_lists[2], 'g^')
plt.gca().legend(('NLTK','Company', 'Linux'))
plt.xlabel('hashtag id')
plt.ylabel('WER')
plt.show()

