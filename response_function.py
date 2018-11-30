from error_function import numbers_to_error

def read_discrete_inputs(_modbus_data):
    print ('Function name : Read Discrete Inputs')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(byte_count):
        print ('Input Status%d : %s' % (i,format(int(_modbus_data[i*2+2:i*2+4],16),'08b')))
    
def read_coils(_modbus_data):
    print ('Function name : Read Coils')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(byte_count):
        print ('Coil Status%d : %s' % (i,format(int(_modbus_data[i*2+2:i*2+4],16),'08b')))

def write_single_coil(_modbus_data):
    print ('Function name : Write Single Coil')
    print ('Output Address : %d' % int(_modbus_data[:4],16))
    print ('Output Value : %d' % int(_modbus_data[4:],16))

def write_multiple_coils(_modbus_data):
    print ('Function name : Write Multiple Coils')
    print ('Starting Address : %s' % int(_modbus_data[:4],16))
    print ('Quantity of Outputs : %s' % int(_modbus_data[4:],16))

def read_input_registers(_modbus_data):
    print ('Function name : Read Input Registers')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(int(byte_count/2)):
        print ('Input Register value%d : %d' % (i,int(_modbus_data[i*4+2:i*4+6])))
	
def read_multiple_holding_registers(_modbus_data):
    print ('Function name : Read Multiple Holding Registers')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(int(byte_count/2)):
        print ('Register value%d : %d' % (i,int(_modbus_data[i*4+2:i*4+6])))
    
def write_single_holding_register(_modbus_data):
    print ('Function name : Write Single Holding Register')
    print ('Register Address : %d' % int(_modbus_data[:4],16))
    print ('Register Value : %d' % int(_modbus_data[4:],16))
	
def write_multiple_holding_registers(_modbus_data):
    print ('Function name : Write Multiple Holding Registers')
    print ('Starting Address : %s' % int(_modbus_data[:4],16))
    print ('Quantity of Registers : %s' % int(_modbus_data[4:],16))
	
def read_write_multiple_registers(_modbus_data):
    print ('Function name : Read/Write Multiple Registers')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte count : %d' % byte_count)
    for i in range(int(byte_count/2)):
        print ('Read Registers value%d : %d' % (i,int(_modbus_data[i*4+2:i*4+6])))

def mask_write_register(_modbus_data):
    print ('Function name : Mask Write Register')
    print ('Reference Address : %d' % int(_modbus_data[:4],16))
    print ('And_Mask : %s' % format(int(_modbus_data[4:8],16),'016b'))
    print ('Or_Mask : %s' % format(int(_modbus_data[8:12],16),'016b'))

def read_fifo_queue(_modbus_data):
    print ('Function name : Read FIFO Queue')
    print ('Byte count : %d' % int(_modbus_data[:4],16))
    fifo_count = int(_modbus_data[4:8],16)
    for i in range(fifo_count):
        print ('FIFO Value Register%d : %d' % (i,int(_modbus_data[i*4+8:i*4+12])))

def read_file_record(_modbus_data):
    print ('Function name : Read File Record')
    resp_data_length = int(_modbus_data[:2],16)
    print ('Resp. Data length : %d bytes' % resp_data_length)
    current_index = 2
    current_seq = 1
    while (current_index < resp_data_length*2+2) :
        file_resp_length = int(_modbus_data[current_index:current_index+2],16)
        print ('Sub-Req. %d, File resp. length : %d bytes' % (current_seq,file_resp_length))
        print ('Sub-Req. %d, Ref. Type : %d' % (current_seq,int(_modbus_data[current_index+2:current_index+4],16)))
        for i in range(int((file_resp_length-1)/2)):
            print ('Sub-Req. %d, Register.Data : %d' % (current_seq,int(_modbus_data[i*4+current_index+4:i*4+current_index+8],16)))
        current_seq = current_seq + 1
        current_index = current_index + (file_resp_length+1)*2

# Not done
def write_file_record(_modbus_data):
    print ('Function name : Write File Record')
	
def read_exception_status(_modbus_data):
    print ('Function name : Read Exception Status')
    print ('Output Data : %d' % int(_modbus_data,16))

# Not done	
def diagnostic(_modbus_data):
    print ('Function name : Diagnostic')

def get_com_event_counter(_modbus_data):
    print ('Function name : Get Com Event Counter')
    print ('Status word : %s' % _modbus_data[:4])
    print ('Event Count %d' % int(_modbus_data[4:],16))

# Not done	
def get_com_event_log(_modbus_data):
    print ('Function name : Get Com Event Log')

# Not done	
def report_slave_id(_modbus_data):
    print ('Function name : Report Slave ID')

# Not done	
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
    if func :
        func(modbus_data)
    else:
        numbers_to_error(argument, modbus_data)
