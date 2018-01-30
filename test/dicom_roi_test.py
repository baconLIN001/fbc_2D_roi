# -*- coding: utf-8 -*-
__author__ = 'bacon'
import dicom
import pylab
from matplotlib import pyplot as plt
import numpy as np

##测试读取dicom 1
# dcm_dir = dicom.read_dicomdir("DICOMDIR")
# print(dcm_dir)
# # dcm = dicom.read_file("I1225000")
# # dcm.image = dcm.pixel_array * dcm.RescaleSlope + dcm.RescaleIntercept
# dcm = dicom.read_file("I1000000")
# dcm.image = dcm.pixel_array * dcm.RescaleSlope + dcm.RescaleIntercept
# print("type of dcm: ", type(dcm))
# print("type of dcm.image: ", type(dcm.image))
# slices = []
# slices.append(dcm)
# print(len(slices))
# img = slices[ int(len(slices)/2) ].image.copy()
# print("type of img: ", type(img))
# print("shape of img: ",img.shape)
# img1 = numpy.uint16(img)
# ret,img2 = cv2.threshold(img, 90,3071, cv2.THRESH_BINARY)
# print("type of ret: ", type(ret))
# print("type of img: ", type(img2))
# print("shape of img2: ", img2.shape)
# img3 = numpy.uint8(img2)
# print("shape of img3: ", img3.shape)
# img4 = numpy.uint16(img2)
# plt.figure()
# plt.subplot(231)
# plt.imshow(slices[int(len(slices) / 2)].image, 'gray')
# plt.title('Original')
# plt.subplot(232)
# plt.imshow(img2, 'gray')
# plt.title('img2')
# plt.subplot(233)
# plt.imshow(img3, 'gray')
# plt.title('uint8')
# plt.subplot(234)
# plt.imshow(img4, 'gray')
# plt.title('uint16')
# plt.subplot(235)
# plt.imshow(img1, 'gray')
# plt.title('ori_uint16')
# plt.show()

##测试读取dicom 2
# dcm = dicom.read_file("I1000000")
# all attrs
# print(dcm.dir('pat'))
# values foe attrs
# print(dcm.PatientName)
#
# data_element = dcm.data_element("PatientsName")
# print(data_element.VR, data_element.value)
# pixel_bytes = dcm.PixelData
# pix = dcm.pixel_array
# print(type(pix[0][0]))
# print(np.amax(pix))
# print(np.amin(pix))
# print(pix)
# pylab.imshow(dcm.pixel_array)
# pylab.show()

##测试获取dicom大小
import util.dicom_roi_read_util as dicom_roi_read_util
# rc = dicom_read_util.get_dicom_size('../data/I1000000')
# print(rc[0])
# print(rc[1])

##测试调用MATLAB
# engine = matlab.engine.start_matlab()
# ret = engine.read_ImageJ_roi('I1000000.roi', 163, 126)
# engine.quit()
# print type(ret)

##测试读取roi文件
# mat_roi = dicom_roi_read_util.read_roi('../data/I1000000', '../data/I1000000.roi')
# print np.sum(mat_roi)
# print mat_roi[130]
# np.savetxt('I1000000.txt',mat_roi.tolist())

##测试处理roi矩阵
# mat_dicom = dicom_roi_read_util.dicom_read('../data/I1000000')
# mat_dicom_roi = dicom_roi_read_util.combine_dicom_roi(mat_dicom, mat_roi)
# print("scale: ", dicom_roi_read_util.get_roi_scale(mat_roi))
# plt.figure()
# plt.subplot(131)
# plt.imshow(mat_roi, 'gray')
# plt.title('roi')
# plt.subplot(132)
# plt.imshow(mat_dicom, 'gray')
# plt.title('dicom')
# plt.subplot(133)
# plt.imshow(mat_dicom_roi, 'gray')
# plt.title('dicom_roi')
# plt.show()

##测试unified大小的roi图像
mat_roi = dicom_roi_read_util.read_roi('../data_sample/I1000000', '../data_sample/I1000000.roi')
mat_dicom = dicom_roi_read_util.dicom_read('../data_sample/I1000000')
mat_dicom_roi = dicom_roi_read_util.combine_dicom_roi(mat_dicom, mat_roi)
mat_unified_roi = dicom_roi_read_util.get_unified_roi(mat_dicom_roi)
print(mat_unified_roi.shape)
print(np.amax(mat_unified_roi))
plt.figure()
plt.subplot(121)
plt.imshow(mat_roi, 'gray')
plt.title('orin')
plt.subplot(122)
plt.imshow(mat_unified_roi, 'gray')
plt.title('unified_roi')
plt.show()