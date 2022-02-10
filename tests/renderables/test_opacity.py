import pytest
from rich.text import Text

from tests.utilities.render import render
from textual.renderables.opacity import Opacity

STOP = "\x1b[0m"


@pytest.fixture
def text():
    return Text("Hello, world!", style="#ff0000 on #00ff00", end="")


def test_simple_opacity(text):
    blended_red_on_green = "\x1b[38;2;127;127;0;48;2;0;255;0m"
    assert render(Opacity(text, opacity=.5)) == (
        f"{blended_red_on_green}Hello, world!{STOP}"
    )


def test_value_zero_sets_foreground_color_to_background_color(text):
    foreground = background = "0;255;0"
    assert render(Opacity(text, opacity=0)) == (
        f"\x1b[38;2;{foreground};48;2;{background}mHello, world!{STOP}"
    )


def test_opacity_value_of_one_noop(text):
    assert render(Opacity(text, opacity=1)) == render(text)


def test_ansi_colors_noop():
    ansi_colored_text = Text("Hello, world!", style="red on green", end="")
    assert render(Opacity(ansi_colored_text, opacity=.5)) == render(ansi_colored_text)


def test_opacity_no_style_noop():
    text_no_style = Text("Hello, world!", end="")
    assert render(Opacity(text_no_style, opacity=.2)) == render(text_no_style)


def test_opacity_only_fg_noop():
    text_only_fg = Text("Hello, world!", style="#ff0000", end="")
    assert render(Opacity(text_only_fg, opacity=.5)) == render(text_only_fg)


def test_opacity_only_bg_noop():
    text_only_bg = Text("Hello, world!", style="on #ff0000", end="")
    assert render(Opacity(text_only_bg, opacity=.5)) == render(text_only_bg)
