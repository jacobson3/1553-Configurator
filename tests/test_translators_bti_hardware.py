import vs_1553_configurator.types as types
from vs_1553_configurator.translators import BTI_1553_HardwareTranslator


def test_create_bcrt_message():
    message_name = "BC to RT1 (SA2)"
    terminal_address = 1
    sub_address = 2
    words = 4

    bcrt = types.BC_RT_Message(message_name, terminal_address, sub_address, words)
    config = types.MIL_STD_1553_Config()
    config.messages = [bcrt]
    translator = BTI_1553_HardwareTranslator(config)
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
    config = types.MIL_STD_1553_Config()
    config.messages = [rtbc]
    translator = BTI_1553_HardwareTranslator(config)
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
    config = types.MIL_STD_1553_Config()
    config.messages = [rtrt]
    translator = BTI_1553_HardwareTranslator(config)
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
    config = types.MIL_STD_1553_Config()
    config.messages = [mc]
    translator = BTI_1553_HardwareTranslator(config)
    hw_message, hw_message_buffer = translator._create_message(mc)

    assert hw_message.name == message_name
    assert hw_message.message_mc.mode_code_number == mode_code
    assert hw_message.message_mc.direction.value == "Rx"
    assert hw_message.message_mc.sa_val1 == sub_address
    assert hw_message.message_mc.ta_val1 == terminal_address

    assert hw_message.message_buffer_idref == hw_message_buffer.id


def test_create_acyclic_frames():
    message_names = ["message1", "message2", "message3", "message4"]
    terminal_addresses = [0, 1, 15, 21]
    merged = tuple(zip(message_names, terminal_addresses))
    frame_name = "testFrame"
    schedule = message_names.copy()
    schedule.reverse()

    config = types.MIL_STD_1553_Config()

    config.messages = [types.BC_RT_Message(name, ta, 4, 4) for name, ta in merged]
    config.acyclic_frames = [types.AcyclicFrame(frame_name, schedule)]

    translator = BTI_1553_HardwareTranslator(config)
    messages, _ = translator._create_messages()
    acyclic_frames = translator._create_acyclic_frames(messages)

    messages.message_command

    test_frame = acyclic_frames.acyclic_frame[0]

    assert test_frame.name == frame_name

    message_ids = [x.id for x in messages.message_command]

    for ref in test_frame.command_message_ref:
        assert ref.message_idref in message_ids


def test_create_minor_frames():
    message_names = ["message1", "message2", "message3", "message4"]
    terminal_addresses = [0, 1, 15, 21]
    merged = tuple(zip(message_names, terminal_addresses))
    frame_name = "testFrame"
    frame_time = 100
    schedule = message_names.copy()
    schedule.reverse()

    config = types.MIL_STD_1553_Config()

    config.messages = [types.BC_RT_Message(name, ta, 4, 4) for name, ta in merged]
    config.minor_frames = [types.MinorFrame(frame_name, schedule, frame_time)]

    translator = BTI_1553_HardwareTranslator(config)
    messages, _ = translator._create_messages()
    minor_frames = translator._create_minor_frames(messages)

    test_frame = minor_frames.minor_frame[0]

    assert test_frame.name == frame_name
    assert test_frame.frame_time == frame_time

    message_ids = [x.id for x in messages.message_command]

    for ref in test_frame.command_message_ref:
        assert ref.message_idref in message_ids


def test_create_major_frames():
    message_names = ["message1", "message2", "message3", "message4"]
    terminal_addresses = [0, 1, 15, 21]
    merged = tuple(zip(message_names, terminal_addresses))
    frame_names = ["Frame1", "Frame2", "Frame3"]
    frame_time = 100
    major_name = "MajorFrame1"
    schedule = message_names.copy()
    schedule.reverse()

    config = types.MIL_STD_1553_Config()

    config.messages = [types.BC_RT_Message(name, ta, 4, 4) for name, ta in merged]
    config.minor_frames = [types.MinorFrame(name, schedule, frame_time) for name in frame_names]
    config.major_frames = [types.MajorFrame(major_name, frame_names)]

    translator = BTI_1553_HardwareTranslator(config)
    messages, _ = translator._create_messages()
    minor_frames = translator._create_minor_frames(messages)
    major_frames = translator._create_major_frames(minor_frames)

    test_frame = major_frames.major_frame[0]

    frame_ids = [x.id for x in minor_frames.minor_frame]

    for ref in test_frame.minor_frame_ref:
        assert ref.minor_frame_idref in frame_ids


if __name__ == "__main__":
    test_create_acyclic_frames()
