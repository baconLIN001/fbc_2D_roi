__author__ = 'bacon'
import matlab.engine
import matlab
from numpy import *

"""
read spedific roi file and return the matrix of the data
"""
def py_mat_read_imageJ_roi(path, rc):
    engine = matlab.engine.start_matlab()
    r = rc[0]
    c = rc[1]
    ret = engine.read_ImageJ_roi(path, r, c)
    engine.quit()
    return mat(ret)