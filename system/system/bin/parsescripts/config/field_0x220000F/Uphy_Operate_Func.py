#!/usr/bin/env python
# coding=utf-8
"""
���ܣ�uphy operate func
��Ȩ��Ϣ����Ϊ�������޹�˾����Ȩ���У�C��2010-2019
�޸ļ�¼��2016-07-08 00349889 ����
"""

__author__ = 'y00349889'

def UphySetExistBit(int_type, mask):
    return(int_type | mask)

def UphyIsModeExistBit(int_type, mask):
    return(int_type & mask)


def UphySetModemModeStatus(mode_type, ModemIdx):
    if (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 0 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_WCDMA') and ( ModemIdx == 0 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 1 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_WCDMA') and ( ModemIdx == 1 ):
        return UphySetExistBit( mode_type,ModemIdx )
    elif (strRatList == 'PLATFORM_RAT_GSM') and ( ModemIdx == 2 ):
        return UphySetExistBit( mode_type,ModemIdx )
    else:
        return 0

