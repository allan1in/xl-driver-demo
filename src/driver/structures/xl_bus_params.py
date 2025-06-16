from ctypes import Structure, Union, c_uint, c_ubyte, c_ushort


class CAN(Structure):
    _fields_ = [
        ("bitRate", c_uint),
        ("sjw", c_ubyte),
        ("tseg1", c_ubyte),
        ("tseg2", c_ubyte),
        ("sam", c_ubyte),
        ("outputMode", c_ubyte),
        ("reserved1", c_ubyte * 7),
        ("canOpMode", c_ubyte)
    ]


class CANFD(Structure):
    _fields_ = [
        ("arbitrationBitRate", c_uint),
        ("sjwAbr", c_ubyte),
        ("tseg1Abr", c_ubyte),
        ("tseg2Abr", c_ubyte),
        ("samAbr", c_ubyte),
        ("outputMode", c_ubyte),
        ("sjwDbr", c_ubyte),
        ("tseg1Dbr", c_ubyte),
        ("tseg2Dbr", c_ubyte),
        ("dataBitRate", c_uint),
        ("canOpMode", c_ubyte)
    ]


class MOST(Structure):
    _fields_ = [
        ("activeSpeedGrade", c_uint),
        ("compatibleSpeedGrade", c_uint),
        ("inicFwVersion", c_uint)
    ]


class FlexRay(Structure):
    _fields_ = [
        ("status", c_uint),
        ("cfgMode", c_uint),
        ("baudrate", c_uint)
    ]


class Ethernet(Structure):
    _fields_ = [
        ("macAddr", c_ubyte * 6),
        ("connector", c_ubyte),
        ("phy", c_ubyte),
        ("link", c_ubyte),
        ("speed", c_ubyte),
        ("clockMode", c_ubyte),
        ("bypass", c_ubyte)
    ]


class TX(Structure):
    _fields_ = [
        ("bitrate", c_uint),
        ("parity", c_uint),
        ("minGap", c_uint)
    ]


class RX(Structure):
    _fields_ = [
        ("bitrate", c_uint),
        ("minBitrate", c_uint),
        ("maxBitrate", c_uint),
        ("parity", c_uint),
        ("minGap", c_uint),
        ("autoBaudrate", c_uint)
    ]


class Dir(Union):
    _fields_ = [
        ("tx", TX),
        ("rx", RX),
        ("raw", c_ubyte * 24)
    ]


class A429(Structure):
    _fields_ = [
        ("channelDirection", c_ushort),
        ("res1", c_ushort),
        ("dir", Dir)
    ]


class Data(Union):
    _fields_ = [
        ("can", CAN),
        ("canFD", CANFD),
        ("most", MOST),
        ("flexray", FlexRay),
        ("ethernet", Ethernet),
        ("a429", A429),
        ("raw", c_ubyte * 28)
    ]


class XLBusParams(Structure):
    _fields_ = [
        ("busType", c_uint),
        ("data", Data)
    ]
