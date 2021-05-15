import cv2
import numpy as np
import pytest
from pathlib import Path

from vizdet import BBoxes, ColorMode

np.random.seed(42)

CLASSES = ["car", "truck"]
LABELS = [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
LABELS_STR = [CLASSES[i] for i in LABELS]
SCORES = np.random.rand(len(LABELS)).tolist()
BOXES = [
    [1039, 347, 1098, 393],
    [1267, 762, 1418, 889],
    [1225, 604, 1327, 693],
    [1789, 682, 1919, 790],
    [1200, 421, 1249, 464],
    [1595, 389, 1726, 514],
    [1089, 575, 1169, 622],
    [1670, 416, 1820, 566],
    [1469, 421, 1529, 482],
    [904, 440, 1043, 615],
    [1261, 302, 1296, 345],
    [1146, 378, 1182, 406],
    [504, 623, 876, 1142],
    [922, 611, 1213, 1107],
    [1221, 464, 1283, 510],
    [1115, 494, 1179, 551],
    [1116, 493, 1180, 551],
]


######################
# Normal functioning #
######################


def test_labels():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, labels=LABELS_STR)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_labels.png"))
    np.testing.assert_allclose(image, result)


def test_labels_list():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(labels_list=CLASSES, font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, labels=LABELS)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_labels_list.png"))
    np.testing.assert_allclose(image, result)


def test_conf():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, labels=LABELS_STR, scores=SCORES)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_labels_conf.png"))
    np.testing.assert_allclose(image, result)


def test_ids():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(color_mode=ColorMode.IDS, font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, ids=LABELS)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_ids.png"))
    np.testing.assert_allclose(image, result)


def test_ids_conf():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(color_mode=ColorMode.IDS, font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, ids=LABELS, scores=SCORES)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_ids_conf.png"))
    np.testing.assert_allclose(image, result)


def test_full():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES, labels=LABELS_STR, ids=LABELS, scores=SCORES)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_full.png"))
    np.testing.assert_allclose(image, result)


def test_full_numpy():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(font_height=30, box_thickness=6, padding=3)
    boxes.draw(
        image,
        np.array(BOXES).astype(int),
        labels=np.array(LABELS_STR),
        ids=np.array(LABELS),
        scores=np.array(SCORES),
    )

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_full.png"))
    np.testing.assert_allclose(image, result)


def test_no_labels():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(font_height=30, box_thickness=6, padding=3)
    boxes.draw(image, BOXES)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_no_labels.png"))
    np.testing.assert_allclose(image, result)


def test_color_list():
    image = cv2.imread(str(Path(__file__).parent / "highway.png"))
    boxes = BBoxes(
        bbox_color_list=((255, 0, 0), (0, 255, 0)),
        font_height=30,
        box_thickness=6,
        padding=3,
    )
    boxes.draw(image, BOXES, labels=LABELS_STR)

    result = cv2.imread(str(Path(__file__).parent / "highway_bboxes_color_list.png"))
    np.testing.assert_allclose(image, result)


##########
# Errors #
##########


def test_labels_list_no_int():
    """ Pass labels_list but labels not integers """
    boxes = BBoxes(labels_list=CLASSES)
    with pytest.raises(TypeError, match="Label `car`"):
        boxes.draw(np.zeros((100, 100, 3)), [[0, 0, 10, 10]], labels=["car"])


def test_labels_list_invalid_ind():
    """ Pass labels_list but labels index invalid """
    boxes = BBoxes(labels_list=CLASSES)
    with pytest.raises(IndexError, match="Label index `10`"):
        boxes.draw(np.zeros((100, 100, 3)), [[0, 0, 10, 10]], labels=[10])


def test_invalid_length():
    """ Various parameters passed and length does not match that of bboxes. """
    boxes = BBoxes()

    with pytest.raises(ValueError, match="The `ids`"):
        boxes.draw(np.zeros((100, 100, 3)), [[0, 0, 10, 10]], ids=[0, 1])

    with pytest.raises(ValueError, match="The `labels`"):
        boxes.draw(np.zeros((100, 100, 3)), [[0, 0, 10, 10]], labels=[0, 1])

    with pytest.raises(ValueError, match="The `scores`"):
        boxes.draw(np.zeros((100, 100, 3)), [[0, 0, 10, 10]], scores=[0, 1])


def test_float_bboxes():
    """ Pass bboxes as floats instead of integers. """
    bboxes = BBoxes()
    with pytest.raises(ValueError, match="The `bboxes` elements"):
        bboxes.draw(np.zeros((100, 100, 3)), [(0.0, 0.0, 10.0, 10.0)])
