import os
import fire
import pandas as pd
import ollama
from textblob import TextBlob
from tika import parser
path = "../data/"
dir_list = os.listdir(path)
element = 0
text = parser.from_file(f'{path}/{dir_list[element]}')
clean_text = str(blob.replace("\n", ""))
blob = TextBlob(text["content"])

ollama.pull('zeffmuks/universal-ner')
ollama_result = ollama.generate(model='zeffmuks/universal-ner', prompt=f'Please extract the entities from this text: {text["content"]}')
print(ollama_result)

ner_results = nlp(clean_text)
df = pd.DataFrame(ner_results)
print(df)

if __name__ == '__main__':
  fire.Fire()