exception_code = {
	    '01': 'ILLEGAL FUNCTION',
		'02': 'ILLEGAL DATA ADDRESS',
		'03': 'ILLEGAL DATA VALUE',
		'04': 'SLAVE DEVICE FAILURE',
		'05': 'ACKNOWLEDGE',
		'06': 'SLAVE DEVICE BUSY',
		'08': 'MEMORY PARITY ERROR',
		'0a': 'GATEWAY PATH UNAVAILABLE',
		'0b': 'GATEWAY TARGET DEVICE FAILED TO RESPOND' 
	}

def get_exception_info(_data):
    info = exception_code.get(_data)
    if info :
        print ('Exception : ' + info)
    else:
        pass
	
switcher = {
	    '82': 'Read Discrete Inputs',
		'81': 'Read Coils',
		'85': 'Write Single Coil',
		'8f': 'Write Multiple Coils',
		'84': 'Read Input Registers',
		'83': 'Read Multiple Holding Registers',
		'86': 'Write Single Holding Register',
		'90': 'Write Multiple Holding Registers',
		'97': 'Read/Write Multiple Registers',
		'96': 'Mask Write Register',
		'98': 'Read FIFO Queue',
		'94': 'Read File Record',
		'95': 'Write File Record',
		'87': 'Read error Status',
		'88': 'Diagnostic',
		'8b': 'Get Com Event Counter',
		'8c': 'Get Com Event Log',
		'91': 'Report Slave ID',
		'ab': 'Read Device Identification or Others'
	}

def numbers_to_error(argument, modbus_data):
    function_name = switcher.get(argument)
    # Execute the function
    if function_name :
        print ('Function name : ' + function_name)
        get_exception_info(modbus_data)
    else:
        pass
