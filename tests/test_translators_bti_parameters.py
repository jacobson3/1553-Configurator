import vs_1553_configurator.types as types
from vs_1553_configurator.translators import BTI_1553_Translator


def test_create_parameter_bcrt():
    message_name = "BC to RT1 (SA2)"
    terminal_address = 1
    sub_address = 2
    words = 4

    bcrt = types.BC_RT_Message(message_name, terminal_address, sub_address, words)
    translator = BTI_1553_Translator([bcrt])
    parameter_messages = translator._create_parameter_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "BC to RT"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_parameter_rtbc():
    message_name = "RT15 to BC"
    terminal_address = 15
    sub_address = 6
    words = 4

    rtbc = types.RT_BC_Message(message_name, terminal_address, sub_address, words)
    translator = BTI_1553_Translator([rtbc])
    parameter_messages = translator._create_parameter_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "RT to BC"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Tx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_parameter_rtrt():
    message_name = "RT1 to RT15"
    terminal_address1 = 15
    sub_address1 = 20
    terminal_address2 = 1
    sub_address2 = 20
    words = 4

    rtrt = types.RT_RT_Message(
        message_name, terminal_address1, sub_address1, terminal_address2, sub_address2, words
    )
    translator = BTI_1553_Translator([rtrt])
    parameter_messages = translator._create_parameter_messages()
    parameter_message = parameter_messages[0]

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


def test_create_parameter_mc():
    message_name = "MC 17"
    terminal_address = 1
    sub_address = 31
    words = 1
    mode_code = 17
    direction = types.MC_Direction.RX

    mc = types.MC_Message(message_name, terminal_address, sub_address, words, mode_code, direction)
    translator = BTI_1553_Translator([mc])
    parameter_messages = translator._create_parameter_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "MC"
    assert parameter_message.number_of_words == words
    assert parameter_message.mode_code == mode_code

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_parameter_terminals():
    message_name = "RT15 to BC"
    terminal_addresses = [0, 1, 15, 21]
    sa = 6
    words = 4

    messages = [types.BC_RT_Message(message_name, ta, sa, words) for ta in terminal_addresses]
    translator = BTI_1553_Translator(messages)
    terminals = translator._create_parameter_terminals()

    terminals_created = [x.terminal_address for x in terminals.terminal]

    assert terminals_created.sort() == terminal_addresses.sort()
