from abc import ABC, abstractmethod
from typing import List
from enum import Enum
import pandas
import vs_1553_configurator.types as types


class MIL_1553_Reader(ABC):
    def __init__(self):
        self.messages = []

    @property
    def messages(self) -> List[types.Message]:
        return self._messages

    @messages.setter
    def messages(self, messages: List[types.Message]):
        self._messages = messages

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
    def __init__(self):
        super().__init__()

    def load_configuration(self, path: str):
        workbook = pandas.read_excel(path, [0, 1, 2])

        self.messages = self._sheet_to_messages(workbook[0])

    def _sheet_to_messages(self, sheet: pandas.DataFrame) -> None:
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

        return message_objects

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


if __name__ == "__main__":
    import os

    absolute_path = os.path.dirname(__file__)
    relative_path = "docs/example configurations/1553Config.xlsx"
    config_path = os.path.abspath(os.path.join(absolute_path, "..", relative_path))

    reader = Excel_1553_Reader()
    reader.load_configuration(config_path)
    print(len(reader.messages))
