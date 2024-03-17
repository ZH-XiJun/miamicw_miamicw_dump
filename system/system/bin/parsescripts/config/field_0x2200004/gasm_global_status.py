#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gasm global status
author          :   sunbing 00184266
modify  record  :   2016-01-09 create file
"""

MACRO_GPHY_MASTER_MODE_BUTT_INDEX   = 0x5
MACRO_SIM_STATUS_BUTT_INDEX         = 0x3
MACRO_RAT_PRIO_BUTT_INDEX           = 0x4

gasm_gphy_master_mode_enum_table = {
0x0 : "GAS_MASTER_MODE_NONE",
0x1 : "GAS_MASTER_MODE_GSM",
0x2 : "GAS_MASTER_MODE_WCDMA",
0x3 : "GAS_MASTER_MODE_TDSCDMA",
0x4 : "GAS_MASTER_MODE_LTE",
0x5 : "GAS_MASTER_MODE_BUTT",
}

gasm_sim_status_enum_table = {
0x0 : "RRC_NAS_UICC_ABSENT",
0x1 : "RRC_NAS_USIM_PRESENT",
0x2 : "RRC_NAS_SIM_PRESET",
0x3 : "RRC_NAS_SIM_STATUS_BUTT",
}

gasm_rat_prio_enum_table = {
0x0 : "RRMM_RAT_PRIO_NULL",
0x1 : "RRMM_RAT_PRIO_LOW",
0x2 : "RRMM_RAT_PRIO_MIDDLE",
0x3 : "RRMM_RAT_PRIO_HIGH",
0x4 : "RRMM_RAT_PRIO_BUTT",
}

def get_gas_gphy_master_mode( enGphyMasterMode):
    for index in gasm_gphy_master_mode_enum_table.keys():
        if index == enGphyMasterMode:
            return gasm_gphy_master_mode_enum_table[index]

    return gasm_gphy_master_mode_enum_table[MACRO_GPHY_MASTER_MODE_BUTT_INDEX]

def get_gas_sim_status( ulSimStatus):
    for index in gasm_sim_status_enum_table.keys():
        if index == ulSimStatus:
            return gasm_sim_status_enum_table[index]

    return gasm_sim_status_enum_table[MACRO_SIM_STATUS_BUTT_INDEX]

def get_gas_rat_prio( enRatPrio):
    for index in gasm_rat_prio_enum_table.keys():
        if index == enRatPrio:
            return gasm_rat_prio_enum_table[index]

    return gasm_sim_status_enum_table[MACRO_RAT_PRIO_BUTT_INDEX]