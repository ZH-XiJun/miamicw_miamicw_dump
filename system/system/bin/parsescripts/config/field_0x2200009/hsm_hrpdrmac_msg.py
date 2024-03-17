#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list hsm hrpdrmac msg
author          :   j00354216
modify  record  :   2016-04-27 create file
"""

hsm_hrpdrmac_msg_enum_table = {
0x3300 : "ID_CNAS_CTTF_HRPD_TRANSMIT_ATI_NTF",
0x3301 : "ID_CNAS_CTTF_HRPD_RECEIVE_ATI_NTF",
}

def get_hsm_hrpdrmac_msg_str( MsgId):
    for MsgIdIndex in hsm_hrpdrmac_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return hsm_hrpdrmac_msg_enum_table[MsgIdIndex]

    return "none"