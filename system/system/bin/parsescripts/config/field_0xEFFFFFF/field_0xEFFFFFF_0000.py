#!/usr/bin/env python
# coding=utf-8
#-*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description    dump dmesg
# * Version       1.0
# * Data          2019.6.28
# * Author        y00428352
#***********************************************************************
import struct
import os
import sys
import string

def PrintExcInfo(infile, field, offset, slen, version, mode, outfile):
        MyOffset = eval(offset)
        infile.seek(MyOffset)
        
        MyLen = int(slen,16)
        for i in range(0, MyLen):
            tag = infile.readline(1)
            if tag >= b'x20' and tag <= b'x7E':
                outfile.writelines(tag.decode(encoding="utf-8"))
            elif tag == b'\x0A':
                outfile.writelines('\n')
        outfile.writelines("dmesg end\n")
        return
        return
 	
def entry_0xEFFFFFF(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0xEFFFFFF':
                print('hidis field is ', field)
                print('current field is', '0xEFFFFFF')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x235C':
                print('hids len is ', slen)
                print('current len is ', '0x235C')
            print("got entry 0xEFFFFFF")
            print(offset)
            outfile.writelines("============FASTBOOT PRINT============\n")
            PrintExcInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1
