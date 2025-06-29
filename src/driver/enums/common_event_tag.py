from enum import Enum

class CommonEventTag(Enum):
    XL_RECEIVE_MSG = 0x0001
    XL_CHIP_STATE = 0x0004
    XL_TRANSCEIVER_INFO = 0x0006
    XL_TRANSCEIVER = XL_TRANSCEIVER_INFO
    XL_TIMER_EVENT = 0x0008
    XL_TIMER = XL_TIMER_EVENT
    XL_TRANSMIT_MSG = 0x000A
    XL_SYNC_PULSE = 0x000B
    XL_APPLICATION_NOTIFICATION = 0x000F