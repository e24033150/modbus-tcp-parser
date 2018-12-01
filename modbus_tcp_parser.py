### python version : 3.6.0
### operating system : windows 10
import socket
import binascii
import os
from query_module import numbers_to_query_functions
from response_module import numbers_to_response_functions

packet_count = 0

# Use raw socket as a network sniffer
def sniff_socket():
    # For Windows
    if os.name == "nt" :
        conn = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        conn.bind(('127.0.0.1', 0))
        conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # For Linux
    else : 
        conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    return conn

# Parse modbus query packet
def modbus_query(_data):
    print ('Transaction ID = %d' % int(_data[:4], 16))
    print ('Length of Modbus TCP PDU = %d bytes' % (int(_data[8:12],16)-1))
    print ('Unit ID = %d' % int(_data[12:14],16))
	#Function code and data analysis
    numbers_to_query_functions(_data[14:16], _data[16:])
    print ('--------------------------------------------------')

# Parse modbus response packet
def modbus_response(_data):
    print ('Transaction ID = %d' % int(_data[:4], 16))
    print ('Length of Modbus TCP PDU = %d bytes' % (int(_data[8:12],16)-1))
    print ('Unit ID = %d' % int(_data[12:14],16))
	#Function code and data analysis
    numbers_to_response_functions(_data[14:16], _data[16:])
    print ('--------------------------------------------------')
	
# Transform raw data into hex string and judge it according to some information in TCP header
def process_raw_data(_raw_data):
    global packet_count
    ascii_data = binascii.hexlify(_raw_data).decode('ascii')

    # TCP flags : (PSH, ACK)=0x018, (ACK)=0x010, (SYN)=0x002, (SYN, ACK)=0x012
    if ascii_data[65:68] == '018':
        # TCP destination port = 502
        if ascii_data[44:48]=='01f6':
            print ('-------------------Modbus Query-------------------')
            packet_count = packet_count + 1
            print ('Modbus Packet Count : %d' % packet_count)
            modbus_query(ascii_data[80:])
        # TCP source port = 502
        elif ascii_data[40:44]=='01f6':
            print ('------------------Modbus Response-----------------')
            packet_count = packet_count + 1
            print ('Modbus Packet Count : %d' % packet_count)
            modbus_response(ascii_data[80:])
        else:
            pass
    elif ascii_data[65:68] == '010':
        print ('ACK Packet')
    elif ascii_data[65:68] == '002':
        print ('SYN Packet')
    elif ascii_data[65:68] == '012':
        print ('SYN/ACK Packet')
    else:
        pass

# Main function
if __name__ == "__main__":
    sniffer = sniff_socket()
    while True:
        raw_data, addr = sniffer.recvfrom(65535)
        process_raw_data(raw_data)
