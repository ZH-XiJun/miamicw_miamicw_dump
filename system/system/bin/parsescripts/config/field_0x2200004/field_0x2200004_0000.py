#!/usr/bin/env python
# coding=utf-8
"""
Copyright © Huawei Technologies Co., Ltd. 2001-2019. All rights reserved.
description     :   analysis guas dump bin
author          :   sunbing 00184266
modify  record  :   2016-01-07 create file
"""

import struct
import os
import sys
import string
from gas.analyse_gas_global import *
from gas.analyse_gas_msg import *
from was.analyse_was_msg import *
from guas_pid import *
from vers_ctrl import *

MACRO_GAS_DEBUG_VERSION_LENGTH          = 8
MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT     = 120
MACRO_GAS_MNTN_REC_MSG_INFO_SIZE        = 8
MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT = 60

MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE        = 8
MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT     = 160

MACRO_MODEM0_ADDR_LENGTH                = 4096
MACRO_MODEM1_ADDR_LENGTH                = 4096

def guas_vers_ctrl( vers_no, outstream):
        global MACRO_GAS_DEBUG_MSG_LIST_LENGTH
        global MACRO_GAS_MODEM0_DUMP_INFO_LENGTH
        global MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH

        if ( MACRO_VERSION_NO_0 == vers_no):
                MACRO_GAS_DEBUG_MSG_LIST_LENGTH         = 8 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
        elif ( MACRO_VERSION_NO_1 == vers_no or MACRO_VERSION_NO_2 == vers_no):
                MACRO_GAS_DEBUG_MSG_LIST_LENGTH         = 8 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
        elif ( MACRO_VERSION_NO_3 == vers_no):
                MACRO_GAS_DEBUG_MSG_LIST_LENGTH         = 8 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
        elif ( MACRO_VERSION_NO_4 == vers_no):
                MACRO_GAS_DEBUG_MSG_LIST_LENGTH         = 8 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT + 4 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT

        MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH    = get_gcomm_global_status_lenth(vers_no)

        MACRO_GAS_MODEM0_DUMP_INFO_LENGTH       = MACRO_GAS_DEBUG_MSG_LIST_LENGTH + \
                                                  MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH + \
                                                  MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH + \
                                                  MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH + \
                                                  MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH + \
                                                  MACRO_GAS_RR_GLOBAL_STATUS_LENGTH + \
                                                  MACRO_GAS_GRR_GLOBAL_STATUS_LENGTH

def analysis_guas_debug_version( instream, fileOffset, outstream):
        instream.seek(fileOffset)

        (version_name_0,) = struct.unpack('>B', instream.read(1))
        (version_name_1,) = struct.unpack('>B', instream.read(1))
        (version_name_2,) = struct.unpack('>B', instream.read(1))
        (version_name_3,) = struct.unpack('>B', instream.read(1))
        (version_space,)  = struct.unpack('>B', instream.read(1))
        (version_no_0,)   = struct.unpack('>B', instream.read(1))
        (version_no_1,)   = struct.unpack('>B', instream.read(1))
        (version_end,)    = struct.unpack('>B', instream.read(1))

        version_name    = "%s%s%s%s" % (chr(version_name_0), chr(version_name_1), chr(version_name_2), chr(version_name_3))
        version_no      = "%s%s" % (chr(version_no_0), chr(version_no_1))

        outstream.writelines(["%-15s%-7s\n" % ("Version Name:", version_name)])
        outstream.writelines(["%-15s%-7s\n" % ("Version No.:", version_no)])

        vers_no = guas_get_version_no( version_name, version_no)

        guas_vers_ctrl( vers_no, outstream)

        return vers_no

def get_gas_msg_str( pid1, pid2, usMsgId):
        if ( 'gphy' == pid1.lower() or 'gphy' == pid2.lower()):
                return get_gas_gphy_msg_str(usMsgId)
        elif ( 'i1_gphy' == pid1.lower() or 'i1_gphy' == pid2.lower()):
                return get_gas_gphy_msg_str(usMsgId)
        elif ( 'timer' == pid1.lower() or 'timer' == pid2.lower()):
                return get_gas_timer_msg_str(usMsgId)
        elif ( 'mmc' == pid1.lower() or 'mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_mmc' == pid1.lower() or 'i1_mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'mm' == pid1.lower() or 'mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_mm' == pid1.lower() or 'i1_mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'gmm' == pid1.lower() or 'gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_gmm' == pid1.lower() or 'i1_gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'wcom' == pid1.lower() or 'wcom' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'i1_wcom' == pid1.lower() or 'i1_wcom' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'wrr' == pid1.lower() or 'wrr' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'i1_wrr' == pid1.lower() or 'i1_wrr' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'rrm' == pid1.lower() or 'rrm' == pid2.lower()):
                return get_gas_rrm_msg_str(usMsgId)
        elif ( 'trrc' == pid1.lower() or 'trrc' == pid2.lower()):
                return get_gas_trrc_msg_str(usMsgId)
        elif ( 'errc' == pid1.lower() or 'errc' == pid2.lower()):
                return get_gas_lrrc_msg_str(usMsgId)
        elif ( 'i1_errc' == pid1.lower() or 'i1_errc' == pid2.lower()):
                return get_gas_lrrc_msg_str(usMsgId)
        elif ( 'ermm' == pid1.lower() or 'ermm' == pid2.lower()):
                return get_gas_lrrc_msg_str(usMsgId)
        elif ( 'i1_ermm' == pid1.lower() or 'i1_ermm' == pid2.lower()):
                return get_gas_lrrc_msg_str(usMsgId)
        elif ( 'css' == pid1.lower() or 'css' == pid2.lower()):
                return get_gas_css_msg_str(usMsgId)
        elif ( 'mta' == pid1.lower() or 'mta' == pid2.lower()):
                return get_gas_mta_msg_str(usMsgId)
        elif ( 'mtc' == pid1.lower() or 'mtc' == pid2.lower()):
                return get_gas_mtc_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() or 'taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgId)
        elif ( 'i1_taf' == pid1.lower() or 'i1_taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgId)
        elif ( 'grm' == pid1.lower() or 'grm' == pid2.lower()):
                return get_gas_grm_msg_str(usMsgId)
        elif ( 'i1_grm' == pid1.lower() or 'i1_grm' == pid2.lower()):
                return get_gas_grm_msg_str(usMsgId)
        elif ( 'usim' == pid1.lower()):
                return get_sim_gas_str(usMsgId)
        elif ( 'usim' == pid2.lower()):
                return get_gas_sim_str(usMsgId)
        elif ( 'i1_usim' == pid1.lower()):
                return get_sim_gas_str(usMsgId)
        elif ( 'i1_usim' == pid2.lower()):
                return get_gas_sim_str(usMsgId)
        elif ( 'msp_pid' == pid1.lower() or 'msp_pid' == pid2.lower()):
                return get_gas_om_msg_str(usMsgId)
        elif ( 'apm' == pid2.lower()):
                return get_gas_apm_msg_str(usMsgId)
        elif ( 'lapdm' == pid1.lower() or 'lapdm' == pid2.lower()):
                return get_gas_lapdm_msg_str(usMsgId)
        elif ( 'ii_lapdm' == pid1.lower() or 'i1_lapdm' == pid2.lower()):
                return get_gas_lapdm_msg_str(usMsgId)
        elif ( 'i1_mta' == pid1.lower() or 'i1_mta' == pid2.lower()):
                return get_gas_mta_msg_str(usMsgId)
        else:
                return 'none'

def analysis_gas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, modem_no):
        instream.seek(fileLocalOffset)

        (usTick,)       = struct.unpack('H', instream.read(2))
        (usMsgId,)      = struct.unpack('H', instream.read(2))
        (usSendPid,)    = struct.unpack('H', instream.read(2))
        (usRcvPid,)     = struct.unpack('H', instream.read(2))

        if ( 0 == modem_no):
            strSendPid      = guas_get_modem0_pid_str( usSendPid)
            strRcvPid       = guas_get_modem0_pid_str( usRcvPid)
        elif ( 1 == modem_no):
            strSendPid      = guas_get_modem1_pid_str( usSendPid)
            strRcvPid       = guas_get_modem1_pid_str( usRcvPid)
        else:
            strSendPid      = guas_get_modem0_pid_str( usSendPid)
            strRcvPid       = guas_get_modem0_pid_str( usRcvPid)

        strMsgId        = get_gas_msg_str( strSendPid, strRcvPid, usMsgId)

        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)
        strTick         = '%x'% usTick

        outstream.writelines(["%-15s%-15s%-60s0x%-10s\n" % ( strSendPid, strRcvPid, strMsgId, strTick.upper())])

def get_gas_mntn_rec_msg_cnt( instream, fileOffset, ulMsgIndex, ulDefaultCnt):
        fileOffset      = fileOffset + ulMsgIndex * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
        instream.seek(fileOffset)

        (usTick,)       = struct.unpack('H', instream.read(2))
        (usMsgId,)      = struct.unpack('H', instream.read(2))
        (usSendPid,)    = struct.unpack('H', instream.read(2))
        (usRcvPid,)     = struct.unpack('H', instream.read(2))

        if ( 0 == usTick and 0 == usMsgId and 0 == usSendPid and 0 == usRcvPid ):
            return ulMsgIndex
        else:
            return ulDefaultCnt

def analysis_gas_mntn_rec_msg_info( instream, fileOffset, outstream, ulMsgIndex, modem_no):
        ulLooper        = 0
        instream.seek(fileOffset)

        ulMsgCnt = get_gas_mntn_rec_msg_cnt(instream, fileOffset, ulMsgIndex, MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT)
        if ( ulMsgIndex == ulMsgCnt ):
            ulStartIndex = 0
        else:
            ulStartIndex = ulMsgIndex

        while ulLooper < ulMsgCnt:
                ulLooperIndex = ( ulLooper + ulStartIndex) % MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
                analysis_gas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, modem_no)
                ulLooper = ulLooper + 1

def analysis_gas_modemX_msg_list( instream, fileOffset, outstream, modem_no):
        instream.seek(fileOffset)

        (ulLastTick,)   = struct.unpack('I', instream.read(4))
        strLastTick     = '%x'% ulLastTick
        outstream.writelines(["%-15s0x%-7s\n" % ("ulLastTick:", strLastTick.upper())])

        (ulMsgIndex,)   = struct.unpack('I', instream.read(4))
        strMsgIndex     = '%x' % ulMsgIndex
        outstream.writelines(["%-15s%d(0x%s)\n" % ("ulMsgIndex:", ulMsgIndex, strMsgIndex.upper())])

        outstream.writelines(["%-15s%-15s%-60s%-10s\n" % ("usSendPid", "usReceivePid","ulMsgId", "usTick")])
        fileOffset      = fileOffset + 8;
        analysis_gas_mntn_rec_msg_info( instream, fileOffset, outstream, ulMsgIndex, modem_no)

def analysis_gas_mntn_rec_nas_msg_info( instream, fileOffset, outstream, ulMsgIndex, modem_no):
        ulLooper        = 0
        instream.seek(fileOffset)

        ulMsgCnt = get_gas_mntn_rec_msg_cnt(instream, fileOffset, ulMsgIndex, MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT)

        if ( ulMsgIndex == ulMsgCnt ):
            ulStartIndex = 0
        else:
            ulStartIndex = ulMsgIndex

        while ulLooper < ulMsgCnt:
                ulLooperIndex = ( ulLooper + ulStartIndex) % MACRO_GAS_MNTN_REC_NAS_MSG_INFO_MAX_CNT
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_GAS_MNTN_REC_MSG_INFO_SIZE
                analysis_gas_mntn_per_rec_msg_info( instream, fileLocalOffset, outstream, modem_no)
                ulLooper = ulLooper + 1

def analysis_gas_modemX_nas_msg_list( instream, fileOffset, outstream, modem_no):
        instream.seek(fileOffset)

        (ulNasMsgIndex,)   = struct.unpack('I', instream.read(4))
        strNasMsgIndex     = '%x'% ulNasMsgIndex
        outstream.writelines(["%-15s0x%-7s\n" % ("ulNasMsgIndex:", strNasMsgIndex.upper())])

        outstream.writelines(["%-15s%-15s%-60s%-10s\n" % ("usSendPid", "usReceivePid","ulMsgId", "usTick")])
        fileOffset      = fileOffset + 4;
        analysis_gas_mntn_rec_nas_msg_info( instream, fileOffset, outstream, ulNasMsgIndex, modem_no)

def get_was_send_msg_str( usMsgId):
        usMatch         = 0
        strGasMsg       = get_gas_was_msg_str(usMsgId)
        strWphyMsg      = get_was_wphy_msg_str(usMsgId)
        strPdcpMsg      = get_was_pdcp_msg_str(usMsgId)
        strRlcMsg       = get_was_rlc_msg_str(usMsgId)
        strMacMsg       = get_was_mac_msg_str(usMsgId)
        strMspMsg       = get_was_om_msg_str(usMsgId)
        strLrrcMsg      = get_was_lrrc_msg_str(usMsgId)
        strNasMsg       = get_gas_nas_msg_str(usMsgId)
        strBmcMsg       = get_was_bmc_msg_str(usMsgId)

        if ( 'none' != strGasMsg):
                usMatch = usMatch + 1

        if ( 'none' != strWphyMsg):
                usMatch = usMatch + 1

        if ( 'none' != strPdcpMsg):
                usMatch = usMatch + 1

        if ( 'none' != strRlcMsg):
                usMatch = usMatch + 1

        if ( 'none' != strMacMsg):
                usMatch = usMatch + 1

        if ( 'none' != strMspMsg):
                usMatch = usMatch + 1

        if ( 'none' != strLrrcMsg):
                usMatch = usMatch + 1

        if ( 'none' != strNasMsg):
                usMatch = usMatch + 1

        if ( 'none' != strBmcMsg):
                usMatch = usMatch + 1

        if ( 1 != usMatch):
                return 'More than one Msg'

        if ( 'none' != strGasMsg):
                return strGasMsg

        if ( 'none' != strWphyMsg):
                 return strWphyMsg

        if ( 'none' != strPdcpMsg):
                 return strPdcpMsg

        if ( 'none' != strRlcMsg):
                return strRlcMsg

        if ( 'none' != strMacMsg):
                return strMacMsg

        if ( 'none' != strMspMsg):
                return strMspMsg

        if ( 'none' != strLrrcMsg):
                return strLrrcMsg

        if ( 'none' != strNasMsg):
                return strNasMsg

        if ( 'none' != strBmcMsg):
                return strBmcMsg

def get_was_msg_str_vers0( strSendPid, usMsgId):
        if ( 'wcom' == strSendPid.lower() or 'wrr' == strSendPid.lower()):
                return get_was_send_msg_str(usMsgId)
        elif ( 'gas' == strSendPid.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'wphy' == strSendPid.lower()):
                return get_was_wphy_msg_str(usMsgId)
        elif ( 'timer' == strSendPid.lower()):
                return get_was_timer_msg_str(usMsgId)
        elif ( 'pdcp' == strSendPid.lower()):
                return get_was_pdcp_msg_str(usMsgId)
        elif ( 'rlc' == strSendPid.lower()):
                return get_was_rlc_msg_str(usMsgId)
        elif ( 'mac' == strSendPid.lower()):
                return get_was_mac_msg_str(usMsgId)
        elif ( 'msp_pid' == strSendPid.lower()):
                return get_was_om_msg_str(usMsgId)
        elif ( 'errc' == strSendPid.lower() or 'ermm' == strSendPid.lower()):
                return get_was_lrrc_msg_str(usMsgId)
        elif ( 'mmc' == strSendPid.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'mm' == strSendPid.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'gmm' == strSendPid.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'bmc' == strSendPid.lower()):
                return get_was_bmc_msg_str(usMsgId)
        else:
                return "none"

def get_was_msg_str_vers1( pid1, pid2, usMsgId):
        if ( 'gas' == pid1.lower() or 'gas' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        if ( 'i1_gas' == pid1.lower() or 'i1_gas' == pid2.lower()):
                return get_gas_was_msg_str(usMsgId)
        elif ( 'wphy' == pid1.lower() or 'wphy' == pid2.lower()):
                return get_was_wphy_msg_str(usMsgId)
        elif ( 'i1_wphy' == pid1.lower() or 'i1_wphy' == pid2.lower()):
                return get_was_wphy_msg_str(usMsgId)
        elif ( 'timer' == pid1.lower() or 'timer' == pid2.lower()):
                return get_was_timer_msg_str(usMsgId)
        elif ( 'pdcp' == pid1.lower() or 'pdcp' == pid2.lower()):
                return get_was_pdcp_msg_str(usMsgId)
        elif ( 'i1_pdcp' == pid1.lower() or 'i1_pdcp' == pid2.lower()):
                return get_was_pdcp_msg_str(usMsgId)
        elif ( 'rlc' == pid1.lower() or 'rlc' == pid2.lower()):
                return get_was_rlc_msg_str(usMsgId)
        elif ( 'i1_rlc' == pid1.lower() or 'i1_rlc' == pid2.lower()):
                return get_was_rlc_msg_str(usMsgId)
        elif ( 'mac' == pid1.lower() or 'mac' == pid2.lower()):
                return get_was_mac_msg_str(usMsgId)
        elif ( 'i1_mac' == pid1.lower() or 'i1_mac' == pid2.lower()):
                return get_was_mac_msg_str(usMsgId)
        elif ( 'msp_pid' == pid1.lower() or 'msp_pid' == pid2.lower()):
                return get_was_om_msg_str(usMsgId)
        elif ( 'errc' == pid1.lower() or 'errc' == pid2.lower()):
                return get_was_lrrc_msg_str(usMsgId)
        elif ( 'i1_errc' == pid1.lower() or 'i1_errc' == pid2.lower()):
                return get_was_lrrc_msg_str(usMsgId)
        elif ( 'ermm' == pid1.lower() or 'ermm' == pid2.lower()):
                return get_was_lrrc_msg_str(usMsgId)
        elif ( 'i1_ermm' == pid1.lower() or 'i1_ermm' == pid2.lower()):
                return get_was_lrrc_msg_str(usMsgId)
        elif ( 'mmc' == pid1.lower() or 'mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_mmc' == pid1.lower() or 'i1_mmc' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'mm' == pid1.lower() or 'mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_mm' == pid1.lower() or 'i1_mm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'gmm' == pid1.lower() or 'gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_gmm' == pid1.lower() or 'i1_gmm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'rabm' == pid1.lower() or 'rabm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'i1_rabm' == pid1.lower() or 'i1_rabm' == pid2.lower()):
                return get_gas_nas_msg_str(usMsgId)
        elif ( 'bmc' == pid1.lower() or 'bmc' == pid2.lower()):
                return get_was_bmc_msg_str(usMsgId)
        elif ( 'i1_bmc' == pid1.lower() or 'i1_bmc' == pid2.lower()):
                return get_was_bmc_msg_str(usMsgId)
        elif ( 'rrm' == pid1.lower() or 'rrm' == pid2.lower()):
                return get_was_rrm_msg_str(usMsgId)
        elif ( 'css' == pid1.lower() or 'css' == pid2.lower()):
                return get_gas_css_msg_str(usMsgId)
        elif ( 'mtc' == pid1.lower() or 'mtc' == pid2.lower()):
                return get_gas_mtc_msg_str(usMsgId)
        elif ( 'taf' == pid1.lower() or 'taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgId)
        elif ( 'i1_taf' == pid1.lower() or 'i1_taf' == pid2.lower()):
                return get_gas_taf_msg_str(usMsgId)
        elif ( 'mta' == pid1.lower() or 'mta' == pid2.lower()):
                return get_guas_mta_msg_str(usMsgId)
        elif ( 'i1_mta' == pid1.lower() or 'i1_mta' == pid2.lower()):
                return get_guas_mta_msg_str(usMsgId)
        elif ( 'bastet' == pid1.lower() or 'bastet' == pid2.lower()):
                return get_guas_bastet_msg_str(usMsgId)
        else:
                return 'none'

def analysis_was_mntn_per_save_exc_msg_info_vers0( instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (ulTimeStamp,)          = struct.unpack('I', instream.read(4))
        (usSendPid,)            = struct.unpack('H', instream.read(2))
        (usMsgId,)              = struct.unpack('H', instream.read(2))

        strSendPid      = guas_get_modem0_pid_str( usSendPid)
        strMsgId        = get_was_msg_str_vers0( strSendPid, usMsgId)

        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)

        outstream.writelines(["%-20s%-60s0x%-27x\n" % ( strSendPid, strMsgId, ulTimeStamp)])

def analysis_was_mntn_per_save_exc_msg_info_vers1( instream, fileLocalOffset, outstream, version):
        instream.seek(fileLocalOffset)

        (usTimeStamp,)  = struct.unpack('H', instream.read(2))
        (usMsgId,)      = struct.unpack('H', instream.read(2))
        (usSendPid,)    = struct.unpack('H', instream.read(2))
        (usRcvPid,)     = struct.unpack('H', instream.read(2))

        if ( 0 == version):
            strSendPid      = guas_get_modem0_pid_str( usSendPid)
            strRcvPid       = guas_get_modem0_pid_str( usRcvPid)
        elif ( 1 == version):
            strSendPid      = guas_get_modem1_pid_str( usSendPid)
            strRcvPid       = guas_get_modem1_pid_str( usRcvPid)
        else:
            strSendPid      = guas_get_modem0_pid_str( usSendPid)
            strRcvPid       = guas_get_modem0_pid_str( usRcvPid)

        strMsgId        = get_was_msg_str_vers1( strSendPid, strRcvPid, usMsgId)

        strSendPid      = '%s(0x%x)' % ( strSendPid, usSendPid)
        strRcvPid       = '%s(0x%x)' % ( strRcvPid, usRcvPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, usMsgId)
        strTick         = '%x'% usTimeStamp

        outstream.writelines(["%-20s%-15s%-60s0x%-10s\n" % ( strSendPid, strRcvPid, strMsgId, strTick.upper())])

def analysis_was_mntn_save_exc_msg_info_vers_01( instream, fileOffset, outstream, ulHandledMsgNum):
        ulLooper        = 0

        outstream.writelines(["%-20s%-60s%-27s\n" % ("usSendPid", "usMsgId", "ulTimeStamp")])

        while ulLooper < MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT:
                ulLooperIndex = ( ulLooper + ulHandledMsgNum) % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
                analysis_was_mntn_per_save_exc_msg_info_vers0( instream, fileLocalOffset, outstream)
                ulLooper = ulLooper + 1

def analysis_was_mntn_save_exc_msg_info_vers_02( instream, fileOffset, outstream, ulHandledMsgNum, version):
        ulLooper        = 0

        outstream.writelines(["%-20s%-15s%-60s%-10s\n" % ("usSendPid", "usReceivePid","ulMsgId", "usTick")])

        while ulLooper < MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT:
                ulLooperIndex = ( ulLooper + ulHandledMsgNum) % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT
                fileLocalOffset = fileOffset + ulLooperIndex * MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE
                analysis_was_mntn_per_save_exc_msg_info_vers1( instream, fileLocalOffset, outstream, version)
                ulLooper = ulLooper + 1

def analysis_was_mntn_save_msgid_in_queue( instream, fileOffset, outstream, ulMsgIdInQueueNum):
        ulLooper        = 0

        outstream.writelines(["%-17s\n" % ("aulMsgIdInQueue[160] := {")])

        while ulLooper < MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT:
                ulLooperIndex = ( ulLooper + ulMsgIdInQueueNum) % MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT
                fileLocalOffset = fileOffset + ulLooperIndex
                instream.seek( fileLocalOffset)

                (ulMsgIdInQueue, )      = struct.unpack('I', instream.read(4))
                outstream.writelines(["0x%-17x" % (ulMsgIdInQueue)])

                if ( 3 == ulLooper % 4):
                        outstream.writelines("\n")

                ulLooper = ulLooper + 1

        outstream.writelines(["%s\n" % ("}")])

def analysis_was_modem0_dump_info_vers_01( instream, fileOffset, outstream):
        outstream.writelines("\n**************************** modem0 was debug msg list vers 01************************\n")

        instream.seek(fileOffset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT )

        (ulHandledMsgNum,)      = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulHandledMsgNum :", ulHandledMsgNum)])

        analysis_was_mntn_save_exc_msg_info_vers_01( instream, fileOffset, outstream, ulHandledMsgNum)

        outstream.writelines("\n")

        instream.seek(fileOffset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT + 4 + 4 * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT )

        (ulMsgIdInQueueNum,)      = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s%-7x\n" % ("ulMsgIdInQueueNum :", ulMsgIdInQueueNum)])

        fileOffset      = fileOffset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT + 4

        analysis_was_mntn_save_msgid_in_queue( instream, fileOffset, outstream, ulMsgIdInQueueNum)

def analysis_was_modem0_dump_info_vers_02( instream, fileOffset, outstream, version):
        outstream.writelines("\n**************************** modem%d was debug msg list vers 02************************\n" % version)

        instream.seek(fileOffset)

        (ulHandledMsgNum,)      = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s0x%-7x\n" % ("ulHandledMsgNum :", ulHandledMsgNum)])

        fileOffset      = fileOffset + 4

        analysis_was_mntn_save_exc_msg_info_vers_02( instream, fileOffset, outstream, ulHandledMsgNum, version)

        outstream.writelines("\n")

        fileOffset      = fileOffset + MACRO_WAS_SAVE_EXC_MSG_INFO_SIZE * MACRO_WAS_SAVE_EXC_MSG_INFO_MAX_CNT

        instream.seek(fileOffset)

        (ulMsgIdInQueueNum,)      = struct.unpack('I', instream.read(4))
        outstream.writelines(["%-15s%-7x\n" % ("ulMsgIdInQueueNum :", ulMsgIdInQueueNum)])

        fileOffset      = fileOffset + 4

        analysis_was_mntn_save_msgid_in_queue( instream, fileOffset, outstream, ulMsgIdInQueueNum)

def analysis_gas_modemX_dump_info( instream, fileOffset, outstream, version, modem_no):
        ###### analysis gas debug msg list ########
        outstream.writelines(["\n**************************** modem%d gas debug msg list *******************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_DEBUG_VERSION_LENGTH
        analysis_gas_modemX_msg_list( instream, fileOffset, outstream, modem_no)

        outstream.writelines(["\n**************************** modem%d gas nas msg list *******************************\n" % (modem_no)])
        fileOffset1     = fileOffset + 8 + MACRO_GAS_MNTN_REC_MSG_INFO_SIZE * MACRO_GAS_MNTN_REC_MSG_INFO_MAX_CNT
        analysis_gas_modemX_nas_msg_list( instream, fileOffset1, outstream, modem_no)

        ###### analysis gasm global status ########
        outstream.writelines(["\n**************************** modem%d GASM global status *******************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_DEBUG_MSG_LIST_LENGTH
        analysis_modemX_gasm_global_status( instream, fileOffset, outstream)

        ###### analysis gcomc global status #######
        outstream.writelines(["\n**************************** modem%d GCOMC global status ******************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_GASM_GLOBAL_STATUS_LENGTH
        analysis_modemX_gcomc_global_status( instream, fileOffset, outstream)

        ###### analysis gcomsi global status ######
        outstream.writelines(["\n**************************** modem%d GCOMSI global status ******************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_GCOMC_GLOBAL_STATUS_LENGTH
        analysis_modemX_gcomsi_global_status( instream, fileOffset, outstream)

        ###### analysis gcomm global status #######
        outstream.writelines(["\n**************************** modem%d GCOMM global status *******************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_GCOMSI_GLOBAL_STATUS_LENGTH
        analysis_modemX_gcomm_global_status( instream, fileOffset, outstream, version)

        ###### analysis rr global status ##########
        outstream.writelines(["\n**************************** modem%d RR global status **********************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_GCOMM_GLOBAL_STATUS_LENGTH
        analysis_modemX_rr_global_status( instream, fileOffset, outstream)

        ###### analysis grr global status #########
        outstream.writelines(["\n**************************** modem%d GRR global status *********************************\n" % (modem_no)])
        fileOffset      = fileOffset + MACRO_GAS_RR_GLOBAL_STATUS_LENGTH
        analysis_modemX_grr_global_status( instream, fileOffset, outstream)

def analysis_guas_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        
        ###### analysis guas debug version ########
        vers_no = analysis_guas_debug_version( instream, fileOffset, outstream)

        #### gas modem0 #########
        fileOffset      = eval(offset)
        analysis_gas_modemX_dump_info( instream, fileOffset, outstream, vers_no, 0)

        ##### was modem0 #########
        fileOffset      = fileOffset + MACRO_GAS_DEBUG_VERSION_LENGTH + MACRO_GAS_MODEM0_DUMP_INFO_LENGTH
        if ( MACRO_VERSION_NO_2 <= vers_no ):
            analysis_was_modem0_dump_info_vers_02( instream, fileOffset, outstream, 0)
        else:
            analysis_was_modem0_dump_info_vers_01( instream, fileOffset, outstream)
        
        if ( MACRO_VERSION_NO_4 > vers_no ):
            ##### gas modem1 #########
            fileOffset      = eval(offset) + MACRO_MODEM0_ADDR_LENGTH
            analysis_gas_modemX_dump_info( instream, fileOffset, outstream, vers_no, 1)

            ##### was modem1 #########
            modem1wasOffset      = fileOffset + MACRO_GAS_MODEM0_DUMP_INFO_LENGTH
            if ( MACRO_VERSION_NO_2 <= vers_no ):
                analysis_was_modem0_dump_info_vers_02( instream, modem1wasOffset, outstream, 1)
            else:
                analysis_was_modem0_dump_info_vers_01( instream, modem1wasOffset, outstream)


            ##### gas modem2 #########
            fileOffset      = fileOffset + MACRO_MODEM1_ADDR_LENGTH
            analysis_gas_modemX_dump_info( instream, fileOffset, outstream, vers_no, 2)

        return True


########################################################################################
def entry_0x2200004(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x2200004':
            print ("hidis field is %s." % (field) ) 
            print ("current field is 0x2200004.")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s." % (version) )
            print ("current version is 0x0000.")
            return error['ERR_CHECK_VERSION']
        elif not (len == '0x2800' or len == '0x1000'):
            print ("hids len is %s." % (len) )
            print ("current len is 0x4000." )
            return error['ERR_CHECK_LEN']
        ########check parameter end##############
        ret = analysis_guas_dump_info( infile, offset, outfile)

        return 0

