from pathlib import Path

import cv2  # type: ignore
import numpy as np

from vizdet import Font, Label


def test_normal():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    label = Label(font_height=50)
    label.draw(image, (1000, 600), "Highway")

    result = cv2.imread(str(Path(__file__).parent / "highway_label_normal.png"))
    np.testing.assert_allclose(image, result)


def test_no_bg():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    label = Label(font_height=50, background_color=None)
    label.draw(image, (1000, 600), "Highway")

    result = cv2.imread(str(Path(__file__).parent / "highway_label_no_bg.png"))
    np.testing.assert_allclose(image, result)


def test_font():
    """Check that various unicode fonts are working with FiraGO."""
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    label = Label(font_height=50)
    label.draw(image, (1000, 600), "šose → шоссе → כביש מהיר")

    result = cv2.imread(str(Path(__file__).parent / "highway_label_font.png"))
    np.testing.assert_allclose(image, result)


def test_different_font():
    """Check that various unicode fonts are working with FiraGO."""
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    font = Font(Path(__file__).parent / "FiraMono-Regular.otf")
    label = Label(font, font_height=50)
    label.draw(image, (1000, 600), "Highway")

    result = cv2.imread(str(Path(__file__).parent / "highway_label_diff_font.png"))
    np.testing.assert_allclose(image, result)


def test_color():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    label = Label(
        font_height=50, text_color=(255, 0, 0), background_color=(255, 255, 0)
    )
    label.draw(image, (1000, 600), "Highway")

    result = cv2.imread(str(Path(__file__).parent / "highway_label_color.png"))
    np.testing.assert_allclose(image, result)
