from enum import Enum

class XLStatus(Enum):
    XL_SUCCESS = 0   # 0x0000
    XL_PENDING = 1   # 0x0001
    XL_ERR_QUEUE_IS_EMPTY = 10  # 0x000A
    XL_ERR_QUEUE_IS_FULL = 11  # 0x000B
    XL_ERR_TX_NOT_POSSIBLE = 12  # 0x000C
    XL_ERR_NO_LICENSE = 14  # 0x000E
    XL_ERR_WRONG_PARAMETER = 101  # 0x0065
    XL_ERR_TWICE_REGISTER = 110  # 0x006E
    XL_ERR_INVALID_CHAN_INDEX = 111  # 0x006F
    XL_ERR_INVALID_ACCESS = 112  # 0x0070
    XL_ERR_PORT_IS_OFFLINE = 113  # 0x0071
    XL_ERR_CHAN_IS_ONLINE = 116  # 0x0074
    XL_ERR_NOT_IMPLEMENTED = 117  # 0x0075
    XL_ERR_INVALID_PORT = 118  # 0x0076
    XL_ERR_HW_NOT_READY = 120  # 0x0078
    XL_ERR_CMD_TIMEOUT = 121  # 0x0079
    XL_ERR_CMD_HANDLING = 122  # 0x007A
    XL_ERR_HW_NOT_PRESENT = 129  # 0x0081
    XL_ERR_NOTIFY_ALREADY_ACTIVE = 131  # 0x0083
    XL_ERR_INVALID_TAG = 132  # 0x0084
    XL_ERR_INVALID_RESERVED_FLD = 133  # 0x0085
    XL_ERR_INVALID_SIZE = 134  # 0x0086
    XL_ERR_INSUFFICIENT_BUFFER = 135  # 0x0087
    XL_ERR_ERROR_CRC = 136  # 0x0088
    XL_ERR_BAD_EXE_FORMAT = 137  # 0x0089
    XL_ERR_NO_SYSTEM_RESOURCES = 138  # 0x008A
    XL_ERR_NOT_FOUND = 139  # 0x008B
    XL_ERR_INVALID_ADDRESS = 140  # 0x008C
    XL_ERR_REQ_NOT_ACCEP = 141  # 0x008D
    XL_ERR_INVALID_LEVEL = 142  # 0x008E
    XL_ERR_NO_DATA_DETECTED = 143  # 0x008F
    XL_ERR_INTERNAL_ERROR = 144  # 0x0090
    XL_ERR_UNEXP_NET_ERR = 145  # 0x0091
    XL_ERR_INVALID_USER_BUFFER = 146  # 0x0092
    XL_ERR_INVALID_PORT_ACCESS_TYPE = 147  # 0x0093
    XL_ERR_NO_RESOURCES = 152  # 0x0098
    XL_ERR_WRONG_CHIP_TYPE = 153  # 0x0099
    XL_ERR_WRONG_COMMAND = 154  # 0x009A
    XL_ERR_INVALID_HANDLE = 155  # 0x009B
    XL_ERR_RESERVED_NOT_ZERO = 157  # 0x009D
    XL_ERR_INIT_ACCESS_MISSING = 158  # 0x009E
    XL_ERR_WRONG_VERSION = 160  # 0x00A0
    XL_ERR_CANNOT_OPEN_DRIVER = 201  # 0x00C9
    XL_ERR_WRONG_BUS_TYPE = 202  # 0x00CA
    XL_ERR_DLL_NOT_FOUND = 203  # 0x00CB
    XL_ERR_INVALID_CHANNEL_MASK = 204  # 0x00CC
    XL_ERR_NOT_SUPPORTED = 205  # 0x00CD
    XL_ERR_CONNECTION_BROKEN = 210  # 0x00D2
    XL_ERR_CONNECTION_CLOSED = 211  # 0x00D3
    XL_ERR_INVALID_STREAM_NAME = 212  # 0x00D4
    XL_ERR_CONNECTION_FAILED = 213  # 0x00D5
    XL_ERR_STREAM_NOT_FOUND = 214  # 0x00D6
    XL_ERR_STREAM_NOT_CONNECTED = 215  # 0x00D7
    XL_ERR_QUEUE_OVERRUN = 216  # 0x00D8
    XL_ERROR = 255  # 0x00FF