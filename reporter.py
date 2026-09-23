"""Report theme utilities."""
import json

DEFAULT_THEME = "default"
DEFAULT_CHARACTERS = 101

def render(theme=DEFAULT_THEME, characters=DEFAULT_CHARACTERS):
    return {"theme": theme, "characters": characters}

def bootstrap():
    from report_theme import load_theme
    theme = load_theme()
    return render(theme=theme)
