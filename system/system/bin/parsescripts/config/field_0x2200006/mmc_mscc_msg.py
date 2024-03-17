#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list mmc mscc msg
author          :   wumai 00167002
modify  record  :   2016-01-22 create file
"""

mmc_mscc_msg_enum_table = {
#mscc->mmc
0x4000 : "ID_MSCC_MMC_START_REQ",
0x4002 : "ID_MSCC_MMC_SIGN_REPORT_REQ",
0x4004 : "ID_MSCC_MMC_MODE_CHANGE_REQ",
0x4006 : "ID_MSCC_MMC_ATTACH_REQ",
0x4008 : "ID_MSCC_MMC_DETACH_REQ",
0x400A : "ID_MSCC_MMC_PLMN_LIST_REQ",
0x400C : "ID_MSCC_MMC_PLMN_LIST_ABORT_REQ",
0x400E : "ID_MSCC_MMC_PLMN_USER_RESEL_REQ",
0x4010 : "ID_MSCC_MMC_PLMN_SPECIAL_REQ",
0x4012 : "ID_MSCC_MMC_POWER_OFF_REQ",
0x4014 : "ID_MSCC_MMC_SYS_CFG_SET_REQ",
0x4016 : "ID_MSCC_MMC_PLMN_SEARCH_REQ",
0x4018 : "ID_MSCC_MMC_SPEC_PLMN_SEARCH_ABORT_REQ",
0x401A : "ID_MSCC_MMC_OM_MAINTAIN_INFO_IND",
0x401C : "ID_MSCC_MMC_UPDATE_UPLMN_NTF",
0x401E : "ID_MSCC_MMC_EOPLMN_SET_REQ",
0x4020 : "ID_MSCC_MMC_NET_SCAN_REQ",
0x4022 : "ID_MSCC_MMC_ABORT_NET_SCAN_REQ",
0x4024 : "ID_MSCC_MMC_OTHER_MODEM_INFO_NOTIFY",
0x4026 : "ID_MSCC_MMC_NCELL_INFO_NOTIFY",
0x4028 : "ID_MSCC_MMC_PS_TRANSFER_NOTIFY",
0x402A : "ID_MSCC_MMC_IMS_VOICE_CAP_NOTIFY",
0x402C : "ID_MSCC_MMC_ACQ_REQ",
0x402E : "ID_MSCC_MMC_REG_REQ",
0x4030 : "ID_MSCC_MMC_POWER_SAVE_REQ",
0x4032 : "ID_MSCC_MMC_SRV_ACQ_REQ",
0x4034 : "ID_MSCC_MMC_BEGIN_SESSION_NOTIFY",
0x4036 : "ID_MSCC_MMC_END_SESSION_NOTIFY",
0x4038 : "ID_MSCC_MMC_IMS_SRV_INFO_NOTIFY",
0x403A : "ID_MSCC_MMC_OTHER_MODEM_DPLMN_NPLMN_INFO_NOTIFY",
0x403C : "ID_MSCC_MMC_CFPLMN_SET_REQ",
0x403E : "ID_MSCC_MMC_CFPLMN_QUERY_REQ",
0x4040 : "ID_MSCC_MMC_SDT_CONNECTED_IND",
0x4042 : "ID_MSCC_MMC_PREF_PLMN_SET_REQ",
0x4044 : "ID_MSCC_MMC_PREF_PLMN_QUERY_REQ",
0x4046 : "ID_MSCC_MMC_IMS_SWITCH_STATE_IND",
0x4048 : "ID_MSCC_MMC_VOICE_DOMAIN_CHANGE_IND",
0x404A : "ID_MSCC_MMC_BG_SEARCH_REQ",
0x404C : "ID_MSCC_MMC_INTERSYS_HRPD_NTF",
0x404E : "ID_MSCC_MMC_MMSS_INFO_NTF",
0x4050 : "ID_MSCC_MMC_STOP_BG_SEARCH_REQ",
0x4052 : "ID_MSCC_MMC_PLMN_PRI_CLASS_QUERY_REQ",
0x4054 : "ID_MSCC_MMC_AUTO_RESEL_SET_REQ",
0x4056 : "ID_MSCC_MMC_GET_GEO_REQ",
0x4058 : "ID_MSCC_MMC_STOP_GET_GEO_REQ",
0x405A : "ID_MSCC_MMC_CL_ASSOCIATED_INFO_NTF",
0x405C : "ID_MSCC_MMC_DPLMN_SET_REQ",
0x405E : "ID_MSCC_MMC_CSG_LIST_SEARCH_REQ",
0x4060 : "ID_MSCC_MMC_CSG_LIST_ABORT_REQ",
0x4062 : "ID_MSCC_MMC_CL_INTERSYS_START_NTF",
0x4064 : "ID_MSCC_MMC_CSG_SPEC_SEARCH_REQ",
0x4066 : "ID_MSCC_MMC_CSG_SPEC_SEARCH_ABORT_REQ",
0x4068 : "ID_MSCC_MMC_CURR_GEO_INFO_NTF",
0x406A : "ID_MSCC_MMC_EPLMN_INFO_NTF",
0x406C : "ID_MSCC_MMC_IMS_REG_DOMAIN_NOTIFY",
0x406E : "ID_MSCC_MMC_RPM_INFO_NTF",
0x4070 : "ID_MSCC_MMC_LTE_LOST_IND",
0x4072 : "ID_MSCC_MMC_EFLOCIINFO_SET_REQ",
0x4074 : "ID_MSCC_MMC_EFLOCIINFO_QRY_REQ",
0x4076 : "ID_MSCC_MMC_EFPSLOCIINFO_SET_REQ",
0x4078 : "ID_MSCC_MMC_EFPSLOCIINFO_QRY_REQ",
0x407A : "ID_MSCC_MMC_BORDER_INFO_SET_REQ",
0x407C : "ID_MSCC_MMC_ACDC_APP_NOTIFY",
0x407E : "ID_MSCC_MMC_USIM_STATUS_NOTIFY",
0x4080 : "ID_MSCC_MMC_NO_CARD_NTY",
0x4082 : "ID_MSCC_MMC_SCREEN_STA_CHANGE_NOTIFY",
0x4084 : "ID_MSCC_MMC_ECBM_NTF",
0x4086 : "ID_MSCC_MMC_EMC_STATUS_NOTIFY",
0x4088 : "ID_MSCC_MMC_UE_USAGE_SETTING_CHANGE_IND",
0x408A : "ID_MSCC_MMC_1X_UE_STATUS_IND",
0x408C : "ID_MSCC_MMC_VOLTE_EMC_380_FAIL_NTF",
#mmc->mscc
0x4001 : "ID_MMC_MSCC_START_CNF",
0x4003 : "ID_MMC_MSCC_SYS_INFO_IND",
0x4005 : "ID_MMC_MSCC_SERVICE_STATUS_IND",
0x4007 : "ID_MMC_MSCC_MM_INFO_IND",
0x4009 : "ID_MMC_MSCC_ATTACH_CNF",
0x400B : "ID_MMC_MSCC_DETACH_CNF",
0x400D : "ID_MMC_MSCC_DETACH_IND",
0x400F : "ID_MMC_MSCC_PLMN_LIST_CNF",
0x4011 : "ID_MMC_MSCC_PLMN_LIST_REJ",
0x4013 : "ID_MMC_MSCC_COVERAGE_AREA_IND",
0x4015 : "ID_MMC_MSCC_POWER_OFF_CNF",
0x4017 : "ID_MMC_MSCC_RSSI_IND",
0x4019 : "ID_MMC_MSCC_PLMN_SPECIAL_SEL_CNF",
0x401B : "ID_MMC_MSCC_DATATRAN_ATTRI_IND",
0x401D : "ID_MMC_MSCC_SYS_CFG_CNF",
0x401F : "ID_MMC_MSCC_PLMN_SELECTION_RLST_IND",
0x4021 : "ID_MMC_MSCC_PLMN_LIST_ABORT_CNF",
0x4023 : "ID_MMC_MSCC_SPEC_PLMN_SEARCH_ABORT_CNF",
0x4025 : "ID_MMC_MSCC_UMTS_CIPHER_INFO_IND",
0x4027 : "ID_MMC_MSCC_GPRS_CIPHER_INFO_IND",
0x4029 : "ID_MMC_MSCC_PLMN_SPECIAL_SEL_REJ",
0x402B : "ID_MMC_MSCC_AC_INFO_CHANGE_IND",
0x402D : "ID_MMC_MSCC_PLMN_RESEL_CNF",
0x402F : "ID_MMC_MSCC_REG_RESULT_IND",
0x4031 : "ID_MMC_MSCC_PLMN_SELE_START_IND",
0x4033 : "ID_MMC_MSCC_EOPLMN_SET_CNF",
0x4035 : "ID_MMC_MSCC_USIM_AUTH_FAIL_IND",
0x4037 : "ID_MMC_MSCC_NET_SCAN_CNF",
0x4039 : "ID_MMC_MSCC_ABORT_NET_SCAN_CNF",
0x403B : "ID_MMC_MSCC_NETWORK_CAPABILITY_INFO_IND",
0x403D : "ID_MMC_MSCC_CAMP_ON_IND",
0x403F : "ID_MMC_MSCC_EPLMN_INFO_IND",
0x4041 : "ID_MMC_MSCC_CS_SERVICE_CONN_STATUS_IND",
0x4043 : "ID_MMC_MSCC_SRV_REJ_IND",
0x4045 : "ID_MMC_MSCC_ACQ_CNF",
0x4047 : "ID_MMC_MSCC_REG_CNF",
0x4049 : "ID_MMC_MSCC_POWER_SAVE_CNF",
0x404B : "ID_MMC_MSCC_ACQ_IND",
0x404D : "ID_MMC_MSCC_PS_SERVICE_CONN_STATUS_IND",
0x404F : "ID_MMC_MSCC_RF_AVAILABLE_IND",
0x4051 : "ID_MMC_MSCC_SRV_ACQ_CNF",
0x4053 : "ID_MMC_MSCC_LMM_CELL_SIGN_INFO_REPORT_IND",
0x4057 : "ID_MMC_MSCC_CFPLMN_SET_CNF",
0x4059 : "ID_MMC_MSCC_CFPLMN_QUERY_CNF",
0x405B : "ID_MMC_MSCC_PREF_PLMN_SET_CNF",
0x405D : "ID_MMC_MSCC_PREF_PLMN_QUERY_CNF",
0x405F : "ID_MMC_MSCC_BG_SEARCH_CNF",
0x4061 : "ID_MMC_MSCC_STOP_BG_SEARCH_CNF",
0x4063 : "ID_MMC_MSCC_PREF_PLMN_INFO_IND",
0x4065 : "ID_MMC_MSCC_MMSS_LTE_UNAVAILABLE_IND",
0x4067 : "ID_MMC_MSCC_PLMN_PRI_CLASS_QUERY_CNF",
0x4069 : "ID_MMC_MSCC_GET_GEO_CNF",
0x406B : "ID_MMC_MSCC_STOP_GET_GEO_CNF",
0x406D : "ID_MMC_MSCC_SRCHED_PLMN_INFO_IND",
0x406F : "ID_MMC_MSCC_DPLMN_SET_CNF",
0x4071 : "ID_MMC_MSCC_INTERSYS_START_IND",
0x4073 : "ID_MMC_MSCC_INTERSYS_END_IND",
0x4075 : "ID_MMC_MSCC_CSG_LIST_SEARCH_CNF",
0x4077 : "ID_MMC_MSCC_CSG_LIST_ABORT_CNF",
0x4079 : "ID_MMC_MSCC_CSG_LIST_REJ",
0x407B : "ID_MMC_MSCC_CSG_SPEC_SEARCH_CNF",
0x407D : "ID_MMC_MSCC_CSG_SPEC_SEARCH_ABORT_CNF",
0x407F : "ID_MMC_MSCC_CSG_ID_HOME_NODEB_NAME_IND",
0x4081 : "ID_MMC_MSCC_PS_REG_CN_RSLT_IND",
0x4083 : "ID_MMC_MSCC_BORDER_INFO_SET_CNF",
0x4085 : "ID_MMC_MSCC_EFLOCIINFO_SET_CNF",
0x4087 : "ID_MMC_MSCC_EFLOCIINFO_QRY_CNF",
0x4089 : "ID_MMC_MSCC_EFPSLOCIINFO_SET_CNF",
0x408B : "ID_MMC_MSCC_EFPSLOCIINFO_QRY_CNF",
0x408D : "ID_MMC_MSCC_DISPLAY_SERVICE_STATUS_IND",
0x408F : "ID_MMC_MSCC_LTE_COMBINED_START_IND",
0x4091 : "ID_MMC_MSCC_TAU_END_IND",
0x4093 : "ID_MMC_MSCC_GET_GEO_IND",
0x4095 : "ID_MMC_MSCC_GPRS_STATE_IND",
0x4097 : "ID_MMC_MSCC_CSFB_STATE_INFO_IND",
0x4099 : "ID_MMC_MSCC_CS_PAGING_IND",
0x409B : "ID_MMC_MSCC_CONNECTED_LOCATION_INFO_IND",
0x409D : "ID_MMC_MSCC_HIGH_PRIO_PS_STATE_IND",
}

def get_mmc_mscc_msg_str( MsgId):
    for MsgIdIndex in mmc_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return mmc_mscc_msg_enum_table[MsgIdIndex]

    return "none"