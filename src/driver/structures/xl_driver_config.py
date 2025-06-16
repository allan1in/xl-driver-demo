from ctypes import Structure, c_uint
from src.driver.structures.xl_channel_config import XLChannelConfig

class XLDriverConfig(Structure):
    _fields_ = [
        ("dllVersion", c_uint),
        ("channelCount", c_uint),
        ("reserved", c_uint * 10),
        ("channel", XLChannelConfig * 64)
    ]