# VIZDET

[![PyPI version](https://badge.fury.io/py/vizdet.svg)](https://badge.fury.io/py/vizdet) ![CI](https://github.com/tadejsv/vizdet/workflows/CI/badge.svg)

![Race example](https://github.com/tadejsv/vizdet/raw/main/_assets/example_race.png)

VIZDET - VIZualization for DEtection and Tracking. This library provides a simple interface to plot detection bounding boxes and their labels on an image. It enables the use of custom fonts, allowing you to create visually pleasing detection plots.

The purpose of this library is enable detection model creators to use an out-of-the-box library for presenting and visually evaluating their detection models, focusing their time on writing the detection models instead. Main features of vizdet are:

* Easy to use, enabling you to create detection plots with ease with minimal code
* Use of custom fonts to make the plots look beautiful and write special unicode characters and characters from non-latin scipts
* Customizable graphical parameters - customize plots according to your taste
* Out of the box options cover the main usecases for object detection, as well as (multi) object tracking - just plug in the detection/tracking results from your model, and you're ready to go
* Lightweight, with the only dependency being OpenCV (and Numpy)

## Installation instructions

This module requires the freetype OpenCV module, which is not included in the PyPI repository package, so
I recommend you install the requirements with conda (create a [conda environment first](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)):

``` sh
conda install libopencv opencv py-opencv -c conda-forge
```

From here you can install the package with pip, as usual

``` sh
pip install vizdet
```

## Quickstart

Let's create our first detection plot. Download [this image](https://github.com/tadejsv/vizdet/raw/main/_assets/race.png) and place it in your working directory. Then, execute this script (you'll also need to install matplotlib to visualize the results)

``` python
import cv2
import matplotlib.pyplot as plt
from vizdet import BBoxes, InfoBox

# Prepare our detection results
boxes = [
    [  6,  74, 156, 266],
    [160,  80, 299, 258],
    [283,  83, 469, 262],    
    [358, 250, 428, 273],
    [  0, 221,  48, 254],
    [156, 244, 257, 270],
    [272, 205, 319, 252],  
    [ 46, 254, 117, 278],
]
labels = [1, 1, 1, 0, 0, 0, 0, 0]
probs = [0.997, 0.995, 0.997, 0.975, 0.976, 0.993, 0.993, 0.992]
classes = ['rollerblade', 'person']

# Create text for info box
into_title = 'Number of objects'
info_desc = [f'{labels.count(idx)} {cl}s' for idx, cl in enumerate(classes)]

# Read image
img = cv2.imread('race.png')

# Prepare objects to draw
bboxes = BBoxes(labels_list=classes)
infobox = InfoBox(width=150)

# Draw detection results on the image
bboxes.draw(img, boxes, labels=labels, labels_conf=probs)
infobox.draw(img, (440, 315), info_desc, into_title)

# Plot results
plt.imshow(img[::-1])
```

The result should be equal to the image above. We drew the detection boxes, shown their labels and probabilities, as well as an information box given some information what is on the image.

All the drawing is done by the `BBoxes` and `InfoBox` classes, which have a simple and intuitive interface. The default font (FiraGO) is used, but this could also be modified. Note that this looks much better than what you would get with the default OpenCV Hershey font.

The result ( `img` ) is a simply numpy array - not some custom plot object that you would get with Matplotlib or similar libraries. This enables you to further customize the image using other tools, if you would like, or to compose multiple images into a video and so on. The possibilities are endless 😉

## License

This source code of this project is released under the Apache 2.0 License, which is available in the `LICENSE` file.

The project also contains the [FiraGO](https://github.com/bBoxType/FiraGO) font, which is distributed under the SIL Open Font License. The `test` directory also includes the [FiraMono](https://fonts.google.com/specimen/Fira+Mono) font, also released under the SIL Open Font License. A copy of the Open Font License is included in the `OFL.txt` file.
