# vizdet
VIZDET - VIZualization for DEtection and Tracking


## Installation instructions

This module requires the freetype OpenCV module, which is not included in the PyPI repository package, so
I recommend you install the requirements with conda (create a [conda environment first](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)):

```sh
conda install libopencv opencv py-opencv -c conda-forge
```

From here you can install the package with pip, as usual

```sh
pip install vizdet
```

## License

This source code of this project is released under the Apache 2.0 License, which is available in the `LICENSE` file.

The project also contains the [FiraGO](https://github.com/bBoxType/FiraGO) font, which is distributed under the SIL Open Font License. The `test` directory also includes the [FiraMono](https://fonts.google.com/specimen/Fira+Mono) font, also released under the SIL Open Font License. A copy of the Open Font License is included in the `OFL.txt` file.
