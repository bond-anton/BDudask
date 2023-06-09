from cffi import FFI


builder = FFI()

builder.cdef(
    '''
    /*
    * Signal number used in DASK
    */
    #define SIGEVENT1 61
    #define SIGEVENT2 62
    #define SIGEVENT3 60
    #define SIGEVENT4 59
    
    
    /*
     * DASK Data Types
     */
    
    typedef uint8_t            U8;
    typedef int16_t            I16;
    typedef uint16_t           U16;
    typedef int32_t            I32;
    typedef uint32_t           U32;
    typedef int64_t            I64;
    typedef uint64_t           U64;
    typedef float              F32;
    typedef double             F64;
    typedef enum{FALSE, TRUE} BOOLEAN;
    
    /*
     * ADLink USB Module Type
     */
    #define USB_1902      1
    #define USB_1903      2
    #define USB_1901      3
    #define USB_2401      4
    #define USB_7250      5
    #define USB_7230      6
    #define USB_2405      7
    #define USB_1210      8
    #define NUM_USBDAQ_TYPE 9 // the last device-type + 1
    
    #define MAX_CARD       32
    
    
    /*
     * Error Number
     */
    #define NoError                     0
    #define ErrorUnknownCardType       -1
    #define ErrorInvalidCardNumber     -2
    #define ErrorTooManyCardRegistered -3
    #define ErrorCardNotRegistered     -4
    #define ErrorFuncNotSupport        -5
    #define ErrorInvalidIoChannel      -6
    #define ErrorInvalidAdRange        -7
    #define ErrorContIoNotAllowed      -8
    #define ErrorDiffRangeNotSupport   -9
    #define ErrorLastChannelNotZero    -10
    #define ErrorChannelNotDescending  -11
    #define ErrorChannelNotAscending   -12
    #define ErrorOpenDriverFailed      -13
    #define ErrorOpenEventFailed       -14
    #define ErrorTransferCountTooLarge -15
    #define ErrorNotDoubleBufferMode   -16
    #define ErrorInvalidSampleRate     -17
    #define ErrorInvalidCounterMode    -18
    #define ErrorInvalidCounter        -19
    #define ErrorInvalidCounterState   -20
    #define ErrorInvalidBinBcdParam    -21
    #define ErrorBadCardType           -22
    #define ErrorInvalidDaRefVoltage   -23
    #define ErrorAdTimeOut             -24
    #define ErrorNoAsyncAI             -25
    #define ErrorNoAsyncAO             -26
    #define ErrorNoAsyncDI             -27
    #define ErrorNoAsyncDO             -28
    #define ErrorNotInputPort          -29
    #define ErrorNotOutputPort         -30
    #define ErrorInvalidDioPort        -31
    #define ErrorInvalidDioLine        -32
    #define ErrorContIoActive          -33
    #define ErrorDblBufModeNotAllowed  -34
    #define ErrorConfigFailed          -35
    #define ErrorInvalidPortDirection  -36
    #define ErrorBeginThreadError      -37
    #define ErrorInvalidPortWidth      -38
    #define ErrorInvalidCtrSource      -39
    #define ErrorOpenFile              -40
    #define ErrorAllocateMemory        -41
    #define ErrorDaVoltageOutOfRange   -42
    #define ErrorLockMemory            -43
    #define ErrorDIODataWidthError     -44
    #define ErrorTaskCodeError         -45
    #define ErrortriggercountError     -46
    #define ErrorInvalidTriggerMode    -47
    #define ErrorInvalidTriggerType    -48
    #define ErrorInvalidCounterValue   -50
    #define ErrorInvalidEventHandle    -60
    #define ErrorNoMessageAvailable    -61
    #define ErrorEventMessgaeNotAdded  -62
    #define ErrorCalibrationTimeOut    -63
    #define ErrorUndefinedParameter    -64
    #define ErrorInvalidBufferID       -65
    #define ErrorInvalidSampledClock   -66
    #define ErrorInvalidOperationMode  -67
    
    
    /*Error number for driver API*/
    #define ErrorConfigIoctl              -201
    #define ErrorAsyncSetIoctl            -202
    #define ErrorDBSetIoctl               -203
    #define ErrorDBHalfReadyIoctl         -204
    #define ErrorContOPIoctl              -205
    #define ErrorContStatusIoctl          -206
    #define ErrorPIOIoctl                 -207
    #define ErrorDIntSetIoctl             -208
    #define ErrorWaitEvtIoctl             -209
    #define ErrorOpenEvtIoctl             -210
    #define ErrorCOSIntSetIoctl           -211
    #define ErrorMemMapIoctl              -212
    #define ErrorMemUMapSetIoctl          -213
    #define ErrorCTRIoctl                 -214
    #define ErrorGetResIoctl              -215
    #define ErrorCalIoctl                 -216
    #define ErrorPMIntSetIoctl            -217
    
    // Jeff added
    #define ErrorAccessViolationDataCopy  -301
    #define ErrorNoModuleFound            -302
    #define ErrorCardIDDuplicated         -303
    #define ErrorCardDisconnected         -304
    #define ErrorInvalidScannedIndex      -305
    #define ErrorUndefinedException       -306
    #define ErrorInvalidDioConfig         -307
    #define ErrorInvalidAOCfgCtrl         -308
    #define ErrorInvalidAOTrigCtrl        -309
    #define ErrorConflictWithSyncMode     -310
    #define ErrorConflictWithFifoMode     -311
    #define ErrorInvalidAOIteration       -312
    #define ErrorZeroChannelNumber        -313
    #define ErrorSystemCallFailed         -314
    #define ErrorTimeoutFromSyncMode      -315
    #define ErrorInvalidPulseCount        -316
    #define ErrorInvalidDelayCount        -317
    #define ErrorConflictWithDelay2       -318
    #define ErrorAOFifoCountTooLarge      -319
    #define ErrorConflictWithWaveRepeat   -320
    #define ErrorConflictWithReTrig       -321
    #define ErrorInvalidTriggerChannel    -322
    #define ErrorInvalidInputSignal       -323
    #define ErrorInvalidConversionSrc     -324
    #define ErrorInvalidRefVoltage        -325
    #define ErrorCalibrateFailed          -326
    #define ErrorInvalidCalData           -327
    #define ErrorChanGainQueueTooLarge    -328
    #define ErrorInvalidCardType          -329
    #define ErrorInvalidSyncMode          -330
    #define ErrorIICVersion               -331
    #define ErrorFX2UpgradeFailed         -332
    #define ErrorInvalidReadCount         -333
    #define ErrorTEDSInvalidSensorNo      -334
    #define ErroeTEDSAccessTimeout        -335
    #define ErrorTEDSChecksumFailed       -336
    #define ErrorTEDSNotIEEE1451_4        -337
    #define ErrorTEDSInvalidTemplateID    -338
    #define ErrorTEDSInvalidPrecisionValue -339
    #define ErrorTEDSUnsupportedTemplate  -340
    #define ErrorTEDSInvalidPropertyID    -341
    #define ErrorTEDSNoRawData            -342
    
    #define ErrorInvalidChannel           -397
    #define ErrorNullPoint                -398
    #define ErrorInvalidParamSetting      -399
    
    // -401 ~ -499 the Kernel error
    #define ErrorAIStartFailed            -401
    #define ErrorAOStartFailed            -402
    #define ErrorConflictWithGPIOConfig   -403
    #define ErrorEepromReadback           -404
    #define ErrorConflictWithInfiniteOp   -405
    #define ErrorWaitingUSBHostResponse   -406
    #define ErrorAOFifoModeTimeout        -407
    #define ErrorInvalidModuleFunction    -408
    #define ErrorAdFifoFull               -409
    #define ErrorInvalidTransferCount     -410
    #define ErrorConflictWithAIConfig     -411
    #define ErrorDDSConfigFailed          -412
    #define ErrorFpgaAccessFailed         -413
    #define ErrorPLDBusy                  -414
    #define ErrorPLDTimeout               -415
    
    #define ErrorUndefinedKernelError     -420
    
    
    
    // the functions supported in the future
    #define ErrorSyncModeNotSupport       -501
    
    /*
     * AD Range
     */
    #define AD_B_10_V     1
    #define AD_B_5_V      2
    #define AD_B_2_5_V    3
    #define AD_B_1_25_V   4
    #define AD_B_0_625_V  5
    #define AD_B_0_3125_V 6
    #define AD_B_0_5_V    7
    #define AD_B_0_05_V   8
    #define AD_B_0_005_V  9
    #define AD_B_1_V      10
    #define AD_B_0_1_V    11
    #define AD_B_0_01_V   12
    #define AD_B_0_001_V  13
    #define AD_U_20_V     14
    #define AD_U_10_V     15
    #define AD_U_5_V      16
    #define AD_U_2_5_V    17
    #define AD_U_1_25_V   18
    #define AD_U_1_V      19
    #define AD_U_0_1_V    20
    #define AD_U_0_01_V   21
    #define AD_U_0_001_V  22
    #define AD_B_2_V      23
    #define AD_B_0_25_V   24
    #define AD_B_0_2_V    25
    #define AD_U_4_V      26
    #define AD_U_2_V      27
    #define AD_U_0_5_V    28
    #define AD_U_0_4_V    29
    #define AD_B_1_5_V    30
    #define AD_B_0_2125_V 31
    #define AD_B_40_V     32 // PCI-9527 AI
    #define AD_B_3_16_V   33 // PCI-9527 AI
    #define AD_B_0_316_V  34 // PCI-9527 AI
    #define AD_B_25_V     35 // Jeff added for USB-2401 AI
    #define AD_B_12_5_V   36
    
    /*Synchronous Mode*/
    #define SYNCH_OP  1
    #define ASYNCH_OP 2
    
    // Input Type
    #define UD_AI_NonRef_SingEnded        0x01
    #define UD_AI_SingEnded               0x02
    #define UD_AI_Differential            0x04
    #define UD_AI_PseudoDifferential      0x08
    
    
    #define UD_AI_Voltage_2D5V_Above      0x20
    #define UD_AI_Voltage_2D5V_Below      0x21
    #define UD_AI_Current                 0x22
    #define UD_AI_RTD_4_Wire              0x23
    #define UD_AI_RTD_3_Wire              0x24
    #define UD_AI_RTD_2_Wire              0x25
    #define UD_AI_Resistor                0x26
    #define UD_AI_ThermoCouple            0x27
    #define UD_AI_Full_Bridge             0x28
    #define UD_AI_Half_Bridge             0x29
    #define UD_AI_ThermoCouple_Gnd        0x2A
    #define UD_AI_350Ohm_Full_Bridge      0x2B
    #define UD_AI_350Ohm_Half_Bridge      0x2C
    #define UD_AI_120Ohm_Full_Bridge      0x2D
    #define UD_AI_120Ohm_Half_Bridge      0x2E
    
    
    // Input Coupling
    #define UD_AI_EnableIEPE         	 0x100
    #define UD_AI_DisableIEPE         	 0x200
    #define UD_AI_Coupling_AC        	 0x400
    #define UD_AI_Coupling_None       	 0x800
    
    
    // Conversion Source
    #define UD_AI_CONVSRC_INT        0x01
    #define UD_AI_CONVSRC_EXT        0x02
    
    
    // wTrigCtrl in UD_AI_Trigger_Config()
    // wTrigCtrl = (Trigger Source | Trigger Edge | ReTrigger )
    #define UD_AI_TRIGSRC_MASK       0x03FF
    #define UD_AI_TRIGEDGE_MASK      0x4000
    #define UD_AI_RE_TRIG_MASK       0x2000
    
    
    // Trigger Source (bit9:0)
    #define UD_AI_TRGSRC_AI0         0x0200
    #define UD_AI_TRGSRC_AI1         0x0201
    #define UD_AI_TRGSRC_AI2         0x0202
    #define UD_AI_TRGSRC_AI3         0x0203
    #define UD_AI_TRGSRC_AI4         0x0204
    #define UD_AI_TRGSRC_AI5         0x0205
    #define UD_AI_TRGSRC_AI6         0x0206
    #define UD_AI_TRGSRC_AI7         0x0207
    #define UD_AI_TRGSRC_AI8         0x0208
    #define UD_AI_TRGSRC_AI9         0x0209
    #define UD_AI_TRGSRC_AI10        0x020A
    #define UD_AI_TRGSRC_AI11        0x020B
    #define UD_AI_TRGSRC_AI12        0x020C
    #define UD_AI_TRGSRC_AI13        0x020D
    #define UD_AI_TRGSRC_AI14        0x020E
    #define UD_AI_TRGSRC_AI15        0x020F
    #define UD_AI_TRGSRC_SOFT        0x0380
    #define UD_AI_TRGSRC_DTRIG       0x0388
    
    
    // Trigger Edge (bit14)
    #define UD_AI_TrigPositive         0x4000
    #define UD_AI_TrigNegative         0x0000
    
    
    // Trigger Edge (bit14)
    //#define UD_AI_Gate_ActiveHigh      0x4000
    //#define UD_AI_Gate_ActiveLow       0x0000
    #define UD_AI_Gate_PauseLow        0x4000
    #define UD_AI_Gate_PauseHigh       0x0000
    
    // ReTrigger (bit13)
    #define UD_AI_EnReTrigger          0x2000 // 0x02000000
    #define UD_AI_DisReTrigger         0x0000 // 0x00000000
    
    // AI Trigger Mode
    #define UD_AI_TRGMOD_POST          0x0000 // 0x00000000
    #define UD_AI_TRGMOD_DELAY         0x4000 // 0x40000000
    #define UD_AI_TRGMOD_PRE           0x8000 // 0x80000000
    #define UD_AI_TRGMOD_MIDDLE        0xC000 // 0xC0000000
    #define UD_AI_TRGMOD_GATED         0x1000 // 0x10000000
    
    // DIO_Config
    #define UD_DIO_DIGITAL_INPUT          0x30
    #define UD_DIO_COUNTER_INPUT          0x31
    #define UD_DIO_DIGITAL_OUTPUT         0x32
    #define UD_DIO_PULSE_OUTPUT           0x33
    
    /*------------------------*/
    /* Constants for USB-1902 */
    /*------------------------*/

    // wConfigCtrl in UD_AI_1902_Config()
    /*Input Type*/ // bit 7:6 in AI_CONFG
    // 2011April29, Jeff changed
    #define P1902_AI_NonRef_SingEnded   0x00
    #define P1902_AI_SingEnded          0x01
    #define P1902_AI_PseudoDifferential 0x02
    #define P1902_AI_Differential       0x02  // P1902_AI_PseudoDifferential
    
    /*Conversion Source*/ // bit 9 in AI_ACQMCR
    #define P1902_AI_CONVSRC_INT        0x00
    #define P1902_AI_CONVSRC_EXT        0x80
    
    
    // wTrigCtrl in UD_AI_1902_Config()
    /*Trigger Source*/ // bit 8:3 in AI_ACQMCR
    #define P1902_AI_TRGSRC_AI0         0x020
    #define P1902_AI_TRGSRC_AI1         0x021
    #define P1902_AI_TRGSRC_AI2         0x022
    #define P1902_AI_TRGSRC_AI3         0x023
    #define P1902_AI_TRGSRC_AI4         0x024
    #define P1902_AI_TRGSRC_AI5         0x025
    #define P1902_AI_TRGSRC_AI6         0x026
    #define P1902_AI_TRGSRC_AI7         0x027
    #define P1902_AI_TRGSRC_AI8         0x028
    #define P1902_AI_TRGSRC_AI9         0x029
    #define P1902_AI_TRGSRC_AI10        0x02A
    #define P1902_AI_TRGSRC_AI11        0x02B
    #define P1902_AI_TRGSRC_AI12        0x02C
    #define P1902_AI_TRGSRC_AI13        0x02D
    #define P1902_AI_TRGSRC_AI14        0x02E
    #define P1902_AI_TRGSRC_AI15        0x02F
    #define P1902_AI_TRGSRC_SOFT        0x030
    #define P1902_AI_TRGSRC_DTRIG       0x031
    
    
    /*Trigger Edge*/ // bit 2 in AI_ACQMCR
    #define P1902_AI_TrgPositive        0x040
    #define P1902_AI_TrgNegative        0x000
    
    /*Gated Trigger Level*/  // bit 2 in AI_ACQMCR
    //#define P1902_AI_Gate_ActiveHigh        0x000
    //#define P1902_AI_Gate_ActiveLow         0x040
    #define P1902_AI_Gate_PauseLow          0x000
    #define P1902_AI_Gate_PauseHigh         0x040
    
    /*Trigger Mode*/
    #define P1902_AI_TRGMOD_POST        0x000
    #define P1902_AI_TRGMOD_GATED       0x080
    #define P1902_AI_TRGMOD_DELAY       0x100
    
    /*ReTrigger*/ // bit 25 in AI_ACQMCR
    #define P1902_AI_EnReTigger         0x200
    
    /**/

    /*
     * AO Constants
     */

    /*Conversion Source*/
    #define P1902_AO_CONVSRC_INT        0x00
    
    #define P1902_AO_TRIG_CTRL_MASK     0xfffff8ee  // (~0x00000711)
    /*Trigger Mode*/
    #define P1902_AO_TRGMOD_POST        0x00
    #define P1902_AO_TRGMOD_DELAY       0x01
    
    /*Trigger Source*/ // bit 24 in AO_TCFIGR
    #define P1902_AO_TRGSRC_SOFT        0x00
    #define P1902_AO_TRGSRC_DTRIG       0x10
    
    /*Trigger Edge*/ // bit 25 in AI_ACQMCR
    #define P1902_AO_TrgPositive        0x100
    #define P1902_AO_TrgNegative        0x000
    
    /*Enable Re-Trigger*/ // bit 10 in AO_TCFIGR
    #define P1902_AO_EnReTigger         0x200
    /* Flag for AO Waveform Seperation Interval COunt Register (AO_WSIC) */
    #define P1902_AO_EnDelay2           0x400
    
    
    /*------------------------*/
    /* Constants for USB-2401 */
    /*------------------------*/
    
    // wConfigCtrl in UD_AI_2401_Config()
    /*Input Type*/ // V >=2.5V, V<2.5, Current, RTD (4 wire), RTD (3-wire), RTD (2-wire), Resistor, Thermocouple, Full-Bridge, Half-Bridge
    #define P2401_Voltage_2D5V_Above      0x00
    #define P2401_Voltage_2D5V_Below      0x01
    #define P2401_Current                 0x02
    #define P2401_RTD_4_Wire              0x03
    #define P2401_RTD_3_Wire              0x04
    #define P2401_RTD_2_Wire              0x05
    #define P2401_Resistor                0x06
    #define P2401_ThermoCouple            0x07
    #define P2401_Full_Bridge             0x08
    #define P2401_Half_Bridge             0x09
    #define P2401_ThermoCouple_Gnd        0x0A
    #define P2401_350Ohm_Full_Bridge      0x0B
    #define P2401_350Ohm_Half_Bridge      0x0C
    #define P2401_120Ohm_Full_Bridge      0x0D
    #define P2401_120Ohm_Half_Bridge      0x0E
    
    /*Conversion Source*/ // bit 9 in AI_ACQMCR
    #define P2401_AI_CONVSRC_INT        0x00
    
        // wTrigCtrl in UD_AI_2401_Config()
        /*Trigger Source*/ // bit 8:3 in AI_ACQMCR
    #define P2401_AI_TRGSRC_SOFT        0x030
    #define P2401_AI_TRGSRC_DTRIG       0x031
    
    /*Trigger Edge*/ // bit 2 in AI_ACQMCR
    #define P2401_AI_TrgPositive        0x040
    #define P2401_AI_TrgNegative        0x000
    
    /*Trigger Mode*/
    #define P2401_AI_TRGMOD_POST        0x000
    
    
    // wMAvgStageCh1 ~ wMAvgStageCh4 in UD_AI_2401_PollConfig()
    #define P2401_Polling_MAvg_Disable    0x00
    #define P2401_Polling_MAvg_2_Sampes   0x01
    #define P2401_Polling_MAvg_4_Sampes   0x02
    #define P2401_Polling_MAvg_8_Sampes   0x03
    #define P2401_Polling_MAvg_16_Sampes  0x04
    
    // wEnContPolling in UD_AI_2401_PollConfig()
    #define P2401_Continue_Polling_Disable 0x00
    #define P2401_Continue_Polling_Enable  0x01
    
    // wPollSpeed in UD_AI_2401_PollConfig()
    #define P2401_ADC_2000_SPS            0x09
    #define P2401_ADC_1000_SPS            0x08
    #define P2401_ADC_640_SPS             0x07
    #define P2401_ADC_320_SPS             0x06
    #define P2401_ADC_160_SPS             0x05
    #define P2401_ADC_80_SPS              0x04
    #define P2401_ADC_40_SPS              0x03
    #define P2401_ADC_20_SPS              0x02
    
    
    
    /*
     * DDS Constants
     */
    #define P2405_AI_MaxDDSFreq        128000
    #define P2405_AI_MinDDSFreq        1000
    
    // #define P2405_AI_POLLING_RATE      20000.0f // (20K = 10240K/512 )
    
    /*
     * AI Constants
     */
    /*AI Select Channel*/
    #define P2405_AI_CH_0					0
    #define P2405_AI_CH_1					1
    #define P2405_AI_CH_2					2
    #define P2405_AI_CH_3					3
    
    /*Input Coupling*/
    #define P2405_AI_EnableIEPE         	0x00000004
    #define P2405_AI_DisableIEPE         	0x00000008
    #define P2405_AI_Coupling_AC        	0x00000010
    #define P2405_AI_Coupling_None       	0x00000020
    
    /*Input Type*/
    #define P2405_AI_Differential			  0x00000000
    #define P2405_AI_PseudoDifferential		  0x00000040
    
    #define P2405_AI_CONVSRC_INT            0x00000000
    #define P2405_AI_CONVSRC_EXT            0x00000200
    
    // wTrigCtrl in UD_AIO_2405_Config() <TBD>
    /* Mask for Trigger bits, Internal use */    
    
    /*Trigger Source*/ 
    #define P2405_AI_TRGSRC_AI0           0x00000200
    #define P2405_AI_TRGSRC_AI1           0x00000208
    #define P2405_AI_TRGSRC_AI2           0x00000210
    #define P2405_AI_TRGSRC_AI3           0x00000218
    #define P2405_AI_TRGSRC_SOFT          0x00000380
    #define P2405_AI_TRGSRC_DTRIG         0x00000388 // digital-trigger, 
    
    /*Trigger Edge*/ 
    #define P2405_AI_TrgPositive          0x00000004
    #define P2405_AI_TrgNegative          0x00000000
    
    //#define P2405_AI_Gate_ActiveHigh      0x00000004
    //#define P2405_AI_Gate_ActiveLow       0x00000000
    #define P2405_AI_Gate_PauseLow        0x00000004
    #define P2405_AI_Gate_PauseHigh       0x00000000
    
    /*ReTrigger*/ // bit 25 in AI_ACQMCR
    #define P2405_AI_EnReTigger           0x2000 // 0x02000000
    
    // wTrigMode in UD_AIO_2405_Config()
    
    /*AI Trigger Mode*/
    #define P2405_AI_TRGMOD_POST          0x0000 // 0x00000000
    #define P2405_AI_TRGMOD_DELAY         0x4000 // 0x40000000
    #define P2405_AI_TRGMOD_PRE           0x8000 // 0x80000000
    #define P2405_AI_TRGMOD_MIDDLE        0xC000// 0xC0000000
    //#define P2405_AI_TRGMOD_GATED         0x00000001
    #define P2405_AI_TRGMOD_GATED         0x1000 // 0x10000000
    
    
    
       
    /*-------------------------------*/
    /* GPIO/GPTC Configuration       */
    /*-------------------------------*/
    #define GPIO_IGNORE_CONFIG 0x00
    
   /*UD_DIO_1902_Config, UD_DIO_2401_Config*/ 
    #define GPTC0_GPO1         0x01
    #define GPI0_3_GPO0_1      0x02
    #define ENC0_GPO0          0x04
    #define GPTC0_TC1          0x08
    
    #define GPTC2_GPO3         0x10
    #define GPI4_7_GPO2_3      0x20
    #define ENC1_GPO2          0x40
    #define GPTC2_TC3          0x80
    
    /*GPIO Port*/
    #define GPIO_PortA         1
    #define GPIO_PortB         2
    
    /*UD_DIO_2405_Config*/ 
    #define P2405_DIGITAL_INPUT          0x30
    #define P2405_COUNTER_INPUT          0x31
    #define P2405_DIGITAL_OUTPUT         0x32
    #define P2405_PULSE_OUTPUT           0x33
    
    /*-------------------------------------------------*/
    /* General Purpose Timer/Counter for USB-1902 */
    /*-------------------------------------------------*/
    /*Counter Mode*/
    #define SimpleGatedEventCNT       0x01
    #define SinglePeriodMSR           0x02
    #define SinglePulseWidthMSR       0x03
    #define SingleGatedPulseGen       0x04
    #define SingleTrigPulseGen        0x05
    #define RetrigSinglePulseGen      0x06
    #define SingleTrigContPulseGen    0x07
    #define ContGatedPulseGen         0x08
    #define EdgeSeparationMSR         0x09
    #define SingleTrigContPulseGenPWM 0x0a
    #define ContGatedPulseGenPWM      0x0b
    #define CW_CCW_Encoder            0x0c
    #define x1_AB_Phase_Encoder       0x0d
    #define x2_AB_Phase_Encoder       0x0e
    #define x4_AB_Phase_Encoder       0x0f
    #define Phase_Z                   0x10
    #define MultipleGatedPulseGen     0x11
    
    // 20190731 added for on-fly change
    /*GPTC on-fly change*/ 
    #define OnFlyChange_Mode          0x80
    #define OnFlyChange_PulseCounters 0x81
    
    /*GPTC clock source*/
    #define GPTC_CLK_SRC_Ext          0x01
    #define GPTC_CLK_SRC_Int          0x00
    #define GPTC_GATE_SRC_Ext         0x02
    #define GPTC_GATE_SRC_Int         0x00
    #define GPTC_UPDOWN_Ext           0x04
    #define GPTC_UPDOWN_Int           0x00
    /*GPTC clock polarity*/
    #define GPTC_CLKSRC_LACTIVE       0x01
    #define GPTC_CLKSRC_HACTIVE       0x00
    #define GPTC_GATE_LACTIVE         0x02
    #define GPTC_GATE_HACTIVE         0x00
    #define GPTC_UPDOWN_LACTIVE       0x04
    #define GPTC_UPDOWN_HACTIVE       0x00
    #define GPTC_OUTPUT_LACTIVE       0x08
    #define GPTC_OUTPUT_HACTIVE       0x00
    /*GPTC OP Parameter*/
    #define IntGate                   0x0  /* Internal Gate */
    #define IntUpDnCTR                0x1  /* Internal Up/Down Counter */
    #define IntENABLE                 0x2  /* Internal Enable */
    
    
    
    /*UD_CTR_Control()*/
    #define UD_CTR_Filter_Disable               0
    #define UD_CTR_Filter_Enable                1
    #define UD_CTR_Reset_Rising_Edge_Counter    2
    #define UD_CTR_Reset_Frequency_Counter      4
    
    #define UD_CTR_Polarity_Positive            8
    #define UD_CTR_Polarity_Negative            0
    
    
    /*--------------------------------------*/
    /* DAQ Event type for the event message */
    /*--------------------------------------*/
    #define AIEnd     0
    #define AOEnd     0
    #define DIEnd     0
    #define DOEnd     0
    #define DBEvent   1
    #define TrigEvent 2
    
    
    /*
     * Encoder/GPTC Constants
    */
    #define P1902_GPTC0                 0x00
    #define P1902_GPTC1                 0x01
    
    /*Encoder Setting Event Control*/
    #define P1902_EPT_PULWIDTH_200us    0x00
    #define P1902_EPT_PULWIDTH_2ms      0x01
    #define P1902_EPT_PULWIDTH_20ms     0x02
    #define P1902_EPT_PULWIDTH_200ms    0x03
    #define P1902_EPT_TRGOUT_GPO        0x04
    #define P1902_EPT_TRGOUT_CALLBACK   0x08
    /*Event Type*/
    #define P1902_EVT_TYPE_EPT0         0x00
    #define P1902_EVT_TYPE_EPT1         0x01
    
    /*---------------------------------*/
    /* Constants for I Squared C (I2C) */
    /*---------------------------------*/
    /*I2C Port*/
    #define I2C_Port_A 0
    /*I2C Control Operation*/
    #define I2C_ENABLE 0
    #define I2C_STOP   1
    
    /* Basic Function */
    I16 UD_Register_Card (U16 CardType, U16 card_num);
    I16 UD_Release_Card (U16 CardNumber);
    I16 UD_Get_FileHandle(U16 CardNumber, int *phDev );
    
    /* AI Function */
    I16 UD_AI_1902_Config ( U16 CardNumber, U16 wConfigCtrl, U16 wTrigCtrl, U32 dwTrgLevel, U32 wReTriggerCnt, U32 dwDelayCount );
    I16 UD_AI_2401_Config ( U16 wCardNumber, U16 wChanCfg1, U16 wChanCfg2, U16 wChanCfg3, U16 wChanCfg4, U16 wTrigCtrl );
    I16 UD_AI_2405_Chan_Config ( U16 CardNumber, U16 wChanCfg1, U16 wChanCfg2, U16 wChanCfg3, U16 wChanCfg4);
    I16 UD_AI_2405_Trig_Config ( U16 CardNumber, U16 wConvSrc, U16 wTrigMode, U16 wTrigCtrl, U32 wReTrigCnt, U32 dwDLY1Cnt, U32 dwDLY2Cnt, U32 dwTrgLevel ); 
    
    I16 UD_AI_1902_CounterInterval ( U16 CardNumber, U32 ScanIntrv, U32 SampIntrv );
    I16 UD_AI_AsyncCheck (U16 CardNumber, BOOLEAN *Stopped, U32 *AccessCnt);
    I16 UD_AI_AsyncClear (U16 CardNumber, U32 *AccessCnt);
    I16 UD_AI_AsyncDblBufferHalfReady (U16 CardNumber, BOOLEAN *HalfReady, BOOLEAN *StopFlag);
    I16 UD_AI_AsyncDblBufferMode (U16 CardNumber, BOOLEAN Enable);
    I16 UD_AI_AsyncDblBufferTransfer (U16 CardNumber, U16 *Buffer);
    I16 UD_AI_AsyncDblBufferTransfer32 ( U16 CardNumber, U32 *pwBuffer );
    I16 UD_AI_AsyncDblBufferOverrun (U16 CardNumber, U16 op, U16 *overrunFlag);
    I16 UD_AI_AsyncDblBufferHandled (U16 CardNumber);
    I16 UD_AI_AsyncDblBufferToFile (U16 CardNumber);
    I16 UD_AI_ContReadChannel (U16 CardNumber, U16 Channel, U16 AdRange, U16 *Buffer, U32 ReadCount, F64 SampleRate, U16 SyncMode);
    I16 UD_AI_ContReadMultiChannels (U16 CardNumber, U16 NumChans, U16 *Chans, U16 *AdRanges, U16 *Buffer, U32 ReadCount,F64 SampleRate, U16 SyncMode);
    I16 UD_AI_ContReadChannelToFile (U16 CardNumber, U16 Channel, U16 AdRange, U8 *FileName, U32 ReadCount, F64 SampleRate, U16 SyncMode);
    I16 UD_AI_ContReadMultiChannelsToFile (U16 CardNumber, U16 NumChans, U16 *Chans, U16 *AdRanges, U8 *FileName, U32 ReadCount, F64 SampleRate, U16 SyncMode);
    I16 UD_AI_InitialMemoryAllocated (U16 CardNumber, U32 *MemSize);
    I16 UD_AI_ReadChannel (U16 CardNumber, U16 Channel, U16 AdRange, U16 *Value);
    I16 UD_AI_VReadChannel (U16 CardNumber, U16 Channel, U16 AdRange, F64 *voltage);
    I16 UD_AI_ReadMultiChannels (U16 CardNumber, U16 NumChans, U16 *Chans, U16 *AdRanges, U16 *Buffer);
    I16 UD_AI_SetTimeOut (U16 CardNumber, U32 TimeOut);
    I16 UD_AI_VoltScale (U16 CardNumber, U16 AdRange, I16 reading, F64 *voltage);
    I16 UD_AI_ContVScale (U16 CardNumber, U16 adRange, void *readingArray, F64 *voltageArray, I32 count);
    I16 UD_AI_AsyncReTrigNextReady (U16 CardNumber, BOOLEAN *Ready, BOOLEAN *StopFlag, U16 *RdyTrigCnt);
    
    /* AB: commented out due to undefined symbol error */
    // I16 UD_AI_EventCallBack (U16 CardNumber, I16 mode, I16 EventType, void (*callbackAddr)(int));
    
    I16 UD_AI_2401_PollConfig ( U16 wCardNumber, U16 wPollSpeed, U16 wMAvgStageCh1, U16 wMAvgStageCh2, U16 wMAvgStageCh3, U16 wMAvgStageCh4 );
    I16 UD_AI_2401_Stop_Poll ( U16 wCardNumber ); 
    I16 UD_AI_DDS_ActualRate_Get ( U16 CardNumber, F64 fSampleRate, F64 *fActualRate );
    
    I16 UD_AI_VoltScale32 ( U16 CardNumber, U16 adRange, U16 inType, U32 reading, F64 *voltage );
    I16 UD_AI_2401_Scale32 ( U16 wCardNumber, U16 adRange, U16 inType, U32 reading, double *voltage );
    
    I16 UD_AI_ContVScale32 ( U16 CardNumber, U16 adRange, U16 inType, U32 readingArray[], F64 voltageArray[], I32 count );
    I16 UD_AI_2401_ContVScale32 ( U16 wCardNumber, U16 adRange, U16 inType, U32 readingArray[], F64 voltageArray[], I32 count );
    
    /* AB: commented out due to undefined symbol error */
    // I16 UD_AI_AsyncBufferTransfer32 ( U16 wCardNumber, U32 *pdwBuffer, U32 offset, U32 count );
    
    /* AO Function */
    I16 UD_AO_1902_Config (U16 CardNumber, U16 ConfigCtrl, U16 TrigCtrl, U32 ReTrgCnt, U32 DLY1Cnt, U32 DLY2Cnt);
    I16 UD_AO_AsyncCheck (U16 CardNumber, BOOLEAN *Stopped, U32 *AccessCnt);
    I16 UD_AO_AsyncClear (U16 CardNumber, U32 *AccessCnt, U16 stop_mode);
    I16 UD_AO_AsyncDblBufferHalfReady (U16 CardNumber, BOOLEAN *HalfReady);
    I16 UD_AO_AsyncDblBufferTransfer (U16 CardNumber, U16 wBufferID, U16 *Buffer);
    I16 UD_AO_AsyncDblBufferMode (U16 CardNumber, BOOLEAN Enable, BOOLEAN bEnFifoMode);
    I16 UD_AO_ContBufferCompose (U16 CardNumber, U16 TotalChnCount, U16 ChnNum, U32 UpdateCount, void *ConBuffer, void *Buffer);
    I16 UD_AO_ContWriteChannel (U16 CardNumber, U16 Channel, void *pAOBuffer, U32 WriteCount, U32 Iterations, U32 CHUI, U16 definite, U16 SyncMode );
    I16 UD_AO_ContWriteMultiChannels ( U16 CardNumber, U16 NumChans, U16 *Chans, void *pAOBuffer, U32 WriteCount, U32 Iterations, U32 CHUI, U16 definite, U16 SyncMode );
    I16 UD_AO_InitialMemoryAllocated (U16 CardNumber, U32 *MemSize);
    I16 UD_AO_SetTimeOut (U16 CardNumber, U32 TimeOut);
    I16 UD_AO_WriteChannel (U16 CardNumber, U16 Channel, I16 Value);
    I16 UD_AO_VWriteChannel (U16 CardNumber, U16 Channel, F64 Voltage);
    I16 UD_AO_VoltScale (U16 CardNumber, U16 Channel, F64 Voltage, I16 *binValue);
    /* AB: commented out due to undefined symbol error */
    // I16 UD_AO_EventCallBack (U16 CardNumber, I16 mode, I16 EventType, void (*callbackAddr)(int));
    
    /*----------------------------------------------------------------------------*/
    I16 UD_DIO_1902_Config ( U16 wCardNumber, U16 wPart1Cfg, U16 wPart2Cfg );
    I16 UD_DIO_2405_Config ( U16 wCardNumber, U16 wPart1Cfg, U16 wPart2Cfg );
    I16 UD_DIO_2401_Config ( U16 wCardNumber, U16 wPart1Cfg );
    
    /*----------------------------------------------------------------------------*/
    /* DI Function */
    I16 UD_DI_ReadLine (U16 CardNumber, U16 Port, U16 Line, U16 *State);
    I16 UD_DI_ReadPort (U16 CardNumber, U16 Port, U32 *Value);
    
    I16 UD_DI_SetCOSInterrupt32 (U16 wCardNumber, U16 wPort, U32 dwCtrl);
    I16 UD_DI_GetCOSLatchData32 (U16 wCardNumber, U16 wPort, U32 *pwCosLData);
    /*----------------------------------------------------------------------------*/
    /* DO Function */
    
    I16 UD_DO_ReadLine (U16 CardNumber, U16 Port, U16 Line, U16 *Value);
    I16 UD_DO_ReadPort (U16 CardNumber, U16 Port, U32 *Value);
    
    I16 UD_DO_WriteLine (U16 CardNumber, U16 Port, U16 Line, U16 Value);
    I16 UD_DO_WritePort (U16 CardNumber, U16 Port, U32 Value);
    
    I16 UD_DO_SetInitPattern (U16 wCardNumber, U16 wPort, U32 dwPattern);
    I16 UD_DO_GetInitPattern (U16 wCardNumber, U16 wPort, U32 *pdwPattern);
    /*----------------------------------------------------------------------------*/
    /* Timer/Counter Function */
    
    
    I16 UD_GPTC_Clear (U16 CardNumber, U16 GCtr);
    I16 UD_GPTC_Control (U16 CardNumber, U16 GCtr, U16 ParamID, U16 Value);
    I16 UD_GPTC_Read (U16 CardNumber, U16 GCtr, U32 *Value);
    I16 UD_GPTC_Setup (U16 CardNumber, U16 GCtr, U16 Mode, U16 SrcCtrl, U16 PolCtrl, U32 Reg1_Val, U32 Reg2_Val, U32 PulseCount);
    I16 UD_GPTC_Status (U16 CardNumber, U16 GCtr, U16 *Value);
    
    I16 UD_CTR_Control ( U16 wCardNumber, U16 wCtr, U32 dwCtrl );
    I16 UD_CTR_ReadFrequency ( U16 wCardNumber, U16 wCtr, F64 *pfValue );
    I16 UD_CTR_ReadEdgeCounter ( U16 wCardNumberr, U16 wCtr, U32 *pdwValue );
    /* AB: commented out due to undefined symbol error */
    // I16 UD_CTR_ReadRisingEdgeCounter ( U16 wCardNumber, U16 wCtr, U32 *pdwValue );    
    
    I16 UD_Read_ColdJunc_Thermo( U16 wCardNumber, double *pfValue );
    /*----------------------------------------------------------------------------*/
    /* Get View Function */
    I16 UD_AI_GetViewX64 (U16 CardNumber, U64 *View);
    /* AB: commented out due to undefined symbol error */
    // I16 UD_AO_GetViewX64 (U16 CardNumber, U64 *View);
    /*---------------------------------------------------------------------------*/
    
    
    I16 UD_AI_Channel_Config ( U16 CardNumber, U16 wChanCfg1, U16 wChanCfg2, U16 wChanCfg3, U16 wChanCfg4);
    I16 UD_AI_Trigger_Config ( U16 CardNumber, U16 wConvSrc, U16 wTrigMode, U16 wTrigCtrl,  \
                                               U32 wReTrigCnt, U32 dwDLY1Cnt, U32 dwDLY2Cnt, U32 dwTrgLevel );                                           
    I16 UD_DIO_Config ( U16 wCardNumber, U16 wPart1Cfg, U16 wPart2Cfg ) ;
    
    I16 usbdaq_WritePort ( U16 wCardNumber, U16 wPortAddr, U32 dwData );
    I16 usbdaq_ReadPort ( U16 wCardNumber, U16 wPortAddr, U32 *pdwData );
    '''
)

builder.cdef(
    '''
    /*==========================================

              Map of DAQ File
        +-------------------------+
        |                         |
        |         Header          |
        |                         |
        +-------------------------+
        |      ChannelRange       |
        |       (Optional)        |
        +-------------------------+
        |   ChannelCompensation   |
        |   (Only for PCI-9524)   |
        +-------------------------+
        |                         |
        |         DAQ data        |
        |                         |
        |                         |
        +-------------------------+

    ============================================*/
    /*size is 60 bytes*/
    typedef struct _DAQFILE_HEADER
    {
        char          ID[10];               //ex "ADLinkDAQ1"
        short         card_type;            //Pci7250, Pci9112...(include DG, HR, HG)
        short         num_of_channel;       //1, 2,...
        unsigned char channel_no;           //used only num_of_channel is 1
        int32_t       num_of_scan;
        short         data_width;           //0: 8 bits, 1: 16 bits, 2: 32 bits
        short         channel_order;        //0: 0-1-2-3, 1: 3-2-1-0, 2: custom
        short         ad_range;
        double        scan_rate;
        short         num_of_channel_range;
        char          start_date[8];        //"12/31/99"
        char          start_time[8];        //"18:30:25"
        char          start_millisec[3];    //"360"
        char          reserved[6];
    } DAQFileHeader;
    
    typedef struct _CHANNEL_RANGE
    {
        unsigned char channel;
        unsigned char range;
    } DAQChannelRange;
    
    typedef struct _Channel_Compensation_9524
    {
        double residual_offset;
        double residual_scaling;
    } ChannelCompensation9524;
    ''',
    packed=True)

builder.set_source('_udask_cffi',
                   '''
                   #include "udask.h"
                   #include "DAQHeader.h"
                   ''',
                   libraries=['usb_dask64'])


if __name__ == '__main__':
    print('Compilation')
    builder.compile(verbose=True)
