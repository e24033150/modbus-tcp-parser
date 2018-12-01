from error_module import numbers_to_error

def read_discrete_inputs(_modbus_data):
    print ('Function name : Read Discrete Inputs')
    print ('Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity of Inputs : %d' % int(_modbus_data[4:],16))
    
def read_coils(_modbus_data):
    print ('Function name : Read Coils')
    print ('Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity of coils : %d' % int(_modbus_data[4:],16))
    
def write_single_coil(_modbus_data):
    print ('Function name : Write Single Coil')
    print ('Output Address : %d' % int(_modbus_data[:4],16))
    print ('Output Value : %d' % int(_modbus_data[4:],16))
    
def write_multiple_coils(_modbus_data):
    print ('Function name : Write Multiple Coils')
    print ('Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity of Outputs : %d' % int(_modbus_data[4:8],16))
    byte_count = int(_modbus_data[8:10],16)
    print ('Byte Count : %d' % byte_count)
    for i in range(byte_count):
        print ('Outputs Value%d : %s' % (i,format(int(_modbus_data[i*2+10:i*2+12],16),'08b')))

def read_input_registers(_modbus_data):
    print ('Function name : Read Input Registers')
    print ('Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity of Input Registers : %d' % int(_modbus_data[4:],16))

def read_multiple_holding_registers(_modbus_data):
    print ('Function name : Read Multiple Holding Registers')
    print ('Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity of Registers : %d' % int(_modbus_data[4:],16))
    
def write_single_holding_register(_modbus_data):
    print ('Function name : Write Single Holding Register')
    print ('Register Address : %d' % int(_modbus_data[:4],16))
    print ('Register Value : %d' % int(_modbus_data[4:],16))
	
def write_multiple_holding_registers(_modbus_data):
    print ('Function name : Write Multiple Holding Registers')
    start_address = int(_modbus_data[:4],16)
    print ('Starting Address : %d' % start_address)
    print ('Quantity of Registers : %d' % int(_modbus_data[4:8],16))
    byte_count = int(_modbus_data[8:10],16)
    print ('Byte Count : %d' % byte_count)
    for i in range(int(byte_count/2)):
        print ('Register %d : %d' % (i+start_address,int(_modbus_data[i*4+10:i*4+14],16)))

def read_write_multiple_registers(_modbus_data):
    print ('Function name : Read/Write Multiple Registers')
    print ('Read Starting Address : %d' % int(_modbus_data[:4],16))
    print ('Quantity to Read : %d' % int(_modbus_data[4:8],16))
    write_start_address = int(_modbus_data[8:12],16)
    print ('Write Starting Address : %d' % write_start_address)
    print ('Quantity to Write : %d' % int(_modbus_data[12:16],16))
    write_byte_count = int(_modbus_data[16:18],16)
    print ('Write Byte Count : %d' % write_byte_count)
    for i in range(int(write_byte_count/2)):
        print ('Register %d : %d' % (i+write_start_address,int(_modbus_data[i*4+18:i*4+22],16)))

def mask_write_register(_modbus_data):
    print ('Function name : Mask Write Register')
    print ('Reference Address : %d' % int(_modbus_data[:4],16))
    print ('And_Mask : %s' % format(int(_modbus_data[4:8],16),'016b'))
    print ('Or_Mask : %s' % format(int(_modbus_data[8:12],16),'016b'))
	
def read_fifo_queue(_modbus_data):
    print ('Function name : Read FIFO Queue')
    print ('FIFO Pointer Address : %d' % int(_modbus_data[:4],16))
	
def read_file_record(_modbus_data):
    print ('Function name : Read File Record')
    byte_count = int(_modbus_data[:2],16)
    print ('Byte Count : %d' % byte_count)
    for i in range(int(byte_count/7)):
        print ('Sub-Req. %d, Ref. Type : %d' % (i,int(_modbus_data[i*14+2:i*14+4],16)))
        print ('Sub-Req. %d, File Number : %d' % (i,int(_modbus_data[i*14+4:i*14+8],16)))
        print ('Sub-Req. %d, Record number : %d' % (i,int(_modbus_data[i*14+8:i*14+12],16)))
        print ('Sub-Req. %d, Record Length : %d' % (i,int(_modbus_data[i*14+12:i*14+16],16)))

def write_file_record(_modbus_data):
    print ('Function name : Write File Record')
    request_data_length = int(_modbus_data[:2],16)
    print ('Request data length : %d bytes' % request_data_length)
    
    current_index = 2
    current_seq = 1
    while (current_index < request_data_length*2+2) :
        print ('Sub-Req. %d, Ref. Type : %s' % (current_seq,_modbus_data[current_index:current_index+2]))
        print ('Sub-Req. %d, File Number : %d' % (current_seq,int(_modbus_data[current_index+2:current_index+6],16)))
        print ('Sub-Req. %d, Record number : %d' % (current_seq,int(_modbus_data[current_index+6:current_index+10],16)))
        record_length = int(_modbus_data[current_index+10:current_index+14],16)
        for i in range(record_length):
            print ('Sub-Req. %d, Register.Data : %d' % (current_seq,int(_modbus_data[i*4+current_index+14:i*4+current_index+18],16)))
        current_seq = current_seq + 1
        current_index = current_index + (record_length)*4 +14
	
def read_exception_status(_modbus_data):
    print ('Function name : Read Exception Status')

def diagnostic(_modbus_data):
    print ('Function name : Diagnostic')
    print ('Sub-function : %s' % _modbus_data[:4])
    print ('Data : %s' % _modbus_data[4:])

def get_com_event_counter(_modbus_data):
    print ('Function name : Get Com Event Counter')

def get_com_event_log(_modbus_data):
    print ('Function name : Get Com Event Log')

def report_slave_id(_modbus_data):
    print ('Function name : Report Slave ID')

def read_device_identification_or_others(_modbus_data):
    print ('Function name : Read Device Identification or Others')
    print ('MEI Type : %s' % _modbus_data[:2])
    print ('MEI type specific data : %s' % _modbus_data[2:])
	
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
	
def numbers_to_query_functions(argument, modbus_data):
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    if func:
        func(modbus_data)
    else:
        numbers_to_error(argument, modbus_data)
