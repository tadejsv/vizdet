from pathlib import Path

import cv2
import numpy as np

from vizdet import InfoBox


def test_draw_full():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    i = InfoBox(width=200, font_height_desc=40, font_height_title=50, padding=15)
    i.draw(image, (1700, 20), ["9 cars", "8 trucks"], "Counts")

    result = cv2.imread(str(Path(__file__).parent / "highway_infobox_full.png"))
    np.testing.assert_allclose(image, result)


def test_draw_color():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    i = InfoBox(
        width=200,
        font_height_desc=40,
        font_height_title=50,
        padding=15,
        title_text_color=(255, 0, 0),
        title_background_color=(0, 255, 0),
    )
    i.draw(image, (1700, 20), ["9 cars", "8 trucks"], "Counts")

    result = cv2.imread(str(Path(__file__).parent / "highway_infobox_color.png"))
    np.testing.assert_allclose(image, result)


def test_draw_no_title():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    i = InfoBox(width=200, font_height_desc=40, font_height_title=50, padding=15)
    i.draw(image, (1700, 20), ["9 cars", "8 trucks"])

    result = cv2.imread(str(Path(__file__).parent / "highway_infobox_no_title.png"))
    np.testing.assert_allclose(image, result)
