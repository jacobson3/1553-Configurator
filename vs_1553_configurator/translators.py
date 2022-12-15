from abc import ABC, abstractmethod
from typing import List
import vs_1553_configurator.types as types
from xsdata.formats.dataclass.serializers import XmlSerializer
from vs_1553_configurator.bti_1553_parameters import (
    Parameters,
    AddressDirection,
    MessageMessageType,
)


class MIL_1553_Translator(ABC):
    def __init__(self, messages: List[types.Message]):
        self.messages = messages

    @property
    def messages(self) -> List[types.Message]:
        return self._messages

    @messages.setter
    def messages(self, messages: List[types.Message]):
        self._messages = messages

    @abstractmethod
    def _create_parameter_messages(self):
        """
        Create Message dataclasses to be flattened to parameters XML
        """
        pass


class BTI_1553_Translator(MIL_1553_Translator):
    def __init__(self, messages: List[types.Message]):
        super().__init__(messages)

    def generate_parameters_xml(self) -> str:
        messages = self._create_parameter_messages()
        terminals = self._create_terminals()
        serializer = XmlSerializer()

        channel = Parameters.Channel(0, terminals, message=messages)
        parameters = Parameters([channel])

        return serializer.render(parameters)

    def _create_parameter_messages(self) -> List[Parameters.Channel.Message]:
        """
        Create Message dataclasses to be flattened to parameters XML
        """
        return [self._create_parameter_message(message) for message in self.messages]

    def _create_parameter_message(self, message: types.Message) -> Parameters.Channel.Message:
        if isinstance(message, types.BC_RT_Message):
            return self._create_bcrt_message(message)

        elif isinstance(message, types.RT_BC_Message):
            return self._create_rtbc_message(message)

        elif isinstance(message, types.RT_RT_Message):
            return self._create_rtrt_message(message)

        elif isinstance(message, types.MC_Message):
            return self._create_mc_message(message)

        else:
            raise TypeError(f'{message.name}, type "{type(message)}", should be of type Message')

    def _create_bcrt_message(self, message: types.Message) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            message.terminal_address, message.sub_address, AddressDirection.RX
        )

        parameter_message = Parameters.Channel.Message(
            message.name, [address], MessageMessageType.BC_TO_RT, message.words
        )

        return parameter_message

    def _create_rtbc_message(self, message: types.Message) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            message.terminal_address, message.sub_address, AddressDirection.TX
        )

        parameter_message = Parameters.Channel.Message(
            message.name, [address], MessageMessageType.RT_TO_BC, message.words
        )

        return parameter_message

    def _create_rtrt_message(self, message: types.Message) -> Parameters.Channel.Message:
        address1 = Parameters.Channel.Message.Address(
            message.terminal_address1, message.sub_address1, AddressDirection.RX
        )

        address2 = Parameters.Channel.Message.Address(
            message.terminal_address2, message.sub_address2, AddressDirection.TX
        )

        parameter_message = Parameters.Channel.Message(
            message.name, [address1, address2], MessageMessageType.RT_TO_RT, message.words
        )

        return parameter_message

    def _create_mc_message(self, message: types.Message) -> Parameters.Channel.Message:
        mc_direction = (
            AddressDirection.RX
            if message.direction == types.MC_Direction.RX
            else AddressDirection.TX
        )

        address = Parameters.Channel.Message.Address(
            message.terminal_address, message.sub_address, mc_direction
        )

        parameter_message = Parameters.Channel.Message(
            message.name,
            [address],
            MessageMessageType.MC,
            message.words,
            mode_code=message.mode_code,
        )

        return parameter_message

    def _create_terminals(self) -> Parameters.Channel.Terminals:
        terminal_set = set([0])  # Start with BC for now
        for message in self.messages:
            terminal_set.update(message.list_terminals())

        # Create terminal object for every item in set
        terminals = [Parameters.Channel.Terminals.Terminal(terminal) for terminal in terminal_set]

        return Parameters.Channel.Terminals(terminals)


if __name__ == "__main__":
    from vs_1553_configurator.readers import Excel_1553_Reader
    import os
    import xml.dom.minidom

    # Get path to config file
    absolute_path = os.path.dirname(__file__)
    relative_path = "docs/example configurations/1553Config.xlsx"
    config_path = os.path.abspath(os.path.join(absolute_path, "..", relative_path))

    # Load config
    reader = Excel_1553_Reader()
    reader.load_configuration(config_path)

    # Translate config
    translator = BTI_1553_Translator(reader.messages)
    xml_string = translator.generate_parameters_xml()

    # Pretty print
    dom_xml = xml.dom.minidom.parseString(xml_string)
    print(dom_xml.toprettyxml())
