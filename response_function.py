def read_discrete_inputs(_modbus_data):
    print ('Function name : Read Discrete Inputs')

def read_coils(_modbus_data):
    print ('Function name : Read Coils')

def write_single_coil(_modbus_data):
    print ('Function name : Write Single Coil')

def write_multiple_coils(_modbus_data):
    print ('Function name : Write Multiple Coils')

def read_input_registers(_modbus_data):
    print ('Function name : Read Input Registers')
	
def read_multiple_holding_registers(_modbus_data):
    print ('Function name : Read Multiple Holding Registers')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(int(byte_count/2)):
        print ('Register %d : %d' % (i,int(_modbus_data[i*4+2:i*4+6])))
	
def write_single_holding_register(_modbus_data):
    print ('Function name : Write Single Holding Register')
    print ('Register Address : %d' % int(_modbus_data[:4],16))
    print ('Register Value : %d' % int(_modbus_data[4:],16))
	
def write_multiple_holding_registers(_modbus_data):
    print ('Function name : Write Multiple Holding Registers')
    print ('Starting Address : %s' % int(_modbus_data[:4],16))
    print ('Quantity of Registers : %s' % int(_modbus_data[4:8],16))
	
def read_write_multiple_registers(_modbus_data):
    print ('Function name : Read/Write Multiple Registers')

def mask_write_register(_modbus_data):
    print ('Function name : Mask Write Register')

def read_fifo_queue(_modbus_data):
    print ('Function name : Read FIFO Queue')
	
def read_file_record(_modbus_data):
    print ('Function name : Read File Record')
		
def write_file_record(_modbus_data):
    print ('Function name : Write File Record')
	
def read_exception_status(_modbus_data):
    print ('Function name : Read Exception Status')
	
def diagnostic(_modbus_data):
    print ('Function name : Diagnostic')
	
def get_com_event_counter(_modbus_data):
    print ('Function name : Get Com Event Counter')
	
def get_com_event_log(_modbus_data):
    print ('Function name : Get Com Event Log')
	
def report_slave_id(_modbus_data):
    print ('Function name : Report Slave ID')
	
def read_device_identification_or_others(_modbus_data):
    print ('Function name : Read Device Identification or Others')
	
switcher = {
	    '02': read_discrete_inputs,
		'01': read_coils,
		'05': write_single_coil,
		'0f': write_multiple_coils,
		'04': read_input_registers,
		'03': read_multiple_holding_registers,
		'06': write_single_holding_register,
		'10': write_multiple_holding_registers,
		'17': read_write_multiple_registers,
		'16': mask_write_register,
		'18': read_fifo_queue,
		'14': read_file_record,
		'15': write_file_record,
		'07': read_exception_status,
		'08': diagnostic,
		'0b': get_com_event_counter,
		'0c': get_com_event_log,
		'11': report_slave_id,
		'2b': read_device_identification_or_others
	}
    	
def numbers_to_response_functions(argument, modbus_data):
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    func(modbus_data)
