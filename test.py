import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer

ps = PorterStemmer()
sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(sentence)
filtered_sentence = [w for w in tokens if not w in stop_words]
# print(filtered_sentence)

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
