#!/usr/bin/env python
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2019-2020. All rights reserved. 
import struct
import os
import sys
import string

def PrintApDiag(infile, field, offset, slen, version, mode, outfile):
        addr = 0
        row = 0
        i = 0
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        print("got entry 0x1200001 PrintApDiag")
        outfile.writelines("offset      data\n")
        for i in range(0, int(int(slen,16)/16)):
            (charbyte1, charbyte2, charbyte3,charbyte4, ) = struct.unpack("IIII", infile.read(16))
            addr = 0x10 * row
            row = row + 1
            #print >> outhandler, "0x%08x: %08x %08x %08x %08x" %(addr, charbyte1, charbyte2, charbyte3, charbyte4)
            outfile.writelines("0x%08x: %08x %08x %08x %08x\n" %(addr, charbyte1, charbyte2, charbyte3, charbyte4))
        return
 	
def entry_0x1200001(infile, field, offset, slen, version, mode, outfile, field_list = None):
        try:
            if not field == '0x1200001':
                print('hidis field is ', field)
                print('current field is', '0x1200001')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x2000':
                print('hids len is ', slen)
                print('current len is ', '0x2000')
                return error['ERR_CHECK_LEN']
            print("got entry 0x1200001")
            outfile.writelines("============AP DIAG============\n")
            PrintApDiag(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
                print(str(e))
                outfile.writelines(str(e))
                return 1
