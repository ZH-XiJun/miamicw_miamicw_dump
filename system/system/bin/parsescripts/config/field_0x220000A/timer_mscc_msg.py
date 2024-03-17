#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list timer mscc msg
author          :   j00354216
modify  record  :   2016-01-27 create file
"""

timer_mscc_msg_enum_table = {
0x00 : "TI_NAS_MSCC_WAIT_IMSA_START_CNF",
0x01 : "TI_NAS_MSCC_WAIT_IMSA_POWER_OFF_CNF",
0x02 : "TI_NAS_MSCC_WAIT_XSD_START_CNF",
0x03 : "TI_NAS_MSCC_WAIT_XSD_POWER_OFF_CNF",
0x04 : "TI_NAS_MSCC_WAIT_HSD_START_CNF",
0x05 : "TI_NAS_MSCC_WAIT_HSD_POWER_OFF_CNF",
0x06 : "TI_NAS_MSCC_WAIT_MMC_START_CNF",
0x07 : "TI_NAS_MSCC_WAIT_MMC_POWER_OFF_CNF",
0x08 : "TI_NAS_MSCC_WAIT_IMSA_IMS_VOICE_CAP_NOTIFY",
0x09 : "TI_NAS_MSCC_WAIT_HSD_BG_SEARCH_CNF",
0x0A : "TI_NAS_MSCC_WAIT_HSD_STOP_BG_SEARCH_CNF",
0x0B : "TI_NAS_MSCC_WAIT_MMC_QRY_PLMN_PRI_CLASS_CNF",
0x0C : "TI_NAS_MSCC_BSR_TIMER",
0x0D : "TI_NAS_MSCC_PERIOD_TRYING_HIGH_PRI_SYSTEM_SEARCH",
0x0E : "TI_NAS_MSCC_WAIT_HSD_ACQUIRE_CNF",
0x0F : "TI_NAS_MSCC_WAIT_HSD_POWER_SAVE_CNF",
0x10 : "TI_NAS_MSCC_WAIT_XSD_POWER_SAVE_CNF",
0x11 : "TI_NAS_MSCC_WAIT_MMC_PLMN_SEARCH_CNF",
0x12 : "TI_NAS_MSCC_WAIT_MMC_POWER_SAVE_CNF",
0x13 : "TI_NAS_MSCC_WAIT_CL_POWER_SAVE_CNF",
0x14 : "TI_NAS_MSCC_WAIT_INIT_LOC_INFO_IND",
0x15 : "TI_NAS_MSCC_SCAN_TIMER",
0x16 : "TI_NAS_MSCC_SLEEP_TIMER",
0x17 : "TI_NAS_MSCC_AVAILABLE_TIMER",
0x18 : "TI_NAS_MSCC_WAIT_CARD_READ_CNF",
0x19 : "TI_NAS_MSCC_WAIT_MMC_BG_SEARCH_CNF",
0x1A : "TI_NAS_MSCC_WAIT_MMC_STOP_BG_SEARCH_CNF",
0x1B : "TI_NAS_MSCC_WAIT_HSD_QRY_HRPD_SYS_INFO_CNF",
0x1C : "TI_NAS_MSCC_WAIT_XSD_SYS_CFG_CNF",
0x1D : "TI_NAS_MSCC_WAIT_HSD_SYS_CFG_CNF",
0x1E : "TI_NAS_MSCC_WAIT_MMC_SYS_CFG_CNF",
0x1F : "TI_NAS_MSCC_WAIT_CL_INTERSYS_END_IND",
0x20 : "TI_NAS_MSCC_1X_SERVICE_CL_SYSTEM_ACQUIRE_PHASE_ONE_TOTAL_TIMER",
0x21 : "TI_NAS_MSCC_WAIT_MMC_RF_AVAILABLE_IND",
0x22 : "TI_NAS_MSCC_1X_BSR_LTE_TIMER",
0x23 : "TI_NAS_MSCC_WAIT_IMSA_REG_CNF",
0x24 : "TI_NAS_MSCC_MODE_SELECTION_RETRY_TIMER",
0x25 : "TI_NAS_MSCC_MODE_SELECTION_WAIT_POWER_SAVE_CNF",
0x26 : "TI_NAS_MSCC_MODE_SELECTION_WAIT_SYS_CFG_CNF",
0x27 : "TI_NAS_MSCC_MODE_SELECTION_XSD_SYS_ACQ_CNF",
0x28 : "TI_NAS_MSCC_MODE_SELECTION_HSD_SYS_ACQ_CNF",
0x29 : "TI_NAS_MSCC_MODE_SELECTION_MMC_SYS_ACQ_CNF",
0x2A : "TI_NAS_MSCC_SYS_ACQ_WAIT_HSD_OVERHEAD_MSG_IND_IN_SRLTE",
0x2B : "TI_NAS_MSCC_WAIT_EHSM_DETACH_CNF",
}

def get_timer_mscc_msg_str( MsgId):
    for MsgIdIndex in timer_mscc_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return timer_mscc_msg_enum_table[MsgIdIndex]

    return "none"