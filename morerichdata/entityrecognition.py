import os
from textblob import TextBlob
from tika import parser

path = "../data/"
dir_list = os.listdir(path)
element = 0

text = parser.from_file(f'../data/{dir_list[element]}')
blob = TextBlob(text["content"])

entities = blob.noun_phrases