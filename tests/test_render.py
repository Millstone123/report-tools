from reporter import render

def test_default():
    r = render()
    assert r["theme"] == "default"
    assert r["characters"] == 101
