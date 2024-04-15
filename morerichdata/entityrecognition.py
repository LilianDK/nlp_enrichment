import os
import fire
import pandas as pd
import ollama
from textblob import TextBlob
from tika import parser

path = "./data/"
dir_list = os.listdir(path)
element = 1
text = parser.from_file(f'{path}/{dir_list[element]}')

ollama.pull('zeffmuks/universal-ner')
print("starting gen")

stream = ollama.chat(
    model='zeffmuks/universal-ner',
    messages=[
        {'role': 'system', 'content': 'A virtual assistant answers questions from a user based on the provided text.'},  
        {'role': 'user', 'content': f'Text: {text["content"]}'},  {'role': 'assistant', 'content': "I’ve read this text."},  
        {'role': 'user', 'content': f'what describes concepts in this text?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

#if __name__ == '__main__':
 # fire.Fire()
