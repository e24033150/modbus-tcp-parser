### python version : 3.6.0
### operating system : windows 10
import socket
import binascii
from query_function import numbers_to_query_functions
from response_function import numbers_to_response_functions

packet_count = 0

# use raw socket as a network sniffer
def sniff_socket():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    conn.bind(('127.0.0.1', 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    return conn

def modbus_query(_data):
    print ('Transaction ID = %d' % int(_data[:4], 16))
    print ('Length of Modbus TCP PDU = %d bytes' % (int(_data[8:12],16)-1))
    print ('Unit ID = %d' % int(_data[12:14],16))
	#function code and data analysis
    numbers_to_query_functions(_data[14:16], _data[16:])
    print ('--------------------------------------------------')

def modbus_response(_data):
    print ('Transaction ID = %d' % int(_data[:4], 16))
    print ('Length of Modbus TCP PDU = %d bytes' % (int(_data[8:12],16)-1))
    print ('Unit ID = %d' % int(_data[12:14],16))
	#function code and data analysis
    numbers_to_response_functions(_data[14:16], _data[16:])
    print ('--------------------------------------------------')
	
# transform raw data and judge it
def process_raw_data(_raw_data):
    global packet_count
    ascii_data = binascii.hexlify(_raw_data).decode('ascii')

    if ascii_data[64:68] == '5018':
        if ascii_data[44:48]=='01f6':
            print ('-------------------Modbus Query-------------------')
            packet_count = packet_count + 1
            print ('Modbus Packet Count : %d' % packet_count)
            modbus_query(ascii_data[80:])
        elif ascii_data[40:44]=='01f6':
            print ('------------------Modbus Response-----------------')
            packet_count = packet_count + 1
            print ('Modbus Packet Count : %d' % packet_count)
            modbus_response(ascii_data[80:])
        else:
            pass
    elif ascii_data[64:68] == '5010':
        print ('ACK Packet')
    elif ascii_data[64:68] == '8002':
        print ('SYN Packet')
    elif ascii_data[64:68] == '8012':
        print ('SYN/ACK Packet')
    else:
        pass

# main function
if __name__ == "__main__":
    sniffer = sniff_socket()
    while True:
        raw_data, addr = sniffer.recvfrom(65565)
        process_raw_data(raw_data)
