bootstrap:
	python3 -c "import json; from reporter import bootstrap; print(json.dumps(bootstrap()))"

test:
	python3 -m pytest tests -q
