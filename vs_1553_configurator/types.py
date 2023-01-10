from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class MC_Direction(Enum):
    """
    Mode code message direction enum
    """

    RX = "Rx"
    TX = "Tx"


class Message(ABC):
    """
    Abstract 1553 message type
    """

    def __init__(self, name: str, options: dict = {}):
        self.options = options
        self.name = name

    @property
    def name(self) -> str:
        """
        Message name, each message must have a unique name
        """
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def options(self) -> dict:
        """
        Dictionary holding optional/non-standard message options
        """
        return self._options

    @options.setter
    def options(self, options: dict):
        self._options = options

    @abstractmethod
    def list_terminals(self) -> List[int]:
        """
        Return list of RX and TX terminal addresses used in this message
        """
        pass


class BC_RT_Message(Message):
    """
    Bus Controller to Remote Terminal message
    """

    def __init__(
        self, name: str, terminal_address: int, sub_address: int, words: int, options: dict = {}
    ):
        super().__init__(name, options)

        self.terminal_address = terminal_address
        self.sub_address = sub_address
        self.words = words

    @property
    def terminal_address(self) -> int:
        """
        The remote terminal address (0 - 31) represented in 5 bits in the command word 1
        """
        return self._ta

    @terminal_address.setter
    def terminal_address(self, ta: int):
        self._ta = ta

    @property
    def sub_address(self) -> int:
        """
        The sub address (location) of data (0 - 31) represented in 5 bits in the command word 1
        """
        return self._sa

    @sub_address.setter
    def sub_address(self, sa: int):
        self._sa = sa

    @property
    def words(self) -> int:
        """
        The number of data words to expect represented in 5 bits in the command word 1
        """
        return self._words

    @words.setter
    def words(self, words: int):
        self._words = words

    def list_terminals(self) -> List[int]:
        return [self.terminal_address]


class RT_BC_Message(Message):
    """
    Remote Terminal to Bus Controller message
    """

    def __init__(
        self, name: str, terminal_address: int, sub_address: int, words: int, options: dict = {}
    ):
        super().__init__(name, options)

        self.terminal_address = terminal_address
        self.sub_address = sub_address
        self.words = words

    @property
    def terminal_address(self) -> int:
        """
        The remote terminal address (0 - 31) represented in 5 bits in the command word 1
        """
        return self._ta

    @terminal_address.setter
    def terminal_address(self, ta: int):
        self._ta = ta

    @property
    def sub_address(self) -> int:
        """
        The sub address (location) of data (0 - 31) represented in 5 bits in the command word 1
        """
        return self._sa

    @sub_address.setter
    def sub_address(self, sa: int):
        self._sa = sa

    @property
    def words(self) -> int:
        """
        The number of data words to expect represented in 5 bits in the command word 1
        """
        return self._words

    @words.setter
    def words(self, words: int):
        self._words = words

    def list_terminals(self) -> List[int]:
        return [self.terminal_address]


class RT_RT_Message(Message):
    """
    Remote Terminal to Remote Terminal message
    """

    def __init__(
        self,
        name: str,
        terminal_address1: int,
        sub_address1: int,
        terminal_address2: int,
        sub_address2: int,
        words: int,
        options: dict = {},
    ):
        super().__init__(name, options)

        self.terminal_address1 = terminal_address1
        self.sub_address1 = sub_address1
        self.terminal_address2 = terminal_address2
        self.sub_address2 = sub_address2
        self.words = words

    @property
    def terminal_address1(self) -> int:
        """
        The remote terminal address (0 - 31) represented in 5 bits in the command word 1
        """
        return self._ta1

    @terminal_address1.setter
    def terminal_address1(self, ta: int):
        self._ta1 = ta

    @property
    def sub_address1(self) -> int:
        """
        The sub address (location) of data (0 - 31) represented in 5 bits in the command word 1
        """
        return self._sa1

    @sub_address1.setter
    def sub_address1(self, sa: int):
        self._sa1 = sa

    @property
    def terminal_address2(self) -> int:
        """
        The remote terminal address (0 - 31) represented in 5 bits in the command word 2
        """
        return self._ta2

    @terminal_address2.setter
    def terminal_address2(self, ta: int):
        self._ta2 = ta

    @property
    def sub_address2(self) -> int:
        """
        The sub address (location) of data (0 - 31) represented in 5 bits in the command word 2
        """
        return self._sa2

    @sub_address2.setter
    def sub_address2(self, sa: int):
        self._sa2 = sa

    @property
    def words(self) -> int:
        """
        The number of data words to expect represented in 5 bits in the command word 1 and 2
        """
        return self._words

    @words.setter
    def words(self, words: int):
        self._words = words

    def list_terminals(self) -> List[int]:
        return [self.terminal_address1, self.terminal_address2]


class MC_Message(Message):
    """
    Mode Code message
    """

    def __init__(
        self,
        name: str,
        terminal_address: int,
        sub_address: int,
        words: int,
        mode_code: int,
        mc_direction: MC_Direction,
        options: dict = {},
    ):
        super().__init__(name, options)

        self.terminal_address = terminal_address
        self.sub_address = sub_address
        self.words = words
        self.mode_code = mode_code
        self.direction = mc_direction

    @property
    def terminal_address(self) -> int:
        """
        The remote terminal address (0 - 31) represented in 5 bits in the command word 1
        """
        return self._ta

    @terminal_address.setter
    def terminal_address(self, ta: int):
        self._ta = ta

    @property
    def sub_address(self) -> int:
        """
        The sub address (location) of data (0 - 31) represented in 5 bits in the command word 1
        """
        return self._sa

    @sub_address.setter
    def sub_address(self, sa: int):
        self._sa = sa

    @property
    def words(self) -> int:
        """
        The number of data words to expect represented in 5 bits in the command word 1
        """
        return self._words

    @words.setter
    def words(self, words: int):
        self._words = words

    @property
    def mode_code(self) -> int:
        """
        Mode code command value
        """
        return self._mode_code

    @mode_code.setter
    def mode_code(self, mode_code: int):
        self._mode_code = mode_code

    @property
    def direction(self) -> MC_Direction:
        """
        Mode code direction (Rx | Tx)
        """
        return self._direction

    @direction.setter
    def direction(self, direction: MC_Direction):
        self._direction = direction

    def list_terminals(self) -> List[int]:
        return [self.terminal_address]


class Frame(ABC):
    """
    Abstract 1553 Frame type
    """

    def __init__(self, name: str, schedule: List[str], options: dict = {}):
        self.options = options
        self.name = name
        self.schedule = schedule

    @property
    def name(self) -> str:
        """
        Frame name, each frame must have a unique name
        """
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def options(self) -> dict:
        """
        Dictionary holding optional/non-standard frame options
        """
        return self._options

    @options.setter
    def options(self, options: dict):
        self._options = options

    @property
    def schedule(self) -> List[str]:
        """
        List of frames/messages defining schedule of the major frame
        """
        return self._schedule

    @schedule.setter
    def schedule(self, frames: List[str]):
        self._schedule = frames


class MajorFrame(Frame):
    """
    Specifies a schedule that can be referenced by the channel for execution
    """

    def __init__(self, name: str, schedule: List[str], options: dict = {}):
        super().__init__(name, schedule, options)


class AcyclicFrame(Frame):
    """
    A schedule of commands and messages that can be transmitted on-demand
    """

    def __init__(self, name: str, schedule: List[str], options: dict = {}):
        super().__init__(name, schedule, options)


class MinorFrame(Frame):
    """
    A schedule of commands and messages that can be referenced in a majorFrame
    """

    def __init__(self, name: str, schedule: List[str], frame_time: int, options: dict = {}):
        super().__init__(name, schedule, options)
        self.frame_time = frame_time

    @property
    def frame_time(self) -> int:
        """
        The length of frame in microseconds. The next minor frame will not begin until this time
        has elapsed.
        """
        return self._frame_time

    @frame_time.setter
    def frame_time(self, frame_time: int):
        self._frame_time = frame_time


class MIL_STD_1553_Config:
    """
    Data object representing all information necessary to define a MIL-STD-1553 bus
    """

    def __init__(self):
        self.messages = []
        self.minor_frames = []
        self.major_frames = []
        self.acyclic_frames = []

    @property
    def messages(self) -> List[Message]:
        """
        Messages communicated over a MIL-STD-1553 bus
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[Message]):
        self._messages = messages

    @property
    def minor_frames(self) -> List[MinorFrame]:
        """
        A list of minor frames with each minor frame being a list of messages to be scheduled
        """
        return self._minor_frames

    @minor_frames.setter
    def minor_frames(self, frames: List[MinorFrame]):
        self._minor_frames = frames

    @property
    def major_frames(self) -> List[MajorFrame]:
        """
        A list of major frames with each major frame being a schedule of several minor frames
        """
        return self._major_frames

    @major_frames.setter
    def major_frames(self, frames: List[MajorFrame]):
        self._major_frames = frames

    @property
    def acyclic_frames(self) -> List[AcyclicFrame]:
        """
        A list of acyclic frames with each frame being a list of messages to be sent when specified
        """
        return self._acyclic_frames

    @acyclic_frames.setter
    def acyclic_frames(self, frames: List[AcyclicFrame]):
        self._acyclic_frames = frames
