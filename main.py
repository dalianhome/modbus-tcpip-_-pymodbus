# chengxin 24/7/2018 testing pymodbus
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
import logging
import logging.handlers as Handlers
import sys
import time
import datetime

# tcp slave ip addr
host = '192.168.0.10'

port = 502
print("yo, amigo, this is local folder")
client = ModbusClient(host, port)
connection = client.connect()
socketOpen = client.is_socket_open()
print(connection)
print(socketOpen)
#above code make sure connection is done

i = True
num1=0
q=1
print("Addr" + "    Data " + "           Logging Time")

while i:
 request = client.read_holding_registers(0x64,2,unit=1)

 if num1 != request.registers[0]:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("400101  "+str(request.registers[0]) + "            "+st)
    # print(st)
    f = open('logFile.txt', 'a')
    f.write('\n' + str(q) + ". "+str(request.registers[0]) + "            "+st)
    num1 = request.registers[0]
    q = q + 1

    
 time.sleep(1)

 if i == False:
     break
client.close()
f.close()
