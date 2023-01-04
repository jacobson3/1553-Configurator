from abc import ABC, abstractmethod
from typing import List
from enum import Enum
import pandas
import vs_1553_configurator.types as types


class MIL_1553_Reader(ABC):
    def __init__(self, config_path: str):
        self.messages = []
        self.major_frames = []
        self.minor_frames = []
        self.acyclic_frames = []
        self.load_configuration(config_path)

    @property
    def messages(self) -> List[types.Message]:
        """
        Defines 1553 message (BC-RT | RT-BC | RT-RT | MC)
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[types.Message]):
        self._messages = messages

    @property
    def major_frames(self) -> List[types.MajorFrame]:
        """
        Specifies a schedule that can be referenced by the channel for execution
        """
        return self._major_frames

    @major_frames.setter
    def major_frames(self, frames: List[types.MajorFrame]):
        self._major_frames = frames

    @property
    def minor_frames(self) -> List[types.MinorFrame]:
        """
        A schedule of commands and messages that can be referenced in a majorFrame
        """
        return self._minor_frames

    @minor_frames.setter
    def minor_frames(self, frames: List[types.MinorFrame]):
        self._minor_frames = frames

    @property
    def acyclic_frames(self) -> List[types.AcyclicFrame]:
        """
        A schedule of commands and messages that can be transmitted on-demand
        """
        return self._acyclic_frames

    @acyclic_frames.setter
    def acyclic_frames(self, frames: List[types.AcyclicFrame]):
        self._acyclic_frames = frames

    @abstractmethod
    def load_configuration(self, path: str):
        """
        Read input configuration file and generate the appropriate intermediate types
        """
        pass


class Excel_Message_Type(str, Enum):
    BCRT = "BC-RT"
    RTBC = "RT-BC"
    RTRT = "RT-RT"
    MC = "MC"


class Excel_1553_Reader(MIL_1553_Reader):
    def __init__(self, config_path: str):
        super().__init__(config_path)

    def load_configuration(self, path: str):
        workbook = pandas.read_excel(path, [0, 1, 2])

        self._sheet_to_messages(workbook[0])
        self._sheet_to_frames(workbook[2])

    def _sheet_to_messages(self, sheet: pandas.DataFrame) -> None:
        """
        Converts Excel sheet to messages, writes messages to class data
        """
        messages = sheet.set_index("name").to_dict("index")

        message_objects = []
        # Iterate through rows in Excel configuration
        for message_name in messages:
            message_type = messages[message_name].get("messageType")
            message_data = messages[message_name]

            # Create message and add it to list of messages
            if message_type == Excel_Message_Type.BCRT:
                message_objects.append(self._create_bcrt_message(message_name, message_data))
            elif message_type == Excel_Message_Type.RTBC:
                message_objects.append(self._create_rtbc_message(message_name, message_data))
            elif message_type == Excel_Message_Type.RTRT:
                message_objects.append(self._create_rtrt_message(message_name, message_data))
            elif message_type == Excel_Message_Type.MC:
                message_objects.append(self._create_mc_message(message_name, message_data))
            else:
                raise TypeError(f"Unknown message type: {message_type}")

        self.messages = message_objects

    def _create_bcrt_message(self, message_name: str, message_data: dict) -> types.Message:
        terminal_address = message_data.get("terminalAddress1")
        sub_address = message_data.get("subAddress1")
        words = message_data.get("words")

        return types.BC_RT_Message(message_name, terminal_address, sub_address, words)

    def _create_rtbc_message(self, message_name: str, message_data: dict) -> types.Message:
        terminal_address = message_data.get("terminalAddress1")
        sub_address = message_data.get("subAddress1")
        words = message_data.get("words")

        return types.RT_BC_Message(message_name, terminal_address, sub_address, words)

    def _create_rtrt_message(self, message_name: str, message_data: dict) -> types.Message:
        terminal_address1 = message_data.get("terminalAddress1")
        sub_address1 = message_data.get("subAddress1")
        terminal_address2 = message_data.get("terminalAddress2")
        sub_address2 = message_data.get("subAddress2")
        words = message_data.get("words")

        return types.RT_RT_Message(
            message_name, terminal_address1, sub_address1, terminal_address2, sub_address2, words
        )

    def _create_mc_message(self, message_name: str, message_data: dict) -> types.Message:
        terminal_address = message_data.get("terminalAddress1")
        sub_address = message_data.get("subAddress1")
        words = message_data.get("words")
        mode_code = message_data.get("MC")
        direction = message_data.get("MCDirection")

        return types.MC_Message(
            message_name, terminal_address, sub_address, words, mode_code, direction
        )

    def _sheet_to_frames(self, sheet: pandas.DataFrame) -> None:
        """
        Converts Excel sheet to frames, writes to acyclic, major, and minor frame class data
        """
        frames_list = sheet.to_dict()

        for frame_name in frames_list:
            frame_time = frames_list.get(frame_name).get(0)
            schedule = self._get_schedule(frames_list.get(frame_name))

            if pandas.isnull(frame_time):
                self.major_frames.append(self._create_major_frame(frame_name, schedule))
            elif frame_time == -1:
                self.acyclic_frames.append(self._create_acyclic_frame(frame_name, schedule))
            else:
                self.minor_frames.append(self._create_minor_frame(frame_name, schedule, frame_time))

    def _get_schedule(self, frame_dict: dict) -> List[str]:
        return [
            frame_dict.get(i)
            for i in range(1, len(frame_dict))
            if not pandas.isnull(frame_dict.get(i))
        ]

    def _create_major_frame(self, frame_name: str, schedule: List[str]) -> types.MajorFrame:
        return types.MajorFrame(frame_name, schedule)

    def _create_minor_frame(
        self,
        frame_name: str,
        schedule: List[str],
        frame_time: int,
    ) -> types.MinorFrame:
        return types.MinorFrame(frame_name, schedule, frame_time)

    def _create_acyclic_frame(self, frame_name: str, schedule: List[str]) -> types.AcyclicFrame:
        return types.AcyclicFrame(frame_name, schedule)


if __name__ == "__main__":
    import os

    absolute_path = os.path.dirname(__file__)
    relative_path = "docs/example configurations/1553Config.xlsx"
    config_path = os.path.abspath(os.path.join(absolute_path, "..", relative_path))

    reader = Excel_1553_Reader(config_path)
