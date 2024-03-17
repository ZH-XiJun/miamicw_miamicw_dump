#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gas css msg
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

gas_css_msg_enum_table = {
0x2 : "CSS_CURR_GEO_IND",
0x5 : "CSS_CURR_GEO_RSP",
}

def get_gas_css_msg_str( MsgId):
    for MsgIdIndex in gas_css_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return gas_css_msg_enum_table[MsgIdIndex]

    return "none"