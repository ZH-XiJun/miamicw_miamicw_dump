#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis secdump dump
# * Version       1.0
# * Data          2019.6.28
# * Author        l00438887
#***********************************************************************
import struct
import os
import sys
import string

def PrintSecDumpInfo(infile, field, offset, slen, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x7F0000F PrintSecDumpInfo, slen is 0x%x" %(int(slen,16)))
        outfile.writelines("offset      data\n")
        for i in range(0, int(int(slen,16)/16)):
            (charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
            addr = 0x10 * row
            row = row + 1
            #print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
            outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
        return

def entry_0x7F0000F(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x7F0000F':
                print('hidis field is ', field)
                print('current field is', '0x7F0000F')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            print("got entry 0x7F0000F")
            outfile.writelines("============NR SECDUMP============\n")
            PrintSecDumpInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1
