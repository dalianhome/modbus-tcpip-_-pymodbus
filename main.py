from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
import logging
import logging.handlers as Handlers
import sys
import time
import datetime
import logging
# host = '192.168.0.10'
host='localhost'
port = 502
print("yo, amigo, this is local folder")
client = ModbusClient(host, port)
connection = client.connect()
socketOpen = client.is_socket_open()
print(connection)
print(socketOpen)

# client = ModbusTcpClient('127.0.0.1')
# client.write_coil(1, True)
# result = client.read_coils(1,2)
# print(result.bits[0])
# client.close()
i = True
num1=0
q=1
print("Addr" + "    Data " + "           Logging Time")
while i:
 request = client.read_holding_registers(0x64,2,unit=1)
# response = client.execute(request)
#  assert (request.function_code < 0x80)

 if num1 != request.registers[0]:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("400101  "+str(request.registers[0]) + "            "+st)
    # print(st)
    f = open('logFile.txt', 'a')
    f.write('\n' + str(q) + ". "+str(request.registers[0]) + "            "+st)
    num1 = request.registers[0]
    q = q + 1
 # else:
 #    print("----------silent----------")
 # print(q)
 time.sleep(1)

 if i == False:
     break
client.close()
f.close()
