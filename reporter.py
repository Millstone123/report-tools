"""Report theme utilities."""
import json

DEFAULT_THEME = "default"
DEFAULT_CHARACTERS = 101

def render(theme=DEFAULT_THEME, characters=DEFAULT_CHARACTERS):
    return {"theme": theme, "characters": characters}
