#!/usr/bin/env python


import tensorflow as tf
import numpy as np

from sklearn import datasets


def main():
    """
    Main Entry
    """
    print("Machine Learning")
    iris = datasets.load_iris()
    print(iris.data)



if __name__ == "__main__":
    main()
