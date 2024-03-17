#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list BastetWrrcinterface.h
author          :   hudong 00377722
modify  record  :   2018-03-27 create file
"""

guas_bastet_msg_enum_table = {
0x0000 : "ID_WRRC_BASTET_RRC_STATUS_IND",
0x0001 : "ID_WRRC_BASTET_NET_QUAL_CB",
0x0002 : "ID_WRRC_BASTET_ID_ENUM_BUTT",
}

def get_guas_bastet_msg_str( MsgId):
    for MsgIdIndex in guas_bastet_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return guas_bastet_msg_enum_table[MsgIdIndex]

    return "none"