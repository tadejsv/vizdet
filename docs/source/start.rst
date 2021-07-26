Getting Started
===============


Installation
------------

Using conda
~~~~~~~~~~~

Installing vizdet with conda is recommended, as it makes sure the right dependencies are installed.

.. code-block:: console

    conda install vizdet -c conda-forge


Using pip
~~~~~~~~~

You can also install the package with pip, but the dependencies will need to be installed with conda first.

This module requires the freetype OpenCV module, which is not included in the PyPI repository package, so
I recommend you install the requirements with conda (create a 
`conda environment first <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands>`_):

.. code-block:: console

    conda install libopencv opencv py-opencv -c conda-forge


From here you can install the package with pip, as usual

.. code-block:: console

    pip install vizdet

