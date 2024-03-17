#!/usr/bin/env python
# coding=utf-8
#-*- coding: utf-8 -*-
#***********************************************************************
# * Copyright     Copyright(c) 2019 - Hisilicon Technoligies Co., Ltd.
# * Filename
# * Description   analysis dmesg
# * Version       1.0
# * Data          2019.12.18
# * Author        y00354081
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
        outfile.writelines(tag.decode(encoding="utf-8"))
        if tag == b'\x0A':
            outfile.writelines('\n')
    outfile.writelines("\n============IMS SDK END============\n")
    return

def entry_0x2200014(infile, field, offset, slen, version, mode, outfile):
        try:
            if not field == '0x2200014':
                print('hidis field is ', field)
                print('current field is', '0x2200014')
                return error['ERR_CHECK_FIELD']
            elif not version == '0x0000':
                print('hidis version is ', version)
                print('current version is ', '0x0000')
                return error['ERR_CHECK_VERSION']
            elif not slen == '0x800':
                print('hids len is ', slen)
                print('current len is ', '0x800')
            outfile.writelines("\n============IMS SDK BEGIN============\n")
            PrintExcInfo(infile, field, offset, slen, version, mode, outfile)
            return 0

        except Exception as e:
            print(str(e))
            outfile.writelines(str(e))
            return 1
