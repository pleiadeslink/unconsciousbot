import requests, json, os
from mastodon import Mastodon
import nltk.data
from nltk import word_tokenize
from sentence_generator import Generator

# Mastodon token and domain
mastodon = Mastodon(
    access_token = 'asdf',
    api_base_url = 'https://domain.com'
)

# How many words we are taking (the bigger the variable, the more strict it will be)
words = 2
text = ""
found = False

# We open the file and apply some tokenizing magic
while(found == False):
    with open("text.txt", 'r',encoding='utf-8') as f:
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sents = sent_detector.tokenize(f.read().strip())
        sent_tokens = [word_tokenize(sent.replace('\n', ' ').lower()) for sent in sents]
        generator = Generator(sent_tokens, words)

        # We capitalize the first word to make it pretty
        text = generator.generate().capitalize()

        # We only accept the result if it is smaller than Mastodon's character limit
        if(len(text) <  500):
            found = True

# Send result to Mastodon
mastodon.status_post(text)