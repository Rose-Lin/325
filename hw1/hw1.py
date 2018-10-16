import nltk
import re
from nltk.book import *
from urllib import request

def lexical_diversity(text):
    return (len(set(text)) / len(text))

def percentage_use(word, words):
    # create a list of all words only
    total_words = len([w for w in text if re.search('\w+',w)])
    occur = words.tokens.count(word)
    return (occur / total_words)

def find_un_prefix():
    wordlist = nltk.corpus.words.words("en")
    # finding un or Un prefix
    un_prefix = [x for x in wordlist if re.search('[uU]n.+', x)]
    return len(un_prefix)

def extract_office_hour():
    url = "http://cs.brynmawr.edu/Courses/cs325/fall2018/index.html"
    response = request.urlopen(url)
    raw_html = response.read().decode('utf8')
    office_hour = re.search('Office.*Hours.*\n', raw_html).group(0)
    # eliminate '</strong>'
    valid_content = re.sub('</?strong>', '', office_hour)
    # eliminate '<br clear='all'>' and newline
    valid_content = re.sub('<.*>\r\n', '', valid_content)
    return valid_content

def get_weather():
    url = "http://w1.weather.gov/xml/current_obs/display.php?stid=KPHL"
    response = request.urlopen(url)
    raw_html = response.read().decode('utf8')
    weather = re.search('<weather>.*</weather>', raw_html)
    # eliminate '</*weather>'
    valid_weather = re.sub('</?weather>',  '', weather.group(0))
    temp = re.search('<temperature_string>.*</temperature_string>', raw_html)
    # eliminate '</*temperature_string>'
    valid_temp = re.sub('</?temperature_string>', '', temp.group(0))
    return (valid_weather, valid_temp)


text_to_examine = [text2, text4, text5, text6]
text_id = [2,4,5,6]
i = 0
for text in text_to_examine:
    print("lexical_diversity for text{}: {}".format(text_id[i], lexical_diversity(text)))
    print("percentage_use for text{}: {}".format(text_id[i], percentage_use('the', text)))
    un_prefix = find_un_prefix()
    print("number of un_prefix in text{}: {}".format(text_id[i], un_prefix))
    i += 1
print (extract_office_hour())
print ("Weather in Phily:\nweather: {}\ntemperature: {}".format(get_weather()[0], get_weather()[1]))
