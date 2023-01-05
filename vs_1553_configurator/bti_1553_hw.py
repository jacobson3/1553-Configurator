from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class BuiltInTestType:
    """
    event_log_on_ecc: The boolean flag defines whether BIT (built-
        in test) configuration will generate an event log entry when an
        ECC event occurs. In this mode, if a single bit error occurs,
        the read value will be corrected, BITSTAT_SINGLE_BIT_ERR will be
        set in the BIT status register and an event log entry is
        generated. If a double bit error occurs, the read value can’t be
        corrected so the card will be stopped, BIT_STAT_DOUBLE_BIT_ERR
        will be set in the BIT status register, and an event log entry
        is generated.
    event_log_on_seu: The boolean flag defines whether BIT (built-
        in test) configuration will generate event log entries for
        single event upsets (SEU) in the FPGA configuration. In this
        mode, if a single event upset is detected, the card will be
        stopped, the single event upset bit will be set in the BIT
        status register, and an event log entry is generated.
    event_log_on_protocol_error: The boolean flag defines whether
        BIT (built-in test) configuration will generate event log
        entries on CBIT (continuous built-in test) errors the 1553
        protocol engine. Every 1553 word transmitted by the card will be
        monitored and checked for accuracy, if a protocol error is
        detected, the card will be stopped, the protocol error bit will
        be set in the BIT status register, and an event log entry is
        generated.
    event_log_on_system_monitor: The boolean flag defines whether
        BIT (built-in test) configuration will generate event log
        entries on System Monitor errors. Temperature sensors will be
        monitored and if a sensor limit is exceeded, the card will be
        stopped, the system monitor error bit will be set in the BIT
        status register, and an event log entry is generated.
    """

    event_log_on_ecc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnECC",
            "type": "Attribute",
        },
    )
    event_log_on_seu: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnSEU",
            "type": "Attribute",
        },
    )
    event_log_on_protocol_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnProtocolError",
            "type": "Attribute",
        },
    )
    event_log_on_system_monitor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnSystemMonitor",
            "type": "Attribute",
        },
    )


class BusController1553TypeSyncMode(Enum):
    SELECTIVE = "Selective"
    ALL = "All"


class BusController1553TypeTriggerMode(Enum):
    NONE = "None"
    EXTERNAL = "External"
    START = "Start"


class Channel1553TypeModeCodes(Enum):
    MC01 = "MC01"
    MC1 = "MC1"
    MC0 = "MC0"
    NONE = "None"


class Channel1553TypeTermination(Enum):
    OFF = "Off"
    ON_A = "OnA"
    ON_B = "OnB"
    ON = "On"


class Channel429TypeMonitorMode(Enum):
    SELECTIVE = "Selective"
    ALL = "All"


class Channel429TypeParity(Enum):
    ODD = "Odd"
    EVEN = "Even"
    DATA = "Data"


class Channel429TypeTimeOrHitCount(Enum):
    TIME = "Time"
    HIT_COUNT = "HitCount"
    NONE = "None"


class Conditions1553TypeCondition(Enum):
    ALWAYS = "ALWAYS"
    FAIL = "FAIL"
    SRQ = "SRQ"
    INS = "INS"
    SSF = "SSF"
    TF = "TF"
    BUSY = "BUSY"
    ME = "ME"
    RESPERR = "RESPERR"
    NORESP = "NORESP"
    ALTBUS = "ALTBUS"
    DIO1_ACT = "DIO1ACT"
    DIO1_NACT = "DIO1NACT"
    DIO2_ACT = "DIO2ACT"
    DIO2_NACT = "DIO2NACT"
    DIO3_ACT = "DIO3ACT"
    DIO3_NACT = "DIO3NACT"
    DIO4_ACT = "DIO4ACT"
    DIO4_NACT = "DIO4NACT"


class Conditions429TypeCondition(Enum):
    ALWAYS = "ALWAYS"
    DIO1_ACT = "DIO1ACT"
    DIO1_NACT = "DIO1NACT"
    DIO2_ACT = "DIO2ACT"
    DIO2_NACT = "DIO2NACT"
    DIO3_ACT = "DIO3ACT"
    DIO3_NACT = "DIO3NACT"
    DIO4_ACT = "DIO4ACT"
    DIO4_NACT = "DIO4NACT"


@dataclass
class DioBankMaskType:
    """
    bank_num: The bank number of DIO. For the bank number 0, the
        LSB of each value corresponds to DIO number 1 and the MSB
        corresponds to DIO number 16 – 1 for 17-32, 2 for 33-48, and 3
        for 49-64 respectively.
    rise_mask: The discrete bitmask specifying up to 16 discrete
        input signals to monitor rising edges.
    fall_mask: The discrete bitmask specifying up to 16 discrete
        input signals to monitor falling edges.
    """

    bank_num: Optional[int] = field(
        default=None,
        metadata={
            "name": "bankNum",
            "type": "Attribute",
            "required": True,
        },
    )
    rise_mask: bytes = field(
        default=b"\xff\xff",
        metadata={
            "name": "riseMask",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    fall_mask: bytes = field(
        default=b"\xff\xff",
        metadata={
            "name": "fallMask",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )


class ErrorInjection1553TypeErrorMessages(Enum):
    TAGGED = "Tagged"
    ANY = "Any"


class ErrorInjection1553TypeState(Enum):
    OFF = "Off"
    ON = "On"
    ONCE = "Once"
    EXTERNAL = "External"


class Label429TypeSdi(Enum):
    ALL = "All"
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_10 = "10"
    VALUE_11 = "11"


class Label429TypeTimeOrHitCount(Enum):
    TIME = "Time"
    HIT_COUNT = "HitCount"


class LabelBuffer429TypeBufferType(Enum):
    FIFO = "FIFO"


class ManchesterError1553TypeHalf(Enum):
    FIRST = "First"
    SECOND = "Second"


class Message1553TypeBus(Enum):
    A = "A"
    B = "B"


class Message429TypeSdi(Enum):
    OFF = "Off"
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_10 = "10"
    VALUE_11 = "11"


class Message429TypeDataWipe(Enum):
    ZEROES = "Zeroes"
    VALUE_123 = "123"
    NONE = "None"


class Message429TypeTimeOrHitCount(Enum):
    TIME = "Time"
    HIT_COUNT = "HitCount"


@dataclass
class MessageBcrt1553Type:
    """
    Specifies the necessary parameters for a bus controller to remote terminal
    message.

    ta_val1: The remote terminal address (0 - 31) represented in 5
        bits in the command word 1.
    sa_val1: The sub address (location) of data (0 - 31)
        represented in 5 bits in the command word 1.
    word_count1: The number of data words to expect represented in
        5 bits in the command word 1.
    """

    class Meta:
        name = "MessageBCRT1553Type"

    ta_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "taVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    sa_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "saVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    word_count1: int = field(
        default=1,
        metadata={
            "name": "wordCount1",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32,
        },
    )


class MessageBuffer1553TypeBufferType(Enum):
    FIFO = "FIFO"
    CIRCULAR = "Circular"


class MessageBuffer429TypeBufferType(Enum):
    FIFO = "FIFO"
    CIRCULAR = "Circular"


@dataclass
class MessageData1553Type:
    """A collection of messageDataWord elements, which specify the actual data
    in the message buffer using 16-bit raw hexadecimal data word
    representations.

    This is used for transmit buffers.

    message_data_word: 16-bit raw data word represented in
        hexadecimal. The maximum number of data words to expect in one
        message command is 32.
    """

    message_data_word: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "messageDataWord",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 40,
            "length": 2,
            "format": "base16",
        },
    )


class MessageMc1553TypeDirection(Enum):
    RX = "Rx"
    TX = "Tx"


class MessageMc1553TypeSaVal1(Enum):
    VALUE_0 = 0
    VALUE_31 = 31


@dataclass
class MessageRtbc1553Type:
    """
    Specifies the necessary parameters for a remote terminal to bus controller
    message.

    ta_val1: The remote terminal address (0 - 31) represented in 5
        bits in the command word 1.
    sa_val1: The sub address (location) of data (0 - 31)
        represented in 5 bits in the command word 1.
    word_count1: The number of data words to expect represented in
        5 bits in the command word 1.
    """

    class Meta:
        name = "MessageRTBC1553Type"

    ta_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "taVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    sa_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "saVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    word_count1: int = field(
        default=1,
        metadata={
            "name": "wordCount1",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32,
        },
    )


@dataclass
class MessageRtrt1553Type:
    """
    Specifies the necessary parameters for a remote terminal to remote terminal
    message.

    ta_val1: The remote terminal address (0 - 31) represented in 5
        bits in the command word 1.
    sa_val1: The sub address (location) of data (0 - 31)
        represented in 5 bits in the command word 1.
    word_count1: The number of data words to expect represented in
        5 bits in the command word 1.
    ta_val2: The remote terminal address (0 - 31) represented in 5
        bits in the command word 2.
    sa_val2: The sub address (location) of data (0 - 31)
        represented in 5 bits in the command word 2.
    word_count2: The number of data words to expect represented in
        last 5 bits in the command word 2.
    """

    class Meta:
        name = "MessageRTRT1553Type"

    ta_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "taVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    sa_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "saVal1",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    word_count1: int = field(
        default=1,
        metadata={
            "name": "wordCount1",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32,
        },
    )
    ta_val2: Optional[int] = field(
        default=None,
        metadata={
            "name": "taVal2",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    sa_val2: Optional[int] = field(
        default=None,
        metadata={
            "name": "saVal2",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    word_count2: int = field(
        default=1,
        metadata={
            "name": "wordCount2",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32,
        },
    )


@dataclass
class MinorFrameRef1553Type:
    """
    A reference to a minor frame and thus the set of commands that it contains
    for execution.

    minor_frame_idref: The ID reference to a specific minor frame.
        This ID should match with of the minor frame IDs defined under
        the minor frames in order to schedule the frame.
    """

    minor_frame_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "minorFrameIDRef",
            "type": "Attribute",
            "required": True,
        },
    )


class ModeCode1553TypeDirection(Enum):
    TX = "Tx"
    RX = "Rx"


@dataclass
class Playback1553Type:
    pass


@dataclass
class PxiType:
    """
    source10_mhz: The boolean flag defines whether the 10MHz, 50%
        duty-cycle source clock is enabled on the PXIe_DSTARC line.
    """

    source10_mhz: Optional[bool] = field(
        default=None,
        metadata={
            "name": "source10MHz",
            "type": "Attribute",
        },
    )


@dataclass
class Rtfilter1553Type:
    """
    Describes one of the 32 possible filters to be used to monitor a remote
    terminal as desired.

    rt_address: The remote terminal address that is specified to
        monitor on the bus. If filtering is inverted, this is instead an
        RT that is specified to not monitor (in combination with bits
        set in the SA and MC masks below it)
    rx_samask: The bitmask of receive sub-addresses that is
        specified to monitor for the remote terminal address defined by
        rtAddress. In each bitmask, the least significant bit
        corresponds to sub-address or mode code number zero and the most
        significant bit corresponds to sub-address or mode code number
        31. If filtering is inverted these are the SAs to not monitor.
    tx_samask: The bitmask of transmit sub-addresses that is
        specified to monitor for the remote terminal address defined by
        rtAddress. If filtering is inverted these are the SAs to not
        monitor.
    rx_mcmask: The bitmask of receive mode codes that is specified
        to monitor for the remote terminal address defined by rtAddress.
        If filtering is inverted these are the MCs to not monitor.
    tx_mcmask: The bitmask of transmit mode codes that is
        specified to monitor for the remote terminal address defined by
        rtAddress. If filtering is inverted these are the MCs to not
        monitor.
    """

    class Meta:
        name = "RTFilter1553Type"

    rt_address: Optional[int] = field(
        default=None,
        metadata={
            "name": "rtAddress",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    rx_samask: bytes = field(
        default=b"\xff\xff\xff\xff",
        metadata={
            "name": "rxSAMask",
            "type": "Attribute",
            "length": 4,
            "format": "base16",
        },
    )
    tx_samask: bytes = field(
        default=b"\xff\xff\xff\xff",
        metadata={
            "name": "txSAMask",
            "type": "Attribute",
            "length": 4,
            "format": "base16",
        },
    )
    rx_mcmask: bytes = field(
        default=b"\xff\xff\xff\xff",
        metadata={
            "name": "rxMCMask",
            "type": "Attribute",
            "length": 4,
            "format": "base16",
        },
    )
    tx_mcmask: bytes = field(
        default=b"\xff\xff\xff\xff",
        metadata={
            "name": "txMCMask",
            "type": "Attribute",
            "length": 4,
            "format": "base16",
        },
    )


class RemoteTerminal1553TypeBusEnable(Enum):
    A = "A"
    B = "B"
    AB = "AB"
    NONE = "None"


class RemoteTerminal1553TypeDataWipe(Enum):
    ZEROES = "Zeroes"
    VALUE_123 = "123"
    CWD = "CWD"
    NONE = "None"


class RemoteTerminal1553TypeResponseMode(Enum):
    VALUE_1553_A = "1553A"
    VALUE_1553_B = "1553B"


class RemoteTerminal1553TypeRtMode(Enum):
    SIMULATE = "Simulate"
    MONITOR = "Monitor"
    DISABLE = "Disable"


class RemoteTerminal1553TypeSyncMode(Enum):
    SELECTIVE = "Selective"
    ALL = "All"


class RxChannel429TypeAutoLabelFilterMode(Enum):
    NONE = "None"
    LABELS = "Labels"
    SDIS = "SDIs"


class RxChannel429TypeDefaultBufferType(Enum):
    FIFO = "FIFO"


class RxChannel429TypeSpeed(Enum):
    AUTO = "Auto"
    LOW = "Low"
    HIGH = "High"


@dataclass
class SchedGap1553Type:
    """
    Specifies a gap to wait before execution of the next command.

    gap_time: The gap time between scheduled messages. Valid gap
        time is between 4.0 and 819.1.
    """

    gap_time: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gapTime",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("4.0"),
            "max_inclusive": Decimal("16382.0"),
            "fraction_digits": 1,
        },
    )


@dataclass
class SchedGap429Type:
    """
    A standalone gap will be scheduled here.

    gap_bit_times: The user-specified schedule gap. This allows
        gap times to be added that don't need to be associated with a
        message directly before it in the schedule.
    allow_async: The boolean flag defines whether asynchronous
        messages can be transmitted during this gap or not. Only applies
        to gapBitTimes &gt;= 36. Gaps smaller than this cannot fit an
        asynchronous message.
    """

    gap_bit_times: int = field(
        default=4,
        metadata={
            "name": "gapBitTimes",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 1048576,
        },
    )
    allow_async: bool = field(
        default=True,
        metadata={
            "name": "allowAsync",
            "type": "Attribute",
        },
    )


@dataclass
class SchedHaltType:
    """Insert a HALT opcode into the BC schedule.

    A HALT opcode will stop the BC schedule from running. The channel
    will be stopped here and may be started at runtime.
    """


@dataclass
class SchedMessageRef1553Type:
    """
    References a message and specifies how its transmission should be handled
    particular to the minor frame.

    message_idref: The ID reference to a specific message. This ID
        should match with one of the message IDs defined under the
        "messages" in order to schedule the message.
    single_shot: The boolean flag defines whether the single shot
        bit is set for the schedule. When set to TRUE, the single shot
        bit instructs the BC schedule to process the specified opcode
        one time, and then to set the skip bit after processing is
        complete. The single-shot bit is FALSE (disabled) by default.
    skip: The boolean flag defines whether the skip bit is set for
        the schedule. When set to TRUE, the skip bit instructs the BC
        schedule to skip over processing the specific opcode. The skip
        bit is FALSE (disabled) by default.
    """

    message_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "messageIDRef",
            "type": "Attribute",
            "required": True,
        },
    )
    single_shot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "singleShot",
            "type": "Attribute",
        },
    )
    skip: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SchedMessageRef429Type:
    """A reference to a defined message node, using the message ID.

    The referenced message will be scheduled here.

    message_idref: The ID reference to a specific message. This ID
        should match with one of the message IDs defined under the
        “messages” node in order to transmit the message.
    gap_bit_times: The user-specified schedule gap. The gap will
        be added (in bit times) after the message is transmitted.
        Setting the gap to less than 4 allows error injection of short
        gaps (gap between 1 and 3) or long words (gap = 0)
    allow_async: The boolean flag defines whether asynchronous
        messages can be transmitted during this message's associated gap
        or not. Only applies to gapBitTimes &gt;= 36. Gaps smaller than
        this cannot fit an asynchronous message.
    """

    message_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "messageIDRef",
            "type": "Attribute",
            "required": True,
        },
    )
    gap_bit_times: int = field(
        default=4,
        metadata={
            "name": "gapBitTimes",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 1048576,
        },
    )
    allow_async: bool = field(
        default=True,
        metadata={
            "name": "allowAsync",
            "type": "Attribute",
        },
    )


@dataclass
class SchedPauseType:
    """Insert a PAUSE opcode into the BC schedule.

    A PAUSE opcode will pause operation of the BC schedule. The channel
    will be paused here and may be resumed at runtime.
    """


@dataclass
class SchedPulseType:
    """
    A standalone discrete (DIO) pulse will be scheduled here.

    dio_num: The DIO number (1-64) being pulsed to the "ON" state
        followed by the "OFF" state when this command is encountered in
        the schedule
    """

    dio_num: int = field(
        default=1,
        metadata={
            "name": "dioNum",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 64,
        },
    )


@dataclass
class SchedRestartType:
    """Insert a RESTART opcode into the BC schedule.

    The schedule will be restarted here.
    """


class SubAddress1553TypeDirection(Enum):
    TX = "Tx"
    RX = "Rx"


class SyncOutputTypeLine(Enum):
    A = "A"
    B = "B"
    C = "C"
    PXITRIGA = "PXITRIGA"
    PXITRIGB = "PXITRIGB"
    PXITRIGC = "PXITRIGC"
    PXISTARC = "PXISTARC"


class SyncOutputTypePolarity(Enum):
    HIGH = "High"
    LOW = "Low"


class TemperatureSensorTypeSensorName(Enum):
    FPGA = "FPGA"
    XCVR = "XCVR"
    MEMORY = "Memory"
    PWR_SUPPLY = "PwrSupply"
    PROCESSOR = "Processor"
    IOMODULE = "IOModule"
    PCB = "PCB"


class TimingTypeDriftSyncSelect(Enum):
    NONE = "None"
    PPS0 = "PPS0"
    PPS1 = "PPS1"
    PWMIRIG0 = "PWMIRIG0"
    PWMIRIG1 = "PWMIRIG1"
    AMIRIG = "AMIRIG"
    VALUE_10_MHZ = "10MHZ"
    HOST = "HOST"


class TimingTypeIrigType(Enum):
    A = "A"
    B = "B"


class TimingTypeResolution(Enum):
    VALUE_1_NS = "1NS"
    VALUE_1_US = "1US"


class TimingTypeTimeSourceSelect(Enum):
    NONE = "None"
    PPS0 = "PPS0"
    PPS1 = "PPS1"
    PWMIRIG0 = "PWMIRIG0"
    PWMIRIG1 = "PWMIRIG1"
    AMIRIG = "AMIRIG"
    VALUE_10_MHZ = "10MHZ"


class TimingTypeTimeSyncSelect(Enum):
    NONE = "None"
    PPS0 = "PPS0"
    PPS1 = "PPS1"
    PWMIRIG0 = "PWMIRIG0"
    PWMIRIG1 = "PWMIRIG1"
    AMIRIG = "AMIRIG"


class TriggerInputTypeCondition(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class TriggerInputTypeLine(Enum):
    A = "A"
    B = "B"
    C = "C"
    PXITRIGA = "PXITRIGA"
    PXITRIGB = "PXITRIGB"
    PXITRIGC = "PXITRIGC"
    PXISTARA = "PXISTARA"
    PXISTARB = "PXISTARB"
    PXISTARC = "PXISTARC"


class TriggerInputTypePolarity(Enum):
    HIGH = "High"
    LOW = "Low"
    RISE = "Rise"
    FALL = "Fall"


class TxChannel429TypeNegativeLeg(Enum):
    SIGNAL = "Signal"
    OPEN = "Open"
    GROUND = "Ground"


class TxChannel429TypeParametricMode(Enum):
    WAVE = "Wave"
    OFF = "Off"


class TxChannel429TypePositiveLeg(Enum):
    SIGNAL = "Signal"
    OPEN = "Open"
    GROUND = "Ground"


class TxChannel429TypeScheduleBuildMethod(Enum):
    NORMAL = "Normal"
    QUICK = "Quick"
    BOTH = "Both"


class TxChannel429TypeScheduleBuildUnit(Enum):
    MILLISECOND = "Millisecond"
    MICROSECOND = "Microsecond"


class TxChannel429TypeScheduleMode(Enum):
    RATE = "Rate"
    EXPLICIT = "Explicit"


class WordCountError1553TypeType(Enum):
    RELATIVE = "Relative"
    ABSOLUTE = "Absolute"


class ZeroCrossingError1553TypeType(Enum):
    LEADING = "Leading"
    MID_BIT = "Mid-bit"


class Message1553GroupDataWipe(Enum):
    ZEROES = "Zeroes"
    CWD = "CWD"
    VALUE_123 = "123"
    NONE = "None"


class Message1553GroupElapseMinOrMax(Enum):
    ELAPSETIME = "Elapsetime"
    MINTIME = "Mintime"
    MAXTIME = "Maxtime"


class Message1553GroupTimeOrHitCount(Enum):
    TIME = "Time"
    HIT_COUNT = "HitCount"


class SchemaVersionGroupSchemaVersion(Enum):
    UNDEFINED = "Undefined"
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"
    VALUE_1_2 = "1.2"
    VALUE_1_3 = "1.3"


class WordPos1553GroupWordPos(Enum):
    CWD1 = "CWD1"
    CWD2 = "CWD2"
    SWD1 = "SWD1"
    SWD2 = "SWD2"
    DWD0 = "DWD0"
    DWD1 = "DWD1"
    DWD2 = "DWD2"
    DWD3 = "DWD3"
    DWD4 = "DWD4"
    DWD5 = "DWD5"
    DWD6 = "DWD6"
    DWD7 = "DWD7"
    DWD8 = "DWD8"
    DWD9 = "DWD9"
    DWD10 = "DWD10"
    DWD11 = "DWD11"
    DWD12 = "DWD12"
    DWD13 = "DWD13"
    DWD14 = "DWD14"
    DWD15 = "DWD15"
    DWD16 = "DWD16"
    DWD17 = "DWD17"
    DWD18 = "DWD18"
    DWD19 = "DWD19"
    DWD20 = "DWD20"
    DWD21 = "DWD21"
    DWD22 = "DWD22"
    DWD23 = "DWD23"
    DWD24 = "DWD24"
    DWD25 = "DWD25"
    DWD26 = "DWD26"
    DWD27 = "DWD27"
    DWD28 = "DWD28"
    DWD29 = "DWD29"
    DWD30 = "DWD30"
    DWD31 = "DWD31"


@dataclass
class BitCountError1553Type:
    """
    Specifies a bit count error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    value: The value of extra bits in the bit count error. The
        least significant bits of value determine the values of extra
        bits in a bit count error.
    count: The number of extra bits.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-1]{1,3}",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -2,
            "max_inclusive": 3,
        },
    )


@dataclass
class Conditions1553Type:
    """
    A container for condition elements, which specify what situations dictate a
    resending of the message or creating an event log depending on the
    associated element.

    condition: The enumeration defines the retry conditions, the
        BC retransmits the message up to the number of retries. Or The
        enumeration defines the event log conditions. A conditional log
        command block causes the core generate an event log list entry
        if condition is evaluated as TRUE.
    """

    condition: List[Conditions1553TypeCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 32,
        },
    )


@dataclass
class Conditions429Type:
    """
    A collection of conditions that must all occur for the event to trigger.

    condition: The enumeration defines what digital I/O condition
        value to test.
    """

    condition: List[Conditions429TypeCondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 32,
        },
    )


@dataclass
class DioBankMasksType:
    """
    dio_bank_mask: A single of sequential log mask setting for DIO
        bank of the core – by defining this node, it enables  sequential
        monitoring on specific transitions of discrete inputs.
    """

    dio_bank_mask: List[DioBankMaskType] = field(
        default_factory=list,
        metadata={
            "name": "dioBankMask",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
        },
    )


@dataclass
class GapError1553Type:
    """
    Specifies a gap error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    gap_length: The time for the gap errors.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )
    gap_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "gapLength",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("818.1"),
            "fraction_digits": 1,
        },
    )


@dataclass
class LabelBuffer429Type:
    """Defines the number of items in the receive label filter buffer.

    Buffers with one item are considered current-value filters and do
    not buffer received messages in a list.

    buffer_max_entries: The maximum number of 4-byte raw message
        data entries allocated in the received buffer. Define 1 here for
        current-value only messages, or greater than 1 for FIFO or
        circular buffers.
    buffer_type: The list buffer type of receiving messages. Only
        the FIFO type is valid. This option is configured only if the
        bufferMaxEntries is greater than 1.
    event_log_on_full: The boolean flag defines whether an event
        log is generated when the buffer is full.
    """

    buffer_max_entries: int = field(
        default=1,
        metadata={
            "name": "bufferMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32764,
        },
    )
    buffer_type: LabelBuffer429TypeBufferType = field(
        default=LabelBuffer429TypeBufferType.FIFO,
        metadata={
            "name": "bufferType",
            "type": "Attribute",
        },
    )
    event_log_on_full: bool = field(
        default=False,
        metadata={
            "name": "eventLogOnFull",
            "type": "Attribute",
        },
    )


@dataclass
class MajorFrame1553Type:
    """
    Specifies a schedule that can be referenced by the channel for execution.

    minor_frame_ref:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    loop_count: The maximum loop count for the BC schedule. When
        the loop count &gt; 0 (enabled), the BC schedule will
        automatically stop when it runs through the schedule loopCount
        times. When 0, the loopCount limit is not used and the schedule
        may run indefinitely.
    """

    minor_frame_ref: List[MinorFrameRef1553Type] = field(
        default_factory=list,
        metadata={
            "name": "minorFrameRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    loop_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "loopCount",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 65535,
        },
    )


@dataclass
class ManchesterError1553Type:
    """
    Specifies a Manchester error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    half: The enumeration defines whether the Manchester error is
        generated on the first half or second half of bit.
    bit_pos: The bit containing a Manchester error. It may range
        from 0 to 19.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )
    half: Optional[ManchesterError1553TypeHalf] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    bit_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitPos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 19,
        },
    )


@dataclass
class MessageBuffer1553Type:
    """
    Defines a buffer of data that can be referenced for transmission or
    reception.

    message_data:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    buffer_max_entries: The maximum number of message data entries
        allocated in the buffer. Define 1 here for current-value only
        messages, or greater than 1 for FIFO or Circular buffers.
    buffer_type: The list buffer type of message data – FIFO or
        Circular. This option is configured only if the bufferMaxEntries
        is greater than 1.
    event_log_on_empty_or_full: The boolean flag defines whether
        an event log is generated when the buffer is empty or full. If
        it is a transmit buffer, it is generated on empty. If is a
        receive buffer, it is generated on full.
    event_log_on_half: The boolean flag defines whether an event
        log is generated when the middle or last entry of the buffer is
        processed.
    """

    message_data: List[MessageData1553Type] = field(
        default_factory=list,
        metadata={
            "name": "messageData",
            "type": "Element",
            "max_occurs": 1023,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    buffer_max_entries: Optional[int] = field(
        default=None,
        metadata={
            "name": "bufferMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 1023,
        },
    )
    buffer_type: Optional[MessageBuffer1553TypeBufferType] = field(
        default=None,
        metadata={
            "name": "bufferType",
            "type": "Attribute",
        },
    )
    event_log_on_empty_or_full: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnEmptyOrFull",
            "type": "Attribute",
        },
    )
    event_log_on_half: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnHalf",
            "type": "Attribute",
        },
    )


@dataclass
class MessageBuffer429Type:
    """A predefined ARINC 429 message data buffer.

    Contains one or more 32-bit ARINC message values. Note that setting
    labelDecimal and SDI attributes on the message will cause the
    corresponding bits in rawData to be ignored.

    raw_data: 4-byte raw data of the message.
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    buffer_max_entries: The maximum number of 4-byte raw message
        data entries allocated in the buffer.
    buffer_type: The message list buffer type – FIFO or Circular.
        This option is configured only if the bufferMaxEntries is
        greater than 1.
    event_log_on_empty: The boolean flag defines whether an event
        log is generated when the buffer is empty.
    """

    raw_data: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "rawData",
            "type": "Element",
            "length": 4,
            "format": "base16",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    buffer_max_entries: int = field(
        default=1,
        metadata={
            "name": "bufferMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32764,
        },
    )
    buffer_type: MessageBuffer429TypeBufferType = field(
        default=MessageBuffer429TypeBufferType.FIFO,
        metadata={
            "name": "bufferType",
            "type": "Attribute",
        },
    )
    event_log_on_empty: bool = field(
        default=False,
        metadata={
            "name": "eventLogOnEmpty",
            "type": "Attribute",
        },
    )


@dataclass
class MessageMc1553Type:
    """
    Specifies the necessary parameters to put a mode code message on the bus.

    ta_val1: The remote terminal address (0 - 31) represented in 5
        bits in the command word.
    sa_val1: The sub address (location) of data (0 - 31)
        represented in 5 bits in the command word.
    mode_code_number: The mode code number (0 - 31) represented in
        the last 5 bits in the command word.
    direction: The direction of mode code command - receive or
        transmit.
    """

    class Meta:
        name = "MessageMC1553Type"

    ta_val1: Optional[int] = field(
        default=None,
        metadata={
            "name": "taVal1",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    sa_val1: Optional[MessageMc1553TypeSaVal1] = field(
        default=None,
        metadata={
            "name": "saVal1",
            "type": "Attribute",
        },
    )
    mode_code_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "modeCodeNumber",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    direction: Optional[MessageMc1553TypeDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ModeCode1553Type:
    """
    Specifies a mode code on the remote terminal.

    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    enable: Enables message skipping on a message. No effect if
        bufferMaxEntries is greater than 1.
    data_wipe: The enumeration defines how the data is
        initialized. Zeroes - the data is initialized to 0, 123 – the
        data is initialized with incrementing values, CWD - the data is
        initialized with command word, or None - data initialization is
        disabled.
    allow_error_injection: The boolean flag defines whether a
        message error can be generated for the message.
    message_buffer_idref: The ID reference to the message buffer.
        This ID should match with one of the message buffer IDs defined
        in message buffers that define the message data words.
    event_log: The boolean flag defines whether event log will be
        generated for the message.
    sync_output: The boolean flag defines whether an output sync
        signal will be generated for the message.
    monitor: The boolean flag defines whether the message will be
        monitored from the bus. This setting controls the monitoring of
        the message from the bus monitor.
    time_or_hit_count: The enumeration defines that the message
        will record hit count or time tag.
    elapse_min_or_max: The enumeration defines that the message
        will record elapse, min, or max time. They may only be recorded
        if the attribute timeOrHitCount="Time"
    mode_code_number: The mode code number (0 – 31) represented in
        the last 5 bits in the command word.
    direction: The message direction – Tx (RT to BC) or Rx (BC to
        RT)
    wrap: The boolean flag defines whether the data wrap is
        enabled – The receive SA data will be automatically wrapped to
        corresponding transmit SA data (RT only).
    """

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    enable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    data_wipe: Optional[Message1553GroupDataWipe] = field(
        default=None,
        metadata={
            "name": "dataWipe",
            "type": "Attribute",
        },
    )
    allow_error_injection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "allowErrorInjection",
            "type": "Attribute",
        },
    )
    message_buffer_idref: int = field(
        default=-1,
        metadata={
            "name": "messageBufferIDRef",
            "type": "Attribute",
        },
    )
    event_log: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLog",
            "type": "Attribute",
        },
    )
    sync_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "syncOutput",
            "type": "Attribute",
        },
    )
    monitor: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    time_or_hit_count: Optional[Message1553GroupTimeOrHitCount] = field(
        default=None,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )
    elapse_min_or_max: Optional[Message1553GroupElapseMinOrMax] = field(
        default=None,
        metadata={
            "name": "elapseMinOrMax",
            "type": "Attribute",
        },
    )
    mode_code_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "modeCodeNumber",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    direction: Optional[ModeCode1553TypeDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    wrap: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ParityError1553Type:
    """
    Specifies a parity error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Rtfilters1553Type:
    """
    A collection of rtFilter elements.

    rt_filter:
    invert: The boolean flag defines whether the remote terminal
        address filters for bus monitoring are inverted. Inverted
        filtering is subtractive rather than additive (additive or
        invert="false" is the default). If only a few RTs/SAs need to be
        filtered out, setting invert="true" allows the filtering
        selections to be much simpler.
    """

    class Meta:
        name = "RTFilters1553Type"

    rt_filter: List[Rtfilter1553Type] = field(
        default_factory=list,
        metadata={
            "name": "rtFilter",
            "type": "Element",
            "max_occurs": 32,
        },
    )
    invert: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SubAddress1553Type:
    """
    Specifies a subaddress on the remote terminal.

    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    enable: Enables message skipping on a message. No effect if
        bufferMaxEntries is greater than 1.
    data_wipe: The enumeration defines how the data is
        initialized. Zeroes - the data is initialized to 0, 123 – the
        data is initialized with incrementing values, CWD - the data is
        initialized with command word, or None - data initialization is
        disabled.
    allow_error_injection: The boolean flag defines whether a
        message error can be generated for the message.
    message_buffer_idref: The ID reference to the message buffer.
        This ID should match with one of the message buffer IDs defined
        in message buffers that define the message data words.
    event_log: The boolean flag defines whether event log will be
        generated for the message.
    sync_output: The boolean flag defines whether an output sync
        signal will be generated for the message.
    monitor: The boolean flag defines whether the message will be
        monitored from the bus. This setting controls the monitoring of
        the message from the bus monitor.
    time_or_hit_count: The enumeration defines that the message
        will record hit count or time tag.
    elapse_min_or_max: The enumeration defines that the message
        will record elapse, min, or max time. They may only be recorded
        if the attribute timeOrHitCount="Time"
    sub_address: The sub address (location) of data.
    direction: The message direction – Tx (RT to BC) or Rx (BC to
        RT)
    wrap: The boolean flag defines whether the data wrap is
        enabled – The receive SA data will be automatically wrapped to
        corresponding transmit SA data.
    """

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_wipe: Optional[Message1553GroupDataWipe] = field(
        default=None,
        metadata={
            "name": "dataWipe",
            "type": "Attribute",
        },
    )
    allow_error_injection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "allowErrorInjection",
            "type": "Attribute",
        },
    )
    message_buffer_idref: int = field(
        default=-1,
        metadata={
            "name": "messageBufferIDRef",
            "type": "Attribute",
        },
    )
    event_log: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLog",
            "type": "Attribute",
        },
    )
    sync_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "syncOutput",
            "type": "Attribute",
        },
    )
    monitor: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    time_or_hit_count: Optional[Message1553GroupTimeOrHitCount] = field(
        default=None,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )
    elapse_min_or_max: Optional[Message1553GroupElapseMinOrMax] = field(
        default=None,
        metadata={
            "name": "elapseMinOrMax",
            "type": "Attribute",
        },
    )
    sub_address: Optional[int] = field(
        default=None,
        metadata={
            "name": "subAddress",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    direction: Optional[SubAddress1553TypeDirection] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    wrap: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SyncError1553Type:
    """
    Specifies a sync error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SyncOutputType:
    """
    A sync output definition defines the sync line and polarity of the sync
    signal.

    line: The enumeration defines the sync output line used to
        output a sync signal on transmission or reception.
    polarity: The enumeration defines the sync output pin polarity
        (high or low).
    """

    line: Optional[SyncOutputTypeLine] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    polarity: Optional[SyncOutputTypePolarity] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TemperatureSensorType:
    """
    index: The index that specifies the temperature sensor.
    sensor_name: The name that specifies the temperature sensor
        for converting to the index if the index is not defined.
    high_thresh: The high threshold of the temperature sensor in
        units of degrees Celsius. If the sensor value exceeds the user
        definable thresholds, the BIT status register will indicate a
        fault.
    low_thresh: The low threshold of the temperature sensor in
        units of degrees Celsius. If the sensor value exceeds the user
        definable thresholds, the BIT status register will indicate a
        fault.
    """

    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 15,
        },
    )
    sensor_name: Optional[TemperatureSensorTypeSensorName] = field(
        default=None,
        metadata={
            "name": "sensorName",
            "type": "Attribute",
        },
    )
    high_thresh: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "highThresh",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-40.000"),
            "max_inclusive": Decimal("99.999"),
            "fraction_digits": 3,
        },
    )
    low_thresh: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "lowThresh",
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-40.000"),
            "max_inclusive": Decimal("99.999"),
            "fraction_digits": 3,
        },
    )


@dataclass
class TimingType:
    """
    drift_max: The value of the device’s maximum drift adjustment
        limit. This value is the limit the device will attempt to bias
        the clock frequency to match an incoming source frequency. The
        default value is 425000000.
    delay_comp: The value of the device’s input compensation. The
        device will adjust the internal time by the set amount to
        account for flight and logic delays in the circuitry and wiring
        when synchronizing time to an external IRIG or PPS source. The
        value is in nano second and the default value is 0.
    irig_control_val: The value of outgoing IRIG control field.
    irig_years: The value to set the device year which is an
        unsigned integer between 2000 and 2099.
    irig_type: The IRIG Time Code A or B. B is default.
    jump_thresh_ppt: The value of the device IRIG/PPS drift
        threshold. The value is in parts per trillion, and it is used to
        set the maximum drift adjustment a time delta can force onto the
        clock frequency. The default value is 425000000.
    jump_thresh_ns: The value of the device IRIG/PPS time
        threshold. The value is in nanosecond, and it is used to set the
        minimum offset value that will force the timer to jump to the
        received time.
    timer_rollover: The value of the device's timer rollover.
    time_source_select: The output timing source configuration –
        PPS0, PPS1, PWM IRIG, AM IRIG, 10MHZ, IRIGA (100 millisecond
        period), IRIGB (1 second period) signal.
    time_sync_select: The timing sync configuration selection -
        PPS0, PPS1, PWM IRIG, AM IRIG, 10MHZ, IRIGA (100 millisecond
        period), IRIGB (1 second period) signal.
    time_enable_user_input_thresh: The boolean flag defines
        whether the user input timing threshold setting is enabled.
    time_input_thresh_val: The user timing input threshold value.
        Valid only if timeEnableUserInputThresh is true. If
        timeSyncSelect = AMIRIG, this sets the amplitude-modulated IRIG
        low threshold.
    drift_sync_select: The drift sync configuration selection -
        PPS0, PPS1, PWM IRIG, AM IRIG, 10MHZ, IRIGA (100 millisecond
        perid), IRIGB (1 second period) signal.
    drift_enable_user_input_thresh: The boolean flag defines
        whether the user input drift threshold setting is enabled.
    drift_input_thresh_val: The user drift input threshold value.
        Valid only if driftEnableUserInputThresh is true. If
        driftSyncSelect = AMIRIG, this sets the amplitude-modulated IRIG
        low threshold
    resolution: The resolution for time-tag timer on the device –
        current, 1 us, 16 us, 1024 us, or 1 ns. This attribute has no
        effect on the OB2 PXIe product and is fixed at 1 ns resolution.
    timer_value: The timer value for setting device timer. The
        valid range is from 0 to 2^64-1.
    """

    drift_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "driftMax",
            "type": "Attribute",
        },
    )
    delay_comp: Optional[int] = field(
        default=None,
        metadata={
            "name": "delayComp",
            "type": "Attribute",
        },
    )
    irig_control_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "irigControlVal",
            "type": "Attribute",
            "length": 4,
            "format": "base16",
        },
    )
    irig_years: Optional[int] = field(
        default=None,
        metadata={
            "name": "irigYears",
            "type": "Attribute",
            "min_inclusive": 2000,
            "max_inclusive": 2099,
        },
    )
    irig_type: Optional[TimingTypeIrigType] = field(
        default=None,
        metadata={
            "name": "irigType",
            "type": "Attribute",
        },
    )
    jump_thresh_ppt: Optional[int] = field(
        default=None,
        metadata={
            "name": "jumpThreshPPT",
            "type": "Attribute",
        },
    )
    jump_thresh_ns: Optional[int] = field(
        default=None,
        metadata={
            "name": "jumpThreshNS",
            "type": "Attribute",
        },
    )
    timer_rollover: Optional[int] = field(
        default=None,
        metadata={
            "name": "timerRollover",
            "type": "Attribute",
        },
    )
    time_source_select: Optional[TimingTypeTimeSourceSelect] = field(
        default=None,
        metadata={
            "name": "timeSourceSelect",
            "type": "Attribute",
        },
    )
    time_sync_select: Optional[TimingTypeTimeSyncSelect] = field(
        default=None,
        metadata={
            "name": "timeSyncSelect",
            "type": "Attribute",
        },
    )
    time_enable_user_input_thresh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "timeEnableUserInputThresh",
            "type": "Attribute",
        },
    )
    time_input_thresh_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "timeInputThreshVal",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    drift_sync_select: Optional[TimingTypeDriftSyncSelect] = field(
        default=None,
        metadata={
            "name": "driftSyncSelect",
            "type": "Attribute",
        },
    )
    drift_enable_user_input_thresh: Optional[bool] = field(
        default=None,
        metadata={
            "name": "driftEnableUserInputThresh",
            "type": "Attribute",
        },
    )
    drift_input_thresh_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "driftInputThreshVal",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    resolution: Optional[TimingTypeResolution] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    timer_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "timerValue",
            "type": "Attribute",
        },
    )


@dataclass
class TriggerInputType:
    """
    A trigger input definition defines the trigger line, trigger polarity, and
    active condition.

    line: The enumeration defines the trigger input line used for
        controlling the transmission.
    polarity: The enumeration defines the trigger input pin
        polarity (high or low).
    condition: The enumeration defines whether the trigger input
        line is active or inactive.
    """

    line: Optional[TriggerInputTypeLine] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    polarity: Optional[TriggerInputTypePolarity] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    condition: Optional[TriggerInputTypeCondition] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WordCountError1553Type:
    """
    Specifies a word count error.

    type: The enumeration defines that an absolute word count
        error or a relative count error will be generated.
    count: The word count error. For the absolute word count
        errors, count may be from 0 to 40. For relative word count
        errors, the sum of count and the word count field in the command
        word must be less than or equal to 40.
    """

    type: Optional[WordCountError1553TypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 40,
        },
    )


@dataclass
class ZeroCrossingError1553Type:
    """
    Specifies a zero-crossing error.

    word_pos: The location within a message of a word error. The
        word position may be from 0 to 31 indicating a data word, or it
        may be one of the following: first or second command word, first
        or second status word.
    type: The enumeration defines whether the zero crossing error
        will be generated on leading zero crossing or mid-bit zero
        crossing.
    nano_sec_shift: The time amount in nanoseconds that the edge
        is shifted. The positive value delays the edge and a negative
        value advances it.
    bit_pos: The bit containing zero crossing error. It may range
        from 0 to 19.
    """

    word_pos: Optional[WordPos1553GroupWordPos] = field(
        default=None,
        metadata={
            "name": "wordPos",
            "type": "Attribute",
            "required": True,
        },
    )
    type: Optional[ZeroCrossingError1553TypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    nano_sec_shift: Optional[int] = field(
        default=None,
        metadata={
            "name": "nanoSecShift",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -200,
            "max_inclusive": 200,
        },
    )
    bit_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitPos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 19,
        },
    )


@dataclass
class BusMonitor1553Type:
    """
    Describes how a virtual bus monitor should be simulated by the hardware on
    the bus.

    rt_filters:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    statistics: The boolean flag defines whether the statistic and
        error monitoring process (message count, error count, and error
        types) is enabled.
    """

    rt_filters: Optional[Rtfilters1553Type] = field(
        default=None,
        metadata={
            "name": "rtFilters",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: SchemaVersionGroupSchemaVersion = field(
        default=SchemaVersionGroupSchemaVersion.UNDEFINED,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )
    statistics: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DefinedError1553Type:
    """
    Defines an error that is available for injection.

    gap_error:
    word_count_error:
    bit_count_error:
    manchester_error:
    sync_error:
    parity_error:
    zero_crossing_error:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    """

    gap_error: Optional[GapError1553Type] = field(
        default=None,
        metadata={
            "name": "gapError",
            "type": "Element",
        },
    )
    word_count_error: Optional[WordCountError1553Type] = field(
        default=None,
        metadata={
            "name": "wordCountError",
            "type": "Element",
        },
    )
    bit_count_error: Optional[BitCountError1553Type] = field(
        default=None,
        metadata={
            "name": "bitCountError",
            "type": "Element",
        },
    )
    manchester_error: Optional[ManchesterError1553Type] = field(
        default=None,
        metadata={
            "name": "manchesterError",
            "type": "Element",
        },
    )
    sync_error: Optional[SyncError1553Type] = field(
        default=None,
        metadata={
            "name": "syncError",
            "type": "Element",
        },
    )
    parity_error: Optional[ParityError1553Type] = field(
        default=None,
        metadata={
            "name": "parityError",
            "type": "Element",
        },
    )
    zero_crossing_error: Optional[ZeroCrossingError1553Type] = field(
        default=None,
        metadata={
            "name": "zeroCrossingError",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )


@dataclass
class MajorFrames1553Type:
    """
    A collection of majorFrame elements.
    """

    major_frame: List[MajorFrame1553Type] = field(
        default_factory=list,
        metadata={
            "name": "majorFrame",
            "type": "Element",
        },
    )


@dataclass
class MessageBuffers1553Type:
    """
    A collection of messageBuffer elements.
    """

    message_buffer: List[MessageBuffer1553Type] = field(
        default_factory=list,
        metadata={
            "name": "messageBuffer",
            "type": "Element",
        },
    )


@dataclass
class MessageBuffers429Type:
    """A collection of message buffers defined for an ARINC 429 transmit
    message or asynchronous buffer.

    Multiple buffers may be defined in order to allow the data to be
    switched at runtime using the predefined data held here.
    """

    message_buffer: List[MessageBuffer429Type] = field(
        default_factory=list,
        metadata={
            "name": "messageBuffer",
            "type": "Element",
        },
    )


@dataclass
class SchedLog1553Type:
    """
    Specifies a command create an event log entry that its execution has
    occurred.

    event_log_conditions:
    tag: The user specified tag value that is used as the
        information value for the event log.
    """

    event_log_conditions: Optional[Conditions1553Type] = field(
        default=None,
        metadata={
            "name": "eventLogConditions",
            "type": "Element",
            "required": True,
        },
    )
    tag: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SchedLog429Type:
    """
    An event log entry will conditionally be created here.

    event_log_conditions:
    tag: The user-specified event tag value.
    """

    event_log_conditions: Optional[Conditions429Type] = field(
        default=None,
        metadata={
            "name": "eventLogConditions",
            "type": "Element",
            "required": True,
        },
    )
    tag: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SequentialLogType:
    """
    dio_bank_masks: A collection of sequential log mask settings
        for DIO banks of the core.
    per_channel_streaming: The boolean flag defines whether
        records recorded by the sequential log are placed into separate
        buffers for each channel. If true, the protocol libraries
        (BTI1553Lib “BM” block and BTI429Lib “Rx” block) must be used to
        process sequential log data that is recorded separately by each
        channel. If false, the records are in a single buffer for the
        entire core and must be processed by VIs in the “Sequential
        Monitor” block of the BTICardLib library. The default value is
        true.
    use_dma: The boolean flag defines whether sequential data is
        buffered directly on the host computer rather than using the on-
        Card buffer. Using host memory (value is true) uses less host
        processing at the cost of a smaller buffer size (1 MB). Using
        on-Card memory (value is false) uses more host processing with a
        larger buffer size (16 MB). It is recommended to only set this
        property to false if perChannelStreaming is also false, since
        perChannelStreaming effectively adds an additional host buffer
        for each channel. The default value is true.
    """

    dio_bank_masks: Optional[DioBankMasksType] = field(
        default=None,
        metadata={
            "name": "dioBankMasks",
            "type": "Element",
        },
    )
    per_channel_streaming: bool = field(
        default=True,
        metadata={
            "name": "perChannelStreaming",
            "type": "Attribute",
        },
    )
    use_dma: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useDMA",
            "type": "Attribute",
        },
    )


@dataclass
class SyncOutputsType:
    """A collection of sync output definitions.

    Sync output definitions will output a sync signal on message
    transmission. Up to seven sync lines may be selected, one for each
    line.
    """

    sync_output: List[SyncOutputType] = field(
        default_factory=list,
        metadata={
            "name": "syncOutput",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 7,
        },
    )


@dataclass
class TemperatureSensorsType:
    """
    temperature_sensor: A System Monitor sensor.
    """

    temperature_sensor: List[TemperatureSensorType] = field(
        default_factory=list,
        metadata={
            "name": "temperatureSensor",
            "type": "Element",
        },
    )


@dataclass
class TriggerInputsType:
    """A collection of trigger input definitions.

    Trigger inputs are AND'ed to determine if the trigger occurs. Up to
    three trigger lines may be selected, one each from A, B, or C.
    """

    trigger_input: List[TriggerInputType] = field(
        default_factory=list,
        metadata={
            "name": "triggerInput",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )


@dataclass
class AcyclicFrame1553Type:
    """A schedule of commands and messages that can be transmitted on-demand
    during a major frame schedule of minor frames.

    If an acyclic frame is requested by the user program, it will be
    transmitted at the end of the current minor frame.

    command_message_ref:
    command_gap:
    command_pulse:
    command_halt:
    command_log:
    command_pause:
    command_restart:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    """

    command_message_ref: List[SchedMessageRef1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandMessageRef",
            "type": "Element",
            "sequential": True,
        },
    )
    command_gap: List[SchedGap1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandGap",
            "type": "Element",
            "sequential": True,
        },
    )
    command_pulse: List[SchedPulseType] = field(
        default_factory=list,
        metadata={
            "name": "commandPulse",
            "type": "Element",
            "sequential": True,
        },
    )
    command_halt: List[SchedHaltType] = field(
        default_factory=list,
        metadata={
            "name": "commandHalt",
            "type": "Element",
            "sequential": True,
        },
    )
    command_log: List[SchedLog1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandLog",
            "type": "Element",
            "sequential": True,
        },
    )
    command_pause: List[SchedPauseType] = field(
        default_factory=list,
        metadata={
            "name": "commandPause",
            "type": "Element",
            "sequential": True,
        },
    )
    command_restart: List[SchedRestartType] = field(
        default_factory=list,
        metadata={
            "name": "commandRestart",
            "type": "Element",
            "sequential": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )


@dataclass
class AsyncMessageList429Type:
    """An asynchronous list buffer used to transmit dynamically defined
    (defined at runtime) data or predefined (defined in the configuration file)
    data.

    This data is placed into a FIFO transmit buffer and transmitted as
    long as data remains in the buffer during gaps in the transmit
    schedule.

    message_buffers:
    async_buffer_max_size: The maximum number of items that can be
        held in the asynchronous list buffer FIFO. None of the message
        buffers defined on this node may have a bufferMaxSize exceeding
        this value.
    """

    message_buffers: Optional[MessageBuffers429Type] = field(
        default=None,
        metadata={
            "name": "messageBuffers",
            "type": "Element",
        },
    )
    async_buffer_max_size: int = field(
        default=512,
        metadata={
            "name": "asyncBufferMaxSize",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32764,
        },
    )


@dataclass
class DefinedErrors1553Type:
    """
    A collection of definedError elements.
    """

    defined_error: List[DefinedError1553Type] = field(
        default_factory=list,
        metadata={
            "name": "definedError",
            "type": "Element",
        },
    )


@dataclass
class Label429Type:
    """A label filter for an ARINC 429 receive channel.

    This label filter will have its own buffer for the reception of data
    and may be configured to be recorded by the sequential monitor (or
    not).

    label_buffer:
    sync_outputs:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    monitor: The boolean flag defines whether the message will be
        recorded in the sequential monitor. This setting controls the
        monitoring of the messages if the channel.monitorMode equal to
        "Selective". If channel.monitorMode equal to "All", this setting
        is ignored.
    label_decimal: The 1-byte label of the ARINC 429 message in
        decimal.
    sdi: The 2-bit SDI of the ARINC 429 message defined as
        enumeration – Off, 00, 01, 10, or 11. All 5 may be defined for a
        given label number, allowing filtering based on the SDI field.
    time_or_hit_count: If hitcount, then the message will record
        hitcount. If time, then the message will record timetag, min,
        and max time. This setting will override the channel setting for
        the same attribute.
    event_log: The boolean flag defines whether the event log will
        be generated for the message reception or not.
    """

    label_buffer: Optional[LabelBuffer429Type] = field(
        default=None,
        metadata={
            "name": "labelBuffer",
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    monitor: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    label_decimal: Optional[int] = field(
        default=None,
        metadata={
            "name": "labelDecimal",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )
    sdi: Label429TypeSdi = field(
        default=Label429TypeSdi.ALL,
        metadata={
            "name": "SDI",
            "type": "Attribute",
        },
    )
    time_or_hit_count: Label429TypeTimeOrHitCount = field(
        default=Label429TypeTimeOrHitCount.TIME,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )
    event_log: bool = field(
        default=False,
        metadata={
            "name": "eventLog",
            "type": "Attribute",
        },
    )


@dataclass
class Message1553Type:
    """
    Defines a particular type of message that can be either added to a schedule
    or sent asynchronously, and associates it with a messageBuffer of data.

    message_bcrt:
    message_rtbc:
    message_rtrt:
    message_mc:
    retry_conditions:
    sync_outputs:
    trigger_inputs:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    enable: Enables message skipping on a message. No effect if
        bufferMaxEntries is greater than 1.
    data_wipe: The enumeration defines how the data is
        initialized. Zeroes - the data is initialized to 0, 123 – the
        data is initialized with incrementing values, CWD - the data is
        initialized with command word, or None - data initialization is
        disabled.
    allow_error_injection: The boolean flag defines whether a
        message error can be generated for the message.
    message_buffer_idref: The ID reference to the message buffer.
        This ID should match with one of the message buffer IDs defined
        in message buffers that define the message data words.
    event_log: The boolean flag defines whether event log will be
        generated for the message.
    sync_output: The boolean flag defines whether an output sync
        signal will be generated for the message.
    monitor: The boolean flag defines whether the message will be
        monitored from the bus. This setting controls the monitoring of
        the message from the bus monitor.
    time_or_hit_count: The enumeration defines that the message
        will record hit count or time tag.
    elapse_min_or_max: The enumeration defines that the message
        will record elapse, min, or max time. They may only be recorded
        if the attribute timeOrHitCount="Time"
    bus: The enumeration defines which bus the message will be
        transmitted on (Bus A or B). Bus A is default.
    retry_count: The number of times the bus controller attempts
        to retransmit the message based on retry conditions.
    """

    message_bcrt: Optional[MessageBcrt1553Type] = field(
        default=None,
        metadata={
            "name": "messageBCRT",
            "type": "Element",
        },
    )
    message_rtbc: Optional[MessageRtbc1553Type] = field(
        default=None,
        metadata={
            "name": "messageRTBC",
            "type": "Element",
        },
    )
    message_rtrt: Optional[MessageRtrt1553Type] = field(
        default=None,
        metadata={
            "name": "messageRTRT",
            "type": "Element",
        },
    )
    message_mc: Optional[MessageMc1553Type] = field(
        default=None,
        metadata={
            "name": "messageMC",
            "type": "Element",
        },
    )
    retry_conditions: Optional[Conditions1553Type] = field(
        default=None,
        metadata={
            "name": "retryConditions",
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    trigger_inputs: Optional[TriggerInputsType] = field(
        default=None,
        metadata={
            "name": "triggerInputs",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    enable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_wipe: Optional[Message1553GroupDataWipe] = field(
        default=None,
        metadata={
            "name": "dataWipe",
            "type": "Attribute",
        },
    )
    allow_error_injection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "allowErrorInjection",
            "type": "Attribute",
        },
    )
    message_buffer_idref: int = field(
        default=-1,
        metadata={
            "name": "messageBufferIDRef",
            "type": "Attribute",
        },
    )
    event_log: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLog",
            "type": "Attribute",
        },
    )
    sync_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "syncOutput",
            "type": "Attribute",
        },
    )
    monitor: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    time_or_hit_count: Optional[Message1553GroupTimeOrHitCount] = field(
        default=None,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )
    elapse_min_or_max: Optional[Message1553GroupElapseMinOrMax] = field(
        default=None,
        metadata={
            "name": "elapseMinOrMax",
            "type": "Attribute",
        },
    )
    bus: Optional[Message1553TypeBus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    retry_count: int = field(
        default=0,
        metadata={
            "name": "retryCount",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 255,
        },
    )


@dataclass
class Message429Type:
    """A single ARINC 429 transmit message.

    The message can be added to a transmit schedule node (when txChannel.scheduleMode is "Explicit")
    or will be automatically scheduled if enabled (when txChannel.scheduleMode = "Rate").

    message_buffers:
    trigger_inputs:
    sync_outputs:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    message_buffer_idref: The ID reference to the message buffer.
        This ID should match with one of the message buffer IDs defined
        in message buffers in order to transmit the message raw data.
    enable: Enables message skipping on a message. No effect if
        bufferMaxEntries is greater than 1.
    single_shot: The boolean flag defines whether the message will
        be transmitted only one time (When set to true, the single-shot
        bit instructs the schedule to process the specified opcode one
        time, and then the skip bit is set after processing is
        complete). The single-shot bit is false (disabled) by default.
    monitor: The boolean flag defines whether the message will be
        recorded in the sequential monitor. This setting controls the
        monitoring of the messages if the channel.monitorMode equal to
        "Selective". If channel.monitorMode equal to "All", this setting
        is ignored.
    min_rate: The minimum message frequency in the interval of the
        message schedule. This is only for channel.scheduleMode equal to
        "Rate". Can be in either ms or us depending on Schedule mode.
    max_rate: The maximum message frequency in the interval of the
        message schedule. This is only for channel.scheduleMode equal to
        "Rate". Can be in either ms or us depending on Schedule mode.
    data_wipe: The enumeration defines what value the message data
        is initialized to. Zeroes – the message data is initialized to
        0, 123 – the message data is initialized to 1, or None – disable
        the message data clear.
    event_log: The boolean flag defines whether the event log will
        be generated for the message or not.
    sync_output: The boolean flag defines whether a sync output
        signal will be generated for the message or not.
    trigger_input: The boolean flag defines whether a trigger
        input signal will control the message transmission.
    parity_error: The boolean flag defines whether a parity error
        will be generated for the message or not.
    label_decimal: The 1-byte label of the ARINC 429 message in
        decimal.
    sdi: The 2-bit SDI of the ARINC 429 message defined as
        enumeration – Off, 00, 01, 10, or 11.
    time_or_hit_count: The enumeration defines whether the message
        will record the hitcount or timetag, min, and max time. If
        hitcount, then the message will record hitcount. If time, then
        the message will record timetag, min, and max time. This setting
        will override the channel setting for the same attribute.
    """

    message_buffers: Optional[MessageBuffers429Type] = field(
        default=None,
        metadata={
            "name": "messageBuffers",
            "type": "Element",
        },
    )
    trigger_inputs: Optional[TriggerInputsType] = field(
        default=None,
        metadata={
            "name": "triggerInputs",
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    message_buffer_idref: int = field(
        default=-1,
        metadata={
            "name": "messageBufferIDRef",
            "type": "Attribute",
        },
    )
    enable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    single_shot: bool = field(
        default=False,
        metadata={
            "name": "singleShot",
            "type": "Attribute",
        },
    )
    monitor: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    min_rate: int = field(
        default=100,
        metadata={
            "name": "minRate",
            "type": "Attribute",
        },
    )
    max_rate: int = field(
        default=200,
        metadata={
            "name": "maxRate",
            "type": "Attribute",
        },
    )
    data_wipe: Message429TypeDataWipe = field(
        default=Message429TypeDataWipe.ZEROES,
        metadata={
            "name": "dataWipe",
            "type": "Attribute",
        },
    )
    event_log: bool = field(
        default=False,
        metadata={
            "name": "eventLog",
            "type": "Attribute",
        },
    )
    sync_output: bool = field(
        default=False,
        metadata={
            "name": "syncOutput",
            "type": "Attribute",
        },
    )
    trigger_input: bool = field(
        default=False,
        metadata={
            "name": "triggerInput",
            "type": "Attribute",
        },
    )
    parity_error: bool = field(
        default=False,
        metadata={
            "name": "parityError",
            "type": "Attribute",
        },
    )
    label_decimal: int = field(
        default=-1,
        metadata={
            "name": "labelDecimal",
            "type": "Attribute",
            "min_inclusive": -1,
            "max_inclusive": 255,
        },
    )
    sdi: Message429TypeSdi = field(
        default=Message429TypeSdi.OFF,
        metadata={
            "name": "SDI",
            "type": "Attribute",
        },
    )
    time_or_hit_count: Message429TypeTimeOrHitCount = field(
        default=Message429TypeTimeOrHitCount.TIME,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )


@dataclass
class MinorFrame1553Type:
    """
    A schedule of commands and messages that can be referenced in a majorFrame.

    command_message_ref:
    command_gap:
    command_pulse:
    command_halt:
    command_log:
    command_pause:
    command_restart:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    frame_time: The length of frame in microseconds. The next
        minor frame will not begin until this time has elapsed, though
        acyclic frames can begin at any time.
    """

    command_message_ref: List[SchedMessageRef1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandMessageRef",
            "type": "Element",
            "sequential": True,
        },
    )
    command_gap: List[SchedGap1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandGap",
            "type": "Element",
            "sequential": True,
        },
    )
    command_pulse: List[SchedPulseType] = field(
        default_factory=list,
        metadata={
            "name": "commandPulse",
            "type": "Element",
            "sequential": True,
        },
    )
    command_halt: List[SchedHaltType] = field(
        default_factory=list,
        metadata={
            "name": "commandHalt",
            "type": "Element",
            "sequential": True,
        },
    )
    command_log: List[SchedLog1553Type] = field(
        default_factory=list,
        metadata={
            "name": "commandLog",
            "type": "Element",
            "sequential": True,
        },
    )
    command_pause: List[SchedPauseType] = field(
        default_factory=list,
        metadata={
            "name": "commandPause",
            "type": "Element",
            "sequential": True,
        },
    )
    command_restart: List[SchedRestartType] = field(
        default_factory=list,
        metadata={
            "name": "commandRestart",
            "type": "Element",
            "sequential": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    frame_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "frameTime",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 20,
            "max_inclusive": 1310700,
        },
    )


@dataclass
class RemoteTerminal1553Type:
    """
    Allows for definition of the 32 remote terminals available on the hardware.

    message_buffers:
    sub_address:
    mode_code:
    sync_outputs:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    rt_address: The remote terminal address (0 – 31)
    rt_mode: The enumeration defines that the RT is enabled for
        simulation,r monitor, or disabled. A simulated RT will respond
        to commands it receives in the manner it is configured, whereas
        a monitored RT will simply hold the data it sees on the bus and
        not respond. Monitor mode is useful for “shadowing” external
        RTs.
    initial_swd: The initial status word used by the simulated
        RTs.
    no_build: The boolean flag defines whether the auto building
        is enabled or disabled. An RT with noBuild set to “true” will
        not create any of the subaddresses or modecodes automatically -
        they must be defined specifically in the configuration file.
        noBuild set to “false” (default) creates all possible
        subaddresses and modecodes under the RT. Only created
        subaddresses and modecodes will can message data so uncreated
        ones will cause the RT to respond to messages to these addresses
        as illegal commands.
    auto_busy: The boolean flag defines whether the auto busy is
        enabled or disabled.
    dynamic_bc: The boolean flag defines whether the RT responds
        to dynamic BC mode code.
    clear_swd_immediate: The Boolean flag defines whether the
        status word bits are cleared immediately.
    bus_enable: The enumeration defines which bus is enabled. AB –
        both bus A and B are enabled, A – bus A is enabled, B – bus B is
        enabled, None – neither bus A or B is enabled. An RT will not
        respond on a bus that is not enabled.
    data_wipe: The enumeration defines how the data is
        initialized. Zeroes – the data is initialized to 0, 123 – the
        data is initialized with incrementing values, CWD – the data is
        initialized with command word, or None – data initialization is
        disabled.
    sync_mode: The enumeration defines that the sync out is
        selected at message level (Selective) or for all messages (All).
    response_mode: The enumeration defines the response mode –
        MIL-STD-1553A or MIL-STD-1553B standard.
    response_time: The response time for the specified Remote
        Terminal on the channel.
    """

    message_buffers: Optional[MessageBuffers1553Type] = field(
        default=None,
        metadata={
            "name": "messageBuffers",
            "type": "Element",
        },
    )
    sub_address: List[SubAddress1553Type] = field(
        default_factory=list,
        metadata={
            "name": "subAddress",
            "type": "Element",
            "max_occurs": 64,
        },
    )
    mode_code: List[ModeCode1553Type] = field(
        default_factory=list,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "max_occurs": 64,
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: Optional[SchemaVersionGroupSchemaVersion] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )
    rt_address: Optional[int] = field(
        default=None,
        metadata={
            "name": "rtAddress",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 31,
        },
    )
    rt_mode: Optional[RemoteTerminal1553TypeRtMode] = field(
        default=None,
        metadata={
            "name": "rtMode",
            "type": "Attribute",
        },
    )
    initial_swd: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "initialSwd",
            "type": "Attribute",
            "length": 2,
            "format": "base16",
        },
    )
    no_build: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noBuild",
            "type": "Attribute",
        },
    )
    auto_busy: Optional[bool] = field(
        default=None,
        metadata={
            "name": "autoBusy",
            "type": "Attribute",
        },
    )
    dynamic_bc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dynamicBC",
            "type": "Attribute",
        },
    )
    clear_swd_immediate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "clearSwdImmediate",
            "type": "Attribute",
        },
    )
    bus_enable: Optional[RemoteTerminal1553TypeBusEnable] = field(
        default=None,
        metadata={
            "name": "busEnable",
            "type": "Attribute",
        },
    )
    data_wipe: Optional[RemoteTerminal1553TypeDataWipe] = field(
        default=None,
        metadata={
            "name": "dataWipe",
            "type": "Attribute",
        },
    )
    sync_mode: Optional[RemoteTerminal1553TypeSyncMode] = field(
        default=None,
        metadata={
            "name": "syncMode",
            "type": "Attribute",
        },
    )
    response_mode: Optional[RemoteTerminal1553TypeResponseMode] = field(
        default=None,
        metadata={
            "name": "responseMode",
            "type": "Attribute",
        },
    )
    response_time: Decimal = field(
        default=Decimal("9.0"),
        metadata={
            "name": "responseTime",
            "type": "Attribute",
            "min_inclusive": Decimal("3.7"),
            "max_inclusive": Decimal("819.1"),
            "fraction_digits": 1,
        },
    )


@dataclass
class Schedule429Type:
    """A predefined ARINC 429 transmit schedule.

    May only be used if txChannel.scheduleMode is "Explicit." Each item
    defined under this node will be scheduled sequentially within the
    transmit schedule. Unless otherwise configured, the schedule will
    repeat back to the beginning after the last item.

    sched_message_ref:
    sched_gap:
    sched_pulse:
    sched_halt:
    sched_pause:
    sched_log:
    sched_restart:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    """

    sched_message_ref: List[SchedMessageRef429Type] = field(
        default_factory=list,
        metadata={
            "name": "schedMessageRef",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_gap: List[SchedGap429Type] = field(
        default_factory=list,
        metadata={
            "name": "schedGap",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_pulse: List[SchedPulseType] = field(
        default_factory=list,
        metadata={
            "name": "schedPulse",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_halt: List[SchedHaltType] = field(
        default_factory=list,
        metadata={
            "name": "schedHalt",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_pause: List[SchedPauseType] = field(
        default_factory=list,
        metadata={
            "name": "schedPause",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_log: List[SchedLog429Type] = field(
        default_factory=list,
        metadata={
            "name": "schedLog",
            "type": "Element",
            "sequential": True,
        },
    )
    sched_restart: List[SchedRestartType] = field(
        default_factory=list,
        metadata={
            "name": "schedRestart",
            "type": "Element",
            "sequential": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )


@dataclass
class SysMonType:
    """
    temperature_sensors: A collection of System Monitor sensors.
    """

    temperature_sensors: Optional[TemperatureSensorsType] = field(
        default=None,
        metadata={
            "name": "temperatureSensors",
            "type": "Element",
        },
    )


@dataclass
class BusMonitor(BusMonitor1553Type):
    class Meta:
        name = "busMonitor"
        namespace = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class AcyclicFrames1553Type:
    """
    A collection of acyclicFrame elements.
    """

    acyclic_frame: List[AcyclicFrame1553Type] = field(
        default_factory=list,
        metadata={
            "name": "acyclicFrame",
            "type": "Element",
        },
    )


@dataclass
class CoreConfigurationType:
    """
    sequential_log: The sequential log settings for the core. This
        node must be present in the configuration file in order for the
        core to utilize the hardware’s sequential monitoring feature.
        Otherwise, data will not be recorded and statistics will not be
        gathered.
    built_in_test: The built-in test setting for the core.
    pxi: The PXIe settings for the core.
    sys_mon: The system monitor settings for the core.
    timing: Timing and Synchronization, IRIG, and Timer settings
        for the core. Timing and Synchronization settings valid only on
        Core 0.
    enable_interrupts: The boolean flag defines whether interrupts
        are enabled for the core.
    """

    sequential_log: SequentialLogType = field(
        default_factory=SequentialLogType,
        metadata={
            "name": "sequentialLog",
            "type": "Element",
        },
    )
    built_in_test: BuiltInTestType = field(
        default_factory=BuiltInTestType,
        metadata={
            "name": "builtInTest",
            "type": "Element",
        },
    )
    pxi: PxiType = field(
        default_factory=PxiType,
        metadata={
            "type": "Element",
        },
    )
    sys_mon: SysMonType = field(
        default_factory=SysMonType,
        metadata={
            "name": "sysMon",
            "type": "Element",
        },
    )
    timing: TimingType = field(
        default_factory=TimingType,
        metadata={
            "type": "Element",
        },
    )
    enable_interrupts: Optional[bool] = field(
        default=None,
        metadata={
            "name": "enableInterrupts",
            "type": "Attribute",
        },
    )


@dataclass
class ErrorInjection1553Type:
    """
    Allows for the definition of errors that are to be injected on the bus for
    testing purposes.

    defined_errors:
    state: The enumeration defines that the error generation is
        disabled (Off), enabled (On), enabled once (Once), or enabled
        externally (External).
    error_messages: The enumeration defines that the errors are
        generated on tagged messages (Tagged) or on any messages (Any).
    preloaded_error_idref: The ID reference to the defined error.
        This ID should match with one of the defined errors.
    """

    defined_errors: Optional[DefinedErrors1553Type] = field(
        default=None,
        metadata={
            "name": "definedErrors",
            "type": "Element",
        },
    )
    state: ErrorInjection1553TypeState = field(
        default=ErrorInjection1553TypeState.OFF,
        metadata={
            "type": "Attribute",
        },
    )
    error_messages: Optional[ErrorInjection1553TypeErrorMessages] = field(
        default=None,
        metadata={
            "name": "errorMessages",
            "type": "Attribute",
            "required": True,
        },
    )
    preloaded_error_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "preloadedErrorIDRef",
            "type": "Attribute",
        },
    )


@dataclass
class Labels429Type:
    """A collection of label filters for an ARINC 429 receive channel.

    Items defined here will have their own buffer for the reception of
    data and may be configured to be recorded by the sequential monitor
    (or not).
    """

    label: List[Label429Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Messages1553Type:
    """
    A collection of messageCommand elements.
    """

    message_command: List[Message1553Type] = field(
        default_factory=list,
        metadata={
            "name": "messageCommand",
            "type": "Element",
        },
    )


@dataclass
class Messages429Type:
    """A collection of ARINC 429 transmit messages.

    Each message defined here can be added to a transmit schedule node (when txChannel.scheduleMode
    is "Explicit") or will be automatically scheduled if enabled
    (when txChannel.scheduleMode = "Rate").
    """

    message: List[Message429Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class MinorFrames1553Type:
    """
    A collection of minorFrame elements.
    """

    minor_frame: List[MinorFrame1553Type] = field(
        default_factory=list,
        metadata={
            "name": "minorFrame",
            "type": "Element",
        },
    )


@dataclass
class RemoteTerminals1553Type:
    """
    A collection of remoteTerminal elements.

    remote_terminal:
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    """

    remote_terminal: List[RemoteTerminal1553Type] = field(
        default_factory=list,
        metadata={
            "name": "remoteTerminal",
            "type": "Element",
            "max_occurs": 32,
        },
    )
    schema_version: Optional[SchemaVersionGroupSchemaVersion] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )


@dataclass
class Schedules429Type:
    """
    A collection of predefined ARINC 429 transmit schedules.
    """

    schedule: List[Schedule429Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class RemoteTerminal(RemoteTerminal1553Type):
    class Meta:
        name = ("remoteTerminal",)
        namespace = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class BusController1553Type:
    """
    Describes how a virtual bus controller should be simulated by the hardware
    on the bus.

    message_buffers:
    messages:
    minor_frames:
    major_frames:
    acyclic_frames:
    sync_outputs:
    trigger_inputs:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    schedule_max_entries: The maximum number of schedule entries
        allocated for the ARINC 429 schedule. The default number is 512.
        For larger schedules, this number should be increased.
    schedule_idref: The ID reference to the MIL-STD-1553 schedule
        major frame. The scheduleIDRef should match with one of major
        frame IDs defined within major frames in order to schedule
        frames for transmit and receive.
    trigger_mode: The enumeration defines no trigger, trigger
        external, or trigger external start.
    event_log_on_halt: The boolean flag defines whether the event
        log on halt is generated for the bus controller (BC).
    event_log_on_pause: The boolean flag defines whether the event
        log on pause is generated for the bus controller (BC).
    step_mode: The boolean flag defines whether the single
        stepping is enabled for BC scheduling.
    sync_mode: The enumeration defines that the sync out is
        selected at message level (Selective) or for all messages (All).
    default_gap: The default gap time between scheduled messages.
        This can be replaced by a unique gap time value defined in the
        schedule gap of minor frames. The valid gap times are between
        4.0 and 819.1.
    timeout: The timeout value in microseconds that sets the
        maximum time the BC will wait before declaring that an RT is
        non-responsive.
    """

    message_buffers: Optional[MessageBuffers1553Type] = field(
        default=None,
        metadata={
            "name": "messageBuffers",
            "type": "Element",
        },
    )
    messages: Optional[Messages1553Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    minor_frames: Optional[MinorFrames1553Type] = field(
        default=None,
        metadata={
            "name": "minorFrames",
            "type": "Element",
        },
    )
    major_frames: Optional[MajorFrames1553Type] = field(
        default=None,
        metadata={
            "name": "majorFrames",
            "type": "Element",
        },
    )
    acyclic_frames: Optional[AcyclicFrames1553Type] = field(
        default=None,
        metadata={
            "name": "acyclicFrames",
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    trigger_inputs: Optional[TriggerInputsType] = field(
        default=None,
        metadata={
            "name": "triggerInputs",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: Optional[SchemaVersionGroupSchemaVersion] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )
    schedule_max_entries: Optional[int] = field(
        default=None,
        metadata={
            "name": "scheduleMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 8187,
        },
    )
    schedule_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "scheduleIDRef",
            "type": "Attribute",
        },
    )
    trigger_mode: Optional[BusController1553TypeTriggerMode] = field(
        default=None,
        metadata={
            "name": "triggerMode",
            "type": "Attribute",
        },
    )
    event_log_on_halt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnHalt",
            "type": "Attribute",
        },
    )
    event_log_on_pause: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eventLogOnPause",
            "type": "Attribute",
        },
    )
    step_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "stepMode",
            "type": "Attribute",
        },
    )
    sync_mode: Optional[BusController1553TypeSyncMode] = field(
        default=None,
        metadata={
            "name": "syncMode",
            "type": "Attribute",
        },
    )
    default_gap: Decimal = field(
        default=Decimal("8.0"),
        metadata={
            "name": "defaultGap",
            "type": "Attribute",
            "min_inclusive": Decimal("4.0"),
            "max_inclusive": Decimal("819.1"),
            "fraction_digits": 1,
        },
    )
    timeout: Decimal = field(
        default=Decimal("19.0"),
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("3.0"),
            "max_inclusive": Decimal("102.3"),
            "fraction_digits": 1,
        },
    )


@dataclass
class RxChannel429Type:
    """
    ARINC 429 receive channel settings.

    labels:
    sync_outputs:
    speed: The speed mode of the specified receive channel - Auto,
        Low, or High.
    speed_khz: The receive parametric frequency rate in KHz on the
        specified receive channel. Only valid when rxChannel.speed is
        "Low" or "High". Default speed when this attribute is not set,
        12.5 KHz for low speed and 100.0 KHz for high speed.
    event_log_on_error: The boolean flag defines whether the event
        log on decoder errors is generated or not.
    default_buffer_monitor: The boolean flag defines whether
        received messages arriving at the default label receive buffer
        will be recorded in the sequential monitor. This setting
        controls the monitoring of the messages if the
        channel.monitorMode equal to "Selective". If channel.monitorMode
        equal to "All", this setting is ignored.
    default_buffer_max_entries: The maximum number of 4-byte raw
        message data entries in the default label receive buffer. This
        is the buffer that holds received messages that have not been
        filtered to a specific label defined in this configuration file.
    default_buffer_type: The default list buffer type of received
        messages. Only the FIFO type is valid.
    default_buffer_event_log: The boolean flag defines whether
        messages received by the default label will generate the event
        log for the specified channel or not.
    default_buffer_event_log_on_full: The boolean flag defines
        whether messages received by the default label will generate an
        event log when the buffer is full.
    auto_label_filter_mode: This attribute defines whether receive
        label filters are created automatically for the channel. If
        "None" - label filters are not created automatically - they must
        be specified within the labels collection. If "Labels" - label
        filters are all created automatically for current value. If
        monitoring of the label is to be changed from the channel
        setting or there is to be a list buffer rather than current
        value - a label definition must be added to the labels
        collection. If "SDI" - label+SDI filters are all created
        automatically for current value. If monitoring of the label is
        to be changed from the channel setting or there is to be a list
        buffer rather than current value - a label definition must be
        added to the labels collection.
    """

    labels: Optional[Labels429Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    speed: RxChannel429TypeSpeed = field(
        default=RxChannel429TypeSpeed.AUTO,
        metadata={
            "type": "Attribute",
        },
    )
    speed_khz: Decimal = field(
        default=Decimal("100.0"),
        metadata={
            "name": "speedKHz",
            "type": "Attribute",
            "min_inclusive": Decimal("2.4"),
            "max_inclusive": Decimal("200.0"),
            "fraction_digits": 1,
        },
    )
    event_log_on_error: bool = field(
        default=False,
        metadata={
            "name": "eventLogOnError",
            "type": "Attribute",
        },
    )
    default_buffer_monitor: bool = field(
        default=False,
        metadata={
            "name": "defaultBufferMonitor",
            "type": "Attribute",
        },
    )
    default_buffer_max_entries: int = field(
        default=1,
        metadata={
            "name": "defaultBufferMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32764,
        },
    )
    default_buffer_type: RxChannel429TypeDefaultBufferType = field(
        default=RxChannel429TypeDefaultBufferType.FIFO,
        metadata={
            "name": "defaultBufferType",
            "type": "Attribute",
        },
    )
    default_buffer_event_log: bool = field(
        default=False,
        metadata={
            "name": "defaultBufferEventLog",
            "type": "Attribute",
        },
    )
    default_buffer_event_log_on_full: bool = field(
        default=False,
        metadata={
            "name": "defaultBufferEventLogOnFull",
            "type": "Attribute",
        },
    )
    auto_label_filter_mode: RxChannel429TypeAutoLabelFilterMode = field(
        default=RxChannel429TypeAutoLabelFilterMode.LABELS,
        metadata={
            "name": "autoLabelFilterMode",
            "type": "Attribute",
        },
    )


@dataclass
class TxChannel429Type:
    """
    ARINC 429 transmit channel settings.

    async_message_list: Only FIFOs may be used for Async List
        buffer.
    messages:
    schedules:
    trigger_inputs:
    sync_outputs:
    schedule_idref: The ID reference to the ARINC 429 schedule. If
        the schedule mode is “Rate”, this ID reference is not used. If
        the schedule mode is “Explicit”, the scheduleIDRef should match
        with one of schedule IDs defined in within the schedules element
        in order to schedule messages for transmit.
    speed_khz: The transmit parametric frequency rate in KHz on
        specified channel - If it is less than 20 KHz, the low speed
        channel configuration is selected; otherwise, the high speed
        channel configuration is selected. Default speed when this
        attribute is not set is 12.5 KHz for low speed and 100.0 KHz for
        high speed.
    parametric_mode: The enumeration defines whether the
        parametric waveform control is enabled or not. This allows the
        use of the positiveLeg, negativeLeg, highVolt, lowVolt,
        nullVolt, cmBiasVolt, highRiseTime, and lowRiseTime attributes
        and is only available on Advanced 429 channels (45x models)
    event_log_on_halt: The boolean flag defines whether the event
        log on schedule halt is generated or not.
    event_log_on_pause: The boolean flag defines whether the event
        log on schedule pause is generated or not.
    paused: Future use.
    schedule_max_entries: The maximum number of schedule entries
        allocated for the ARINC 429 schedule. The default number is 512.
        For larger schedules, this number should be increased.
    schedule_mode: The schedule mode – Explicit or Rate. Explicit
        requires one or more schedules under the “schedule” element.
        Rate will use the “minRate” and “maxRate” attributes of messages
        to build the schedule at runtime.
    schedule_build_method: The schedule build mode method –
        Normal, Quick, or Both. If the Both method is selected, the
        Quick method is chosen first, if failed, then the Normal method
        is chosen, finally the legacy method. Valid only if scheduleMode
        is "Rate".
    schedule_build_unit: The schedule build unit defines the
        scheduling periods in milliseconds or microseconds. Valid only
        if scheduleMode is "Rate".
    positive_leg: The output state of the transmitter's positive
        leg. Signal – connect the leg to normal transmit signal, Open –
        leave the leg open, and Ground – short the leg to ground. Valid
        only if parametricMode is "Wave".
    negative_leg: The output state of the transmitter's negative
        leg. Signal – connect the leg to normal transmit signal, Open –
        leave the leg open, and Ground – short the leg to ground. Valid
        only if parametricMode is "Wave".
    high_volt: The differential voltage of the first half of all
        one-bits for the parametric waveform configuration in volts. 6G
        devices with parametric waveform capability provide control over
        transmit amplitude, offset voltage, null voltage, common-mode
        bias, rise time, and fall time. Valid only if parametricMode is
        "Wave."
    low_volt: The differential voltage of the first half of all
        zero-bits for the parametric waveform configuration in volts.
        Valid only if parametricMode is "Wave".
    null_volt: The differential voltage of the second half of all
        bits for the parametric waveform configuration in volts. Valid
        only if parametricMode is "Wave".
    cm_bias_volt: The single-ended common mode bias of the entire
        signal for the parametric waveform configuration in volts. Valid
        only if parametricMode is "Wave".
    high_rise_time: The rise and fall time of all one-bits for the
        parametric waveform configuration in microseconds. Valid only if
        parametricMode is "Wave".
    low_rise_time: The rise and fall time of all zero-bits for the
        parametric waveform configuration in microseconds. Valid only if
        parametricMode is "Wave".
    """

    async_message_list: Optional[AsyncMessageList429Type] = field(
        default=None,
        metadata={
            "name": "asyncMessageList",
            "type": "Element",
        },
    )
    messages: Optional[Messages429Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    schedules: Optional[Schedules429Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    trigger_inputs: Optional[TriggerInputsType] = field(
        default=None,
        metadata={
            "name": "triggerInputs",
            "type": "Element",
        },
    )
    sync_outputs: Optional[SyncOutputsType] = field(
        default=None,
        metadata={
            "name": "syncOutputs",
            "type": "Element",
        },
    )
    schedule_idref: Optional[int] = field(
        default=None,
        metadata={
            "name": "scheduleIDRef",
            "type": "Attribute",
        },
    )
    speed_khz: Decimal = field(
        default=Decimal("100.0"),
        metadata={
            "name": "speedKHz",
            "type": "Attribute",
            "min_inclusive": Decimal("2.4"),
            "max_inclusive": Decimal("200.0"),
            "fraction_digits": 1,
        },
    )
    parametric_mode: TxChannel429TypeParametricMode = field(
        default=TxChannel429TypeParametricMode.OFF,
        metadata={
            "name": "parametricMode",
            "type": "Attribute",
        },
    )
    event_log_on_halt: bool = field(
        default=False,
        metadata={
            "name": "eventLogOnHalt",
            "type": "Attribute",
        },
    )
    event_log_on_pause: bool = field(
        default=False,
        metadata={
            "name": "eventLogOnPause",
            "type": "Attribute",
        },
    )
    paused: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    schedule_max_entries: int = field(
        default=512,
        metadata={
            "name": "scheduleMaxEntries",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 8187,
        },
    )
    schedule_mode: TxChannel429TypeScheduleMode = field(
        default=TxChannel429TypeScheduleMode.EXPLICIT,
        metadata={
            "name": "scheduleMode",
            "type": "Attribute",
        },
    )
    schedule_build_method: TxChannel429TypeScheduleBuildMethod = field(
        default=TxChannel429TypeScheduleBuildMethod.BOTH,
        metadata={
            "name": "scheduleBuildMethod",
            "type": "Attribute",
        },
    )
    schedule_build_unit: TxChannel429TypeScheduleBuildUnit = field(
        default=TxChannel429TypeScheduleBuildUnit.MILLISECOND,
        metadata={
            "name": "scheduleBuildUnit",
            "type": "Attribute",
        },
    )
    positive_leg: TxChannel429TypePositiveLeg = field(
        default=TxChannel429TypePositiveLeg.SIGNAL,
        metadata={
            "name": "positiveLeg",
            "type": "Attribute",
        },
    )
    negative_leg: TxChannel429TypeNegativeLeg = field(
        default=TxChannel429TypeNegativeLeg.SIGNAL,
        metadata={
            "name": "negativeLeg",
            "type": "Attribute",
        },
    )
    high_volt: Decimal = field(
        default=Decimal("10.000"),
        metadata={
            "name": "highVolt",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    low_volt: Decimal = field(
        default=Decimal("-10.000"),
        metadata={
            "name": "lowVolt",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    null_volt: Decimal = field(
        default=Decimal("0.000"),
        metadata={
            "name": "nullVolt",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    cm_bias_volt: Decimal = field(
        default=Decimal("0.000"),
        metadata={
            "name": "cmBiasVolt",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    high_rise_time: Decimal = field(
        default=Decimal("1.800"),
        metadata={
            "name": "highRiseTime",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    low_rise_time: Decimal = field(
        default=Decimal("1.800"),
        metadata={
            "name": "lowRiseTime",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )


@dataclass
class RemoteTerminals(RemoteTerminals1553Type):
    class Meta:
        name = "remoteTerminals"
        namespace = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class Channel429Type:
    """
    An ARINC 429 channel.

    tx_channel:
    rx_channel:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    hardware_channel: The actual hardware channel number - each
        card has multiple cores and each core has multiple channels. -1
        may be set as a “Don't Care” value so the application can set
        the channel number dynamically.
    channel_buffer_max_size_kb: The maximum size of the channel
        sequential monitor buffer which stores data records received and
        transmitted on the channel.
    parity: The enumeration defines that the parity bit of the
        ARINC 429 message is set as Odd, Even, or Data.
    enable: Future use.
    monitor_mode: The enumeration defines that the sequential
        record is enabled at message level (Selective) or entire channel
        (All).
    time_or_hit_count: If hitcount, then the channel will record
        hitcount on messages by default. If time, then the channel will
        record timetag, min, and max time on messages by default.
        Setting to None means this setting is fully controlled at the
        message level. This can be overridden by the message setting.
    statistics: The boolean flag defines whether the statistic and
        error monitoring process (message count, error count, and error
        type) is enabled or not.
    self_test_bus: Enables the internal transmit/receive
        wraparound for the channel. Only one transmit channel should
        enable this setting at a time. One or more receive channels may
        also enable this setting to allow the channel to receive the
        transmit channel's transmissions.
    """

    tx_channel: Optional[TxChannel429Type] = field(
        default=None,
        metadata={
            "name": "txChannel",
            "type": "Element",
        },
    )
    rx_channel: Optional[RxChannel429Type] = field(
        default=None,
        metadata={
            "name": "rxChannel",
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: SchemaVersionGroupSchemaVersion = field(
        default=SchemaVersionGroupSchemaVersion.UNDEFINED,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )
    hardware_channel: int = field(
        default=-1,
        metadata={
            "name": "hardwareChannel",
            "type": "Attribute",
        },
    )
    channel_buffer_max_size_kb: int = field(
        default=1024,
        metadata={
            "name": "channelBufferMaxSizeKB",
            "type": "Attribute",
            "min_inclusive": 512,
            "max_inclusive": 16384,
        },
    )
    parity: Channel429TypeParity = field(
        default=Channel429TypeParity.ODD,
        metadata={
            "type": "Attribute",
        },
    )
    enable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    monitor_mode: Channel429TypeMonitorMode = field(
        default=Channel429TypeMonitorMode.SELECTIVE,
        metadata={
            "name": "monitorMode",
            "type": "Attribute",
        },
    )
    time_or_hit_count: Channel429TypeTimeOrHitCount = field(
        default=Channel429TypeTimeOrHitCount.TIME,
        metadata={
            "name": "timeOrHitCount",
            "type": "Attribute",
        },
    )
    statistics: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    self_test_bus: bool = field(
        default=False,
        metadata={
            "name": "selfTestBus",
            "type": "Attribute",
        },
    )


@dataclass
class Simulation1553Type:
    """
    Encapsulates nodes that describe the simulation of MIL-STD-1553-compliant
    hardware on a bus.
    """

    bus_monitor: Optional[BusMonitor1553Type] = field(
        default=None,
        metadata={
            "name": "busMonitor",
            "type": "Element",
        },
    )
    bus_controller: Optional[BusController1553Type] = field(
        default=None,
        metadata={
            "name": "busController",
            "type": "Element",
        },
    )
    remote_terminals: Optional[RemoteTerminals1553Type] = field(
        default=None,
        metadata={
            "name": "remoteTerminals",
            "type": "Element",
        },
    )
    error_injection: Optional[ErrorInjection1553Type] = field(
        default=None,
        metadata={
            "name": "errorInjection",
            "type": "Element",
        },
    )


@dataclass
class BusController(BusController1553Type):
    class Meta:
        name = "busController"
        namespace = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class Channel1553Type:
    """
    Represents a 1553 channel at its highest level.

    simulation:
    playback:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    hardware_channel: The actual hardware channel number - each
        card has multiple cores and each core has multiple channels. -1
        may be set as a “Don't Care” value so the application can set
        the channel number dynamically.
    channel_buffer_max_size_kb: The maximum size of the channel
        sequential monitor buffer which stores data records received and
        transmitted on the channel.
    amplitude_adjust_enable: The boolean flag defines whether the
        parametric amplitude control is enabled.
    amplitude_percent: The percentage of the amplitude control
        value used for configuration. 50% is used as default while 100%
        is twice the default amplitude. Actual voltage varies depending
        on bus loading and driver strength.
    termination: The enumeration defines whether the direct
        coupled termination resistance is set to off (Bus A and B) or on
        (Bus A, B, or both A and B)
    mode_codes: The enumeration defines whether the mode code is
        enabled (MC0, MC1, or MC01) or disabled (None). The sub address
        (SA) 0b00000 will be selected for the mode code if it is MC0, SA
        0b11111 will be selected for the mode code if it is MC1, or
        random SA 0b00000 or 0b11111 will be selected for the mode code
        if it is MC01.
    broadcast: The boolean flag defines whether the broadcast is
        enabled. When broadcast is enabled, RT31 is treated as the
        broadcast RT and holds all broadcast message data.
    """

    simulation: Optional[Simulation1553Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    playback: Optional[Playback1553Type] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: Optional[SchemaVersionGroupSchemaVersion] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )
    hardware_channel: int = field(
        default=0,
        metadata={
            "name": "hardwareChannel",
            "type": "Attribute",
        },
    )
    channel_buffer_max_size_kb: Optional[int] = field(
        default=None,
        metadata={
            "name": "channelBufferMaxSizeKB",
            "type": "Attribute",
            "min_inclusive": 512,
            "max_inclusive": 16384,
        },
    )
    amplitude_adjust_enable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "amplitudeAdjustEnable",
            "type": "Attribute",
        },
    )
    amplitude_percent: Decimal = field(
        default=Decimal("50.00"),
        metadata={
            "name": "amplitudePercent",
            "type": "Attribute",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("100.00"),
            "fraction_digits": 2,
        },
    )
    termination: Optional[Channel1553TypeTermination] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mode_codes: Optional[Channel1553TypeModeCodes] = field(
        default=None,
        metadata={
            "name": "modeCodes",
            "type": "Attribute",
        },
    )
    broadcast: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Channel429(Channel429Type):
    class Meta:
        name = "channel429"
        namespace = "http://www.ballardtech.com/DatabusSchemas/"


@dataclass
class CoreType:
    """
    Represents a (potential) multichannel piece of hardware at its highest
    level.

    core_configuration:
    channel1553:
    channel429:
    id: The ID used as a unique reference to the object.
    name: The name used as a unique human readable reference to
        the object.
    schema_version: Targeted version of schema this document has
        been created for. The version number must exactly match the
        version used by the VI Library and the XML Configuration Editor.
    """

    core_configuration: Optional[CoreConfigurationType] = field(
        default=None,
        metadata={
            "name": "coreConfiguration",
            "type": "Element",
        },
    )
    channel1553: List[Channel1553Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    channel429: List[Channel429Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
        },
    )
    name: str = field(
        default="",
        metadata={
            "type": "Attribute",
            "min_length": 0,
            "max_length": 256,
            "white_space": "preserve",
        },
    )
    schema_version: SchemaVersionGroupSchemaVersion = field(
        default=SchemaVersionGroupSchemaVersion.UNDEFINED,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
        },
    )


@dataclass
class Channel1553(Channel1553Type):
    class Meta:
        name = "channel1553"


@dataclass
class Core(CoreType):
    class Meta:
        name = "core"
        namespace = "http://www.ballardtech.com/DatabusSchemas/"
