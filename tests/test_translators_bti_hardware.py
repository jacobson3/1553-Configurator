import vs_1553_configurator.types as types
from vs_1553_configurator.translators import BTI_1553_HardwareTranslator


def test_create_bcrt_message():
    message_name = "BC to RT1 (SA2)"
    terminal_address = 1
    sub_address = 2
    words = 4

    bcrt = types.BC_RT_Message(message_name, terminal_address, sub_address, words)
    translator = BTI_1553_HardwareTranslator([bcrt], [], [], [])
    hw_message, hw_message_buffer = translator._create_message(bcrt)

    assert hw_message.name == message_name
    assert hw_message.message_bcrt.word_count1 == words
    assert hw_message.message_bcrt.ta_val1 == terminal_address
    assert hw_message.message_bcrt.sa_val1 == sub_address

    assert hw_message.message_buffer_idref == hw_message_buffer.id


def test_create_rtbc_message():
    message_name = "RT15 to BC"
    terminal_address = 15
    sub_address = 6
    words = 4

    rtbc = types.RT_BC_Message(message_name, terminal_address, sub_address, words)
    translator = BTI_1553_HardwareTranslator([rtbc], [], [], [])
    hw_message, hw_message_buffer = translator._create_message(rtbc)

    assert hw_message.name == message_name
    assert hw_message.message_rtbc.word_count1 == words
    assert hw_message.message_rtbc.ta_val1 == terminal_address
    assert hw_message.message_rtbc.sa_val1 == sub_address

    assert hw_message.message_buffer_idref == hw_message_buffer.id


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
    translator = BTI_1553_HardwareTranslator([rtrt], [], [], [])
    hw_message, hw_message_buffer = translator._create_message(rtrt)

    assert hw_message.name == message_name
    assert hw_message.message_rtrt.word_count1 == words
    assert hw_message.message_rtrt.word_count2 == words
    assert hw_message.message_rtrt.ta_val1 == terminal_address1
    assert hw_message.message_rtrt.sa_val1 == sub_address1
    assert hw_message.message_rtrt.ta_val2 == terminal_address2
    assert hw_message.message_rtrt.sa_val2 == sub_address2

    assert hw_message.message_buffer_idref == hw_message_buffer.id


def test_create_mc_message():
    message_name = "MC 17"
    terminal_address = 1
    sub_address = 31
    words = 1
    mode_code = 17
    direction = types.MC_Direction.RX

    mc = types.MC_Message(message_name, terminal_address, sub_address, words, mode_code, direction)
    translator = BTI_1553_HardwareTranslator([mc], [], [], [])
    hw_message, hw_message_buffer = translator._create_message(mc)

    assert hw_message.name == message_name
    assert hw_message.message_mc.mode_code_number == mode_code
    assert hw_message.message_mc.direction.value == "Rx"
    assert hw_message.message_mc.sa_val1 == sub_address
    assert hw_message.message_mc.ta_val1 == terminal_address

    assert hw_message.message_buffer_idref == hw_message_buffer.id
