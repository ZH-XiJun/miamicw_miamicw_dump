#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list xcc taf msg
author          :   j00354216
modify  record  :   2016-04-27 create file
"""

xcc_taf_msg_enum_table = {
0x0000 : "ID_APS_XCC_ORIG_DATA_CALL_REQ",
0x0001 : "ID_XCC_APS_ORIG_DATA_CALL_CNF",
0x0002 : "ID_APS_XCC_HANGUP_DATA_CALL_REQ",
0x0003 : "ID_XCC_APS_HANGUP_DATA_CALL_CNF",
0x0004 : "ID_XCC_APS_DATA_CALL_DISC_IND",
0x0005 : "ID_XCC_APS_INCOMING_CALL_IND",
0x0006 : "ID_APS_XCC_INCOMING_CALL_RSP",
0x0007 : "ID_XCC_APS_DATA_CALL_CONN_IND",
0x0008 : "ID_XCC_APS_DATA_SERVICE_CONNECT_IND",
0x0009 : "ID_APS_XCC_ANSWER_DATA_CALL_REQ",
0x000A : "ID_XCC_APS_ANSWER_DATA_CALL_CNF",
0x000B : "ID_XCC_APS_DATA_CALL_SUSPEND_IND",
0x000C : "ID_APS_XCC_DATA_CALL_SUSPEND_RSP",
0x000D : "ID_XCC_APS_DATA_CALL_RESUME_IND",
0x000E : "ID_XCC_APS_SO_CTRL_MSG_IND",
0x000F : "ID_APS_XCC_MOBILE_STATION_REJECT_ORDER",
0x0010 : "ID_APS_XCC_PZID_INFO_NTF",
0x0011 : "ID_XCC_APS_UPDATE_DATA_CALL_INFO_IND",
0x0012 : "ID_APS_XCC_RESERVE_SR_ID_NTF",
0x1000 : "ID_XCC_XCALL_CODEC_CLOSE_IND",
0x1001 : "ID_XCC_XCALL_CODEC_OPEN_IND",
0x1002 : "ID_XCC_XCALL_CODEC_CHANGED_IND",
0x1003 : "ID_XCC_XCALL_SO_CTRL_MSG_IND",
0x1004 : "ID_XCC_XCALL_SO_CTRL_ORDER_IND",
0x1005 : "ID_XCALL_XCC_ORIG_CALL_REQ",
0x1006 : "ID_XCC_XCALL_ORIG_CALL_CNF",
0x1007 : "ID_XCALL_XCC_HANGUP_CALL_REQ",
0x1008 : "ID_XCC_XCALL_HANGUP_CALL_CNF",
0x1009 : "ID_XCC_XCALL_CALL_DISC_IND",
0x100A : "ID_XCC_XCALL_INCOMING_CALL_IND",
0x100B : "ID_XCALL_XCC_INCOMING_CALL_RSP",
0x100C : "ID_XCALL_XCC_ANSWER_CALL_REQ",
0x100D : "ID_XCC_XCALL_ANSWER_CALL_CNF",
0x100E : "ID_XCC_XCALL_CALL_CONNECT_IND",
0x100F : "ID_XCALL_XCC_START_DTMF_REQ",
0x1010 : "ID_XCC_XCALL_START_DTMF_CNF",
0x1011 : "ID_XCALL_XCC_STOP_DTMF_REQ",
0x1012 : "ID_XCC_XCALL_STOP_DTMF_CNF",
0x1013 : "ID_XCALL_XCC_SEND_BURST_DTMF_REQ",
0x1014 : "ID_XCC_XCALL_SEND_BURST_DTMF_CNF",
0x1015 : "ID_XCALL_XCC_SEND_FLASH_REQ",
0x1016 : "ID_XCC_XCALL_SEND_FLASH_CNF",
0x1017 : "ID_XCC_XCALL_INFO_REC_IND",
0x1018 : "ID_XCC_XCALL_NDSS_RESULT_IND",
0x1019 : "ID_XCALL_XCC_SEND_CONT_DTMF_REQ",
0x101A: "ID_XCC_XCALL_SEND_CONT_DTMF_CNF",
0x101B : "ID_XCC_XCALL_CONT_DTMF_IND",
0x101C : "ID_XCC_XCALL_BURST_DTMF_IND",
0x101D : "ID_XCALL_XCC_ECC_SERVICE_REQ",
0x101E : "ID_XCC_XCALL_ECC_SERVICE_CNF",
0x101F : "ID_XCC_XCALL_TCH_ASSIGN_CMPL_IND",
0x1020 : "ID_XCALL_XCC_PRIVACY_MODE_SET_REQ",
0x1021 : "ID_XCC_XCALL_PRIVACY_MODE_SET_CNF",
0x1022 : "ID_XCALL_XCC_PRIVACY_MODE_QRY_REQ",
0x1023 : "ID_XCC_XCALL_PRIVACY_MODE_QRY_CNF",
0x1024 : "ID_XCC_XCALL_PRIVACY_MODE_IND",
}

def get_xcc_taf_msg_str( MsgId):
    for MsgIdIndex in xcc_taf_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return xcc_taf_msg_enum_table[MsgIdIndex]

    return "none"