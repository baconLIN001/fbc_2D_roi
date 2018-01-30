# -*- coding: utf-8 -*-
__author__ = 'bacon'
import matlab.engine
import matlab
import numpy as np
import util.py_matlab_util as py_matlab_util
import os
import dicom

"""
call matlab to read specific roi file
"""
def matlab_read_roi(path, rc):
    ret = py_matlab_util.py_mat_read_imageJ_roi(path, rc)
    return ret

"""
convert specific roi file to npy
"""
def roi_to_npy(in_path,r, c, out_path):
    res = py_matlab_util.py_mat_read_imageJ_roi(in_path, r, c)
    np.save(out_path, res)

'''find all roi files in a dic'''
def find_all_dicoms_and_rois(path):
    # file_list = os.listdir(path)
    # print(file_list)
    roi_list = []
    dicom_list = []
    for root, dirs, files in os.walk(path):
        dicom_file = " "
        roi_file = " "
        for i in files:
            if i[0]=="I":
                # print(i)
                n = len(i)
                if i[n-3:n] == "roi":
                    roi_file = i
                else:
                    dicom_file = i
        if dicom_file[0] == roi_file[0] == "I":
            roi_list.append(root+"\\"+roi_file)
            dicom_list.append(root+"\\"+dicom_file)

    return dicom_list, roi_list

"""
read specific path DICOM file,return uint16 narray
"""
def dicom_read(path):
    dcm = dicom.read_file(path)
    pix = dcm.pixel_array
    return pix

"""
get the size of the dicom file
"""
def get_dicom_size(path):
    dcm = dicom.read_file(path)
    return dcm.pixel_array.shape

"""
save specific DICOM file to .npy file
"""
def dicom_to_npy(in_path, out_path):
    pix = dicom_read(in_path)
    np.save(out_path, pix)

"""
read roi
"""
def read_roi(d_path, r_path):
    size = get_dicom_size(d_path)
    ##对于二维的shape不用处理直接使用，对于三维的shape需要获得dicom的长宽
    if len(size)==3:
        size=size[1:]
    rc = []
    for i in size:
        rc.append(int(i))
    roi_ret = matlab_read_roi(r_path, rc)
    return roi_ret

"""
multiply dicom with roi to get the real roi area
"""
def combine_dicom_roi(dicom_mat, roi_mat):
    return np.multiply(dicom_mat,roi_mat)

"""
get max width and height scale of a roi matrix that all are "1"s
"""
def get_roi_scale(mat):
    size = mat.shape
    mat = mat.tolist()
    r = size[0]
    c = size[1]
    h_up = c
    h_bottom = 0
    w_left = c
    w_right = 0
    for i in range(r):
        for j in range(c):
            if int(mat[i][j]) == 1:
                if i < h_up:
                    h_up = i
                if i > h_bottom:
                    h_bottom = i
                if w_left > j:
                    w_left = j
                break
        for j in range(c-1, 0, -1):
            if int(mat[i][j]) == 1:
                if w_right < j:
                    w_right = j
                break
    w_scale = w_right - w_left
    h_scale = h_bottom - h_up
    return w_scale, h_scale

"""
get a roi point
"""
def get_roi_point(mat):
    size = mat.shape
    mat = mat.tolist()
    r = size[0]
    c = size[1]
    point_x = c
    point_y = c
    for i in range(r):
        for j in range(c):
            if int(mat[i][j]) == 1:
                point_x = i
                point_y = j
                break
    return point_x, point_y

"""
get roi middle point
"""
def get_roi_middle_point(mat):
    size = mat.shape
    mat = mat.tolist()
    r = size[0]
    c = size[1]
    h_up = c
    h_bottom = 0
    w_left = c
    w_right = 0
    for i in range(r):
        for j in range(c):
            if int(mat[i][j]) != 0:
                if i < h_up:
                    h_up = i
                if i > h_bottom:
                    h_bottom = i
                if w_left > j:
                    w_left = j
                break
        for j in range(c-1, 0, -1):
            if int(mat[i][j]) != 0:
                if w_right < j:
                    w_right = j
                break
    # print(w_right,w_left,h_bottom,h_up)
    mid_x = int((w_right + w_left)/2)
    mid_y = int((h_bottom + h_up)/2)
    return mid_x, mid_y

"""
get smaller unified size(200*200) roi
"""
def get_unified_roi(mat):
    mid_x, mid_y = get_roi_middle_point(mat)
    # print(mid_x, mid_y)
    zero_mat = np.zeros((750, 750))
    size = mat.shape
    r = size[0]
    c = size[1]
    print(r,c)
    zero_mat[375-int(r/2):375+int(r/2), 375-int(c/2):375+int(c/2)] = mat
    return zero_mat[375-int(r/2)+mid_x-100:375-int(r/2)+mid_x+100, 375-int(c/2)+mid_y-100:375-int(c/2)+mid_y+100]