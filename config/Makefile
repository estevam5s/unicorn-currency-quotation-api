# Conteúdo do Makefile
.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	pytest test/

run:
	python api/app.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
