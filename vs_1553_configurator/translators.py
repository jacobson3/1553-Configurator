from abc import ABC
from typing import List, Tuple
import vs_1553_configurator.types as types
from xsdata.formats.dataclass.serializers import XmlSerializer
from vs_1553_configurator.bti_1553_parameters import (
    Parameters,
    AddressDirection,
    MessageMessageType,
)
import vs_1553_configurator.bti_1553_hw as hw


class MIL_1553_Translator(ABC):
    def __init__(self, messages: List[types.Message]):
        self.messages = messages

    @property
    def messages(self) -> List[types.Message]:
        return self._messages

    @messages.setter
    def messages(self, messages: List[types.Message]):
        self._messages = messages


class BTI_1553_Translator(MIL_1553_Translator):
    def __init__(self, messages: List[types.Message]):
        super().__init__(messages)
        self.id = -1

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def generate_parameters_xml(self) -> str:
        """
        Returns XML string representing the VeriStand parameters XML for BTI 1553 hardware
        """
        messages = self._create_parameter_messages()
        terminals = self._create_parameter_terminals()
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
            return self._create_parameter_bcrt(message)

        elif isinstance(message, types.RT_BC_Message):
            return self._create_parameter_rtbc(message)

        elif isinstance(message, types.RT_RT_Message):
            return self._create_parameter_rtrt(message)

        elif isinstance(message, types.MC_Message):
            return self._create_parameter_mc(message)

        else:
            raise TypeError(f'{message.name}, type "{type(message)}", should be of type Message')

    def _create_parameter_bcrt(self, message: types.Message) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            message.terminal_address, message.sub_address, AddressDirection.RX
        )

        parameter_message = Parameters.Channel.Message(
            message.name, [address], MessageMessageType.BC_TO_RT, message.words
        )

        return parameter_message

    def _create_parameter_rtbc(self, message: types.Message) -> Parameters.Channel.Message:
        address = Parameters.Channel.Message.Address(
            message.terminal_address, message.sub_address, AddressDirection.TX
        )

        parameter_message = Parameters.Channel.Message(
            message.name, [address], MessageMessageType.RT_TO_BC, message.words
        )

        return parameter_message

    def _create_parameter_rtrt(self, message: types.Message) -> Parameters.Channel.Message:
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

    def _create_parameter_mc(self, message: types.Message) -> Parameters.Channel.Message:
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

    def _create_parameter_terminals(self) -> Parameters.Channel.Terminals:
        terminal_set = set([0])  # Start with BC for now
        for message in self.messages:
            terminal_set.update(message.list_terminals())

        # Create terminal object for every item in set
        terminals = [Parameters.Channel.Terminals.Terminal(terminal) for terminal in terminal_set]

        return Parameters.Channel.Terminals(terminals)

    def generate_hw_xml(self) -> str:
        """
        Returns XML string representing the VeriStand hardware XML for BTI 1553 hardware
        """
        core_id = self.get_uid()

        core_config = hw.CoreConfigurationType()
        simulation_1553 = hw.Simulation1553Type(bus_controller=self._create_hw_bus_controller())
        channel_1553 = hw.Channel1553Type(id=self.get_uid(), simulation=simulation_1553)

        core = hw.Core(
            core_configuration=core_config,
            channel1553=channel_1553,
            id=core_id,
            name="CoreName",
            schema_version=hw.SchemaVersionGroupSchemaVersion.VALUE_1_1,
        )

        serializer = XmlSerializer()

        return serializer.render(core, {"bti": hw.__NAMESPACE__})

    def get_uid(self) -> int:
        """
        Generate an ID that increases by 1 ever time function is called
        """
        self.id += 1
        return self.id

    def _create_hw_bus_controller(self) -> hw.BusController1553Type:
        schedule_id = self.get_uid()
        messages = []
        message_buffers = []

        # For each message generate bti message and buffer, add to respective list
        for message in self.messages:
            hw_message, hw_message_buffer = self._create_hw_message(message)
            messages.append(hw_message)
            message_buffers.append(hw_message_buffer)

        hw_message_buffers = hw.MessageBuffers1553Type(message_buffers)
        hw_messages = hw.Messages1553Type(messages)

        return hw.BusController1553Type(
            id=self.get_uid(),
            schedule_idref=schedule_id,
            messages=hw_messages,
            message_buffers=hw_message_buffers,
        )

    def _create_hw_message(
        self, message: types.Message
    ) -> Tuple[hw.Message1553Type, hw.MessageBuffers1553Type]:
        """
        Generate bti message and message buffer for given 1553 message
        """
        buffer_id = self.get_uid()

        if isinstance(message, types.BC_RT_Message):
            hw_message = self._create_hw_bcrt(message, buffer_id)
        elif isinstance(message, types.RT_BC_Message):
            hw_message = self._create_hw_rtbc(message, buffer_id)
        elif isinstance(message, types.RT_RT_Message):
            hw_message = self._create_hw_rtrt(message, buffer_id)
        elif isinstance(message, types.MC_Message):
            hw_message = self._create_hw_mc(message, buffer_id)
        else:
            raise TypeError(f'{message.name}, type "{type(message)}", should be of type Message')

        return (hw_message, self._create_hw_message_buffer(buffer_id))

    def _create_hw_bcrt(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        bcrt = hw.MessageBcrt1553Type(
            message.terminal_address,
            message.sub_address,
            message.words,
        )
        return hw.Message1553Type(
            message_bcrt=bcrt,
            id=self.get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_hw_rtbc(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        rtbc = hw.MessageRtbc1553Type(
            message.terminal_address,
            message.sub_address,
            message.words,
        )
        return hw.Message1553Type(
            message_rtbc=rtbc,
            id=self.get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_hw_rtrt(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        rtrt = hw.MessageRtrt1553Type(
            message.terminal_address1,
            message.sub_address1,
            message.words,
            message.terminal_address2,
            message.sub_address2,
            message.words,
        )
        return hw.Message1553Type(
            message_rtrt=rtrt,
            id=self.get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_hw_mc(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        mc_direction = (
            hw.ModeCode1553TypeDirection.RX
            if message.direction == types.MC_Direction.RX
            else hw.ModeCode1553TypeDirection.TX
        )

        mc = hw.MessageMc1553Type(
            message.terminal_address,
            message.sub_address,
            message.mode_code,
            mc_direction,
        )
        return hw.Message1553Type(
            message_mc=mc,
            id=self.get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_hw_message_buffer(self, id: int) -> hw.MessageBuffer1553Type:
        buffer_name = f"messageBuffer ID{id}"
        return hw.MessageBuffer1553Type(id=id, name=buffer_name)


if __name__ == "__main__":
    from vs_1553_configurator.readers import Excel_1553_Reader
    import os

    # import xml.dom.minidom

    # Get path to config file
    absolute_path = os.path.dirname(__file__)
    relative_path = "docs/example configurations/1553Config.xlsx"
    config_path = os.path.abspath(os.path.join(absolute_path, "..", relative_path))

    # Load config
    reader = Excel_1553_Reader()
    reader.load_configuration(config_path)

    # Translate config
    translator = BTI_1553_Translator(reader.messages)
    parameters_xml = translator.generate_parameters_xml()
    hw_xml = translator.generate_hw_xml()

    # Pretty print
    # dom_parameters = xml.dom.minidom.parseString(parameters_xml)
    # print(dom_parameters.toprettyxml())

    print(hw_xml)
