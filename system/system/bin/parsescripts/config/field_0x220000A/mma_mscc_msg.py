#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mma mscc msg
author          :   j00354216
modify  record  :   2016-01-27 create file
"""

mma_mscc_msg_enum_table = {
0x0001 : "ID_MSCC_MMC_START_REQ",
0x0002 : "ID_MMA_MSCC_SIGN_REPORT_REQ",
0x0003 : "ID_MMA_MSCC_MODE_CHANGE_REQ",
0x0004 : "ID_MMA_MSCC_ATTACH_REQ",
0x0005 : "ID_MMA_MSCC_DETACH_REQ",
0x0006 : "ID_MMA_MSCC_PLMN_LIST_REQ",
0x0007 : "ID_MMA_MSCC_PLMN_LIST_ABORT_REQ",
0x0008 : "ID_MMA_MSCC_PLMN_USER_RESEL_REQ",
0x0009 : "ID_MMA_MSCC_PLMN_SPECIAL_REQ",
0x000A : "ID_MMA_MSCC_POWER_OFF_REQ",
0x000B : "ID_MMA_MSCC_SYS_CFG_SET_REQ",
0x000C : "ID_MMA_MSCC_SYSTEM_ACQUIRE_REQ",
0x000D : "ID_MMA_MSCC_SPEC_PLMN_SEARCH_ABORT_REQ",
0x000E : "ID_MMA_MSCC_OM_MAINTAIN_INFO_IND",
0x000F : "ID_MMA_MSCC_UPDATE_UPLMN_NTF",
0x0010 : "ID_MMA_MSCC_EOPLMN_SET_REQ",
0x0011 : "ID_MMA_MSCC_NET_SCAN_REQ",
0x0012 : "ID_MMA_MSCC_ABORT_NET_SCAN_REQ",
0x0013 : "ID_MMA_MSCC_OTHER_MODEM_INFO_NOTIFY",
0x0014 : "ID_MMA_MSCC_NCELL_INFO_NOTIFY",
0x0015 : "ID_MMA_MSCC_PS_TRANSFER_NOTIFY",
0x0016 : "ID_MMA_MSCC_ACQ_REQ",
0x0017 : "ID_MMA_MSCC_REG_REQ",
0x0018 : "ID_MMA_MSCC_POWER_SAVE_REQ",
0x0019 : "ID_MMA_MSCC_SRV_ACQ_REQ",
0x001A : "ID_MMA_MSCC_BEGIN_SESSION_NOTIFY",
0x001B : "ID_MMA_MSCC_END_SESSION_NOTIFY",
0x001C : "ID_MMA_MSCC_IMS_SRV_INFO_NOTIFY",
0x001D : "ID_MMA_MSCC_OTHER_MODEM_DPLMN_NPLMN_INFO_NOTIFY",
0x001E : "ID_MMA_MSCC_CDMA_MO_CALL_START_NTF",
0x001F : "ID_MMA_MSCC_CDMA_MO_CALL_REDIAL_SYS_ACQ_NTF",
0x0020 : "ID_MMA_MSCC_CDMA_MO_CALL_SUCCESS_NTF",
0x0021 : "ID_MMA_MSCC_CDMA_MO_CALL_END_NTF",
0x0022 : "ID_MMA_MSCC_CFREQ_LOCK_NTF",
0x0023 : "ID_MMA_MSCC_CDMACSQ_SET_REQ",
0x0024 : "ID_MMA_MSCC_CFPLMN_SET_REQ",
0x0025 : "ID_MMA_MSCC_CFPLMN_QUERY_REQ",
0x0026 : "ID_MMA_MSCC_SDT_CONNECTED_IND",
0x0027 : "ID_MMA_MSCC_PREF_PLMN_SET_REQ",
0x0028 : "ID_MMA_MSCC_PREF_PLMN_QUERY_REQ",
0x0029 : "ID_MMA_MSCC_IMS_START_REQ",
0x002A : "ID_MMA_MSCC_IMS_STOP_REQ",
0x002B : "ID_MMA_MSCC_VOICE_DOMAIN_CHANGE_IND",
0x002C : "ID_MMA_MSCC_AUTO_RESEL_SET_REQ",
0x002D : "ID_MMA_MSCC_HANDSET_INFO_QRY_REQ",
0x002E : "ID_MMA_MSCC_GET_GEO_REQ",
0X002F : "ID_MMA_MSCC_STOP_GET_GEO_REQ",
0x0030 : "ID_MMA_MSCC_PS_RAT_TYPE_NTF",
0x0031 : "ID_MMA_MSCC_QUIT_CALL_BACK_NTF",
0x0032 : "ID_MMA_MSCC_SET_CSIDLIST_REQ",
0x0033 : "ID_MMA_MSCC_DPLMN_SET_REQ",
0x0034 : "ID_MMA_MSCC_CSG_LIST_SEARCH_REQ",
0x0035 : "ID_MMA_MSCC_CSG_LIST_ABORT_REQ",
0x0036 : "ID_MMA_MSCC_CSG_SPEC_SEARCH_REQ",
0x0037 : "ID_MMA_MSCC_CSG_SPEC_SEARCH_ABORT_REQ",
0x0038 : "ID_MMA_MSCC_IMS_DOMAIN_CFG_SET_REQ",
0x0039 : "ID_MMA_MSCC_ROAM_IMS_SUPPORT_SET_REQ",
0x003A : "ID_MMA_MSCC_AP_AREA_LOST_IND",
0x003B : "ID_MMA_MSCC_IMS_REG_DOMAIN_NOTIFY",
0x003C : "ID_MMA_MSCC_RPM_INFO_NTF",
0x003D : "ID_MMA_MSCC_LTE_LOST",
0x003E : "ID_MMA_MSCC_MULTIMODE_CFG_NOTIFY",
0x003F : "ID_MMA_MSCC_CDMA_ENTER_DORM_FOR_PRIOR_SYS_NTF",
0x0040 : "ID_MMA_MSCC_EFLOCIINFO_SET_REQ",
0x0041 : "ID_MMA_MSCC_EFLOCIINFO_QRY_REQ",
0x0042 : "ID_MMA_MSCC_EFPSLOCIINFO_SET_REQ",
0x0043 : "ID_MMA_MSCC_EFPSLOCIINFO_QRY_REQ",
0x0044 : "ID_MMA_MSCC_BORDER_INFO_SET_REQ",
0x0045 : "ID_MMA_MSCC_CDMA_MO_SMS_START_NTF",
0X0046 : "ID_MMA_MSCC_CDMA_MO_SMS_END_NTF",
0x0047 : "ID_MMA_MSCC_IMS_SMS_CFG_SET_REQ",
0x0048 : "ID_MMA_MSCC_ACDC_APP_NOTIFY",
0x0049 : "ID_MMA_MSCC_IMS_SWITCH_SET_REQ",
0x004A : "ID_MMA_MSCC_IMS_VIDEO_CALL_CAP_SET_REQ",
0x004B : "ID_MMA_MSCC_USIM_STATUS_NOTIFY",
0x004C : "ID_MMA_MSCC_MODE_SWITCH_RSP",
0x004D : "ID_MMA_MSCC_NO_CARD_NTY",
0x004E : "ID_MMA_MSCC_RCS_SWITCH_QRY_REQ",
0x004F : "ID_MMA_MSCC_EMC_STATUS_NOTIFY",
0x0050 : "ID_MMA_MSCC_UE_USAGE_SETTING_IND",
0x0051 : "ID_MMA_MSCC_VOLTE_EMC_380_FAIL_NTF",
0x1001 : "ID_MSCC_MMA_START_CNF",
0x1002 : "ID_MSCC_MMA_3GPP_SYS_INFO_IND",
0x1003 : "ID_MSCC_MMA_SERVICE_STATUS_IND",
0x1004 : "ID_MSCC_MMA_MM_INFO_IND",
0x1005 : "ID_MSCC_MMA_ATTACH_CNF",
0x1006 : "ID_MSCC_MMA_DETACH_CNF",
0x1007 : "ID_MSCC_MMA_DETACH_IND",
0x1008 : "ID_MSCC_MMA_PLMN_LIST_CNF",
0x1009 : "ID_MSCC_MMA_PLMN_LIST_REJ",
0x100A : "ID_MSCC_MMA_COVERAGE_AREA_IND",
0x100B : "ID_MSCC_MMA_POWER_OFF_CNF",
0x100C : "ID_MSCC_MMA_RSSI_IND",
0x100D : "ID_MSCC_MMA_PLMN_SPECIAL_SEL_CNF",
0x100E : "ID_MSCC_MMA_DATATRAN_ATTRI_IND",
0x100F : "ID_MSCC_MMA_SYS_CFG_CNF",
0x1010 : "ID_MSCC_MMA_SYSTEM_ACQUIRE_END_IND",
0x1011 : "ID_MSCC_MMA_PLMN_LIST_ABORT_CNF",
0x1012 : "ID_MSCC_MMA_SPEC_PLMN_SEARCH_ABORT_CNF",
0x1013 : "ID_MSCC_MMA_UMTS_CIPHER_INFO_IND",
0x1014 : "ID_MSCC_MMA_GPRS_CIPHER_INFO_IND",
0x1015 : "ID_MSCC_MMA_PLMN_SPECIAL_SEL_REJ",
0x1016 : "ID_MSCC_MMA_AC_INFO_CHANGE_IND",
0x1017 : "ID_MSCC_MMA_PLMN_RESEL_CNF",
0x1018 : "ID_MSCC_MMA_REG_RESULT_IND",
0x1019 : "ID_MSCC_MMA_SYSTEM_ACQUIRE_START_IND",
0x101A : "ID_MSCC_MMA_EOPLMN_SET_CNF",
0x101B : "ID_MSCC_MMA_USIM_AUTH_FAIL_IND",
0x101C : "ID_MSCC_MMA_NET_SCAN_CNF",
0x101D : "ID_MSCC_MMA_ABORT_NET_SCAN_CNF",
0x101E : "ID_MSCC_MMA_NETWORK_CAPABILITY_INFO_IND",
0x101F : "ID_MSCC_MMA_CAMP_ON_IND",
0x1020 : "ID_MSCC_MMA_EPLMN_INFO_IND",
0x1021 : "ID_MSCC_MMA_CS_SERVICE_CONN_STATUS_IND",
0x1022 : "ID_MSCC_MMA_SRV_REJ_IND",
0x1023 : "ID_MSCC_MMA_ACQ_CNF",
0x1024 : "ID_MSCC_MMA_REG_CNF",
0x1025 : "ID_MSCC_MMA_POWER_SAVE_CNF",
0x1026 : "ID_MSCC_MMA_ACQ_IND",
0x1027 : "ID_MSCC_MMA_PS_SERVICE_CONN_STATUS_IND",
0x1028 : "ID_MSCC_MMA_RF_AVAILABLE_IND",
0x1029 : "ID_MSCC_MMA_SRV_ACQ_CNF",
0x102A : "ID_MSCC_MMA_LMM_CELL_SIGN_INFO_REPORT_IND",
0x102B : "ID_MSCC_MMA_IMS_VOICE_CAP_IND",
0x102C : "ID_MSCC_MMA_1X_SYSTEM_SERVICE_INFO_IND",
0x102D : "ID_MSCC_MMA_CDMACSQ_SET_CNF",
0x102E : "ID_MSCC_MMA_CDMACSQ_SIGNAL_QUALITY_IND",
0x102F : "ID_MSCC_MMA_HRPD_SERVICE_STATUS_IND",
0x1030 : "ID_MSCC_MMA_CFPLMN_SET_CNF",
0x1031 : "ID_MSCC_MMA_CFPLMN_QUERY_CNF",
0x1032 : "ID_MSCC_MMA_PREF_PLMN_SET_CNF",
0x1033 : "ID_MSCC_MMA_PREF_PLMN_QUERY_CNF",
0x1034 : "ID_MSCC_MMA_HRPD_OVERHEAD_MSG_IND",
0x1035 : "ID_MSCC_MMA_HRPD_SYS_ACQ_CNF",
0x1036 : "ID_MSCC_MMA_1X_SYSTEM_TIME_IND",
0x1038 : "ID_MSCC_MMA_IMS_SWITCH_STATE_IND",
0x1039 : "ID_MSCC_MMA_IMS_START_CNF",
0x103A : "ID_MSCC_MMA_IMS_STOP_CNF",
0x103B : "ID_MSCC_MMA_INTERSYS_START_IND",   
0x103C : "ID_MSCC_MMA_INTERSYS_END_IND",   
0x103D : "ID_MSCC_MMA_HANDSET_INFO_QRY_CNF",   
0x103E : "ID_MSCC_MMA_GET_GEO_CNF",
0x103F : "ID_MSCC_MMA_STOP_GET_GEO_CNF", 
0x1042 : "ID_MSCC_MMA_1X_SID_NID_IND",
0x1043 : "ID_MSCC_MMA_SET_CSIDLIST_CNF",
0x1044 : "ID_MSCC_MMA_1X_EMC_CALL_BACK_IND", 
0x1045 : "ID_MSCC_MMA_SYNC_SERVICE_AVAIL_IND", 
0x1046 : "ID_MSCC_MMA_SRCHED_PLMN_INFO_IND",
0x1047 : "ID_MSCC_MMA_1X_UE_STATUS_IND",
0x1048 : "ID_MMA_MSCC_HDR_CSQ_SET_REQ",
0x1049 : "ID_MSCC_MMA_HDR_CSQ_SET_CNF",
0x104A : "ID_MSCC_MMA_HDR_CSQ_QUALITY_IND",
0x104B : "ID_MSCC_MMA_DPLMN_SET_CNF",
0x104C : "ID_MSCC_MMA_CSG_LIST_SEARCH_CNF",
0x104D : "ID_MSCC_MMA_CSG_LIST_ABORT_CNF",
0x104E : "ID_MSCC_MMA_CSG_LIST_REJ",
0x104F : "ID_MSCC_MMA_DATA_CALL_REDIAL_SYS_ACQ_IND",
0x1050 : "ID_MSCC_MMA_CSG_SPEC_SEARCH_CNF",
0x1051 : "ID_MSCC_MMA_CSG_SPEC_SEARCH_ABORT_CNF",
0x1052 : "ID_MSCC_MMA_CSG_ID_HOME_NODEB_NAME_IND",
0x1053 : "ID_MSCC_MMA_IMS_DOMAIN_CFG_SET_CNF",
0x1054 : "ID_MSCC_MMA_ROAM_IMS_SUPPORT_SET_CNF",
0x1055 : "ID_MSCC_MMA_PRL_HEADER_INFO_IND",
0x1056 : "ID_MSCC_MMA_MSPL_MLPL_HEADER_INFO_IND",
0x1057 : "ID_MSCC_MMA_MODE_SWITCH_IND",
}

def get_mma_mscc_msg_str( MsgId):
    for MsgIdIndex in mma_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mma_mscc_msg_enum_table[MsgIdIndex]

    return "none"