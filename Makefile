bootstrap:
	python3 -c "from report_tools import bootstrap; print(json.dumps(bootstrap()))"

test:
	python3 -m pytest tests -q
