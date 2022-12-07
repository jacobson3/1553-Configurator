from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class AddressDirection(Enum):
    RX = "Rx"
    TX = "Tx"


class MessageMessageType(Enum):
    BC_TO_RT = "BC to RT"
    RT_TO_BC = "RT to BC"
    RT_TO_RT = "RT to RT"
    MC = "MC"


class ParameterEncoding(Enum):
    BNR = "BNR"
    BCD = "BCD"
    DISCRETE = "Discrete"


@dataclass
class Parameters:
    class Meta:
        name = "parameters"

    channel: List["Parameters.Channel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 256,
        }
    )

    @dataclass
    class Channel:
        hardware_channel: Optional[int] = field(
            default=None,
            metadata={
                "name": "hardwareChannel",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 255,
            }
        )
        terminals: Optional["Parameters.Channel.Terminals"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        acyclic_frame: List["Parameters.Channel.AcyclicFrame"] = field(
            default_factory=list,
            metadata={
                "name": "acyclicFrame",
                "type": "Element",
            }
        )
        message: List["Parameters.Channel.Message"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class Terminals:
            terminal: List["Parameters.Channel.Terminals.Terminal"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 32,
                }
            )

            @dataclass
            class Terminal:
                terminal_address: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "terminalAddress",
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 31,
                    }
                )
                terminal_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "terminalName",
                        "type": "Element",
                    }
                )

        @dataclass
        class AcyclicFrame:
            create_trigger_channel: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "createTriggerChannel",
                    "type": "Element",
                }
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

        @dataclass
        class Message:
            """
            :ivar name:
            :ivar address:
            :ivar message_type:
            :ivar number_of_words:
            :ivar mode_code:
            :ivar create_timestamp_channel: Automatic creation of read-
                only VeriStand channel for timestamp is only supported
                for Rx messages/endpoints.
            :ivar parameters:
            """
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            address: List["Parameters.Channel.Message.Address"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 2,
                }
            )
            message_type: Optional[MessageMessageType] = field(
                default=None,
                metadata={
                    "name": "messageType",
                    "type": "Element",
                    "required": True,
                }
            )
            number_of_words: Optional[int] = field(
                default=None,
                metadata={
                    "name": "numberOfWords",
                    "type": "Element",
                    "required": True,
                    "min_inclusive": 0,
                    "max_inclusive": 32,
                }
            )
            mode_code: Optional[int] = field(
                default=None,
                metadata={
                    "name": "modeCode",
                    "type": "Element",
                    "min_inclusive": 0,
                    "max_inclusive": 31,
                }
            )
            create_timestamp_channel: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "createTimestampChannel",
                    "type": "Element",
                }
            )
            parameters: Optional["Parameters.Channel.Message.Parameters"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )

            @dataclass
            class Address:
                terminal_address: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "terminalAddress",
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 31,
                    }
                )
                sub_address: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "subAddress",
                        "type": "Element",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 31,
                    }
                )
                direction: AddressDirection = field(
                    default=AddressDirection.RX,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )

            @dataclass
            class Parameters:
                parameter: List["Parameters.Channel.Message.Parameters.Parameter"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class Parameter:
                    """
                    :ivar encoding:
                    :ivar signed:
                    :ivar start_bit:
                    :ivar number_of_bits:
                    :ivar scale:
                    :ivar offset:
                    :ivar name: For Discrete encoding, there is one
                        "name" element per Bit
                    :ivar unit:
                    :ivar default_value:
                    """
                    encoding: List[ParameterEncoding] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    signed: List[bool] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    start_bit: List[int] = field(
                        default_factory=list,
                        metadata={
                            "name": "startBit",
                            "type": "Element",
                            "min_inclusive": 0,
                            "max_inclusive": 511,
                        }
                    )
                    number_of_bits: List[int] = field(
                        default_factory=list,
                        metadata={
                            "name": "numberOfBits",
                            "type": "Element",
                            "min_inclusive": 1,
                            "max_inclusive": 53,
                        }
                    )
                    scale: List[float] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    offset: List[float] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    name: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    unit: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                        }
                    )
                    default_value: List[float] = field(
                        default_factory=list,
                        metadata={
                            "name": "defaultValue",
                            "type": "Element",
                        }
                    )
