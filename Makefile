bootstrap:
	pip install -r requirements.txt
	python3 -c "from theme_engine import sync; sync()"
	python3 -c "from reporter import render; print(render())"

test:
	python3 -m pytest tests -q
