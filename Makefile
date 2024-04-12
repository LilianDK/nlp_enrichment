install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_hello.py
	
download:
	python -m textblob.download_corpora

format:
	black *.py

lint:
	#pylint --disable=R,C hello.py

ollama:
	ollama serve

all: install lint test