﻿#######################################################################################################################################
#   filename        :   exparse_python_frame.py
#
#   author          :   dongtinghuan 00212987
#
#   description     :   config for exparse python sripts frame
#
#   modify  record  :   2014-07-21 create file
#
#######################################################################################################################################
import struct
import os
import sys
import string
from config import *
reload(sys)
sys.setdefaultencoding('utf8')

def exc_1000001A(infile,offset,outfile):
    oam_dict = {}
    print_num = 0
    len = (49152 - 20) # first msg except
    infile.seek(int(offset, 16) + 20)

    outfile.writelines(["  %-25s%s\n" % ("alloc_Taskid", "alloc_size")])

    for i in range(0, (len),20):
        (addmsg, ) = struct.unpack('I',infile.read(4))
        (alloc_slice, ) = struct.unpack('I',infile.read(4))
        (msgcont, ) = struct.unpack('I',infile.read(4))
        (alloc_size, ) = struct.unpack('I',infile.read(4))
        (alloc_pid, ) = struct.unpack('I',infile.read(4))

        if alloc_pid == 0 and alloc_size == 0:
            break

        outfile.writelines(['  %-25d%d\n' % (alloc_pid,alloc_size)])

        print_num += 1

        if alloc_pid in oam_dict:
            oam_dict[alloc_pid] += 1
        else:
            oam_dict[alloc_pid] = 1

    outfile.write("\r\n\r\n  total:\r\n")

    all_alloc_num = 0;
    dict1= sorted(oam_dict.iteritems(), key=lambda d:d[1], reverse = True)
    print dict1
    for oam_key in dict1:
        # print 'alloc_pid=%d, alloc_num=%d' % (oam_key,oam_dict[oam_key])
        outfile.writelines(['  %-25d%d\n' % (oam_key[0],oam_key[1])])
        all_alloc_num += oam_key[1]

    outfile.writelines(['all_alloc_num=%d\n' % all_alloc_num])

def exc_1000001B(infile,offset,outfile):
    oam_dict = {}
    print_num = 0
    len = (49152 - 20) # first msg except
    infile.seek(int(offset, 16) + 20)
    #outfile.write('file_id \t line_no \t alloc_pid \t alloc_size \t alloc_tick\r\n')
    outfile.writelines(["  %-25s%s\n" % ("alloc_pid", "alloc_num")])

    (file_id, ) = struct.unpack('I',infile.read(4))
    (line_no, ) = struct.unpack('I',infile.read(4))
    (alloc_pid, ) = struct.unpack('I',infile.read(4))
    (alloc_size, ) = struct.unpack('I',infile.read(4))
    (alloc_tick, ) = struct.unpack('I',infile.read(4))
    keyalloc = alloc_size

    for i in range(0, (len - 20),20):
        (file_id, ) = struct.unpack('I',infile.read(4))
        (line_no, ) = struct.unpack('I',infile.read(4))
        (alloc_pid, ) = struct.unpack('I',infile.read(4))
        (alloc_size, ) = struct.unpack('I',infile.read(4))
        (alloc_tick, ) = struct.unpack('I',infile.read(4))

        #outfile.write('%d' % file_id  + ' \t %d' % line_no + ' \t %d' % alloc_pid + ' \t %d' % alloc_size + ' \t %X' % alloc_tick+'\r\n')
        #outfile.write('%d' % file_id  + ' \t %d' % line_no + ' \t %d' % alloc_pid + ' \t %d' % alloc_size + ' \t %X' % alloc_tick+'\r\n')

        #if print_num < 16:
            #print 'file_id=%X,line_no=%X,alloc_pid=%X, alloc_size=%X,alloc_tick=%X' % (file_id,line_no,alloc_pid,alloc_size,alloc_tick)
            #print '\n'
            #print_num += 1

        if alloc_pid == 0 and alloc_size == 0:
            break

        print_num += 1

        if alloc_pid in oam_dict:
            oam_dict[alloc_pid] += 1
        else:
            oam_dict[alloc_pid] = 1

    all_alloc_num = 0;
    dict1= sorted(oam_dict.iteritems(), key=lambda d:d[1], reverse = True)
    for oam_key in dict1:
        # print 'alloc_pid=%d, alloc_num=%d' % (oam_key,oam_dict[oam_key])
        outfile.writelines(['  %-25d%d\n' % (oam_key[0],oam_key[1])])
        all_alloc_num += oam_key[1]

    outfile.writelines(['all_alloc_num=%d\n' % all_alloc_num])

d       = {0xF0:'RST          ',
           0xF1:'CLASS_SWITCH ',
           0xF2:'GET_CARD_STAU',
           0xF3:'SND_DATA1    ',
           0xF4:'RCV1         ',
           0xF5:'SND_DATA2    ',
           0xF6:'SND_DATA3    ',
           0xF7:'SND_DATA4    ',
           0xF8:'RCV2         ',
           0xF9:'RCV3         ',
           0xFA:'RCV4         ',
           0xFB:'DEACT        '}
def ReplaceKey(key):
    for k in d:
        if (k == key):
            return d[k]

    return '             '

def exc_100000CD(infile,offset,outfile):
    print_key = 0
    len = (0xD000 - 0xC000) # first msg except
    infile.seek(int(offset, 16)+0xC000)
    outfile.write('snd_pid\trcv_pid\tfunc_id\tfunc_name  \t   start_slice\tend_slice \t diff_slice\r\n')

    for i in range(0, len,16):
        (pid, ) = struct.unpack('h',infile.read(2))
        (pid1, ) = struct.unpack('h',infile.read(2))
        (FUC, ) = struct.unpack('h',infile.read(2))
        (FUC1, ) = struct.unpack('h',infile.read(2))
        (start_lice, ) = struct.unpack('I',infile.read(4))
        (end_slice, ) = struct.unpack('I',infile.read(4))

        if (print_key > start_lice):
            outfile.write('                                         %X' % print_key  + " - 80s(80*32764) = 0x%X"%(print_key - 80*32764) + '\r\n ################################ new log end #######################################\r\n')
        print_key = start_lice

        if (0 == end_slice):
            outfile.write('%d' % pid  + ' \t %d' % pid1 + ' \t %02X' % FUC + ' \t %s' % ReplaceKey(FUC)+' \t %X' % start_lice + ' \t %X' % end_slice +'\r\n')
        else:
            if(0xF0 == FUC):
                outfile.write('%d' % pid + ' \t %d' % pid1 + ' \t %02X' % FUC + ' \t %s' % ReplaceKey(FUC) +
                              ' \t %X' % start_lice + ' \t %X' % end_slice + ' \t %d' % (end_slice - start_lice) + ' =========# card reset #========\r\n')
            else:
                tempslice=(end_slice - start_lice)
                if (1000 < tempslice):
                    outfile.write('%d' % pid  + ' \t %d' % pid1 + ' \t %02X' % FUC  + ' \t %s' % ReplaceKey(FUC)+
                                  ' \t %X' % start_lice + ' \t %X' % end_slice + ' \t %d' % tempslice + ' \t=%.2f' % (tempslice / 32764.0) +'s\r\n')
                else:
                    outfile.write('%d' % pid + ' \t %d' % pid1 + ' \t %02X' % FUC + ' \t %s' % ReplaceKey(FUC) +
                                  ' \t %X' % start_lice + ' \t %X' % end_slice + ' \t %d' % tempslice + '\r\n')

def entry_0x7200000(infile, field, offset, len, version, mode, outfile, errcode):

    try:
        print type(errcode)
        if ('268435482' == errcode):
            outfile.write(('\r\n 请查看申请消息最多的PID：\r\n\r\n').decode('utf-8').encode('gbk'))
            exc_1000001A(infile,offset,outfile)
        elif ('268435483' == errcode):
            outfile.write(('\r\n 请查看申请内存最多的PID：\r\n\r\n').decode('utf-8').encode('gbk'))
            exc_1000001B(infile,offset,outfile)
        else:
            print "error code is" 

        #outfile.write(('\r\n================= 各组件PID 与 USIM交互信息解析 ================= \r\n\r\n').decode('utf-8').encode('gbk'))
        exc_100000CD(infile,offset,outfile)
    except Exception, e:
        #traceback.print_exc()
        outfile.write(str(e))
        return 0
    return 0

