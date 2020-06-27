# cleaning text

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))
tokenized_word = word_tokenize(cleaned_text, "English",)




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

ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()