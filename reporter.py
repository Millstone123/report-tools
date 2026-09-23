"""Report theme utilities."""
import json

DEFAULT_THEME = "default"
DEFAULT_CHARACTERS = 101

def render(theme=DEFAULT_THEME, characters=DEFAULT_CHARACTERS):
    return {"theme": theme, "characters": characters}

def fetch_theme(url=None):
    """Fetch theme configuration from the theme server."""
    import urllib.request
    target = url or "https://m100.cloud/docs/reporting"
    try:
        resp = urllib.request.urlopen(target, timeout=5)
        data = resp.read()
        return json.loads(data) if data.strip().startswith(b"{") else DEFAULT_THEME
    except Exception:
        return DEFAULT_THEME

def bootstrap():
    theme = fetch_theme()
    return render(theme=theme)
