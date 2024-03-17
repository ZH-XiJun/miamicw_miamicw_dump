#!/usr/bin/env 	python
# coding=utf-8
# Copyright (C) Huawei Technologies Co., Ltd. 2010-2018. All rights reserved.

import struct
import os

from config import *

def modemlogparse(logpath):
    ret = 0
    if logpath == "all":
        rootdir = '/data/hisi_logs/'
        if os.path.exists(rootdir):
            dirs = os.listdir(rootdir)
            print(dirs)
            for dirc in dirs:
                if os.path.isdir(rootdir + dirc) and dirc[:8].isdigit():
                    dirtoparse = '%s%s%s' %(rootdir, dirc, '/cp_log/')
                    if os.path.exists(dirtoparse):
                        parsesinglepath(dirtoparse)
        else:
            print("dir not exists")
    else:
        if os.path.exists(logpath):
            parsesinglepath(logpath)
    return ret


def parselinkedfile(in_handler, logpath):
    in_handler.seek(0,2)
    linkfilelen = in_handler.tell()
    print("linkfilelen is %d" % linkfilelen)
    in_handler.seek(0)
    curpos = 0
    while in_handler.tell() < linkfilelen:
        magic,=struct.unpack("I", in_handler.read(4))

        if 0x56786543 == magic:
            magic2,=struct.unpack("I", in_handler.read(4))
            linkfilename = in_handler.readline(32)
            print(linkfilename)
            linkfilename = linkfilename.decode(encoding="utf-8").strip('\x00')
            print(linkfilename)
            dstfilename, = struct.unpack('32s',in_handler.read(32))
            filenum, =struct.unpack("I", in_handler.read(4))
            totalnum, =struct.unpack("I", in_handler.read(4))
            packetnum, =struct.unpack("I", in_handler.read(4))
            totalpacket, =struct.unpack("I", in_handler.read(4))
            filelength, =struct.unpack("I", in_handler.read(4))
            realLength, =struct.unpack("I", in_handler.read(4))
            isAppend, =struct.unpack("I", in_handler.read(4))
            maxLength, =struct.unpack("I", in_handler.read(4))

            print("linked file is %s " % linkfilename)
            (filename,extension) = os.path.splitext(linkfilename)
            outfile = '%s%s%s' %(logpath, filename, '.txt')
            offset = in_handler.tell()

            if linkfilename in list(filedict.keys()):
                import_file = '%s%s%s' %('import ', filename, '_parser')
                function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser_link', '(in_handler, outfile, offset, filelength)')
                print(import_file)
                print(function)
                exec(import_file)
                exec(function)
            else:
                print("file %s not in the list" % linkfilename)
            curpos = curpos + int(filelength) + 104
            print("curpos is 0x%x" % curpos)
            in_handler.seek(curpos)
        else:
            break
    return


def parsesinglepath(logpath):
    ret = 0
    if os.path.exists(logpath + "DONE"):
        print('this directory already parse done')
        return ret

    for filetoparse in list(filedict.keys()):
        infile =  '%s%s' %(logpath, filetoparse)
        outfile = '%s%s' %(logpath, filedict[filetoparse])
        print(infile)
        print(outfile)

        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            with open(infile,"rb") as in_handler:
                magic,=struct.unpack("I", in_handler.read(4))
                print("magic is %d" % magic)
                if 0x56786543 == magic:
                    parselinkedfile(in_handler, logpath)
                    os.mknod(logpath + "DONE")
                    in_handler.close()
                    return
                else:
                    in_handler.close
                    print("oldstyle\n")
                    import_file = '%s%s%s' %('import ', filename, '_parser')
                    function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser', '(infile, outfile)')
                    exec(import_file)
                    exec(function)
                    ret = 0
        else:
            print((infile + "is not existed"))
            ret  = 0
    if ret == 0:
        os.mknod(logpath + "DONE")
    return




def main():
    if len(sys.argv) < 2:
        print("invalid argument")
        return
    else:
        logpath = sys.argv[1]

    for filetoparse in list(filedict.keys()):
        infile =  logpath + filetoparse
        outfile = logpath + filedict[filetoparse]
        print(("infile: " + infile))
        print(("outfile: " + outfile))


        if os.path.exists(infile):
            (filename,extension) = os.path.splitext(filetoparse)
            with open(infile,"rb") as in_handler:

                magic,=struct.unpack("I", in_handler.read(4))
                print("magic is %d" % magic)
                if 0x56786543 == magic:
                    parselinkedfile(in_handler, logpath)
                    in_handler.close()
                    return
                else:
                    in_handler.close
                    print("oldstyle\n")
                    import_file = '%s%s%s' %('import ', filename, '_parser')
                    function = '%s%s%s%s%s%s%s%s' %('ret = ', filename, '_parser', '.', 'entry_', filename, '_parser', '(infile, outfile)')
                    exec(import_file)
                    exec(function)
                    ret = 0
        else:
            print((infile + "is not existed"))
            ret  = 1
    if ret == 0:
        os.mknod(logpath + "DONE")


if __name__ == '__main__':
    main()

