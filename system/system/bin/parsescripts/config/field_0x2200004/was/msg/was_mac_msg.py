#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list RrcMacInterface.h
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

was_mac_msg_enum_table = {
0x0000 : "ID_MAC_RRC_ACTIVE_IND",
0x0001 : "ID_MAC_RRC_STATUS_IND",
0x0002 : "ID_RRC_MAC_C_CONFIG_REQ",
0x0003 : "ID_MAC_RRC_C_CONFIG_CNF",
0x0004 : "ID_RRC_MAC_D_CONFIG_REQ",
0x0005 : "ID_MAC_RRC_D_CONFIG_CNF",
0x0006 : "ID_RRC_MAC_E_VIRTUAL_CONFIG_REQ",
0x0007 : "ID_MAC_RRC_E_VIRTUAL_CONFIG_CNF",
0x0008 : "ID_RRC_MAC_HS_CONFIG_REQ",
0x0009 : "ID_MAC_RRC_HS_CONFIG_CNF",
0x000C : "ID_RRC_MAC_HS_RESET_REQ",
0x000D : "ID_MAC_RRC_HS_RESET_CNF",
0x000E : "ID_RRC_MAC_RELEASE_REQ",
0x000F : "ID_MAC_RRC_RELEASE_CNF",
0x0010 : "ID_RRC_MAC_TFC_CONTROL_REQ",
0x0011 : "ID_MAC_RRC_TFC_CONTROL_IND",
0x0012 : "ID_RRC_MAC_CIPHER_CONFIG_REQ",
0x0013 : "ID_MAC_RRC_CIPHER_CONFIG_CNF",
0x0014 : "ID_MAC_RRC_CIPHER_ACTIVE_IND",
0x0015 : "ID_RRC_MAC_MEAS_CONFIG_REQ",
0x0016 : "ID_MAC_RRC_MEAS_CONFIG_CNF",
0x0017 : "ID_MAC_RRC_MEAS_IND",
0x0018 : "ID_RRC_MAC_MEAS_REL_REQ",
0x0019 : "ID_MAC_RRC_MEAS_REL_CNF",
0x001A : "ID_MAC_RRC_PCCH_DATA_IND",
0x001B : "ID_MAC_RRC_BCCH_DATA_IND",
0x001C : "ID_MAC_RRC_ERROR_IND",
0x001D : "ID_RRC_MAC_COMPRESS_MODE_CFG_REQ",
0x001E : "ID_RRC_MAC_COMPRESS_MODE_CFG_CNF",
0x0020 : "ID_RRC_MAC_TFC_SLOT_CFG_REQ",
0x0021 : "ID_RRC_MAC_TFC_SLOT_CFG_CNF",
0x0022 : "ID_RRC_MAC_STOP_UL_TX_REQ",
0x0023 : "ID_MAC_RRC_STOP_UL_TX_CNF",
0x0024 : "ID_RRC_MAC_CONTINUE_UL_TX_REQ",
0x0025 : "ID_MAC_RRC_CONTINUE_UL_TX_CNF",
0x0026 : "ID_RRC_MAC_TGPS_PRE_CHK_REQ",
0x0027 : "ID_MAC_RRC_TGPS_PRE_CHK_CNF",
0x0028 : "ID_RRC_MAC_EHS_CONFIG_REQ",
0x0029 : "ID_MAC_RRC_EHS_CONFIG_CNF",
0x002A : "ID_RRC_MAC_EHS_RESET_REQ",
0x002B : "ID_MAC_RRC_EHS_RESET_CNF",
0x002C : "ID_RRC_MAC_BCBD_CALCULATE_REQ",
0x002D : "ID_MAC_RRC_BCBD_CALCULATE_CNF",
0x002E : "ID_RRC_MAC_BHS_CALCULATE_REQ",
0x002F : "ID_MAC_RRC_BHS_CALCULATE_CNF",
0x0030 : "ID_RRC_MAC_CIPHER_RESERVE_REQ",
0x0031 : "ID_MAC_RRC_CIPHER_RESERVE_CNF",
0x0032 : "ID_RRC_MAC_C_CONFIG_REQ_MNTN_COMM_PARAM",
0x0033 : "ID_RRC_MAC_C_CONFIG_REQ_MNTN_DLCCH1",
0x0034 : "ID_RRC_MAC_C_CONFIG_REQ_MNTN_DLCCH2",
0x0035 : "ID_MAC_RRC_EHS_RX_DATA_IND",
0x0036 : "ID_RRC_MAC_I_VIRTUAL_CONFIG_REQ",
0x0037 : "ID_MAC_RRC_I_VIRTUAL_CONFIG_CNF",
0x0038 : "ID_RRC_MAC_ASC_CONFIG_IND",
0x0039 : "ID_RRC_MAC_AS_ACTIVE_DSDS_STATUS_IND",
0x8002 : "ID_RRC_MAC_C_CONFIG_REDUCE_REQ",
0x8004 : "ID_RRC_MAC_D_CONFIG_REDUCE_REQ",
0x8005 : "ID_WTTF_MEM_TEST_REQ",
0x8006 : "ID_WTTF_MEM_TEST_CNF",
0x8007 : "ID_RRC_MAC_QUIT_REQ",
}

def get_was_mac_msg_str( MsgId):
    for MsgIdIndex in was_mac_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return was_mac_msg_enum_table[MsgIdIndex]

    return "none"