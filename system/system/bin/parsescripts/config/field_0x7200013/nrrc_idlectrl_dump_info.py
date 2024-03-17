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

#max num of parallel fsm is 6
NRRC_PARALLEL_FSM_BUTT=6

LTE_NR_PROTOCOL_VER_ENUM_TABLE = {
    0x01:"LTE_NR_PROTOCOL_VER_V8",
    0x02:"LTE_NR_PROTOCOL_VER_V9",
    0x04:"LTE_NR_PROTOCOL_VER_V10",
    0x08:"LTE_NR_PROTOCOL_VER_V11",
    0x10:"LTE_NR_PROTOCOL_VER_V12",
    0x20:"LTE_NR_PROTOCOL_VER_V13",
    0x40:"LTE_NR_PROTOCOL_VER_V14",
    0x80:"LTE_NR_PROTOCOL_VER_V15",
}

NRRC_CCB_NET_DEPLOY_TYPE_ENUM = {
    0:"NRRC_CCB_NET_DEPLOY_TYPE_NONE",
    1:"NRRC_CCB_NET_DEPLOY_TYPE_SA",
    2:"NRRC_CCB_NET_DEPLOY_TYPE_ENDC",
}

NRRC_PTL_STATE_ENUM = {
    0:"NRRC_PTL_STATE_NULL",
    1:"NRRC_PTL_STATE_IDLE",
    2:"NRRC_PTL_STATE_CONN",
    3:"NRRC_PTL_STATE_INACTIVE",
}

NRRC_UE_STATE_ENUM = {
    0:"NRRC_UE_STATE_NULL",                                    
    1:"NRRC_UE_STATE_DEACTIVE",                                    
    2:"NRRC_UE_STATE_ACTIVE",
}

NRRC_MASTER_CTRL_FSM_ENUM = {
    0:"NRRC_MASTER_CTRL_FSM_IDLECTRL",                                    
    1:"NRRC_MASTER_CTRL_FSM_CONNCTRL",     
}

NRRC_UTRAN_MODE_ENUM = {
    0:"NRRC_UTRAN_MODE_WCDMA",                                    
    1:"NRRC_UTRAN_MODE_TDSCDMA",                                      
    2:"NRRC_UTRAN_MODE_NULL",  
}

NRRC_UE_CAMPED_STATE_ENUM = {
    0:"NRRC_UE_CAMPED_STATE_NORMALLY",                                    
    1:"NRRC_UE_CAMPED_STATE_ANY_CELL",                                      
}

NRRC_POWER_STATUS_ENUM = {
    0:"NRRC_POWER_STATUS_NONE",                                    
    1:"NRRC_POWER_STATUS_ON",                                      
    2:"NRRC_POWER_STATUS_OFF",  
}


NRRC_PARALLEL_FSM_ENUM = {
    0:"NRRC_PARALLEL_FSM_IDLECTRL",
    1:"NRRC_PARALLEL_FSM_CONNCTRL",
    2:"NRRC_PARALLEL_FSM_MEAS",
    3:"NRRC_PARALLEL_FSM_CSRCH",
    4:"NRRC_PARALLEL_FSM_SIB",
    5:"NRRC_PARALLEL_FSM_BGSCTRL"
}

def GET_NRRC_PARALLEL_FSM_STR(ParallelFsm):
    for fsmid_index in NRRC_PARALLEL_FSM_ENUM.keys():
        if fsmid_index == ParallelFsm:
            return NRRC_PARALLEL_FSM_ENUM[fsmid_index]

    return "LTE_NR_PROTOCOL_VER_BUTT"
    
def GET_LTE_NR_PROTOCOL_VER_STR(ProtocolVer):
    for fsmid_index in LTE_NR_PROTOCOL_VER_ENUM_TABLE.keys():
        if fsmid_index == ProtocolVer:
            return LTE_NR_PROTOCOL_VER_ENUM_TABLE[fsmid_index]

    return "LTE_NR_PROTOCOL_VER_BUTT"

def GET_NRRC_CCB_NET_DEPLOY_TYPE_STR(NetDeployType):
    for fsmid_index in NRRC_CCB_NET_DEPLOY_TYPE_ENUM.keys():
        if fsmid_index == NetDeployType:
            return NRRC_CCB_NET_DEPLOY_TYPE_ENUM[fsmid_index]

    return "NRRC_CCB_NET_DEPLOY_TYPE_BUTT"

def GET_NRRC_PTL_STATE_STR(PtlState):
    for fsmid_index in NRRC_PTL_STATE_ENUM.keys():
        if fsmid_index == PtlState:
            return NRRC_PTL_STATE_ENUM[fsmid_index]

    return "NRRC_PTL_STATE_BUTT"
    
    
def GET_NRRC_UE_STATE_STR(UeState):
    for fsmid_index in NRRC_UE_STATE_ENUM.keys():
        if fsmid_index == UeState:
            return NRRC_UE_STATE_ENUM[fsmid_index]

    return "NRRC_UE_STATE_BUTT"
    
    
def GET_NRRC_MASTER_CTRL_FSM_STR(MasterCtrlFsm):
    for fsmid_index in NRRC_MASTER_CTRL_FSM_ENUM.keys():
        if fsmid_index == MasterCtrlFsm:
            return NRRC_MASTER_CTRL_FSM_ENUM[fsmid_index]

    return "NRRC_MASTER_CTRL_FSM_BUTT"    
    
def GET_NRRC_UTRAN_MODE_STR(UtranMode):
    for fsmid_index in NRRC_UTRAN_MODE_ENUM.keys():
        if fsmid_index == UtranMode:
            return NRRC_UTRAN_MODE_ENUM[fsmid_index]

    return "NRRC_UTRAN_MODE_BUTT"    


def GET_NRRC_UE_CAMPED_STATE_STR(CampState):
    for fsmid_index in NRRC_UE_CAMPED_STATE_ENUM.keys():
        if fsmid_index == CampState:
            return NRRC_UE_CAMPED_STATE_ENUM[fsmid_index]

    return "NRRC_UE_CAMPED_STATE_ENUM_BUTT"     

    
def GET_NRRC_POWER_STATUS_STR(PowerState):
    for fsmid_index in NRRC_POWER_STATUS_ENUM.keys():
        if fsmid_index == PowerState:
            return NRRC_POWER_STATUS_ENUM[fsmid_index]

    return "NRRC_POWER_STATUS_ENUM_BUTT"   
