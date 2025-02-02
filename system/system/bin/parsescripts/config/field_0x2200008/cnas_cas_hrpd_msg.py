#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list lmm mm msg
author          :   fanjing 00179208
modify  record  :   2016-02-01 create file
"""

cnas_cas_hrpd_msg_enum_table = {
    0x5100 :     "ID_CNAS_CAS_HRPD_START_REQ",                
    0x5101 :     "ID_CAS_CNAS_HRPD_START_CNF",                
    0x5102 :     "ID_CNAS_CAS_HRPD_POWER_OFF_REQ",            
    0x5103 :     "ID_CAS_CNAS_HRPD_POWER_OFF_CNF",            
    0x5104 :     "ID_CNAS_CAS_HRPD_SYSTEM_SYNC_REQ",          
    0x5105 :     "ID_CAS_CNAS_HRPD_SYSTEM_SYNC_CNF",          
    0x5106 :     "ID_CNAS_CAS_HRPD_STOP_SYSTEM_SYNC_REQ",     
    0x5107 :     "ID_CAS_CNAS_HRPD_STOP_SYSTEM_SYNC_CNF",     
    0x5108 :     "ID_CAS_CNAS_HRPD_NETWORK_LOST_IND",         
    0x5109 :     "ID_CNAS_CAS_HRPD_SYS_CFG_REQ",              
    0x510A :     "ID_CAS_CNAS_HRPD_SYS_CFG_CNF",              
    0x510B :     "ID_CNAS_CAS_HRPD_CONN_OPEN_REQ",            
    0x510C :     "ID_CAS_CNAS_HRPD_CONN_OPEN_IND",            
    0x510D :     "ID_CNAS_CAS_HRPD_CONN_CLOSE_REQ",           
    0x510E :     "ID_CAS_CNAS_HRPD_CONN_CLOSE_IND",           
    0x510F :     "ID_CAS_CNAS_HRPD_CAS_STATUS_IND",         
    0x5110 :     "ID_CNAS_CAS_HRPD_SESSION_SEED_NTF",                          
    0x5111 :     "ID_CNAS_CAS_HRPD_SUSPEND_REQ",              
    0x5112 :     "ID_CAS_CNAS_HRPD_SUSPEND_CNF",              
    0x5113 :     "ID_CNAS_CAS_HRPD_SESSION_BEGIN_NTF",        
    0x5114 :     "ID_CNAS_CAS_HRPD_SESSION_END_NTF",          
    0x5115 :     "ID_CAS_CNAS_HRPD_SUSPEND_IND",              
    0x5116 :     "ID_CNAS_CAS_HRPD_SUSPEND_RSP",              
    0x5117 :     "ID_CAS_CNAS_HRPD_RESUME_IND",               
    0x5118 :     "ID_CNAS_CAS_HRPP_RESUME_RSP",               
    0x5119 :     "ID_CAS_CNAS_HRPD_SUBNET_ID_CHECK_REQ",      
    0x511A :     "ID_CNAS_CAS_HRPD_SUBNET_ID_CHECK_CNF",      
    0x511B :     "ID_CNAS_CAS_HRPD_DISABLE_LTE_NTF",          
    0x511C :     "ID_CNAS_CAS_HRPD_ENABLE_LTE_NTF",           
    0x511D :     "ID_CAS_CNAS_HRPD_IRAT_FROM_LTE_NTF",        
    0x511E :     "ID_CAS_CNAS_HRPD_IRAT_TO_LTE_NTF",          
    0x511F :     "ID_CAS_CNAS_HRPD_PILOT_SEARCH_REQ_IND",     
    0x5120 :     "ID_CNAS_CAS_HRPD_PILOT_SEARCH_SUCC_NTF",    
    0x5121 :     "ID_CNAS_CAS_HRPD_PILOT_SEARCH_FAIL_NTF",    
    0x5122 :     "ID_CAS_CNAS_HRPD_PILOT_SEARCH_STOP_IND",    
    0x5123 :     "ID_CNAS_CAS_HRPD_BSR_LTE_REQ",              
    0x5124 :     "ID_CAS_CNAS_HRPD_BSR_LTE_CNF",              
    0x5125 :     "ID_CNAS_CAS_HRPD_STOP_BSR_LTE_REQ",         
    0x5126 :     "ID_CAS_CNAS_HRPD_STOP_BSR_LTE_CNF",         
    0x5127 :     "ID_CAS_CNAS_HRPD_BSR_FREQ_LIST_QUERY_REQ",  
    0x5128 :     "ID_CNAS_CAS_HRPD_BSR_FREQ_LIST_QUERY_CNF",  
    0x5129 :     "ID_CAS_CNAS_HRPD_SYSTEM_TIME_IND",          
    0x512A :     "ID_CNAS_CAS_HRPD_FREQ_LOCK_NTF",            
    0x512B :     "ID_CNAS_CAS_HRPD_SUSPEND_REL_REQ",          
    0x512C :     "ID_CAS_CNAS_HRPD_SUSPEND_REL_CNF",
    0x512D :     "ID_CNAS_CAS_HRPD_OOC_REQ",
    0x512E :     "ID_CAS_CNAS_HRPD_OOC_CNF",
    0x512F :     "ID_CAS_CNAS_HRPD_GET_AVOID_INFO_REQ",	
    0x5130 :     "ID_CNAS_CAS_HRPD_GET_AVOID_INFO_CNF",
    0x5131 :     "ID_CNAS_CAS_HRPD_PDP_ACTIVE_BEGIN_NTF", 	
    0x7100 :     "ID_CAS_CNAS_HRPD_PAGE_IND",                 
    0x7101 :     "ID_CNAS_CAS_HRPD_SLOT_VOTE_NTF",            
    0x7102 :     "ID_CAS_CNAS_HRPD_CONN_DENY_IND",            
    0x7103 :     "ID_CNAS_CAS_HRPD_SIGNAL_PROTECT_START_NTF",            
    0x7104 :     "ID_CNAS_CAS_HRPD_SIGNAL_PROTECT_END_NTF",            
    0x9100 :     "ID_CAS_CNAS_HRPD_OHM_NOT_CURRENT_IND",      
    0x9101 :     "ID_CAS_CNAS_HRPD_OVERHEAD_MSG_IND",         
    0x8100 :     "ID_CAS_CNAS_HRPD_IDLE_HO_IND",              
    0x8101 :     "ID_CNAS_CAS_HRPD_SET_SIGNAL_QUALITY_REQ",   
    0x8102 :     "ID_CAS_CNAS_HRPD_SET_SIGNAL_QUALITY_CNF",   
    0x8103 :     "ID_CAS_CNAS_HRPD_SIGNAL_QUALITY_IND",       
    0x8104 :     "ID_CAS_CNAS_HRPD_DATA_SERVICE_AVAILBLE_IND",
    0x6100 :     "ID_CAS_CNAS_HRPD_PA_RAT_MODE_NTF",          
    0x6101 :     "ID_CAS_CNAS_HRPD_SESSION_CHANGE_IND",       
    0x6102 :     "ID_CNAS_CAS_HRPD_SCP_ACTIVE_REQ",           
    0x6103 :     "ID_CAS_CNAS_HRPD_SCP_ACTIVE_CNF",           
    0x6104 :     "ID_CAS_CNAS_HRPD_SESSION_NEG_START_IND",    
    0x6105 :     "ID_CAS_CNAS_HRPD_SESSION_NEG_END_IND",      
    0x6106 :     "ID_CNAS_CAS_HRPD_SCP_DEACTIVE_REQ",         
    0x6107 :     "ID_CAS_CNAS_HRPD_SCP_DEACTIVE_CNF",         
    0x6108 :     "ID_CAS_CNAS_HRPD_HSM_COMMIT_IND",           
    0x6109 :     "ID_CAS_CNAS_HRPD_HLU_COMMIT_IND", 
    0x610A :     "ID_CNAS_CAS_HRPD_STOP_SCP_ACTIVE_NTF",
}

def get_cnas_cas_hrpd_msg_str( MsgId):
    for MsgIdIndex in cnas_cas_hrpd_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cnas_cas_hrpd_msg_enum_table[MsgIdIndex]

    return "unknown"
