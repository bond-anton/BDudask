from udask import ffi, lib, check_error

card_type = lib.USB_1902  # You can also use USB_1903 or USB_1901
card_num = 0

ai_count = 20480
u1902_timebase = 80000000.0  # 80 MHz
scan_interval = 1600  # Scan Interval: U1902_TIMEBASE/1600 = 20us (SI counter >= SI2 * channels number)
sample_interval = 1600  # Sample Interval: U1902_TIMEBASE/1600 = 20us (50 kHz) (SI2 counter)
sampling_rate = u1902_timebase / sample_interval

config_ctrl = lib.P1902_AI_PseudoDifferential | lib.P1902_AI_CONVSRC_INT
trig_ctrl = lib.P1902_AI_TRGMOD_POST | lib.P1902_AI_TRGSRC_SOFT
trigger_level = 0  # Ignore for P1902_AI_TRGSRC_SOFT
re_trigger_count = 0  # Ignore in Double Buffer Mode
delay_count = 0  # Ignore for P1902_AI_TRGSRC_SOFT


ai_read_count = ai_count
channel = 0
ad_range = lib.AD_B_10_V

# stopped = False
# half_ready = False
stopped = ffi.new('BOOLEAN *')
stopped[0] = False
half_ready = ffi.new('BOOLEAN *')
half_ready[0] = False

# access_cnt = 0
access_cnt = ffi.new('U32 *')
access_cnt[0] = 0
buf_idx = 0
# overrun_flag = 0
overrun_flag = ffi.new('U16 *')
overrun_flag[0] = 0
file_name = 'ai_data'

print('This sample performs infinite AI acquisition from AI Channel %d' % channel)
print('at %6.3f kHz sampling rate by Double buffer mode.' % (sampling_rate / 1e3))

card = lib.UD_Register_Card(card_type, card_num)
if card != card_num:
    print('ERROR:', check_error(card)['description'])
    exit(1)
print('Registered card:', card)

print('Configure AI')
err = lib.UD_AI_1902_Config(card, config_ctrl, trig_ctrl, trigger_level, re_trigger_count, delay_count)
if err < 0:
    print('ERROR:', check_error(err)['description'])
    lib.UD_Release_Card(card)
    exit(1)

print('Set Scan and Sampling Rate')
err = lib.UD_AI_1902_CounterInterval(card, scan_interval, sample_interval)
if err < 0:
    print('ERROR:', check_error(err)['description'])
    lib.UD_Release_Card(card)
    exit(1)

print('Enable Double Buffer Mode')
err = lib.UD_AI_AsyncDblBufferMode(card, 1)  # double-buffer mode
if err < 0:
    print('ERROR:', check_error(err)['description'])
    lib.UD_Release_Card(card)
    exit(1)

print('AI Acquisition Start')
err = lib.UD_AI_ContReadChannelToFile(card, channel, ad_range, bytes(file_name, 'utf-8'),
                                      ai_read_count, sampling_rate, lib.ASYNCH_OP)
# err = lib.UD_AI_ContReadMultiChannelsToFile(card, channels_number, chanels, ad_ranges, bytes(file_name, 'utf-8'),
#                                             ai_read_count, sampling_rate, lib.ASYNCH_OP)
if err < 0:
    print('ERROR:', check_error(err)['description'])
    lib.UD_Release_Card(card)
    exit(1)

print('\nAI Infinite Acquisition is started...\n')
try:
    while True:
        # Check Buffer Ready
        err = lib.UD_AI_AsyncDblBufferHalfReady(card, half_ready, stopped)
        if err < 0:
            print('ERROR:', check_error(err)['description'])
            lib.UD_AI_AsyncClear(card, access_cnt)
            lib.UD_Release_Card(card)
            exit(1)

        if half_ready[0]:
            if buf_idx == 0:
                # The acquired AI data are stored in buffer 0,
                # You can process the data of buffer 0 in HERE if you need.
                print('Buffer0 Half Ready...')
                print('Write %d samples of Buffer0 to %s.dat file...' % ((ai_read_count / 2), file_name))
                lib.UD_AI_AsyncDblBufferToFile(card)
                lib.UD_AI_AsyncDblBufferOverrun(card, 0, overrun_flag)
                if overrun_flag[0]:
                    print('OVERRUN...')
                    lib.UD_AI_AsyncDblBufferOverrun(card, 1, overrun_flag)
                buf_idx = 1
                print('                              Press Enter to stop...\n')
            else:
                # The acquired AI data are stored in buffer 1,
                # You can process the data of buffer 1 in HERE if you need.
                print('Buffer1 Half Ready...')
                print('Write %d samples of Buffer1 to %s.dat file...' % ((ai_read_count / 2), file_name))
                lib.UD_AI_AsyncDblBufferToFile(card)
                lib.UD_AI_AsyncDblBufferOverrun(card, 0, overrun_flag)
                if overrun_flag[0]:
                    print('OVERRUN...')
                    lib.UD_AI_AsyncDblBufferOverrun(card, 1, overrun_flag)
                buf_idx = 0
                print('                              Press Enter to stop...\n')
except KeyboardInterrupt:
    pass

print('Clear AI Setting and Get Remaining data')
err = lib.UD_AI_AsyncClear(card, access_cnt)
if err < 0:
    print('ERROR:', check_error(err)['description'])
    lib.UD_AI_AsyncClear(card, access_cnt)
    lib.UD_Release_Card(card)
    exit(1)

card = lib.UD_Release_Card(card)
if card < 0:
    print('ERROR:', check_error(card)['description'])
    exit(1)
print('Released card:', card)
