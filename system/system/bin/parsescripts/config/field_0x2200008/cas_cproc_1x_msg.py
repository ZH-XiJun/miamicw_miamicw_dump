#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   list gmm ll msg
author          :   fanjing 00179208
modify  record  :   2016-02-01 create file
"""

cas_cproc_1x_msg_enum_table = {
    0x2000 :     "ID_CAS_CPROC_1X_LONG_CODE_CFG_REQ",                                                      
    0x2001 :     "ID_CPROC_CAS_1X_LONG_CODE_CFG_CNF",                                                   
    0x2002 :     "ID_CAS_CPROC_1X_REL_ALL_REQ",                                                         
    0x2003 :     "ID_CPROC_CAS_1X_REL_ALL_CNF",                                                         
    0x2008 :     "ID_CAS_CPROC_1X_SET_WORK_MODE_REQ",                                                   
    0x2009 :     "ID_CPROC_CAS_1X_SET_WORK_MODE_CNF",                                                   
    0x200A :     "ID_CPROC_CAS_1X_GOOD_FRAME_IND",                                                      
    0x200B :     "ID_CPROC_CAS_1X_HANDOFF_FAIL_IND",                                                    
    0x200C :     "ID_CPROC_CAS_1X_TCH_LOST_IND",                                          
    0x2040 :     "ID_CAS_CPROC_1X_SIGNAL_LEVEL_REQ",                                      
    0x2041 :     "ID_CPROC_CAS_1X_SIGNAL_LEVEL_CNF",                                      
    0x2042 :     "ID_CAS_CPROC_1X_SIGNAL_LEVEL_STOP_REQ",                                 
    0x2043 :     "ID_CPROC_CAS_1X_SIGNAL_LEVEL_STOP_CNF",                                 
    0x2044 :     "ID_CAS_CPROC_1X_SIGNAL_LEVEL_SUSPEND_REQ",                              
    0x2045 :     "ID_CPROC_CAS_1X_SIGNAL_LEVEL_SUSPEND_CNF",                              
    0x2046 :     "ID_CAS_CPROC_1X_SIGNAL_LEVEL_RESUME_REQ",                               
    0x2047 :     "ID_CPROC_CAS_1X_SIGNAL_LEVEL_RESUME_CNF",                               
    0x2048 :     "ID_CAS_CPROC_1X_PILOT_SEARCH_RESUME_REQ",                               
    0x2049 :     "ID_CPROC_CAS_1X_PILOT_SEARCH_RESUME_CNF",                               
    0x204A :     "ID_CAS_CPROC_1X_PILOT_SEARCH_STOP_REQ",                                 
    0x204B :     "ID_CPROC_CAS_1X_PILOT_SEARCH_STOP_CNF",                                 
    0x204C :     "ID_CAS_CPROC_1X_PILOT_SEARCH_SUSPEND_REQ",                              
    0x204D :     "ID_CPROC_CAS_1X_PILOT_SEARCH_SUSPEND_CNF",                              
    0x204E :     "ID_CAS_CPROC_1X_PILOT_SEARCH_REQ",                                      
    0x204F :     "ID_CPROC_CAS_1X_PILOT_SEARCH_IND",                                      
    0x2050 :     "ID_CPROC_CAS_1X_PILOT_SEARCH_DONE_IND",                                 
    0x2051 :     "ID_CPROC_CAS_1X_ACTION_IND",                                            
    0x2052 :     "ID_CAS_CPROC_1X_CCI_REQ",                                               
    0x2053 :     "ID_CPROC_CAS_1X_CCI_CNF",                                               
    0x2054 :     "ID_CPROC_CAS_1X_CCI_IND",                                               
    0x2055 :     "ID_CAS_CPROC_1X_FSYNC_START_REQ",                                       
    0x2056 :     "ID_CPROC_CAS_1X_FSYNC_START_CNF",                                       
    0x2057 :     "ID_CAS_CPROC_1X_FSYNC_STOP_REQ",                                        
    0x2058 :     "ID_CPROC_CAS_1X_FSYNC_STOP_CNF",                                        
    0x2059 :     "ID_CAS_CPROC_1X_TCH_CONFIG_REQ",                                        
    0x205A :     "ID_CPROC_CAS_1X_TCH_CONFIG_CNF",                                        
    0x205D :     "ID_CAS_CPROC_1X_COMMON_CH_CONFIG_REQ",                                  
    0x205E :     "ID_CPROC_CAS_1X_COMMON_CH_CONFIG_CNF",                                  
    0x205F :     "ID_CAS_CPROC_1X_CHANNEL_REL_REQ",                                       
    0x2060 :     "ID_CPROC_CAS_1X_CHANNEL_REL_CNF",                                       
    0x2061 :     "ID_CAS_CPROC_1X_STOP_COMMON_CH_MONITOR_REQ",                            
    0x2062 :     "ID_CPROC_CAS_1X_STOP_COMMON_CH_MONITOR_CNF",                            
    0x2063 :     "ID_CPROC_CAS_1X_SET_TIMING_CNF",                                        
    0x2064 :     "ID_CAS_CPROC_1X_SET_TIMING_REQ",                                        
    0x2065 :     "ID_CAS_CPROC_1X_PWRCTRL_CONFIG_REQ",                                    
    0x2066 :     "ID_CPROC_CAS_1X_PWRCTRL_CONFIG_CNF",                                    
    0x2067 :     "ID_CPROC_CAS_1X_PWRCTRL_IND",
    0x2068 :     "ID_CAS_CPROC_1X_OLPC_RSLT_RPT_REQ",            
    0x2069 :     "ID_CPROC_CAS_1X_ERROR_IND",                    
    0x206A :     "ID_CAS_CPROC_1X_START_COMMON_CH_MONITOR_REQ",  
    0x206B :     "ID_CPROC_CAS_1X_START_COMMON_CH_MONITOR_CNF",  
    0x206C :     "ID_CPROC_CAS_1X_RF_IND",                       
    0x206D :     "ID_CPROC_CAS_1X_NO_RF_IND",                    
    0x206E :     "ID_CAS_CPROC_1X_TIME_SYNC_REQ",                
    0x206F :     "ID_CPROC_CAS_1X_TIME_SYNC_IND",                
    0x2070 :     "ID_CAS_CPROC_1X_TRAFFIC_INFO_REQ",             
    0x2071 :     "ID_CAS_CPROC_1X_SLOTTED_MODE_CONTINUE_REQ",    
    0x2072 :     "ID_CPROC_CAS_1X_VE_MODE_IND",                  
    0x2073 :     "ID_CAS_CPROC_1X_IDLE_FER_REQ",
    0x2074 :     "ID_CPROC_CAS_1X_SCH_STOP_IND"	,
    0x2075 :     "ID_CPROC_CAS_1X_DISABLE_RTCH_IND",
    0x2076 :     "ID_CPROC_CAS_1X_SLEEP_IND",
    0x2077 :     "ID_CPROC_CAS_1X_WAKEUP_IND",
    0x2078 :     "ID_CPROC_CAS_1X_EXIT_SYNC_TO_PILOT_RESEARCH_IND",
    0x2079 :     "ID_CPROC_CAS_1X_DISABLE_RSCH_IND",
    0x207A :     "ID_CAS_CPROC_1X_SWITCH_TAS_ANT_REQ",
    0x207B :     "ID_CPROC_CAS_1X_SLOTTED_MODE_HANDOFF_DELAY_IND",
    0x207C :     "ID_CPROC_CAS_1X_SLOT_MODE_INFO_IND",
    0x2100 :     "ID_CAS_CPROC_1X_IDLEACCESS_MEAS_REQ",                                   
    0x2101 :     "ID_CPROC_CAS_1X_IDLEACCESS_MEAS_CNF",                                   
    0x2102 :     "ID_CPROC_CAS_1X_IDLEACCESS_MEAS_IND",                                   
    0x2103 :     "ID_CAS_CPROC_1X_TCH_MEAS_REQ",                                          
    0x2104 :     "ID_CPROC_CAS_1X_TCH_MEAS_CNF",                                          
    0x2105 :     "ID_CPROC_CAS_1X_TCH_MEAS_IND",                                          
    0x2106 :     "ID_CAS_CPROC_1X_AGPS_MEAS_REQ",                                         
    0x2107 :     "ID_CPROC_CAS_1X_SLOT_MODE_MEAS_IND",
}

def get_cas_cproc_1x_msg_str( MsgId):
    for MsgIdIndex in cas_cproc_1x_msg_enum_table.keys():
        if MsgIdIndex == MsgId:
            return cas_cproc_1x_msg_enum_table[MsgIdIndex]

    return "unknown"
