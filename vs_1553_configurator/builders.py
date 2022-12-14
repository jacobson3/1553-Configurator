from abc import ABC, abstractmethod
from enum import Enum
from vs_1553_configurator.bti_1553_parameters import (
    Parameters,
    AddressDirection,
    MessageMessageType,
)


class MC_Direction(Enum):
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
        Message name
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
    def create_parameter_message(self) -> Parameters.Channel.Message:
        """
        Create Message dataclass object to be flattened to parameters XML
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

    def create_parameter_message(self) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            self.terminal_address, self.sub_address, AddressDirection.RX
        )

        message = Parameters.Channel.Message(
            self.name, [address], MessageMessageType.BC_TO_RT, self.words
        )

        return message


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

    def create_parameter_message(self) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            self.terminal_address, self.sub_address, AddressDirection.TX
        )

        message = Parameters.Channel.Message(
            self.name, [address], MessageMessageType.RT_TO_BC, self.words
        )

        return message


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
        The number of data words to expect represented in 5 bits in the command word 1
        """
        return self._words

    @words.setter
    def words(self, words: int):
        self._words = words

    def create_parameter_message(self) -> Parameters.Channel.Message:
        address1 = Parameters.Channel.Message.Address(
            self.terminal_address1, self.sub_address1, AddressDirection.RX
        )

        address2 = Parameters.Channel.Message.Address(
            self.terminal_address2, self.sub_address2, AddressDirection.TX
        )

        message = Parameters.Channel.Message(
            self.name, [address1, address2], MessageMessageType.RT_TO_RT, self.words
        )

        return message


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
        Mode code direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction: MC_Direction):
        self._direction = direction

    def create_parameter_message(self) -> Parameters.Channel.Message:

        mc_direction = (
            AddressDirection.RX if self.direction == MC_Direction.RX else AddressDirection.TX
        )

        address = Parameters.Channel.Message.Address(
            self.terminal_address, self.sub_address, mc_direction
        )

        message = Parameters.Channel.Message(
            self.name, [address], MessageMessageType.MC, self.words, mode_code=self.mode_code
        )

        return message


if __name__ == "__main__":
    from xsdata.formats.dataclass.serializers import XmlSerializer

    message_list = []
    message_list.append(BC_RT_Message("bcrt_test_message", 3, 21, 5))
    message_list.append(RT_BC_Message("rtbc_test_message", 15, 3, 4))
    message_list.append(RT_RT_Message("rtrt_test_message", 15, 20, 1, 20, 4))
    message_list.append(MC_Message("mc_test_message", 1, 31, 1, 17, MC_Direction.RX))

    parameter_messages = []
    for message in message_list:
        parameter_messages.append(message.create_parameter_message())

    channel = Parameters.Channel(0, message=parameter_messages)

    serializer = XmlSerializer()
    print(serializer.render(channel))
