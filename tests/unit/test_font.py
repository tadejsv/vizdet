import os
from pathlib import Path

from vizdet import Font


def test_default_font():
    default = Font.get_default()
    size = default.font.getTextSize("Text!", 10, -1)

    assert size == ((22, 8), 0)


def test_default_font_cache():
    default1 = Font.get_default()
    default2 = Font.get_default()

    assert default1 is default2


def test_load_custom_font_fname():
    fname = os.getcwd() + "/vizdet/fonts/FiraGO-Regular.ttf"
    font = Font(fname)
    size = font.font.getTextSize("Text!", 10, -1)

    assert size == ((22, 8), 0)


def test_load_custom_font_path():
    path = Path.cwd() / "vizdet/fonts/FiraGO-Regular.ttf"
    font = Font(path)
    size = font.font.getTextSize("Text!", 10, -1)

    assert size == ((22, 8), 0)
