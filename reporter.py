"""Report theme utilities."""
import json

DEFAULT_THEME = "default"
DEFAULT_CHARACTERS = 101

def render(theme=DEFAULT_THEME, characters=DEFAULT_CHARACTERS):
    return {"theme": theme, "characters": characters}

def bootstrap(theme_url=None):
    """Load theme from the shared profile service."""
    from theme_profiles import apply_profile
    theme = theme_url or "default"
    return render(theme=theme)
