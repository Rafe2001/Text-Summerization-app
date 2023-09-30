#Text cleaning
#Sentence tokenization
#Word tokenization
#Word-frequency table
#Summarization

import spacy
from string import punctuation
from heapq import nlargest
from spacy.lang.en.stop_words import STOP_WORDS


def summarize(raw_text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(raw_text)
#print(doc)
    tokens = [token.text for token in doc]                   #tokenization of text
#print(tokens)
    punctuations = punctuation + '\n'
#print(punctuation)
    word_freq = {}                                   # calculating the word frequencies
    
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuations:
           if word.text not in word_freq.keys():
               word_freq[word.text] = 1
           else:
               word_freq[word.text] += 1        
#print(word_freq)
## Sentence Tokenization
    max_frequency = max(word_freq.values())
#print(max_frequency)
    for word in word_freq.keys():
       word_freq[word] = word_freq[word] / max_frequency                       #Normalizing in the range from 0 to 1
#print(word_freq)
    sent_tokens = [sent for sent in doc.sents]
#print(sent_tokens)
# word frequency table
    sentence_scores = {}
    for sent in sent_tokens:
       for word in sent:
           if word.text.lower() in word_freq.keys():
               if sent not in sentence_scores.keys():
                   sentence_scores[sent] = word_freq[word.text.lower()]
               else:
                   sentence_scores[sent] += word_freq[word.text.lower()]
#print(sentence_scores)
    select_length = int(len(sent_tokens)*0.3)
#print(select_length)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
#print(summary)
    final_summary = [word.text for word in summary]
    final_summary = ' '.join(final_summary)
    return final_summary, doc, len(final_summary.split()), len(raw_text.split())