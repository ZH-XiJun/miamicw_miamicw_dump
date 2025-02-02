#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   list pid
author          :   yudihu 00307564
modify  record  :   2018-05-14 create file
"""

import string

nrnas_pid_enum_table = {
     1: "TIMER",
     2: "GCOMC",
     6: "I1_MSCC",
    11: "I1_WRR",
    20: "I1_USIM",
    21: "I1_STK",
    22: "I1_PIH",
    23: "I1_PB",
    24:	"I1_GRM",
    25: "I1_DL",
    26:	"I1_LL",
    27: "I1_SN",
    28:	"I1_GAS",
    29:	"I1_MM",
    30:	"I1_MMC",
    31:	"I1_GMM",
    32: "I1_MMA",
    33: "I1_CC",
    34: "I1_SS",
    35: "I1_TC",
    36: "I1_SMS",
    37: "I1_RABM",
    38: "I1_SM",
    40: "I1_TAF",
    41: "T1_VC",
    42: "I1_DRV_AGENT",
    43: "I1_MTA",
    44:	"I1_GPHY",
    45: "I1_DRX",
    46: "I1_IDLE",
    47: "I1_APM",
    48: "I1_SLEEP",
    88: "EHSM",
    98: "I1_NAS",
    99: "NAS",
   123: "I1_LMM",
   100: "TOOL",
   101: "USIM",
   102: "SI_STK",
   103: "SI_PIH",
   104: "SI_PB",
   118: "MSCC",
   128:	"GAS",
   129:	"LAPDM",
   130: "GRM",
   131: "LL",
   132: "SN",
   133: "WRR",
   134: "WCOM",
   140: "RABM",
   141: "MMC",
   142: "MM",
   143: "GMM",
   144: "CC",
   145: "SM",
   146: "SMS",
   147: "SS",
   148: "TC",
   152: "TAF",
   153: "PPP",
   155: "NAS_COMM",
   156: "I1_NAS_COMM",
   157: "MMA",
   158: "SLEEP",
   165: "VC",
   170: "CSS",
   171: "ERRC",
   172: "ERMM",
   173: "LMM",
   174: "ESM",
   175: "PS_RABM",
   201: "APM",
   203: "WPHY",
   205: "GPHY",
   209: "MTA",
   217: "TRRC",
   219: "MTC",
   222: "IMSA",
   225: "RRM",
   232: "I2_MM",
   233: "I2_MMC",
   234: "I2_GMM",
   235: "I2_MMA",
   236: "I2_CC",
   237: "I2_SS",
   238: "I2_TC",
   239: "I2_SMS",
   240: "I2_RABM",
   241: "I2_SM",
   243: "I2_TAF",
   244: "I2_VC",
   245: "I2_DRV_AGENT",
   246: "I2_MTA",
   247: "I2_MSCC",
   250: "I2_NAS_COMM",
   254: "I2_USIM",
   260: "I2_LL",
   262: "I2_GAS",
   296: "REGM",
   297: "I1_REGM",
   298: "I2_REGM",
   308: "DSM",
   131072: "NRRC",
   131077: "NRMM",
   131078: "SDAP_UL",
   131086: "NRSM",
   131089: "PCF",
   131090: "NREAP" 
}

def nrnas_get_pid_str( pid):
    for pidIndex in nrnas_pid_enum_table.keys():
        if pidIndex == pid:
            return nrnas_pid_enum_table[pidIndex]

    return "none"