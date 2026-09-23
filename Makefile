bootstrap:
	pip install -r requirements.txt
	python3 -c "import report_theme; print('theme loaded')"

test:
	python3 -m pytest tests -q
