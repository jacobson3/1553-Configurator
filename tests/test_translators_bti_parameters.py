import vs_1553_configurator.types as types
from vs_1553_configurator.translators import BTI_1553_ParameterTranslator


def test_create_bcrt_message():
    message_name = "BC to RT1 (SA2)"
    terminal_address = 1
    sub_address = 2
    words = 4

    bcrt = types.BC_RT_Message(message_name, terminal_address, sub_address, words)
    config = types.MIL_STD_1553_Config()
    config.messages = [bcrt]
    translator = BTI_1553_ParameterTranslator(config)
    parameter_messages = translator._create_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "BC to RT"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_rtbc_message():
    message_name = "RT15 to BC"
    terminal_address = 15
    sub_address = 6
    words = 4

    rtbc = types.RT_BC_Message(message_name, terminal_address, sub_address, words)
    config = types.MIL_STD_1553_Config()
    config.messages = [rtbc]
    translator = BTI_1553_ParameterTranslator(config)
    parameter_messages = translator._create_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "RT to BC"
    assert parameter_message.number_of_words == words

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Tx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_rtrt_message():
    message_name = "RT1 to RT15"
    terminal_address1 = 15
    sub_address1 = 20
    terminal_address2 = 1
    sub_address2 = 20
    words = 4

    rtrt = types.RT_RT_Message(
        message_name, terminal_address1, sub_address1, terminal_address2, sub_address2, words
    )
    config = types.MIL_STD_1553_Config()
    config.messages = [rtrt]
    translator = BTI_1553_ParameterTranslator(config)
    parameter_messages = translator._create_messages()
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


def test_create_mc_message():
    message_name = "MC 17"
    terminal_address = 1
    sub_address = 31
    words = 1
    mode_code = 17
    direction = types.MC_Direction.RX

    mc = types.MC_Message(message_name, terminal_address, sub_address, words, mode_code, direction)
    config = types.MIL_STD_1553_Config()
    config.messages = [mc]
    translator = BTI_1553_ParameterTranslator(config)
    parameter_messages = translator._create_messages()
    parameter_message = parameter_messages[0]

    assert parameter_message.name == message_name
    assert parameter_message.message_type.value == "MC"
    assert parameter_message.number_of_words == words
    assert parameter_message.mode_code == mode_code

    assert len(parameter_message.address) == 1
    assert parameter_message.address[0].direction.value == "Rx"
    assert parameter_message.address[0].sub_address == sub_address
    assert parameter_message.address[0].terminal_address == terminal_address


def test_create_terminals():
    message_name = "RT15 to BC"
    terminal_addresses = [0, 1, 15, 21]
    sa = 6
    words = 4

    config = types.MIL_STD_1553_Config()
    config.messages = [
        types.BC_RT_Message(message_name, ta, sa, words) for ta in terminal_addresses
    ]
    translator = BTI_1553_ParameterTranslator(config)
    terminals = translator._create_terminals()

    terminals_created = [x.terminal_address for x in terminals.terminal]

    assert terminals_created.sort() == terminal_addresses.sort()


def test_create_acyclic_frames():
    schedule = ["message1", "message2", "message3", "message4"]
    frame_name = "testFrame"

    config = types.MIL_STD_1553_Config()
    config.acyclic_frames = [types.AcyclicFrame(frame_name, schedule)]

    translator = BTI_1553_ParameterTranslator(config)
    acyclic_frames = translator._create_acyclic_frames()

    assert acyclic_frames[0].name == frame_name
    assert acyclic_frames[0].create_trigger_channel is True
