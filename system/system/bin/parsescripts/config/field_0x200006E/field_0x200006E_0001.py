#!/usr/bin/env python
# coding=utf-8 
"""
功能：parse ICC dump memory
版权信息：华为技术有限公司，版权所有（C）2010-2019
修改记录：
"""
import sys
from config import *

def parse_icc_bin_send(fifo_type, infile, offset, outfile):
	infile.seek(offset)
	(front, ) = struct.unpack('I', infile.read(4))
	(rear, )  = struct.unpack("I", infile.read(4))
	(size, )  = struct.unpack("I", infile.read(4))

	# 队列头
	s1 = "******************************************** [%s] ********************************************\n" % (fifo_type)
	outfile.writelines(s1)
	outfile.writelines('%-14s%-14s%-14s\n' %('front', 'rear', 'size'))
	outfile.writelines('0x%-11x 0x%-11x 0x%-11x\n' % (front, rear, size))

	# 10条消息
	outfile.writelines('%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s\n' %('channel_id', '  send_task_id', '   recv_task_id', '    len', '            pos', '                 duration_prev', '    duration_post', '   data'))
	for i in range(1, 11):
		(channel_id, )    = struct.unpack("I", infile.read(4))
		(send_task_id, )  = struct.unpack("I", infile.read(4))
		(recv_task_id, )  = struct.unpack("I", infile.read(4))
		(len, )           = struct.unpack("I", infile.read(4))
		(pos, )           = struct.unpack("I", infile.read(4))
		(duration_prev, ) = struct.unpack("I", infile.read(4))
		(duration_post, ) = struct.unpack("I", infile.read(4))
		#outfile.writelines('0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x 0x%-11x\n' % (channel_id, send_task_id, recv_task_id, len, pos, duration_prev, duration_post))
		outfile.writelines('0x%08X    0x%08X    0x%08X    0x%08X    0x%08X   0x%08X    0x%08X' % (channel_id, send_task_id, recv_task_id, len, pos, duration_prev, duration_post))
		outfile.writelines('     ')
		for j in range(1, 11):
			(data, ) = struct.unpack("I", infile.read(4))
			outfile.writelines('0x%08X  ' %(data)) 
		outfile.writelines('\n')
	outfile.writelines('\n\n')

def parse_icc_bin_recv(fifo_type, infile, offset, outfile):
	infile.seek(offset)
	(front, ) = struct.unpack('I', infile.read(4))
	(rear, )  = struct.unpack("I", infile.read(4))
	(size, )  = struct.unpack("I", infile.read(4))

	# 队列头
	s1 = "******************************************** [%s] ********************************************\n" % (fifo_type)
	outfile.writelines(s1)
	outfile.writelines('%-14s%-14s%-14s\n' %('front', 'rear', 'size'))
	outfile.writelines('0x%-11x 0x%-11x 0x%-11x\n' % (front, rear, size))

	# 10条消息
	outfile.writelines('%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s%-14s\n' %('channel_id', '  send_task_id', '   recv_task_id', '    len', '           pos', '                  before_recv_slice', '    in_read_cb_slice', '   after_recv_slice', '   max_cb_slice_delta', '     max_cb_chan_id', '    cnt', '             sum', '                   avg'))
	for i in range(1, 11):
		(channel_id, )         = struct.unpack("I", infile.read(4))
		(send_task_id, )       = struct.unpack("I", infile.read(4))
		(recv_task_id, )       = struct.unpack("I", infile.read(4))
		(len, )                = struct.unpack("I", infile.read(4))
		(pos, )                = struct.unpack("I", infile.read(4))
		(before_recv_slice, )  = struct.unpack("I", infile.read(4))
		(in_read_cb_slice, )   = struct.unpack("I", infile.read(4))
		(after_recv_slice, )   = struct.unpack("I", infile.read(4))
		(max_cb_slice_delta, ) = struct.unpack("I", infile.read(4))
		(max_cb_chan_id, )     = struct.unpack("I", infile.read(4))
		(cnt, )                = struct.unpack("I", infile.read(4))
		(sum, )                = struct.unpack("I", infile.read(4))
		(avg, )                = struct.unpack("I", infile.read(4))
		outfile.writelines('0x%08X   0x%08X     0x%08X    0x%08X   0x%08X    0x%08X           0x%08X           0x%08X        0x%08X              0x%08X           0x%08X      0x%08X      0x%08X\n' % (channel_id, send_task_id, recv_task_id, len, pos, before_recv_slice, in_read_cb_slice, after_recv_slice, max_cb_slice_delta, max_cb_chan_id, cnt, sum, avg))
	outfile.writelines('\n\n')

def entry_0x200006E(infile, field, offset, len, version, mode, outfile):
	########check parameter start#############
	if not field == '0x200006E':
		print('hidis field is ', field)
		print('current field is', '0x200006E')
		return error['ERR_CHECK_FIELD']
	elif not version == '0x0000':
		print('hidis version is ', version)
		print('current version is ', '0x00')
#		return error['ERR_CHECK_VERSION']
	elif not len == '0x400':
		print('hids len is ', len)
		print('current len is ', '0x400')
#		return error['ERR_CHECK_LEN']
	#########check parameter end##############

	parse_icc_bin_send('fifo_send', infile, eval(offset), outfile)
	parse_icc_bin_recv('fifo_recv', infile, infile.tell(), outfile)
	return 0