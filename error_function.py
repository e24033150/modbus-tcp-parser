def read_discrete_inputs(_modbus_data):
    print ('Function name : Read Discrete Inputs')
    get_exception_info(_modbus_data)

def read_coils(_modbus_data):
    print ('Function name : Read Coils')
    get_exception_info(_modbus_data)

def write_single_coil(_modbus_data):
    print ('Function name : Write Single Coil')
    get_exception_info(_modbus_data)

def write_multiple_coils(_modbus_data):
    print ('Function name : Write Multiple Coils')
    get_exception_info(_modbus_data)

def read_input_registers(_modbus_data):
    print ('Function name : Read Input Registers')
    get_exception_info(_modbus_data)

def read_multiple_holding_registers(_modbus_data):
    print ('Function name : Read Multiple Holding Registers')
    get_exception_info(_modbus_data)
    
def write_single_holding_register(_modbus_data):
    print ('Function name : Write Single Holding Register')
    get_exception_info(_modbus_data)
    
def write_multiple_holding_registers(_modbus_data):
    print ('Function name : Write Multiple Holding Registers')
    get_exception_info(_modbus_data)
    
def read_write_multiple_registers(_modbus_data):
    print ('Function name : Read/Write Multiple Registers')
    get_exception_info(_modbus_data)

def mask_write_register(_modbus_data):
    print ('Function name : Mask Write Register')
    get_exception_info(_modbus_data)

def read_fifo_queue(_modbus_data):
    print ('Function name : Read FIFO Queue')
    get_exception_info(_modbus_data)
	
def read_file_record(_modbus_data):
    print ('Function name : Read File Record')
    get_exception_info(_modbus_data)
		
def write_file_record(_modbus_data):
    print ('Function name : Write File Record')
    get_exception_info(_modbus_data)
	
def read_exception_status(_modbus_data):
    print ('Function name : Read error Status')
    get_exception_info(_modbus_data)
	
def diagnostic(_modbus_data):
    print ('Function name : Diagnostic')
    get_exception_info(_modbus_data)
	
def get_com_event_counter(_modbus_data):
    print ('Function name : Get Com Event Counter')
    get_exception_info(_modbus_data)
	
def get_com_event_log(_modbus_data):
    print ('Function name : Get Com Event Log')
    get_exception_info(_modbus_data)
	
def report_slave_id(_modbus_data):
    print ('Function name : Report Slave ID')
    get_exception_info(_modbus_data)
	
def read_device_identification_or_others(_modbus_data):
    print ('Function name : Read Device Identification or Others')
    get_exception_info(_modbus_data)
		
switcher = {
	    '82': read_discrete_inputs,
		'81': read_coils,
		'85': write_single_coil,
		'8f': write_multiple_coils,
		'84': read_input_registers,
		'83': read_multiple_holding_registers,
		'86': write_single_holding_register,
		'90': write_multiple_holding_registers,
		'97': read_write_multiple_registers,
		'96': mask_write_register,
		'98': read_fifo_queue,
		'94': read_file_record,
		'95': write_file_record,
		'87': read_exception_status,
		'88': diagnostic,
		'8b': get_com_event_counter,
		'8c': get_com_event_log,
		'91': report_slave_id,
		'ab': read_device_identification_or_others
	}

def numbers_to_error(argument, modbus_data):
    func = switcher.get(argument)
    # Execute the function
    if func :
        func(modbus_data)
    else:
        pass	
		
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