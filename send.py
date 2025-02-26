import time
import socket
import streamlit as st
import pickle  # If want to share array data

UDP_IP = "192.168.1.255"
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


class sending_data:
    # def close_socket():
    #     sock.close()
    #     return True

    def stopper(x):
        with_stopper = []
        for index, item in enumerate(x):
            with_stopper.append(item)
            if index + 1 != len(x):
                with_stopper.append((x[index][1], x[index + 1][0], x[index][2], 1))
            else:
                with_stopper.append((x[index][1], x[index][1], x[index][2], 1))
        return with_stopper

    def send_data(data1, data2, data3):
        buffer_data1 = data1.to_bytes(2, byteorder='little')
        buffer_data2 = data2.to_bytes(2, byteorder='little')
        buffer_data3 = data3.to_bytes(2, byteorder='little')

        buffer_to_send = buffer_data1 + buffer_data2 + buffer_data3
        # print(' '.join(f'{byte:02x}' for byte in buffer_to_send), end=' ')
        print(f"sending index:{data1}, flow:{data2}, and duration:{data3} to {UDP_IP}:{UDP_PORT}")

        sock.sendto(buffer_to_send, (UDP_IP, UDP_PORT))