#!/usr/bin/env python
# coding=utf-8
"""

功能；复位log分析脚本
版权信息：华为技术有限公司，版权所有(C) 2010-2019
修改记录：
	2019-11-08 尹鹏 创建内容
	2019-11-08 尹鹏 修改注释
"""



import struct
import os
import sys
import string

from nrrc_state import *
from nrrc_idlectrl_dump_info import *
import nrrc_pid_msg

NRRC_COMM_EXC_MAX_SAVE_MSG_NUM = 300
NRRC_COMM_EXC_MAX_SAVE_FSM_NUM = 50
NRRC_FSM_MAX_STACK_DEPTH       = 8
NRRC_FSM_MAX_HIGH_MSG_NUM      = 20
NRRC_INTRA_MSG_MAX_NUM         = 10


def analysis_nrps_msg_info( instream, fileOffset, outstream):
        ulLooper = 0
        strSendPid = 'nonPid'
        strRcvPid  = 'nonPid'
        strMsgid   = 'UnKnowId'
        
        instream.seek(fileOffset)

        (ItemNumTmp,) = struct.unpack('I', instream.read(4))

        ItemNum = ItemNumTmp

        #print("\n-------------ItemNum=%d-----------------\n" %(ItemNum))
        
        outstream.writelines(["%-15s%-20s%-20s%-15s%-70s\n" % ("TimeStamp", "SendPid", "RcvPid", "Aug","MsgId")])

        if ItemNum < NRRC_COMM_EXC_MAX_SAVE_MSG_NUM:
            MsgItemsNum = ItemNum
        else:
            MsgItemsNum = NRRC_COMM_EXC_MAX_SAVE_MSG_NUM
        while ulLooper < MsgItemsNum:
                #instream.seek(fileOffset + 16*(ulLooper) + 4)
                (ulTimeStamp,)      = struct.unpack('I', instream.read(4))
                (ulSendPid,)        = struct.unpack('H', instream.read(2)) 
                (ulRcvPid,)         = struct.unpack('H', instream.read(2))               
                (ulMsgId,)          = struct.unpack('I', instream.read(4))
                (ulAug,)            = struct.unpack('I', instream.read(4))
                
                #print("\n-------------ulLooper=%d-----------------\n" %(ulLooper))
                strSendPid = nrrc_pid_msg.Nrps_Get_Pid_Str(ulSendPid)
                strRcvPid  = nrrc_pid_msg.Nrps_Get_Pid_Str(ulRcvPid)
                strMsgid  = nrrc_pid_msg.Nrps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
                if 0xbd00 == ulMsgId:
                    timerid = 0x0000ffff & ulAug
                    strMsgid = Nrps_Get_Nrrc_StaTiId_Str(timerid)
                    
                strTimeStamp_Merge   = '0x%08x'% ulTimeStamp
                strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
                strRcvPid_Merge      = '%s(0x%x)' % ( strRcvPid, ulRcvPid)
                strAug_Merge         = '0x%08x' % ulAug
                #print("\n-------------GetPidStrSucc-----------------\n")
                if 0xbd00 == ulMsgId:
                    strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, timerid)
                else:
                    strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)
                
                #print("\n-------------strMsgId_Merge-----------------\n")
                outstream.writelines(["%-15s%-20s%-20s%-15s%-70s\n" % (strTimeStamp_Merge, strSendPid_Merge, strRcvPid_Merge, strAug_Merge, strMsgId_Merge)])
                ulLooper = ulLooper + 1
                
        
        return True


def analysis_nrrc_state_info( instream, fileOffset, outstream):
        ulLooper = 0
        instream.seek(fileOffset)
        
        strFsmId        = 'unkown'
        strMainState    = 'unkown'
        strSubState     = 'unkown'
        strStaTiId      = 'unkown'
        strRrcConnState = 'unkown'
        strLteState     = 'unkown'
        strRrcFlowCtrlFlg = 'unkown'

        CurrentPositionStr = ("0x%x" %(instream.tell()))
        outstream.writelines(["\n(1) IDLECTRL FSM STATE INFO[OffSet=%s]\n" % CurrentPositionStr])
        outstream.writelines(["%-35s%-58s%-58s\n" % ("TimeStamp", "MainState", "SubState")])

        (ItemNum,) = struct.unpack('I', instream.read(4))
        #outstream.writelines("\n-------------ItemNum=%d-----------------\n" %(ItemNum))
        
        while ulLooper < min(ItemNum,NRRC_COMM_EXC_MAX_SAVE_FSM_NUM):
                instream.seek(fileOffset + 8*(ulLooper) + 4)
                (ulTimeStamp,)  = struct.unpack('I', instream.read(4))
                (enMainState,)  = struct.unpack('H', instream.read(2))
                (enSubState,)   = struct.unpack('H', instream.read(2))

                #get mainstate
                strMainState   = Nrps_Get_Nrrc_MainState_Str(enMainState)
                
                #get substate
                strSubState    = Nrps_Get_Nrrc_SubState_Str(enSubState)
                
                strTimeStamp_Merge  = '0x%08x'% ulTimeStamp
                strMainState_Merge  = 'MS[0x%x]:%s'% ( enMainState, strMainState)
                strSubState_Merge   = 'SS[0x%x]:%s'% ( enSubState, strSubState)
                
                outstream.writelines(["%-35s%-58s%-58s\n" % (strTimeStamp_Merge, strMainState_Merge, strSubState_Merge)])
                ulLooper = ulLooper + 1
        
        return True


def analysis_nrrc_idlectrl_dump_info( instream, fileOffset, outstream):
        ulLooper = 0
        FsmStruList = []
        instream.seek(fileOffset)
        #print fileOffset
        #print instream.tell()
        
        #1. IDLECTRL BASIC INFO
        CurrentPositionStr = ("0x%x" %(instream.tell()))
        outstream.writelines(["\n(1) IDLECTRL BASIC INFO[OffSet=%s]\n\n" % CurrentPositionStr])

        #1.1 get data
        (PtlVer,)        = struct.unpack('I', instream.read(4))
        (NetDeployType,) = struct.unpack('B', instream.read(1))
        (PtlState,)      = struct.unpack('B', instream.read(1))
        (UeState,)       = struct.unpack('B', instream.read(1))
        (MasterFsm,)     = struct.unpack('B', instream.read(1))
        (UtranMode,)     = struct.unpack('B', instream.read(1))
        (CapState,)      = struct.unpack('B', instream.read(1))
        (PowerStatus,)   = struct.unpack('B', instream.read(1))
        (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte

        #1.2 get string
        strPtlVer        = '[0x%x]%s' %(PtlVer, GET_LTE_NR_PROTOCOL_VER_STR(PtlVer))
        strNetDeployType = '[0x%x]%s' %(NetDeployType, GET_NRRC_CCB_NET_DEPLOY_TYPE_STR(NetDeployType)) 
        strPtlState      = '[0x%x]%s' %(PtlState, GET_NRRC_PTL_STATE_STR(PtlState))
        strUeState       = '[0x%x]%s' %(UeState, GET_NRRC_UE_STATE_STR(UeState))
        strMasterFsm     = '[0x%x]%s' %(MasterFsm, GET_NRRC_MASTER_CTRL_FSM_STR(MasterFsm))
        strUtranMode     = '[0x%x]%s' %(UtranMode, GET_NRRC_UTRAN_MODE_STR(UtranMode))
        strCapState      = '[0x%x]%s' %(CapState, GET_NRRC_UE_CAMPED_STATE_STR(CapState))
        strPowerStatus   = '[0x%x]%s' %(PowerStatus, GET_NRRC_POWER_STATUS_STR(PowerStatus))

        #1.3 output to outstream
        outstream.writelines(["\t%-35s%-58s\n" % ("strPtlVer", strPtlVer)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strNetDeployType", strNetDeployType)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strPtlState", strPtlState)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strUeState", strUeState)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strMasterFsm", strMasterFsm)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strUtranMode", strUtranMode)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strCapState", strCapState)])
        outstream.writelines(["\t%-35s%-58s\n" % ("strPowerStatus", strPowerStatus)])

        #2. NRRC_IDLECTRL_FSM_INFO_STRU
        CurrentPositionStr = ("0x%x" %(instream.tell()))
        outstream.writelines(["\n(2) IDLECTRL FSM STACK INFO[OffSet=%s]\n\n" % CurrentPositionStr])
        outstream.writelines(["\t%-35s%-38s%-38s%-60s%-70s\n" % ("PARALLEL FSM", "FSM ID", "MainState", "SubState", "StatId")])
        while ulLooper < (NRRC_PARALLEL_FSM_BUTT):
            #get Parallel fsm
            strParallelFsm   = '[0x%x]%s' %(ulLooper, GET_NRRC_PARALLEL_FSM_STR(ulLooper))
            #GetCurrentFsm
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            (ItemNum,)  = struct.unpack('B', instream.read(1))

            #print("\n-------------ItemNum=%d-----------------\n" %(ItemNum))
            LoopFsmStack = 0
            while LoopFsmStack <= NRRC_FSM_MAX_STACK_DEPTH:
                (usFsmId,)      = struct.unpack('H', instream.read(2))
                (usMainState,)  = struct.unpack('H', instream.read(2))
                (usSubState,)   = struct.unpack('H', instream.read(2))
                (usStaTId,)     = struct.unpack('H', instream.read(2))
                if (LoopFsmStack >= ItemNum) and (LoopFsmStack < NRRC_FSM_MAX_STACK_DEPTH):
                    LoopFsmStack = LoopFsmStack + 1
                    continue
                
                #get usFsmId
                strFsmId       = '[0x%x]%s' %(usFsmId, Nrps_Get_Nrrc_FsmId_Str(usFsmId))
                #get mainstate
                strMainState   = '[0x%x]%s' %(usMainState, Nrps_Get_Nrrc_MainState_Str(usMainState))
                #get substate
                strSubState    = '[0x%x]%s' %(usSubState, Nrps_Get_Nrrc_SubState_Str(usSubState))
                #get substate
                strStatId      = '[0x%x]%s' %(usStaTId, Nrps_Get_Nrrc_StaTiId_Str(usStaTId))

                #print to file
                #outstream.writelines(["%-30s%-38s%-38s%-38s%-70s\n" % (strParallelFsm, strFsmId, strMainState, strSubState, strStatId)])
                #append to List
                FsmStruList.append(["\t%-35s%-38s%-38s%-60s%-70s\n" % (strParallelFsm, strFsmId, strMainState, strSubState, strStatId)])
                LoopFsmStack = LoopFsmStack + 1

            #Output To outstream
            #print("\n-------------len(FsmStruList)-=%d-----------------\n" %(len(FsmStruList)))
            #print("\n%s\n" %(FsmStruList))
            outstream.writelines(FsmStruList[len(FsmStruList)-1]) #current fsm

            #Add fsm stack
            ucLoopFsmStru=0
            for ucLoopFsmStru in range(len(FsmStruList)-1):
                outstream.writelines(FsmStruList[ucLoopFsmStru]) # fsm stack

            #clear FsmStruList
            FsmStruList=[]
            ulLooper = ulLooper + 1
            
        #3. NRRC_IDLECTRL_EXTERNAL_MSG_STRU
        CurrentPositionStr = ("0x%x" %(instream.tell()))
        outstream.writelines(["\n(3) IDLECTRL EXTERNAL MSG IN BUFFER[OffSet=%s]\n\n"%CurrentPositionStr])
        outstream.writelines(["\t%-35s%-20s%-20s%-15s%-70s\n" % ("PARALLEL FSM", "SEND PID", "RCV PID", "PRIVATE", "MSG ID")])
        for ulLooper in range(NRRC_PARALLEL_FSM_BUTT):
            #get Parallel fsm
            strParallelFsm   = '[0x%x]%s' %(ulLooper, GET_NRRC_PARALLEL_FSM_STR(ulLooper))
                
            (ucMsgBuffCnt,)  = struct.unpack('B', instream.read(1))
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            (Rsv,)           = struct.unpack('B', instream.read(1)) #reserved byte
            
            #print("\n-------------ucMsgBuffCnt=%d-----------------\n" %(ucMsgBuffCnt))
            LoopMsgBuff   = 0
            for LoopMsgBuff in range(NRRC_FSM_MAX_HIGH_MSG_NUM):
                (ulSendPid,)        = struct.unpack('H', instream.read(2)) 
                (ulRcvPid,)         = struct.unpack('H', instream.read(2))               
                (ulMsgId,)          = struct.unpack('I', instream.read(4))
                (ulAug,)            = struct.unpack('I', instream.read(4))
                
                if(LoopMsgBuff >= ucMsgBuffCnt):
                    continue
                
                strSendPid = nrrc_pid_msg.Nrps_Get_Pid_Str(ulSendPid)
                strRcvPid  = nrrc_pid_msg.Nrps_Get_Pid_Str(ulRcvPid)
                strMsgid   = nrrc_pid_msg.Nrps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
                
                if 0xbd00 == ulMsgId:
                    timerid = 0x0000ffff & ulAug
                    strMsgid = nrrc_pid_msg.Nrps_Get_Nrrc_StaTiId_Str(timerid)
                    
                strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
                strRcvPid_Merge      = '%s(0x%x)' % ( strRcvPid, ulRcvPid)
                strAug_Merge         = '0x%08x' % ulAug
                if 0xbd00 == ulMsgId:
                    strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, timerid)
                else:
                    strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)

                outstream.writelines(["\t%-35s%-20s%-20s%-15s%-70s\n" % (strParallelFsm, strSendPid_Merge, strRcvPid_Merge, strAug_Merge, strMsgId_Merge)])
               
        #4. NRRC_IDLECTRL_INTERIOR_MSG_STRU
        CurrentPositionStr = ("0x%x" %(instream.tell()))
        outstream.writelines(["\n(4) IDLECTRL INTRA MSG IN BUFFER[OffSet=%s]\n\n"%CurrentPositionStr])
        outstream.writelines(["\t%-20s%-20s%-15s%-70s\n" % ("SEND PID", "RCV PID", "PRIVATE", "MSG ID")])
        (usIntraMsgBuffCnt,)    = struct.unpack('H', instream.read(2))
        (Rsv,)                = struct.unpack('B', instream.read(1)) #reserved byte
        (Rsv,)                = struct.unpack('B', instream.read(1)) #reserved byte
        
        #print("\n-------------ucMsgBuffCnt=%d-----------------\n" %(usIntraMsgBuffCnt))
        
        LoopIntraMsg=0
        for LoopIntraMsg in range(NRRC_INTRA_MSG_MAX_NUM):
            (ulSendPid,)        = struct.unpack('H', instream.read(2)) 
            (ulRcvPid,)         = struct.unpack('H', instream.read(2))               
            (ulMsgId,)          = struct.unpack('I', instream.read(4))
            (ulAug,)            = struct.unpack('I', instream.read(4))
                
            if(LoopIntraMsg >= usIntraMsgBuffCnt):
                continue

            strSendPid = nrrc_pid_msg.Nrps_Get_Pid_Str(ulSendPid)
            strRcvPid  = nrrc_pid_msg.Nrps_Get_Pid_Str(ulRcvPid)
            strMsgid   = nrrc_pid_msg.Nrps_Get_MsgId_Str(strSendPid, strRcvPid,ulMsgId)
            
            if 0xbd00 == ulMsgId:
                timerid = 0x0000ffff & ulAug
                strMsgid = nrrc_pid_msg.Nrps_Get_Nrrc_StaTiId_Str(timerid)
                
            strSendPid_Merge     = '%s(0x%x)' % ( strSendPid, ulSendPid)
            strRcvPid_Merge      = '%s(0x%x)' % ( strRcvPid, ulRcvPid)
            strAug_Merge         = '0x%08x' % ulAug
            if 0xbd00 == ulMsgId:
                strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, timerid)
            else:
                strMsgId_Merge       = '%s(0x%x)' % ( strMsgid, ulMsgId)

            outstream.writelines(["\t%-20s%-20s%-15s%-70s\n" % (strSendPid_Merge, strRcvPid_Merge, strAug_Merge, strMsgId_Merge)])
            
        return True



def analysis_nrps_dump_info( infile, offset, outfile):
        instream = infile
        outstream  = outfile
        fileOffset = eval(offset)
        idlectrlinfooffset = fileOffset
        
        outstream.writelines(["************************************************************\n"])
        outstream.writelines(["******** NRPS_DUMP_ANALYSIS_2019_05_15_VERSION_1.0 *********\n"])
        outstream.writelines(["************************************************************\n\n"])
        
        outstream.writelines(["************************************  NRPS MSG INFO ***************************************\n"])
        analysis_nrps_msg_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + NRRC_COMM_EXC_MAX_SAVE_MSG_NUM*16 + 4
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************ NRRC STATE INFO ***************************************\n"])
        analysis_nrrc_state_info(infile, fileOffset, outfile)
        fileOffset = fileOffset + NRRC_COMM_EXC_MAX_SAVE_FSM_NUM*8 + 4
        outstream.writelines(["\n"])
        
        outstream.writelines(["************************************ NRRC IDLECTRL DUMP INFO ***************************************\n"])
        idlectrlinfooffset = idlectrlinfooffset + 0x1800
        analysis_nrrc_idlectrl_dump_info(infile, idlectrlinfooffset, outfile)
        outstream.writelines(["\n"])

        outstream.writelines(["\n"])
        outstream.writelines(["************************************************************\n"])
        outstream.writelines(["******** NRPS_DUMP_ANALYSIS_2019_05_15_VERSION_1.0 *********\n"])
        outstream.writelines(["************************************************************\n\n"])
        return True


########################################################################################
def entry_0x7200013(infile, field, offset, len, version, mode, outfile):

        ########check parameter start#############
        if not field == '0x7200013':
            print('hidis field is ', field)
            print('current field is', '0x7200013')
            return error['ERR_CHECK_FIELD']
        elif not len == '0x2800':
            print('hids len is ', len)
            print('current len is ', '0x2800')
            return error['ERR_CHECK_LEN']
        #########check parameter end##############

        ret = analysis_nrps_dump_info( infile, offset, outfile)

        return 0

#for single script para modem_dump.bin
'''
filein = open("modem_dump.bin", 'rb+')
fileout = open("OutPut.txt", "w+")
#Modem_dump.bin 0x25090c 0x262a0c
entry_0x7200013(filein, "0x7200013", '0x262a0c', '0x2800', 0, 0, fileout)
filein.close()
fileout.close();
'''
