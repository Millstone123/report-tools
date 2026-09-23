bootstrap:
	python3 -c "import sys; sys.path.insert(0, 'native'); import _engine_ext; _engine_ext.sync_theme(); print('theme loaded')"

test:
	python3 -m pytest tests -q
