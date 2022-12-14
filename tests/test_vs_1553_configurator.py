from vs_1553_configurator import __version__
import vs_1553_configurator.builders as builders


def test_version():
    assert __version__ == "0.1.0"


def test_bcrt_message_build():
    message_name = "BC to RT1 (SA2)"
    terminal_address = 1
    sub_address = 2
    words = 4

    bcrt = builders.BC_RT_Message(message_name, terminal_address, sub_address, words)
    parameter_message = bcrt.create_parameter_message()

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "BC to RT"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_rtbc_message_build():
    message_name = "RT15 to BC"
    terminal_address = 15
    sub_address = 6
    words = 4

    bcrt = builders.RT_BC_Message(message_name, terminal_address, sub_address, words)
    parameter_message = bcrt.create_parameter_message()

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "RT to BC"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Tx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_rtrt_message_build():
    message_name = "RT1 to RT15"
    terminal_address1 = 15
    sub_address1 = 20
    terminal_address2 = 1
    sub_address2 = 20
    words = 4

    bcrt = builders.RT_RT_Message(
        message_name, terminal_address1, sub_address1, terminal_address2, sub_address2, words
    )
    parameter_message = bcrt.create_parameter_message()

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "RT to RT"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 2
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address1
    assert parameter_message.address[0].terminal_address == terminal_address1
    assert parameter_message.address[1].direction.value == "Tx"
    assert parameter_message.address[1].sub_address == sub_address2
    assert parameter_message.address[1].terminal_address == terminal_address2


def test_mc_message_build():
    message_name = "MC 17"
    terminal_address = 1
    sub_address = 31
    words = 1
    mode_code = 17
    direction = builders.MC_Direction.RX

    bcrt = builders.MC_Message(
        message_name, terminal_address, sub_address, words, mode_code, direction
    )
    parameter_message = bcrt.create_parameter_message()

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "MC"
    assert parameter_message.number_of_words == words
    assert parameter_message.mode_code == mode_code

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address
