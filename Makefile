bootstrap:
	pip install -r requirements.txt
	python3 -c "from report_theme import load_theme; print(load_theme())"

test:
	python3 -m pytest tests -q
