#!/usr/bin/env python
"""
Copyright © Huawei Technologies Co., Ltd. 2010-2019. All rights reserved.
description     :   analysis guas dump bin
author          :   wumai 00167002
modify  record  :   2016-01-22 create file
"""

import struct
import os
import sys
import string
from nas_pid import *
from at_css_msg import *
from at_imsa_msg import *
from at_mn_msg import *
from at_mta_msg import *
from at_ndis_msg import *
from at_oam_msg import *
from at_phy_msg import *
from at_rabm_msg import *
from at_rnic_msg import *
from at_xpds_msg import *
from at_at_msg import *
from at_ccm_msg import *
from at_drvagent_msg import *
from at_ftm_msg import *
from at_l4a_msg import *
from at_mma_msg import *
from at_ppp_msg import *
from at_taf_dsm_msg import *

MACRO_AT_MAX_LOG_MSG_NUM   = 100
MACRO_AT_MSG_INFO_SIZE     = 16

MACRO_AT_MAX_PORT_NUM      = 37
MACRO_AT_PORT_INFO_SIZE    = 24
MACRO_AT_CMD_NAME_LEN      = 12


def get_at_msg_str( pid, ulMsgId):
        if ( 'i0_xpds' == pid.lower() or 'i1_xpds' == pid.lower() or 'i2_xpds' == pid.lower()):
                return get_at_xpds_msg_str(ulMsgId)
        elif ( 'rnic' == pid.lower()):
                return get_at_rnic_msg_str(ulMsgId)
        elif ( 'rabm' == pid.lower() or 'i1_rabm' == pid.lower()):
                return get_at_rabm_msg_str(ulMsgId)
        elif ( 'i1_stk' == pid.lower() or 'i1_pih' == pid.lower() or 'i1_pb' == pid.lower()):
                return get_at_oam_msg_str(ulMsgId)
        elif ( 'si_stk' == pid.lower() or 'si_pih' == pid.lower() or 'si_pb' == pid.lower()):
                return get_at_oam_msg_str(ulMsgId)
        elif ( 'i2_stk' == pid.lower() or 'i2_pih' == pid.lower() or 'i2_pb' == pid.lower()):
                return get_at_oam_msg_str(ulMsgId)
        elif ( 'ndis' == pid.lower()):
                return get_at_ndis_msg_str(ulMsgId)
        elif ( 'i0_imsa' == pid.lower() or 'i1_imsa' == pid.lower()):
                return get_at_imsa_msg_str(ulMsgId)
        elif ( 'css' == pid.lower()):
                return get_at_css_msg_str(ulMsgId)
        elif ( 'mta' == pid.lower() or 'i1_mta' == pid.lower() or 'i2_mta' == pid.lower()):
                return get_at_mta_msg_str(ulMsgId)
        elif ( 'mma' == pid.lower() or 'i1_mma' == pid.lower() or 'i2_mma' == pid.lower()):
                return get_at_mma_msg_str(ulMsgId)
        elif ( 'at' == pid.lower()):
                return get_at_at_msg_str(ulMsgId)
        elif ( 'i0_ccm' == pid.lower() or 'i1_ccm' == pid.lower() or 'i2_ccm' == pid.lower()):
                return get_at_ccm_msg_str(ulMsgId)
        elif ( 'i0_drv_agent' == pid.lower() or 'i1_drv_agent' == pid.lower() or 'i2_drv_agent' == pid.lower()):
                return get_at_drvagent_msg_str(ulMsgId)
        elif ( 'i0_sys_ftm' == pid.lower() or 'i1_sys_ftm' == pid.lower()):
                return get_at_ftm_msg_str(ulMsgId)
        elif ( 'i0_l4_l4a' == pid.lower() or 'i1_l4_l4a' == pid.lower()):
                return get_at_l4a_msg_str(ulMsgId)
        elif ( 'ppp' == pid.lower()):
                return get_at_ppp_msg_str(ulMsgId)
        elif ( 'taf' == pid.lower() or 'i1_taf' == pid.lower() or 'i2_taf' == pid.lower()):
                return get_at_taf_dsm_msg_str(ulMsgId)
        elif ( 'i0_dsm' == pid.lower() or 'i1_dsm' == pid.lower() or 'i2_dsm' == pid.lower()):
                return get_at_taf_dsm_msg_str(ulMsgId)
        else:
                return 'none'

def analysis_at_mntn_per_rec_msg_info(index, instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (ulSendPid,)        = struct.unpack('I', instream.read(4))
        (ulMsgId,)          = struct.unpack('I', instream.read(4))
        (ulSliceStart,)     = struct.unpack('I', instream.read(4))
        (ulSliceEnd,)       = struct.unpack('I', instream.read(4))

        strSendPid      = guas_get_pid_str(ulSendPid)
        strMsgId        = get_at_msg_str(strSendPid, ulMsgId)

        strSendPid      = '%s(0x%x)' % ( strSendPid, ulSendPid)
        strMsgId        = '%s(0x%x)' % ( strMsgId, ulMsgId)
        strStartSlice   = '0x%x'% ulSliceStart
        strEndSlice     = '0x%x'% ulSliceEnd

        outstream.writelines(["%-6s%-20s%-60s%-20s%-20s\n" % (index, strSendPid, strMsgId, strStartSlice, strEndSlice)])

def analysis_at_mntn_per_rec_port_info(index, instream, fileLocalOffset, outstream):
        instream.seek(fileLocalOffset)

        (ulRcvStreamCnt,)  = struct.unpack('I', instream.read(4))
        (ulSndStreamCnt,)  = struct.unpack('I', instream.read(4))
        (strCmdName,)      = struct.unpack('12s', instream.read(12))
        (ulClientStatus,)  = struct.unpack('I', instream.read(4))
        strRcvStreamCnt    = '%-10d(0x%-8x)' % ( ulRcvStreamCnt, ulRcvStreamCnt)
        strSndStreamCnt    = '%-10d(0x%-8x)' % ( ulSndStreamCnt, ulSndStreamCnt)
        outstream.writelines(["%-6d%-30s%-30s%-60s%-20d\n" % (index, strRcvStreamCnt, strSndStreamCnt, strCmdName, ulClientStatus)])

def analysis_at_msg_port_dump_info( instream, fileOffset, outstream):
        ulMsgLooper        = 0
        ulPortLooper       = 0

        outstream.writelines(["%-6s%-20s%-60s%-20s%-20s\n" % ("index", "ulSendPid", "ulMsgName", "ulSliceStart", "ulSliceEnd")])
        while ulMsgLooper < MACRO_AT_MAX_LOG_MSG_NUM:
            ulLooperIndex = ulMsgLooper % MACRO_AT_MAX_LOG_MSG_NUM
            fileLocalOffset = fileOffset + ulLooperIndex * MACRO_AT_MSG_INFO_SIZE
            analysis_at_mntn_per_rec_msg_info(ulMsgLooper, instream, fileLocalOffset, outstream)
            ulMsgLooper = ulMsgLooper + 1

        fileLocalOffset = fileOffset + MACRO_AT_MAX_LOG_MSG_NUM * MACRO_AT_MSG_INFO_SIZE

        instream.seek(fileLocalOffset)
        (ulCurIndex,) = struct.unpack('I', instream.read(4))
        outstream.writelines(["\n last proc msg index is %d.\n\n" % (ulCurIndex - 1)])

        #offset add index len and reserv len
        fileLocalOffset = fileLocalOffset + 8;

        outstream.writelines(["%-6s%-30s%-30s%-60s%-20s\n" % ("index", "ulRcvStreamCnt", "ulSndStreamCnt", "aucCmdName", "ulClientStatus")])
        while ulPortLooper < MACRO_AT_MAX_PORT_NUM:
            analysis_at_mntn_per_rec_port_info(ulPortLooper, instream, fileLocalOffset, outstream)
            fileLocalOffset = fileLocalOffset + MACRO_AT_PORT_INFO_SIZE
            ulPortLooper = ulPortLooper + 1


def analysis_at_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)

        ulbeginTick     = 0
        ulEndTick       = 0

        outstream.writelines(["\n**************************** analysis_at_dump_info begin!*******************************\n"])
        global GLOBAL_Offset

        instream.seek(fileOffset)
        (ulBeginTick,)       = struct.unpack('I', instream.read(4))
        strBeginTick         = '%x'% ulBeginTick
        print ("AT DUMP Begin tag is %s" % (strBeginTick))

        #在0xaa55aa55之后有4字节的reserve位，所以偏移需要加8
        fileOffset = fileOffset + 8

#       Old Version begin is 0xaa55aa55
        global Global_Version
        if ulBeginTick == 2857740885:
            Global_Version = 0x01
            analysis_at_msg_port_dump_info(instream, fileOffset, outstream)

        #2857740885 = 0xaa55aa55 find end tick
        while ulEndTick != 2857740885:
                (ulEndTick,)       = struct.unpack('I', instream.read(4))

        strEndTick         = '%x'% ulEndTick
        print ("AT DUMP End tag is %s" % (strEndTick))


        outstream.writelines(["\n**************************** analysis_at_dump_info end!*******************************\n"])

        return True

########################################################################################
def entry_0x1200003(infile, field, offset, len, version, mode, outfile):
        ########check parameter start#############
        if not field == '0x1200003':
            print ("hidis field is %s" % (field))
            print ("current field is 0x1200003")
            return error['ERR_CHECK_FIELD']
        elif not version == '0x0000':
            print ("hidis version is %s" % (version))
            print ("current version is 0x0000")
            return error['ERR_CHECK_VERSION']
        #########check parameter end##############
        ret = analysis_at_dump_info( infile, offset, outfile)

        #c = msvcrt.getch()
        return 0

