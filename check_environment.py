#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imports all packages required for the block course "Advanced Geoscripting"
"""

__author__ = "Christina Ludwig, GIScience Research Group, Heidelberg University"
__email__ = "christina.ludwig@uni-heidelberg.de"


def check_packages():
    """
    Checks whether all required packages for the course are available
    :return:
    """

    try:
        import numpy
        import geopandas
        import rasterio
        import requests
        import pylint
        import pytest
        import cython
        import sklearn
        import scipy
        import seaborn
        import plotly
    except ModuleNotFoundError as e:
        print("Ups, something went wrong! There was an error importing the package '{}': '{}'".format(e.name, e))
        print("Seems like it is not installed in your environment. How to solve this problem: "
              "\n1. Make sure that the correct anaconda environment is activated and run this program again. "
              "\n2. If you still get this error, install the missing package using 'conda install {}'. "
              "\n3. If you still get this error, write a post in the course "
              "forum (https://github.com/orgs/geoscripting/teams/advanced-geoscripting-2020).".format(e.name, e.name))
        return 1

    print("Great! All required Python packages were found. You're ready for the course!")
    return 1


def main():
    print("Checking required packages. This may take a few seconds ... ")
    check_packages()
    return 0

if __name__ == "__main__":
    main()
