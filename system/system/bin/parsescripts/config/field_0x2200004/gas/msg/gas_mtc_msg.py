#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas mtc msg
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

gas_mtc_msg_enum_table = {
0x0001 : "MTC_RRC_INTRUSION_ACTION_SET_REQ",
0x0002 : "RRC_MTC_INTRUSION_ACTION_SET_CNF",
0x0003 : "MTC_RRC_INTRUSION_BAND_SET_REQ",
0x0004 : "RRC_MTC_INTRUSION_BAND_SET_CNF",
0x0005 : "MTC_RRC_NOTCH_CHANNEL_IND",
0x0006 : "RRC_MTC_INTRUSION_BAND_BAND_INFO_IND",
0x0007 : "MTC_RRC_BAND_CNF_IND",
0x0008 : "RRC_MTC_AREA_LOST_IND",
0x0009 : "MTC_RRC_TDS_LTE_RF_CONTROL_IND",
0x000A : "RRC_MTC_NCELL_INFO_IND",
0x000B : "MTC_RRC_GSM_CELL_INFO_IND",
0x000C : "RRC_MTC_USING_FREQ_IND",
0x000D : "MTC_RRC_RSE_CFG_IND",
0x000E : "RRC_MTC_USING_FREQ_IND",
0x000F : "MTC_RRC_AR_SENSOR_STATE_IND",
0x0011 : "MTC_ERRC_POWER_STATE_NOTIFY",
0x0012 : "RRC_MTC_GSM_CELL_INFO_EX_IND",
}

def get_gas_mtc_msg_str( MsgId):
    for MsgIdIndex in gas_mtc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_mtc_msg_enum_table[MsgIdIndex]

    return "none"