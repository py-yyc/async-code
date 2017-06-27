#!/usr/bin/env python3

import os, sys
import socket as s
import asyncio

loop = asyncio.get_event_loop()

# import eventloop
# loop = eventloop.get_event_loop()

async def echo_server(server_addr):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.bind(server_addr)
    sock.listen(5) # allowed unaccepted connections in backlog

    print(f"listening on: {server_addr[0]}:{server_addr[1]}")

    while True:
        client, client_addr = await loop.sock_accept(sock)
        print(f"connection from: {client_addr[0]}:{client_addr[1]}")
        loop.create_task( echo_handler(client) )

async def echo_handler(client):
    client_addr = client.getpeername()

    with client:
        while True:
            data = await loop.sock_recv(client, 1024)
            if not data:
                break
            await loop.sock_sendall(client, b'got: '+data)

    print(f"connection closed: {client_addr[0]}:{client_addr[1]}")

def main(port):
    try:
        loop.create_task( echo_server( ('0.0.0.0',port) ) )
        loop.run_forever()

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    port = 2500
    main( port )
