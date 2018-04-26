#!/usr/bin/env python


import numpy as np


class Collection(object):
  """
  A sample collection
  """
  def __init__(self, path):
    self.__sample_file = open(path)


  def __del__(self):
    self.__sample_file.close()


  def eof(self):
    """
    End of sample file
    """
    return False


  def next(self):
    """
    Get next sample
    """
    line = self.__sample_file.readline().strip()
    if line:
        return np.fromstring(line)
    else:
        return None

