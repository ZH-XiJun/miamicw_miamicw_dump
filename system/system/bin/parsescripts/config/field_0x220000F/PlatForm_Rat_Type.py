#!/usr/bin/env python
# coding=utf-8
"""
���ܣ���ȡ��ʽ����
��Ȩ��Ϣ����Ϊ�������޹�˾����Ȩ���У�C��2010-2019
�޸ļ�¼��2016-07-08 00349889 ����
"""

import string

platform_rat_type_enum_table = {
    0   : "PLATFORM_RAT_GSM",
    1   : "PLATFORM_RAT_WCDMA",
    2  : "PLATFORM_RAT_LTE",
    3  : "PLATFORM_RAT_TDS",
    4  : "PLATFORM_RAT_1X",
    5  : "PLATFORM_RAT_HRPD",
}

def UPHY_GetRatType(ucIdx):
    if ucIdx in platform_rat_type_enum_table:
        strRlt = platform_rat_type_enum_table[ucIdx]
    else:
        strRlt = "PLATFORM_RAT_BUTT"
    return strRlt
