# TCP client example

"""
    <GALATEA WEB: Web system simulations>
    Copyright (C) 2016  Erik Velasquez erikvelasquez.25@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
"""

data = "0 Exit\n"
data = "1 Start\n"
data = "2 Sleep value\n"
data = "3 Stop\n"
data = "4 Yield\n"
data = "5 Pause\n"
data = "6 Set Var value\n"
data = "7 Get Var\n"
data = "8 Informacion\n"
data = "9 Informacion\n"
"""
import time
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))

"""
while 1:
    print "Waiting respond:"
    data = client_socket.recv(512)
    if ( data == 'q' or data == 'Q'):
        client_socket.close()
        break;
    else:
        print "RECIEVED:" , data
        data = raw_input ( "SEND( TYPE q or Q to Quit):" )
        if (data <> 'Q' and data <> 'q'):
            client_socket.sendall(data)
        else:
            client_socket.send(data)
            client_socket.close()
            break;
"""
"""
while 1:
    for x in range(1,10):
        data = str(x) + " Informacion\n"
        client_socket.sendall(data)
        time.sleep(5)

    data = "0 Informacion\n"
    client_socket.sendall(data)
    client_socket.close()
    break;
"""

data = "1 Start\n"
client_socket.sendall(data)
time.sleep(5)

data = "4 Yield\n"
client_socket.sendall(data)
time.sleep(5)

data = "5 Pause\n"
client_socket.sendall(data)
time.sleep(5)

data = "1 Start\n"
client_socket.sendall(data)
time.sleep(5)


data = "0 Exit\n"
client_socket.sendall(data)
time.sleep(1)
client_socket.close()
