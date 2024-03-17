#!/usr/bin/env python
# coding=utf-8
"""

功能；复位log分析脚本
版权信息：华为技术有限公司，版权所有(C) 2010-2019
修改记录：
        2019-11-08 尹鹏 创建内容
        2019-11-08 尹鹏 修改注释
"""

import string

Nrrc_fsm_id_enum_table = {
    0  : "NRRC_IDLECTRL_FSM_PRE_PROCESS",
    1  : "NRRC_IDLECTRL_FSM_IDLE",
    2  : "NRRC_IDLECTRL_FSM",
    3  : "NRRC_IDLECTRL_CSEL_FSM",
    4  : "NRRC_CONNCTRL_FSM_PRE_PROCESS",
    5  : "NRRC_CONNCTRL_FSM_VACANT",
    6  : "NRRC_CONNCTRL_FSM",
    7  : "NRRC_FSM_ITFCM",
    8  : "NRRC_MEAS_FSM_PRE_PROCESS",
    9  : "NRRC_MEAS_FSM_IDLE",
    10 : "NRRC_MEAS_FSM",
    11 : "NRRC_CSRCH_FSM_PRE_PROCESS",
    12 : "NRRC_CSRCH_FSM_IDLE",
    13 : "NRRC_CSRCH_FSM",
    14 : "NRRC_SIB_FSM_PRE_PROCESS",
    15 : "NRRC_SIB_FSM_IDLE",
    16 : "NRRC_SIB_FSM",
    17 : "NRRC_BGSCTRL_FSM_PRE_PROCESS",
    18 : "NRRC_BGSCTRL_FSM_IDLE",
    19 : "NRRC_BGSCTRL_FSM",
    20 : "NRRC_FSM_ID_BUTT"
}

nrrc_fsm_main_state_enum_table = {
    0 :"NRRC_STATE_PRE_PROCESS",
    1 :"NRRC_IDLECTRL_MS_IDLE",
    2 :"NRRC_IDLCTRL_MS_POWER_ON",
    3 :"NRRC_IDLCTRL_MS_POWER_OFF",
    4 :"NRRC_IDLECTRL_MS_PRE_EST",
    5 :"NRRC_IDLECTRL_MS_REL",
    6 :"NRRC_IDLECTRL_MS_RELALL",
    7 :"NRRC_IDLECTRL_MS_SI_UPDATE",
    8 :"NRRC_IDLECTRL_MS_RESEL",
    9 :"NRRC_IDLECTRL_MS_STOP_RESEL",
    10:"NRRC_IDLECTRL_MS_NR2L_IRAT_RESEL",
    11:"NRRC_IDLECTRL_MS_L2NR_IRAT_RESEL",
    12:"NRRC_IDLECTRL_MS_L2NR_IRAT_STOP_RESEL",
    13:"NRRC_IDLECTRL_MS_NR2L_IRAT_REDIR",
    14:"NRRC_IDLECTRL_MS_L2NR_IRAT_REDIR",
    15:"NRRC_IDLECTRL_MS_L2NR_IRAT_STOP_REDIR",
    16:"NRRC_IDLECTRL_MS_STOP_EST",
    17:"NRRC_IDLECTRL_MS_LOST_COVERAGE",
    18:"NRRC_IDLECTRL_MS_SUSPEND",
    19:"NRRC_IDLECTRL_MS_OOS",
    20:"NRRC_IDLECTRL_MS_SYS_CFG",
    21:"NRRC_IDLECTRL_MS_REEST",
    22:"NRRC_IDLECTRL_MS_STOP_REEST",
    23:"NRRC_IDLECTRL_MS_SRCH_ERROR",
    24:"NRRC_IDLECTRL_MS_FREQ_LOCK",
    25:"NRRC_IDLECTRL_MS_L2MA_ERROR_PROC",
    26:"NRRC_IDLECTRL_MS_ABNORMAL_RECOVER",
    27:"NRRC_IDLECTRL_MS_INACTIVE_TO_CONN",
    28:"NRRC_IDLECTRL_MS_ESCAPE_BAR_SRCH",
    29:"NRRC_IDLECTRL_MS_STOP_INACTIVE_TO_CONN",
    30:"NRRC_IDLECTRL_MS_CONN_TO_INACTIVE",
    31:"NRRC_IDLECTRL_MS_WAIT_CONN_TO_IDLE",
    32:"NRRC_IDLECTRL_MS_INACTIVE_TO_IDLE",
    33:"NRRC_IDLECTRL_MS_INTRA_REL",
    34:"NRRC_IDLECTRL_MS_LOW_TEMP_LIMIT",
    35:"NRRC_CSEL_MS_SPEC_PLMN_SRCH",
    36:"NRRC_CSEL_MS_STOP_PLMN_SRCH",
    37:"NRRC_CSEL_MS_PLMN_LIST_SRCH",
    38:"NRRC_CSEL_MS_AS_SEARCH",
    39:"NRRC_CONNCTRL_MS_VACANT",
    40:"NRRC_CONNCTRL_MS_NSA_SCG_CHANGE",
    41:"NRRC_CONNCTRL_MS_NSA_SCG_REL",
    42:"NRRC_CONNCTRL_MS_CONN_SCG_FAIL",
    43:"NRRC_CONNCTRL_MS_CONN_RECFG",
    44:"NRRC_CONNCTRL_MS_CONN_SUSPEND",
    45:"NRRC_CONNCTRL_MS_SMC_CNT_CHK",
    46:"NRRC_CONNCTRL_MS_SMC_ACT",
    47:"NRRC_CONNCTRL_MS_CONN_TO_IDLE",
    48:"NRRC_CONNCTRL_MS_CONN_REL",
    49:"NRRC_CONNCTRL_MS_UECAP_ENQ",
    50:"NRRC_CONNCTRL_MS_CONN_EST",
    51:"NRRC_CONNCTRL_MS_CONN_RESUME",
    52:"NRRC_CONNCTRL_MS_CONN_RESUME_NEW_SETUP",
    53:"NRRC_CONNCTRL_MS_CONN_REEST",
    54:"NRRC_CONNCTRL_MS_CONN_REEST_NEW_SETUP",
    55:"NRRC_CONNCTRL_MS_INTRA_RAT_HO",
    56:"NRRC_CONNCTRL_MS_CONN_SYSINFO",
    57:"NRRC_CONNCTRL_MS_N2L_HO",
    58:"NRRC_CONNCTRL_MS_L2N_HO",
    59:"NRRC_CONNCTRL_MS_MEAS_RECFG",
    60:"NRRC_CONNCTRL_MS_PUCCH_SRS_RELEASE",
    61:"NRRC_CONNCTRL_MS_SYS_CFG",
    62:"NRRC_CONNCTRL_MS_RF_OCCUPY",
    63:"NRRC_CONNCTRL_MS_NSA_DISABLE_ENDC",
    64:"NRRC_CONNCTRL_MS_ITFCM",
    65:"NRRC_MEAS_MS_IDLE",
    66:"NRRC_MEAS_MS_MEAS_CONFIG",
    67:"NRRC_CSRCH_MS_IDLE",
    68:"NRRC_CSRCH_MS_CELL_SRCH",
    69:"NRRC_SIB_MS_IDLE",
    70:"NRRC_SIB_MS_RUNNING",
    71:"NRRC_SIB_MS_STOPPING",
    72:"NRRC_BGSCTRL_MS_IDLE",
    73:"NRRC_BGSCTRL_MS_BG_RUN",
    74:"NRRC_BGSCTRL_MS_BG_STOP",
    75:"NRRC_BGSCTRL_MS_BG_SUSPEND",
    76:"NRRC_BGSCTRL_MS_BG_RESUME",
}

nrrc_fsm_substate_enum_table = {
    0  :"NRRC_IDLECTRL_SS_IDLE",
    1  :"NRRC_IDLECTRL_SS_WAIT_USIM_CNF",
    2  :"NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_CNF",
    3  :"NRRC_IDLECTRL_SS_WAIT_NRL2_REL_ALL_CNF",
    4  :"NRRC_IDLECTRL_SS_PWR_OFF_WAIT_SET_WORK_MODE_CNF",
    5  :"NRRC_IDLECTRL_SS_PWR_OFF_WAIT_NRL2_REL_ALL_CNF",
    6  :"NRRC_IDLECTRL_SS_PWR_OFF_WAIT_RL_ALL_CNF",
    7  :"NRRC_IDLECTRL_SS_WAIT_IRAT_REL_ALL_CNF",
    8  :"NRRC_IDLECTRL_SS_WAIT_STOP_BGS_CNF",
    9  :"NRRC_IDLECTRL_SS_WAIT_SUSPEND_BGS_CNF",
    10 :"NRRC_IDLECTRL_SS_WAIT_IDLE_MEAS_STOP_CNF",
    11 :"NRRC_IDLECTRL_SS_WAIT_CONN_MEAS_STOP_CNF",
    12 :"NRRC_IDLECTRL_SS_WAIT_STOP_SIB_OSI_RCV_CNF",
    13 :"NRRC_IDLECTRL_SS_WAIT_STOP_SYSINFO_CNF",
    14 :"NRRC_IDLECTRL_SS_WAIT_SUSPEND_RSP",
    15 :"NRRC_IDLECTRL_SS_WAIT_CONN_REL",
    16 :"NRRC_IDLECTRL_SS_WAIT_STOP_SIB_CNF",
    17 :"NRRC_IDLECTRL_SS_WAIT_SIB_SYSINFO_IND",
    18 :"NRRC_IDLECTRL_SS_WAIT_BGS_SUSPEND_CNF",
    19 :"NRRC_IDLECTRL_SS_WAIT_GET_SYSINFO_IND",
    20 :"NRRC_IDLECTRL_SS_WAIT_GET_MIB_IND",
    21 :"NRRC_IDLECTRL_SS_WAIT_GET_RMSI_IND",
    22 :"NRRC_IDLECTRL_SS_WAIT_RL_ALL_CNF",
    23 :"NRRC_IDLECTRL_SS_WAIT_LRRC_REL_ALL_CNF",
    24 :"NRRC_IDLECTRL_SS_WAIT_CAMP_MAINCELL_CNF",
    25 :"NRRC_IDLECTRL_SS_WAIT_CELL_SRCH_CNF",
    26 :"NRRC_IDLECTRL_SS_WAIT_PRE_RESOURCE_CNF",
    27 :"NRRC_IDLECTRL_SS_WAIT_BGS_RESUME_CNF",
    28 :"NRRC_IDLECTRL_SS_WAIT_L2_PRE_RESOURCE_CNF",
    29 :"NRRC_IDLECTRL_SS_WAIT_MIBBAR_STOP_SYSINFO_CNF",
    30 :"NRRC_IDLECTRL_SS_WAIT_MIB_FAIL_STOP_SYSINFO_CNF",
    31 :"NRRC_IDLECTRL_SS_WAIT_RMSI_FAIL_STOP_SYSINFO_CNF",
    32 :"NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_STOP_SYSINFO_CNF",
    33 :"NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_STOP_BGS_CNF",
    34 :"NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_REL_ALL_CNF",
    35 :"NRRC_CSEL_SS_WAIT_SET_WORK_MODE_CNF",
    36 :"NRRC_CSEL_SS_WAIT_SIB_STOP_CNF",
    37 :"NRRC_CSEL_SS_WAIT_MEAS_STOP_CNF",
    38 :"NRRC_CSEL_SS_WAIT_REL_NPHY_ALL_CNF",
    39 :"NRRC_CSEL_SS_WAIT_CELL_SEARCH_CNF",
    40 :"NRRC_CSEL_SS_WAIT_CELL_SEARCH_REQ",
    41 :"NRRC_CSEL_SS_WAIT_SIB_READ_MULTI_MIB_IND",
    42 :"NRRC_CSEL_SS_WAIT_READ_MIB_SIB_STOP_CNF",
    43 :"NRRC_CSEL_SS_WAIT_SIB_SYSINFO_IND",
    44 :"NRRC_CSEL_SS_WAIT_NPHY_CAMP_CNF",
    45 :"NRRC_CSEL_SS_WAIT_NPHY_PRE_RESOURCE_CFG_CNF",
    46 :"NRRC_CSEL_SS_WAIT_NL2_PRE_RESOURCE_CFG_CNF",
    47 :"NRRC_CSEL_SS_CELL_SRCH_TIMEOUT_WAIT_REL_NPHY_ALL_CNF",
    48 :"NRRC_CSEL_SS_WAIT_CSRCH_STOP_CNF",
    49 :"NRRC_CSEL_SS_CONTINUE_CELL_SEARCH_WAIT_SIB_STOP_CNF",
    50 :"NRRC_CSEL_SS_REL_NPHY_WAIT_REL_NPHY_ALL_CNF",
    51 :"NRRC_CSEL_SS_CAMP_FAIL_WAIT_REL_NPHY_ALL_CNF",
    52 :"NRRC_CSEL_SS_WAIT_BGS_STOP_CNF",
    53 :"NRRC_IDLECTRL_SS_WAIT_NPHY_REL_ALL_CNF",
    54 :"NRRC_IDLECTRL_SS_WAIT_CSEL_STOP_CELL_SRCH_CNF",
    55 :"NRRC_IDLECTRL_SS_IN_REL_NPHY_WAIT_REL_NPHY_ALL_CNF",
    56 :"NRRC_IDLECTRL_SS_WAIT_INTRA_FAIL_RESUME_RSP",
    57 :"NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_DEACT_CNF",
    58 :"NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_ACT_CNF",
    59 :"NRRC_IDLECTRL_SS_WAIT_LRRC_RESEL_CNF",
    60 :"NRRC_IDLECTRL_SS_WAIT_LRRC_RESEL_STOP_CNF",
    61 :"NRRC_IDLECTRL_SS_WAIT_IRAT_FAIL_RESUME_RSP",
    62 :"NRRC_IDLECTRL_SS_WAIT_RESUME_RSP",
    63 :"NRRC_IDLECTRL_SS_WAIT_SUSPEND_REL_RESUME_RSP",
    64 :"NRRC_IDLECTRL_SS_WAIT_SUSPEND_REL_SWM_DEACT_CNF",
    65 :"NRRC_IDLECTRL_SS_WAIT_LRRC_REDIR_CNF",
    66 :"NRRC_IDLECTRL_SS_WAIT_LRRC_REDIR_STOP_CNF",
    67 :"NRRC_IDLECTRL_SS_REEST_WAIT_SET_SLAVE_WORK_MODE_CNF",
    68 :"NRRC_IDLECTRL_SS_REEST_WAIT_SET_MASTER_WORK_MODE_CNF",
    69 :"NRRC_IDLECTRL_SS_REEST_WAIT_LTE_CELL_SRCH_CNF",
    70 :"NRRC_IDLECTRL_SS_WAIT_REEST_STOP_LTE_CELL_SRCH_CNF",
    71 :"NRRC_IDLECTRL_SS_REEST_SRCH_NR_WAIT_SET_SLAVE_WORK_MODE_CNF",
    72 :"NRRC_CSEL_SS_WAIT_CSS_CURR_GEO_RSP",
    73 :"NRRC_CSEL_SS_WAIT_CSS_GET_CLOUD_PREF_FREQ_RSP",
    74 :"NRRC_CSEL_SS_WAIT_CSS_GET_CLOUD_PREF_BAND_RSP",
    75 :"NRRC_CSEL_SS_WAIT_NRL2_REL_ALL_CNF",
    76 :"NRRC_IDLECTRL_RCV_OSI_SS_WAIT_SUSPEND_BGS_CNF",
    77 :"NRRC_IDLECTRL_SS_WAIT_NRL2_BACKUP_REL_CNF",
    78 :"NRRC_CONNCTRL_SS_VACANT",
    79 :"NRRC_CONNCTRL_SS_WAIT_PRE_MEAS_CTRL_CNF",
    80 :"NRRC_CONNCTRL_SS_WAIT_MEAS_CTRL_CNF",
    81 :"NRRC_CONNCTRL_SS_WAIT_MEAS_STOP_CNF",
    82 :"NRRC_CONNCTRL_SS_WAIT_MEAS_REL_STOP_CNF",
    83 :"NRRC_CONNCTRL_SS_WAIT_STOP_SYSINFO_CNF",
    84 :"NRRC_CONNCTRL_SS_WAIT_CSEL_CNF",
    85 :"NRRC_CONNCTRL_SS_WAIT_CSEL_STOP_CNF",
    86 :"NRRC_CONNCTRL_SS_WAIT_PDCP_STOP_CNF",
    87 :"NRRC_CONNCTRL_SS_WAIT_SDAP_PDCP_STOP_CNF",
    88 :"NRRC_CONNCTRL_SS_WAIT_MAC_RLC_REEST_CNF",
    89 :"NRRC_CONNCTRL_SS_WAIT_L1_L2_CONFIG_CNF",
    90 :"NRRC_CONNCTRL_SS_WAIT_MAC_RA_CNF",
    91 :"NRRC_CONNCTRL_SS_WAIT_PDCP_DATA_CNF",
    92 :"NRRC_CONNCTRL_SS_WAIT_PDCP_CONTINUE_CNF",
    93 :"NRRC_CONNCTRL_SS_WAIT_SDAP_PDCP_CONTINUE_CNF",
    94 :"NRRC_CONNCTRL_SS_WAIT_SYNC_CNF",
    95 :"NRRC_CONNCTRL_SS_WAIT_L2_L1_REL_CNF",
    96 :"NRRC_CONNCTRL_SS_WAIT_L2_REL_CNF",
    97 :"NRRC_CONNCTRL_SS_WAIT_PDCP_CNT_CHK_CNF",
    98 :"NRRC_CONNCTRL_SS_WAIT_SECU_FAIL_CONFIG_CNF",
    99 :"NRRC_CONNCTRL_SS_WAIT_SECU_CONFIG_CNF",
    100:"NRRC_CONNCTRL_SS_CONN_TO_IDLE_WAIT_L2_L1_CNF",
    101:"NRRC_CONNCTRL_SS_CONN_TO_IDLE_WAIT_L1_RELALL_CNF",
    102:"NRRC_CONNCTRL_SS_WAIT_PRE_RES_CONFIG_CNF",
    103:"NRRC_CONNCTRL_SS_WAIT_OTHER_RAT_UECAP_CNF",
    104:"NRRC_CONNCTRL_SS_WAIT_COOR_CAPA_CNF",
    105:"NRRC_CONNCTRL_SS_WAIT_IDLECTRL_EST_CNF",
    106:"NRRC_CONNCTRL_SS_WAIT_RRM_APPLY_CNF",
    107:"NRRC_CONNCTRL_SS_WAIT_CCCH_DATA_IND",
    108:"NRRC_CONNCTRL_SS_WAIT_L1L2_SRB1_CONFIG_CNF",
    109:"NRRC_CONNCTRL_SS_WAIT_IDLECTRL_REL_CNF",
    110:"NRRC_CONNCTRL_SS_WAIT_IDLECTRL_INACTIVE_TO_CONN_CNF",
    111:"NRRC_CONNCTRL_SS_WAIT_L2_DATA_IND",
    112:"NRRC_CONNCTRL_SS_WAIT_L1_CONN_TO_IDLE_CNF",
    113:"NRRC_CONNCTRL_SS_WAIT_NRMM_EST_REQ",
    114:"NRRC_CONNCTRL_SS_WAIT_INTRA_RAT_HO_CNF",
    115:"NRRC_CONNCTRL_SS_WAIT_NRMM_SUSPEND_RSP",
    116:"NRRC_CONNCTRL_SS_WAIT_IRAT_BEGIN_MEAS_STOP_CNF",
    117:"NRRC_CONNCTRL_SS_WAIT_LRRC_RELALL_CNF",
    118:"NRRC_CONNCTRL_SS_WAIT_LRRC_HANDOVER_CNF",
    119:"NRRC_CONNCTRL_SS_WAIT_IRAT_SUCC_MEAS_STOP_CNF",
    120:"NRRC_CONNCTRL_SS_WAIT_NRMM_RESUME_RSP",
    121:"NRRC_CONNCTRL_SS_WAIT_LRRC_HANDOVER_STOP_CNF",
    122:"NRRC_CONNCTRL_SS_WAIT_SET_MASTER_WORK_MODE_CNF",
    123:"NRRC_CONNCTRL_SS_WAIT_SEC_PARA_RSP",
    124:"NRRC_CONNCTRL_SS_WAIT_NPHY_HO_CNF",
    125:"NRRC_CONNCTRL_SS_WAIT_SET_SLAVE_WORK_MODE_CNF",
    126:"NRRC_CONNCTRL_SS_WAIT_LRRC_NR_SCG_START_RSP",
    127:"NRRC_CONNCTRL_SS_WAIT_L1_PUCCH_SRS_RELEASE_CNF",
    128:"NRRC_CONNCTRL_SS_WAIT_L2_REVERT_CONFIG_CNF",
    129:"NRRC_CONNCTRL_SS_WAIT_IDLECTRL_SYS_CFG_CNF",
    130:"NRRC_CONNCTRL_SS_WAIT_PDCP_RELEASE_CNF",
    131:"NRRC_CONNCTRL_SS_WAIT_SRB1_PDCP_CONTINUE_CNF",
    132:"NRRC_CONNCTRL_SS_WAIT_L2_SECU_CONFIG_CNF",
    133:"NRRC_CONNCTRL_SS_WAIT_L2_CONFIG_CNF",
    134:"NRRC_CONNCTRL_SS_WAIT_IDLECTRL_RF_OCCUPY_CNF",
    135:"NRRC_CONNCTRL_SS_WAIT_L1_DSDS_SUSPEND_CNF",
    136:"NRRC_CONNCTRL_SS_WAIT_RF_RECOVER",
    137:"NRRC_CONNCTRL_SS_WAIT_L1_DSDS_RESUME_CNF",
    138:"NRRC_CONNCTRL_SS_WAIT_L1_REL_CNF",
    139:"NRRC_CONNCTRL_SS_WAIT_LRRC_RCV_LPHY_HO_CNF_NTF_CNF",
    140:"NRRC_CONNCTRL_SS_WAIT_NRMM_RNA_UPDATE_RSP",
    141:"NRRC_CONNCTRL_SS_WAIT_RESUME_INIT_L1_L2_CONFIG_CNF",
    142:"NRRC_CONNCTRL_SS_WAIT_RESUME_NORMAL_MAC_RLC_REEST_CNF",
    143:"NRRC_CONNCTRL_SS_WAIT_RESUME_NORMAL_PDCP_STOP_CNF",
    144:"NRRC_CONNCTRL_SS_ITFCM_WAIT_L1_L2_CNF",
    145:"NRRC_MEAS_SS_IDLE",
    146:"NRRC_MEAS_SS_WAIT_NPHY_CNF",
    147:"NRRC_MEAS_SS_WAIT_IRAT_CNF",
    148:"NRRC_MEAS_SS_WAIT_GAP_CFG_CNF",
    149:"NRRC_MEAS_SS_WAIT_SIB_CNF",
    150:"NRRC_CSRCH_SS_IDLE",
    151:"NRRC_CSRCH_SS_WAIT_CELL_SEARCHING_IND",
    152:"NRRC_CSRCH_SS_WAIT_BAND_SCAN_IND",
    153:"NRRC_CSRCH_SS_WAIT_FREQ_RSSI_SCAN_IND",
    154:"NRRC_CSRCH_SS_WAIT_CSRCH_CONTINUE_NTF",
    155:"NRRC_SIB_SS_IDLE",
    156:"NRRC_SIB_SS_WAIT_NR_ANR_START_CNF",
    157:"NRRC_SIB_SS_WAIT_IRAT_ANR_START_CNF",
    158:"NRRC_SIB_SS_WAIT_PBCH_SETUP_CNF",
    159:"NRRC_SIB_SS_WAIT_MIB_IND",
    160:"NRRC_SIB_SS_WAIT_PBCH_RELEASE_CNF",
    161:"NRRC_SIB_SS_WAIT_PDSCH_BCH_SETUP_CNF",
    162:"NRRC_SIB_SS_WAIT_SIB1_IND",
    163:"NRRC_SIB_SS_WAIT_PDSCH_BCH_RELEASE_CNF",
    164:"NRRC_SIB_SS_WAIT_NR_ANR_STOP_CNF",
    165:"NRRC_SIB_SS_WAIT_IRAT_ANR_STOP_CNF",
    166:"NRRC_SIB_SS_WAIT_IRAT_ANR_STOP_SYSINFO_REQ",
    167:"NRRC_SIB_SS_WAIT_SI_CONFIG_CNF",
    168:"NRRC_SIB_SS_WAIT_OSI_IND",
    169:"NRRC_BGSCTRL_SS_IDLE",
    170:"NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_START_CNF",
    171:"NRRC_BGSCTRL_SS_WAIT_CSRCH_BG_SEARCH_CNF",
    172:"NRRC_BGSCTRL_SS_WAIT_SIB_READ_MULTI_MIB_IND",
    173:"NRRC_BGSCTRL_SS_WAIT_SIB_READ_RMSI_IND",
    174:"NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_STOP_CNF",
    175:"NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_START_CNF",
    176:"NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_STOP_CNF",
    177:"NRRC_BGSCTRL_SS_WAIT_READ_MIB_SIB_STOP_CNF",
    178:"NRRC_BGSCTRL_SS_CONTINUE_CELL_SEARCH_WAIT_SIB_STOP_CNF",
    179:"NRRC_BGSCTRL_SS_WAIT_CSRCH_STOP_BG_SRCH_CNF",
    180:"NRRC_BGSCTRL_SS_WAIT_STOP_SIB_CNF",
    181:"NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_SUSPEND_CNF",
    182:"NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_RESUME_CNF",
    183:"NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_SUSPEND_CNF",
    184:"NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_RESUME_CNF",
    185:"NRRC_BGSCTRL_SS_SUSPEND_NEED_BGS_NEXT_RAT",
    186:"NRRC_SS_ID_BUTT"
}

nrrc_state_timer_enum_table = {      
    #PTL TIMER                              
    1 :"TI_NRRC_PTL_T300",
    2 :"TI_NRRC_PTL_T301",
    3 :"TI_NRRC_PTL_T302",
    4 :"TI_NRRC_PTL_T303",
    5 :"TI_NRRC_PTL_T304",
    6 :"TI_NRRC_PTL_T305",
    7 :"TI_NRRC_PTL_T306",
    8 :"TI_NRRC_PTL_T307",
    9 :"TI_NRRC_PTL_T308",
    10:"TI_NRRC_PTL_T310_MCG",
    11:"TI_NRRC_PTL_T311",
    12:"TI_NRRC_PTL_T310_SCG",
    13:"TI_NRRC_PTL_T319",
    14:"TI_NRRC_PTL_T380",
    15:"TI_NRRC_PTL_T390",
    16:"TI_NRRC_CMM_CELL_EVT_TRIG",
    17:"TI_NRRC_CMM_PERIOD_RPT",
    18:"TI_NRRC_CONN_REL_MSG_DELAY_TIMER",
    19:"TI_NRRC_PTL_CAMPON",
    20:"TI_NRRC_PTL_BARRED",
    21:"TI_NRRC_PTL_LOSTCOVERAGE",
    22:"TI_NRRC_PTL_FORB",
    23:"TI_NRRC_PTL_RESELECTION",
    24:"TI_NRRC_PTL_START_ON_DEMAND_TIMER",
    25:"TI_NRRC_PTL_STOP_ON_DEMAND_TIMER",
    26:"TI_NRRC_PTL_MP_TIMER",
    27:"TI_NRRC_PTL_RESEL_TRIED",
    28:"TI_NRRC_PTL_3H_TIMER",
    29:"TI_NRRC_PTL_T320",
    30:"TI_NRRC_PTL_T300_CONN_EST_FAIL",
    31:"TI_NRRC_PTL_RF_OCCUPY_PROTECT",
    32:"TI_NRRC_PTL_IDLE_NORMALHYST",
    33:"TI_NRRC_PTL_LTE_BARRED",
    34:"TI_NRRC_PTL_LTE_FORB",
    35:"TI_NRRC_PTL_LTE_S_CHECK",
    36:"TI_NRRC_PTL_RF_SHORT_OCCUPY_PROTECT",
    37:"TI_NRRC_PTL_DISABLE_ENDC_PROTECT",
    38:"TI_NRRC_PTL_ENDC_SHORT_OCCUPY_RESUME_PHY_PROTECT",
    39:"TI_NRRC_PTL_DSDS_NORF_LOST_COVERAGE",
    40:"TI_NRRC_PTL_DECODE_RMSI_TIMER",
    41:"TI_NRRC_PTL_DT_PERIOD_RPT_SERVING_CELL_IND",
    42:"TI_NRRC_PTL_DEMAND_SI_START_NPHY_TIMER",
    43:"TI_NRRC_PTL_DEMAND_SI_STOP_NPHY_TIMER",
    44:"TI_NRRC_PTL_T321",
    45:"TI_NRRC_PTL_RB_INFO_EVENT_RPT",
    46:"TI_NRRC_PTL_WAIT_DEDPRI_INFO",
    47:"TI_NRRC_PTL_OSI_RCV_FAILED_DELAY",
    48:"TI_NRRC_PTL_T345",
    49:"TI_NRRC_PTL_REEST_RECOVER_PROTECT",
    50:"TI_NRRC_CONN_VOTE_DFS_PROTECT",
    51:"TI_NRRC_PTL_RCV_CLOUD_UECAP",
    52:"TI_NRRC_CONN_WAKE_LOCK_PROTECT",
    53:"TI_NRRC_PTL_CONN_SYSINFO_FAIL_RETRY",
    54:"TI_NRRC_UECAP_CLOUD_WAKE_LOCK_PROTECT",
    55:"TI_NRRC_REDUCE_CAMP_THRSHOLD",
    56:"TI_NRRC_CONN_DISABLE_SRB3",
    57:"TI_NRRC_PTL_RRC_PAGING_RF_TASK_PROTECT",

    #STATE PROTECT TIMER 
    0x1002:"TI_NRRC_CONNCTRL_WAIT_PRE_MEAS_CTRL_CNF",
    0x1003:"TI_NRRC_CONNCTRL_WAIT_MEAS_CTRL_CNF",
    0x1004:"TI_NRRC_CONNCTRL_WAIT_MEAS_STOP_CNF",
    0x1005:"TI_NRRC_CONNCTRL_WAIT_STOP_SYSINFO_CNF",
    0x1006:"TI_NRRC_CONNCTRL_WAIT_CSEL_CNF",
    0x1007:"TI_NRRC_CONNCTRL_WAIT_CSEL_STOP_CNF",
    0x1008:"TI_NRRC_CONNCTRL_WAIT_PDCP_STOP_CNF",
    0x1009:"TI_NRRC_CONNCTRL_WAIT_MAC_RLC_REEST_CNF",
    0x100A:"TI_NRRC_CONNCTRL_WAIT_MAC_RA_CNF",
    0x100B:"TI_NRRC_CONNCTRL_WAIT_PDCP_DATA_CNF",
    0x100C:"TI_NRRC_CONNCTRL_WAIT_PDCP_CONTINUE_CNF",
    0x100D:"TI_NRRC_CONNCTRL_WAIT_SRB1_PDCP_CONTINUE_CNF",
    0x100E:"TI_NRRC_CONNCTRL_WAIT_SYNC_CNF",
    0x100F:"TI_NRRC_CONNCTRL_WAIT_PDCP_CNT_CHK_CNF",
    0x1010:"TI_NRRC_CONNCTRL_WAIT_IDLECTRL_EST_CNF",
    0x1011:"TI_NRRC_CONNCTRL_WAIT_RRM_APPLY_CNF",
    0x1012:"TI_NRRC_CONNCTRL_WAIT_IDLECTRL_REL_CNF",
    0x1013:"TI_NRRC_CONNCTRL_WAIT_PRE_CFG_CNF",
    0x1014:"TI_NRRC_CONNCTRL_CONN_TO_IDLE_WAIT_L1_RELALL_CNF",
    0x1015:"TI_NRRC_CONNCTRL_WAIT_L2_UL_INFO_TRANS_DATA_CNF",
    0x1016:"TI_NRRC_CONNCTRL_WAIT_IDLECTRL_INACTIVE_TO_CONN_CNF",
    0x1017:"TI_NRRC_CONNCTRL_SS_SMC_WAIT_SECU_CFG_CNF",
    0x1018:"TI_NRRC_CONNCTRL_WAIT_MAC_RESET_CNF",
    0x1019:"TI_NRRC_CONNCTRL_WAIT_NRMM_EST_REQ",
    0x101A:"TI_NRRC_CONNCTRL_ITFCM_WAIT_L1_L2_CNF",
    0x101B:"TI_NRRC_CONNCTRL_WAIT_NRMM_SUSPEND_RSP",
    0x101C:"TI_NRRC_CONNCTRL_WAIT_IRAT_BEGIN_MEAS_STOP_CNF",
    0x101D:"TI_NRRC_CONNCTRL_WAIT_LRRC_RELALL_CNF",
    0x101E:"TI_NRRC_CONNCTRL_WAIT_SET_SLAVE_WORK_MODE_CNF",
    0x101F:"TI_NRRC_CONNCTRL_WAIT_LRRC_HANDOVER_CNF",
    0x1020:"TI_NRRC_CONNCTRL_WAIT_IRAT_SUCC_MEAS_STOP_CNF",
    0x1021:"TI_NRRC_CONNCTRL_WAIT_NRMM_RESUME_RSP",
    0x1022:"TI_NRRC_CONNCTRL_WAIT_SET_MASTER_WORK_MODE_CNF",
    0x1023:"TI_NRRC_CONNCTRL_WAIT_LRRC_HANDOVER_STOP_CNF",
    0x1024:"TI_NRRC_CONNCTRL_WAIT_SEC_PARA_RSP",
    0x1025:"TI_NRRC_CONNCTRL_WAIT_IDLECTRL_SYS_CFG_CNF",
    0x1026:"TI_NRRC_CONNCTRL_WAIT_LRRC_NR_SCG_START_RSP",
    0x1027:"TI_NRRC_CONNCTRL_WAIT_IDLECTRL_RF_OCCUPY_CNF",
    0x1028:"TI_NRRC_CONNCTRL_WAIT_L1_DSDS_SUSPEND_CNF",
    0x1029:"TI_NRRC_CONNCTRL_WAIT_RF_RECOVER",
    0x102A:"TI_NRRC_CONNCTRL_WAIT_L1_DSDS_RESUME_CNF",
    0x102B:"TI_NRRC_CONNCTRL_WAIT_SDAP_PDCP_STOP_CNF",
    0x102C:"TI_NRRC_CONNCTRL_WAIT_SDAP_PDCP_CONTINUE_CNF",
    0x102D:"TI_NRRC_CONNCTRL_WAIT_LRRC_RCV_LPHY_HO_CNF_NTF_CNF",
    0x102E:"TI_NRRC_CONNCTRL_WAIT_NRMM_RNA_UPDATE_RSP",
    0x102F:"TI_NRRC_CONNCTRL_WAIT_L2_RA_SUCC_IND",
    0x1030:"TI_NRRC_CONNCTRL_WAIT_RESUME_NORMAL_PDCP_STOP_CNF",
    0x1031:"TI_NRRC_CONNCTRL_WAIT_PDCP_RELEASE_CNF",
    0x1101:"TI_NRRC_UECAP_WAIT_COOR_CAPA_CNF",
    0x1201:"TI_NRRC_IDLECTRL_SS_WAIT_USIM_CNF",
    0x1202:"TI_NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_CNF",
    0x1203:"TI_NRRC_IDLECTRL_SS_WAIT_NRL2_REL_ALL_CNF",
    0x1204:"TI_NRRC_IDLECTRL_SS_WAIT_IRAT_REL_ALL_CNF",
    0x1205:"TI_NRRC_IDLECTRL_SS_WAIT_STOP_BGS_CNF",
    0x1206:"TI_NRRC_IDLECTRL_SS_WAIT_SUSPEND_BGS_CNF",
    0x1207:"TI_NRRC_IDLECTRL_SS_WAIT_IDLE_MEAS_STOP_CNF",
    0x1208:"TI_NRRC_IDLECTRL_SS_WAIT_CONN_MEAS_STOP_CNF",
    0x1209:"TI_NRRC_IDLECTRL_SS_WAIT_STOP_SYSINFO_CNF",
    0x120A:"TI_NRRC_IDLECTRL_SS_WAIT_STOP_SIB_CNF",
    0x120B:"TI_NRRC_IDLECTRL_SS_WAIT_STOP_SIB_OSI_RCV_CNF",
    0x120C:"TI_NRRC_IDLECTRL_SS_WAIT_BGS_SUSPEND_CNF",
    0x120D:"TI_NRRC_IDLECTRL_SS_WAIT_GET_SYSINFO_IND",
    0x120E:"TI_NRRC_IDLECTRL_SS_WAIT_GET_MIB_IND",
    0x120F:"TI_NRRC_IDLECTRL_SS_WAIT_GET_RMSI_IND",
    0x1210:"TI_NRRC_IDLECTRL_SS_WAIT_RL_ALL_CNF",
    0x1211:"TI_NRRC_IDLECTRL_SS_WAIT_LRRC_REL_ALL_CNF",
    0x1212:"TI_NRRC_IDLECTRL_SS_WAIT_CAMP_MAINCELL_CNF",
    0x1213:"TI_NRRC_IDLECTRL_SS_WAIT_CELL_SRCH_CNF",
    0x1214:"TI_NRRC_IDLECTRL_SS_WAIT_PRE_RESOURCE_CNF",
    0x1215:"TI_NRRC_IDLECTRL_SS_WAIT_BGS_RESUME_CNF",
    0x1216:"TI_NRRC_IDLECTRL_SS_WAIT_L2_PRE_RESOURCE_CNF",
    0x1217:"TI_NRRC_IDLECTRL_SS_WAIT_MIBBAR_STOP_SYSINFO_CNF",
    0x1218:"TI_NRRC_IDLECTRL_SS_WAIT_MIB_FAIL_STOP_SYSINFO_CNF",
    0x1219:"TI_NRRC_IDLECTRL_SS_WAIT_RMSI_FAIL_STOP_SYSINFO_CNF",
    0x121A:"TI_NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_STOP_SYSINFO_CNF",
    0x121B:"TI_NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_STOP_BGS_CNF",
    0x121C:"TI_NRRC_IDLECTRL_SS_CAMP_FAIL_WAIT_REL_ALL_CNF",
    0x121D:"TI_NRRC_IDLECTRL_SS_WAIT_CONN_REL",
    0x121E:"TI_NRRC_CSEL_SS_WAIT_SET_WORK_MODE_CNF",
    0x121F:"TI_NRRC_CSEL_SS_WAIT_MEAS_STOP_CNF",
    0x1220:"TI_NRRC_CSEL_SS_WAIT_REL_NPHY_ALL_CNF",
    0x1221:"TI_NRRC_CSEL_SS_WAIT_CELL_SEARCH_CNF",
    0x1222:"TI_NRRC_CSEL_SS_WAIT_CELL_SEARCH_REQ",
    0x1223:"TI_NRRC_CSEL_SS_WAIT_SIB_READ_MULTI_MIB_IND",
    0x1224:"TI_NRRC_CSEL_SS_WAIT_READ_MIB_STOP_SYSINFO_CNF",
    0x1225:"TI_NRRC_CSEL_SS_WAIT_READ_MIB_TIMEOUT_STOP_SYSINFO_CNF",
    0x1226:"TI_NRRC_CSEL_SS_WAIT_SIB_SYSINFO_IND",
    0x1227:"TI_NRRC_CSEL_SS_WAIT_NPHY_CAMP_CNF",
    0x1228:"TI_NRRC_CSEL_SS_WAIT_NPHY_PRE_RESOURCE_CFG_CNF",
    0x1229:"TI_NRRC_CSEL_SS_WAIT_NL2_PRE_RESOURCE_CFG_CNF",
    0x122A:"TI_NRRC_CSEL_SS_CELL_SRCH_TIMEOUT_WAIT_REL_NPHY_ALL_CNF",
    0x122B:"TI_NRRC_CSEL_SS_WAIT_CSRCH_STOP_CNF",
    0x122C:"TI_NRRC_CSEL_SS_CONTINUE_CELL_SEARCH_WAIT_SIB_STOP_CNF",
    0x122D:"TI_NRRC_CSEL_SS_REL_NPHY_WAIT_REL_NPHY_ALL_CNF",
    0x122E:"TI_NRRC_CSEL_SS_WAIT_SIB_STOP_CNF",
    0x122F:"TI_NRRC_CSEL_SS_CAMP_FAIL_WAIT_REL_NPHY_ALL_CNF",
    0x1230:"TI_NRRC_CSEL_SS_WAIT_BGS_STOP_CNF",
    0x1231:"TI_NRRC_IDLECTRL_SS_SYS_CFG_WAIT_REL_ALL_CNF",
    0x1232:"TI_NRRC_IDLECTRL_SS_WAIT_CSEL_STOP_CELL_SRCH_CNF",
    0x1233:"TI_NRRC_IDLECTRL_SS_IN_REL_NPHY_WAIT_REL_NPHY_ALL_CNF",
    0x1234:"TI_NRRC_IDLECTRL_SS_REL_NPHY_WAIT_REL_NPHY_ALL_CNF",
    0x1235:"TI_NRRC_IDLECTRL_SS_WAIT_SUSPEND_RSP",
    0x1236:"TI_NRRC_IDLECTRL_SS_WAIT_INTRA_FAIL_RESUME_RSP",
    0x1237:"TI_NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_DEACT_CNF",
    0x1238:"TI_NRRC_IDLECTRL_SS_WAIT_SET_WORK_MODE_ACT_CNF",
    0x1239:"TI_NRRC_IDLECTRL_SS_WAIT_LRRC_RESEL_CNF",
    0x123A:"TI_NRRC_IDLECTRL_SS_WAIT_LRRC_RESEL_STOP_CNF",
    0x123B:"TI_NRRC_IDLECTRL_SS_WAIT_IRAT_FAIL_RESUME_RSP",
    0x123C:"TI_NRRC_IDLECTRL_SS_WAIT_RESUME_RSP",
    0x123D:"TI_NRRC_IDLECTRL_SS_WAIT_SUSPEND_REL_RESUME_RSP",
    0x123E:"TI_NRRC_IDLECTRL_SS_WAIT_SUSPEND_REL_SWM_DEACT_CNF",
    0x123F:"TI_NRRC_IDLECTRL_SS_WAIT_LRRC_REDIR_CNF",
    0x1240:"TI_NRRC_IDLECTRL_SS_WAIT_LRRC_REDIR_STOP_CNF",
    0x1241:"TI_NRRC_IDLECTRL_SS_REEST_SRCH_WAIT_LTE_SRCH_CNF",
    0x1242:"TI_NRRC_IDLECTRL_SS_STOP_REEST_WAIT_STOP_LTE_SRCH_CNF",
    0x1243:"TI_NRRC_CSEL_SS_WAIT_CSS_CURR_GEO_RSP",
    0x1244:"TI_NRRC_CSEL_SS_WAIT_CSS_GET_CLOUD_PREF_FREQ_RSP",
    0x1245:"TI_NRRC_CSEL_SS_WAIT_CSS_GET_CLOUD_PREF_BAND_RSP",
    0x1246:"TI_NRRC_CSEL_SS_WAIT_LRRC_DED_PRIORITY_INHERIT_CNF",
    0x1247:"TI_NRRC_IDLECTRL_RCV_OSI_SS_WAIT_SUSPEND_BGS_CNF",
    0x1248:"TI_NRRC_CSEL_SS_WAIT_NRL2_REL_ALL_CNF",
    0x1249:"TI_NRRC_IDLECTRL_SS_WAIT_NRL2_BACKUP_REL_CNF",
    0x1301:"TI_NRRC_MEAS_SS_WAIT_NPHY_CNF",
    0x1302:"TI_NRRC_MEAS_SS_WAIT_IRAT_CNF",
    0x1303:"TI_NRRC_MEAS_SS_WAIT_GAP_CFG_CNF",
    0x1304:"TI_NRRC_MEAS_SS_WAIT_SIB_CNF",
    0x1401:"TI_NRRC_CSRCH_SS_WAIT_CELL_SEARCHING_IND",
    0x1402:"TI_NRRC_CSRCH_SS_WAIT_FREQ_RSSI_SCAN_IND",
    0x1403:"TI_NRRC_CSRCH_SS_WAIT_BAND_SCAN_IND",
    0x1404:"TI_NRRC_CSRCH_SS_WAIT_CSRCH_CONTINUE_NTF",
    0x1501:"TI_NRRM_SIB_WAIT_PBCH_SETUP_CNF",
    0x1502:"TI_NRRM_SIB_WAIT_MIB_IND",
    0x1503:"TI_NRRM_SIB_WAIT_PBCH_RELEASE_CNF",
    0x1504:"TI_NRRM_SIB_WAIT_PDSCH_BCH_SETUP_CNF",
    0x1505:"TI_NRRM_SIB_WAIT_SIB1_IND",
    0x1506:"TI_NRRM_SIB_WAIT_PDSCH_BCH_RELEASE_CNF",
    0x1507:"TI_NRRC_SIB_SS_WAIT_SI_CONFIG_CNF",
    0x1508:"TI_NRRC_SIB_SS_WAIT_OSI_IND",
    0x1509:"TI_NRRM_SIB_WAIT_NR_ANR_START_CNF",
    0x150A:"TI_NRRM_SIB_WAIT_NR_ANR_STOP_CNF",
    0x150B:"TI_NRRM_SIB_WAIT_IRAT_ANR_START_CNF",
    0x150C:"TI_NRRM_SIB_WAIT_IRAT_ANR_STOP_CNF",
    0x150D:"TI_NRRM_SIB_WAIT_IRAT_ANR_STOP_SYSINFO_REQ",
    0x1601:"TI_NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_START_CNF",
    0x1602:"TI_NRRC_BGSCTRL_SS_WAIT_CSRCH_BG_SEARCH_CNF",
    0x1603:"TI_NRRC_BGSCTRL_SS_WAIT_SIB_READ_RMSI_IND",
    0x1604:"TI_NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_STOP_CNF",
    0x1605:"TI_NRRC_BGSCTRL_SS_WAIT_LTE_BG_SRCH_IND",
    0x1606:"TI_NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_START_CNF",
    0x1607:"TI_NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_STOP_CNF",
    0x1608:"TI_NRRC_BGSCTRL_SS_WAIT_SIB_READ_MULTI_MIB_IND",
    0x1609:"TI_NRRC_BGSCTRL_SS_WAIT_READ_MIB_STOP_SYSINFO_CNF",
    0x160A:"TI_NRRC_BGSCTRL_SS_CONTINUE_CELL_SEARCH_WAIT_SIB_STOP_CNF",
    0x160B:"TI_NRRC_BGSCTRL_SS_WAIT_CSRCH_STOP_BG_SRCH_CNF",
    0x160C:"TI_NRRC_BGSCTRL_SS_WAIT_STOP_SIB_CNF",
    0x160D:"TI_NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_SUSPEND_CNF",
    0x160E:"TI_NRRC_BGSCTRL_SS_WAIT_NPHY_BG_SRCH_RESUME_CNF",
    0x160F:"TI_NRRC_BGSCTRL_PROTECT_SLAVE_SUSPEND",
    0x1610:"TI_NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_SUSPEND_CNF",
    0x1611:"TI_NRRC_BGSCTRL_SS_WAIT_IRAT_BG_SRCH_RESUME_CNF",
}

def Nrps_Get_Nrrc_FsmId_Str(fsmid):
    for fsmid_index in Nrrc_fsm_id_enum_table.keys():
        if fsmid_index == fsmid:
            return Nrrc_fsm_id_enum_table[fsmid_index]

    return "NRRC_FSM_ID_BUTT"

def Nrps_Get_Nrrc_MainState_Str(state):
    for index in nrrc_fsm_main_state_enum_table.keys():
        if index == state:
            return nrrc_fsm_main_state_enum_table[index]

    return "NRRC_MS_ID_BUTT"

def Nrps_Get_Nrrc_SubState_Str(state):
    for index in nrrc_fsm_substate_enum_table.keys():
        if index == state:
            return nrrc_fsm_substate_enum_table[index]

    return "NRRC_SS_ID_BUTT"

def Nrps_Get_Nrrc_StaTiId_Str(timerid):
    for index in nrrc_state_timer_enum_table.keys():
        if index == timerid:
            return nrrc_state_timer_enum_table[index]

    return "TI_NRRC_STATE_BUTT"
