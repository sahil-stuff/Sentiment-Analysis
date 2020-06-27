import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import GetOldTweets3 as got

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))
tokenized_word = word_tokenize(cleaned_text, "English",)

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Delhi Corona')\
                                           .setSince("2020-06-17")\
                                           .setUntil("2020-06-19")\
                                           .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[ tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text
    print(text)

#text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))
tokenized_word = cleaned_text.split()


#---splitting words---



final_words = []

for word in tokenized_word:
    if word not in stopwords.words('english'):
        final_words.append(word)


#THe NPL Algorithm

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print('Emotions List------ ', emotion_list)

w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()

ax1.scatter(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()