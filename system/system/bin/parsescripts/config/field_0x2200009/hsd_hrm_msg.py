#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsd hrm msg
author          :   j00354216
modify  record  :   2016-04-27 create file
"""

hsd_hrm_msg_enum_table = {
0x0000 : "ID_HSD_HRM_START_REQ",
0x0001 : "ID_HRM_HSD_START_CNF",
0x0002 : "ID_HSD_HRM_POWEROFF_REQ",
0x0003 : "ID_HRM_HSD_POWEROFF_CNF",
}

def get_hsd_hrm_msg_str( MsgId):
    for MsgIdIndex in hsd_hrm_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsd_hrm_msg_enum_table[MsgIdIndex]

    return "none"