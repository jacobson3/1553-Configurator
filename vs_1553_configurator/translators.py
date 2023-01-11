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
    """
    Abstract class responsible for transforming data objects into config files
    """

    def __init__(self, configuration: types.MIL_STD_1553_Config):
        self.messages = configuration.messages
        self.major_frames = configuration.major_frames
        self.minor_frames = configuration.minor_frames
        self.acyclic_frames = configuration.acyclic_frames

    @property
    def messages(self) -> List[types.Message]:
        """
        List of 1553 messages (BCRT | RTBC | RTRT | MC)
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[types.Message]):
        self._messages = messages

    @property
    def major_frames(self) -> List[types.MajorFrame]:
        """ "
        List of major frames, each major frame containts a list of minor frames to be executed
        """
        return self._major_frames

    @major_frames.setter
    def major_frames(self, frames: List[types.MajorFrame]):
        self._major_frames = frames

    @property
    def minor_frames(self) -> List[types.MinorFrame]:
        """
        List of minor frames, each minor frame contains a list of messages
        to be executed periodically
        """
        return self._minor_frames

    @minor_frames.setter
    def minor_frames(self, frames: List[types.MinorFrame]):
        self._minor_frames = frames

    @property
    def acyclic_frames(self) -> List[types.AcyclicFrame]:
        """
        List of acyclic frames, each acyclic frame contains a list of messages to be executed
        """
        return self._acyclic_frames

    @acyclic_frames.setter
    def acyclic_frames(self, frames: List[types.AcyclicFrame]):
        self._acyclic_frames = frames


class BTI_1553_ParameterTranslator(MIL_1553_Translator):
    """
    Generates parameter XML file from config data used by VeriStand to control BTI 1553 hardware
    """

    def __init__(self, config: types.MIL_STD_1553_Config):
        super().__init__(config)
        self.id = -1

    @property
    def id(self) -> int:
        """
        Counter used to generate incrementing unique ids
        """
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def generate_parameters_xml(self) -> str:
        """
        Returns XML string representing the VeriStand parameters XML for BTI 1553 hardware
        """
        messages = self._create_messages()
        terminals = self._create_terminals()
        acyclic_frames = self._create_acyclic_frames()
        serializer = XmlSerializer()

        channel = Parameters.Channel(0, terminals, acyclic_frames, messages)
        parameters = Parameters([channel])

        return serializer.render(parameters)

    def _create_messages(self) -> List[Parameters.Channel.Message]:
        """
        Create Message dataclasses to be flattened to parameters XML
        """
        return [self._create_message(message) for message in self.messages]

    def _create_message(self, message: types.Message) -> Parameters.Channel.Message:
        """
        Returns BTI specific message object generated from input message data object
        """

        # Create message of specific type depending on incoming mesage type
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
        """
        Create terminal data objects to be flattened to XML
        """
        terminal_set = set([0])  # Always include BC

        # Add any terminal address to set if it is referenced in a message
        for message in self.messages:
            terminal_set.update(message.list_terminals())

        # Create terminal object for every item in set
        terminals = [Parameters.Channel.Terminals.Terminal(terminal) for terminal in terminal_set]

        return Parameters.Channel.Terminals(terminals)

    def _create_acyclic_frames(self) -> List[Parameters.Channel.AcyclicFrame]:
        """
        Create acyclic frame data objects to be flattened to XML
        """
        return [Parameters.Channel.AcyclicFrame(name=frame.name) for frame in self.acyclic_frames]


class BTI_1553_HardwareTranslator(MIL_1553_Translator):
    """
    Generates hardware XML file from config data used by VeriStand to control BTI 1553 hardware
    """

    def __init__(self, config: types.MIL_STD_1553_Config):
        super().__init__(config)
        self.id = -1

    @property
    def id(self) -> int:
        """
        Counter used to generate incrementing unique ids
        """
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def generate_hw_xml(self) -> str:
        """
        Returns XML string representing the VeriStand hardware XML for BTI 1553 hardware
        """

        # Create Bus Controller and all Remote Terminals
        bus_controller = self._create_bus_controller()
        remote_terminals = self._create_remote_terminals_type()

        # Wrap up 1553 BC and RTs into BTI hardware objects
        simulation_1553 = hw.Simulation1553Type(
            bus_controller=bus_controller, remote_terminals=remote_terminals
        )
        channel_1553 = hw.Channel1553Type(id=self._get_uid(), simulation=simulation_1553)

        core_id = self._get_uid()
        core_config = hw.CoreConfigurationType()
        core = hw.Core(
            core_configuration=core_config,
            channel1553=channel_1553,
            id=core_id,
            name="CoreName",
            schema_version=hw.SchemaVersionGroupSchemaVersion.VALUE_1_1,
        )

        # Generates and returns XML string from previously created data objects
        serializer = XmlSerializer()
        return serializer.render(core, {"bti": hw.__NAMESPACE__})

    def _get_uid(self) -> int:
        """
        Generate an ID that increases by 1 ever time function is called
        """
        self.id += 1
        return self.id

    def _create_bus_controller(self) -> hw.BusController1553Type:
        """
        Returns data object representing the Bus Controller defined by this class's data
        """
        id = self._get_uid()

        messages, message_buffers = self._create_messages()
        acyclic_frames = self._create_acyclic_frames(messages)
        minor_frames = self._create_minor_frames(messages)
        major_frames = self._create_major_frames(minor_frames)

        return hw.BusController1553Type(
            message_buffers,
            messages,
            minor_frames,
            major_frames,
            acyclic_frames,
            id=id,
            schedule_idref=major_frames.major_frame[0].id,  # VeriStand can only use 1 major frame
        )

    def _create_messages(
        self,
    ) -> Tuple[hw.Messages1553Type, hw.MessageBuffers1553Type]:
        """
        Returns both message and message buffer objects.
        Each message has a corresponding message buffer.
        """

        messages = []
        message_buffers = []

        # For each message generate bti message and buffer, add to respective list
        for message in self.messages:
            hw_message, hw_message_buffer = self._create_message(message)

            messages.append(hw_message)
            message_buffers.append(hw_message_buffer)

        # Wrap lists into BTI specific list objects
        hw_messages = hw.Messages1553Type(messages)
        hw_message_buffers = hw.MessageBuffers1553Type(message_buffers)

        return (hw_messages, hw_message_buffers)

    def _create_message(
        self, message: types.Message
    ) -> Tuple[hw.Message1553Type, hw.MessageBuffer1553Type]:
        """
        Generate bti message and message buffer for given 1553 message
        """
        buffer_id = self._get_uid()

        # Function called depends on incoming message type
        if isinstance(message, types.BC_RT_Message):
            hw_message = self._create_bcrt_message(message, buffer_id)
        elif isinstance(message, types.RT_BC_Message):
            hw_message = self._create_rtbc_message(message, buffer_id)
        elif isinstance(message, types.RT_RT_Message):
            hw_message = self._create_rtrt_message(message, buffer_id)
        elif isinstance(message, types.MC_Message):
            hw_message = self._create_mc_message(message, buffer_id)
        else:
            raise TypeError(f'{message.name}, type "{type(message)}", should be of type Message')

        return (hw_message, self._create_message_buffer(buffer_id))

    def _create_bcrt_message(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        bcrt = hw.MessageBcrt1553Type(
            message.terminal_address,
            message.sub_address,
            message.words,
        )
        return hw.Message1553Type(
            message_bcrt=bcrt,
            id=self._get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_rtbc_message(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
        rtbc = hw.MessageRtbc1553Type(
            message.terminal_address,
            message.sub_address,
            message.words,
        )
        return hw.Message1553Type(
            message_rtbc=rtbc,
            id=self._get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_rtrt_message(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
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
            id=self._get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_mc_message(self, message: types.Message, buffer_id: int) -> hw.Message1553Type:
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
            id=self._get_uid(),
            name=message.name,
            message_buffer_idref=buffer_id,
        )

    def _create_message_buffer(self, id: int) -> hw.MessageBuffer1553Type:
        buffer_name = f"messageBuffer ID{id}"
        return hw.MessageBuffer1553Type(id=id, name=buffer_name)

    def _create_acyclic_frames(self, messages: hw.Messages1553Type) -> hw.AcyclicFrames1553Type:

        acyclic_frames = [
            self._create_acyclic_frame(frame, messages) for frame in self.acyclic_frames
        ]

        return hw.AcyclicFrames1553Type(acyclic_frames)

    def _create_acyclic_frame(
        self,
        frame: types.AcyclicFrame,
        messages: hw.Messages1553Type,
    ) -> hw.AcyclicFrame1553Type:

        # Convert list of message names into list of corresponding message ids
        message_ids = [self._get_message_id(name, messages) for name in frame.schedule]

        message_refs = [hw.SchedMessageRef1553Type(id) for id in message_ids]

        return hw.AcyclicFrame1553Type(message_refs, id=self._get_uid(), name=frame.name)

    def _get_message_id(self, name: str, messages: hw.Messages1553Type) -> int:
        """
        Returns ID of the message with name matching the name input parameter
        """
        filtered_messages = list(filter(lambda x: (x.name == name), messages.message_command))

        if filtered_messages[0] is None:
            raise BaseException(f'Frame references message with name "{name}" which was not found')
        else:
            return filtered_messages[0].id

    def _create_minor_frames(self, messages: hw.Messages1553Type) -> hw.MinorFrames1553Type:

        minor_frames = [self._create_minor_frame(frame, messages) for frame in self.minor_frames]

        return hw.MinorFrames1553Type(minor_frames)

    def _create_minor_frame(
        self,
        frame: types.MinorFrame,
        messages: hw.Messages1553Type,
    ) -> hw.MinorFrame1553Type:

        # Convert list of message names into list of corresponding message ids
        message_ids = [self._get_message_id(name, messages) for name in frame.schedule]

        message_refs = [hw.SchedMessageRef1553Type(id) for id in message_ids]

        return hw.MinorFrame1553Type(
            message_refs, id=self._get_uid(), name=frame.name, frame_time=frame.frame_time
        )

    def _create_major_frames(self, frames: hw.MinorFrames1553Type) -> hw.MajorFrames1553Type:
        scheduled_frame = self.major_frames[0]  # VS only allows for one running major frame

        frame_refs = self._get_frame_refs(scheduled_frame.schedule, frames)

        major_frame = hw.MajorFrame1553Type(frame_refs, self._get_uid(), scheduled_frame.name, 0)

        return hw.MajorFrames1553Type([major_frame])

    def _get_frame_refs(
        self, schedule: List[str], frames: hw.MinorFrames1553Type
    ) -> List[hw.MinorFrameRef1553Type]:

        frame_refs = []

        for name in schedule:
            filtered_frames = list(filter(lambda x: (x.name == name), frames.minor_frame))

            if filtered_frames[0] is None:
                raise BaseException(
                    f'Frame references message with name "{name}" which was not found'
                )
            else:
                frame_refs.append(hw.MinorFrameRef1553Type(filtered_frames[0].id))

        return frame_refs

    def _create_remote_terminals_type(self) -> hw.RemoteTerminals1553Type:

        # Gather set of all terminal addresses referenced in messages
        message_terminals = [message.list_terminals() for message in self.messages]
        terminals = set().union(*message_terminals)

        remote_terminals = [self._create_remote_terminal(ta) for ta in terminals]

        return hw.RemoteTerminals1553Type(remote_terminals)

    def _create_remote_terminal(self, terminal_address: int) -> hw.RemoteTerminal1553Type:

        message_buffers = []
        sub_addresses = []
        mode_codes = []

        # Filter messages to only include ones with relevant terminal addresses
        filtered_messages = list(
            filter(lambda x: (terminal_address in x.list_terminals()), self.messages)
        )

        # Create messages with MC message being separated from BCRT, RTBC, and RTRT messages
        for message in filtered_messages:
            buffer_id = self._get_uid()
            message_buffers.append(self._create_message_buffer(buffer_id))

            if isinstance(message, types.MC_Message):
                mode_code = self._create_rt_mode_code(message, buffer_id)
                mode_codes.append(mode_code)
            else:
                sub_address = self._create_sub_address(message, terminal_address, buffer_id)
                sub_addresses.append(sub_address)

        return hw.RemoteTerminal1553Type(
            hw.MessageBuffers1553Type(message_buffers),
            sub_addresses,
            mode_codes,
            id=self._get_uid(),
            name=f"RT{terminal_address}",
            rt_address=terminal_address,
        )

    def _create_rt_mode_code(
        self, message: types.MC_Message, buffer_id: int
    ) -> hw.ModeCode1553Type:
        direction = (
            hw.ModeCode1553TypeDirection.RX
            if message.direction == types.MC_Direction.RX
            else hw.ModeCode1553TypeDirection.TX
        )

        mode_code = hw.ModeCode1553Type(
            self._get_uid(),
            f"MC{message.mode_code}",
            message_buffer_idref=buffer_id,
            mode_code_number=message.mode_code,
            direction=direction,
        )

        return mode_code

    def _create_sub_address(
        self, message: types.Message, terminal_address: int, buffer_id: int
    ) -> hw.SubAddress1553Type:

        if isinstance(message, types.BC_RT_Message):
            sub_address = hw.SubAddress1553Type(
                self._get_uid(),
                f"SA{message.sub_address}",
                message_buffer_idref=buffer_id,
                sub_address=message.sub_address,
                direction=hw.SubAddress1553TypeDirection.RX,
            )
        elif isinstance(message, types.RT_BC_Message):
            sub_address = hw.SubAddress1553Type(
                self._get_uid(),
                f"SA{message.sub_address}",
                message_buffer_idref=buffer_id,
                sub_address=message.sub_address,
                direction=hw.SubAddress1553TypeDirection.TX,
            )
        else:  # RTRT message
            if message.terminal_address1 == terminal_address:
                address = message.sub_address1
                direction = hw.SubAddress1553TypeDirection.RX
            else:
                address = message.sub_address2
                direction = hw.SubAddress1553TypeDirection.TX

            sub_address = hw.SubAddress1553Type(
                self._get_uid(),
                f"SA{address}",
                message_buffer_idref=buffer_id,
                sub_address=address,
                direction=direction,
            )

        return sub_address


if __name__ == "__main__":
    from vs_1553_configurator.readers import Excel_1553_Reader
    import os
    import sys
    import xml.dom.minidom

    # Get path to config file
    absolute_path = os.path.dirname(__file__)
    relative_path = "docs/example configurations/1553Config.xlsx"
    config_path = os.path.abspath(os.path.join(absolute_path, "..", relative_path))

    # Load config
    reader = Excel_1553_Reader(config_path)

    # Translate configs
    parameter_translator = BTI_1553_ParameterTranslator(reader.config)
    hw_translator = BTI_1553_HardwareTranslator(reader.config)

    parameters_xml = parameter_translator.generate_parameters_xml()
    hw_xml = hw_translator.generate_hw_xml()

    # Pretty print
    dom_parameters = xml.dom.minidom.parseString(parameters_xml)
    sys.stdout.write(dom_parameters.toprettyxml())

    print("")

    dom_hw = xml.dom.minidom.parseString(hw_xml)
    sys.stdout.write(dom_hw.toprettyxml())
