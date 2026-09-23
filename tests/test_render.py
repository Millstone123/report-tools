from _engine_ext import sync_theme
from reporter import render

def test_default():
    sync_theme()
    r = render()
    assert r["theme"] == "default"
    assert r["characters"] == 101
