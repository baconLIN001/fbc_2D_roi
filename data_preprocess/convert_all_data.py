# -*- coding: utf-8 -*-
__author__ = 'bacon'
import util.dicom_roi_read_util as dicom_roi_read_util

import os
def get_all_benigns(path):
    benign_dicom_list, benign_roi_list = dicom_roi_read_util.find_all_dicoms_and_rois(path)
    return benign_dicom_list, benign_roi_list

def get_all_malignancy(path):
    malignancy_dicom_list, malignancy_roi_list = dicom_roi_read_util.find_all_dicoms_and_rois(path)
    return malignancy_dicom_list, malignancy_roi_list

def apart_adc_and_dce(list):
    adc_list = []
    dce_list = []
    for i in list:
        if "ADC" in i:
            adc_list.append(i)
        if "DCE" in i:
            dce_list.append(i)
    return adc_list, dce_list

def get_file_lists(benign_path, malignancy_path):
    benign_dicom_list, benign_roi_list = get_all_benigns(benign_path)
    malignancy_dicom_list, malignancy_roi_list = get_all_malignancy(malignancy_path)
    # print(len(benign_dicom_list), benign_dicom_list)
    # print(len(benign_roi_list), benign_roi_list)
    # print(len(malignancy_dicom_list), malignancy_dicom_list)
    # print(len(malignancy_roi_list), malignancy_roi_list)
    adc_b_d_list, dce_b_d_list = apart_adc_and_dce(benign_dicom_list)
    adc_b_r_list, dce_b_r_list = apart_adc_and_dce(benign_roi_list)
    adc_m_d_list, dce_m_d_list = apart_adc_and_dce(malignancy_dicom_list)
    adc_m_r_list, dce_m_r_list = apart_adc_and_dce(malignancy_roi_list)
    # print(len(adc_b_d_list), adc_b_d_list)
    # print(len(dce_b_d_list), dce_b_d_list)
    # print(len(adc_b_r_list), adc_b_r_list)
    # print(len(dce_b_r_list), dce_b_r_list)
    # print(len(adc_m_d_list), adc_m_d_list)
    # print(len(dce_m_d_list), dce_m_d_list)
    # print(len(adc_m_r_list), adc_m_r_list)
    # print(len(dce_m_r_list), dce_m_r_list)
    adc_d_list = adc_m_d_list + adc_b_d_list
    dce_d_list = dce_m_d_list + dce_b_d_list
    d_list = adc_d_list + dce_d_list
    # print(len(adc_d_list), adc_d_list)
    # print(len(dce_d_list), dce_d_list)
    # print(len(d_list), d_list)
    adc_r_list = adc_m_r_list + adc_b_r_list
    dce_r_list = dce_m_r_list + dce_b_r_list
    r_list = adc_r_list + dce_r_list
    # print(len(adc_r_list), adc_r_list)
    # print(len(dce_r_list), dce_r_list)
    # print(len(r_list), r_list)
    return d_list, r_list

if __name__ == '__main__':
    benign_path = 'G:\\Work\\FBC\\data\\FBCMRI\\FBCMRI\\benign'
    malignancy_path = 'G:\\Work\\FBC\\data\\FBCMRI\\FBCMRI\\malignancy'
    ##将dicom图像的size输出到文件
    # dicom_f = open('dicom_size.txt','w')
    # for i in d_list:
    #     # print(dicom_read_util.get_dicom_size(i))
    #     dicom_f.writelines(str(dicom_read_util.get_dicom_size(i))+"\n")
    # dicom_f.close()

    ##两个特例，其shape是三维的
    # print(d_list[69])
    # print(d_list[76])

    ##判断r_list和d_list是否一一对应
    # for i in range(len(r_list)):
    #     if r_list[i][:len(r_list[i])-4] != d_list[i]:
    #         print(r_list[i])

    ##读取所有roi并确认roi范围区间
    # scale_f = open('adc_r_scale.txt', 'w')
    # for roi_path in adc_r_list:
    #     mat_roi = dicom_roi_read_util.read_roi(roi_path[:len(roi_path)-4], roi_path)
    #     scale_f.write(roi_path+" :  " + str(dicom_roi_read_util.get_roi_scale(mat_roi))+"\n")
    # scale_f.close()
