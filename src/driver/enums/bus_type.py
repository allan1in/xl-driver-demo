from enum import Enum

class BusType(Enum):
    XL_BUS_TYPE_NONE = 0x00000000
    XL_BUS_TYPE_CAN = 0x00000001
    XL_BUS_TYPE_LIN = 0x00000002
    XL_BUS_TYPE_FLEXRAY = 0x00000004
    XL_BUS_TYPE_AFDX = 0x00000008
    XL_BUS_TYPE_MOST = 0x00000010
    XL_BUS_TYPE_DAIO = 0x00000040
    XL_BUS_TYPE_J1708 = 0x00000100
    XL_BUS_TYPE_KLINE = 0x00000800
    XL_BUS_TYPE_ETHERNET = 0x00001000
    XL_BUS_TYPE_A429 = 0x00002000