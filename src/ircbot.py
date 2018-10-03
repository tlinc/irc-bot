#!/usr/src/Python-3.7.0

import socket
import time
import sys

def join(s):
    s.send("JOIN #cmsc491\r\n")


def user():
    cmd = "USER tim.lin 0 * :Tim.Lin\r\n"
    return cmd


def nick():
    cmd = "NICK dg79418\r\n"
    return cmd


def pong(s):
    s.send('PONG' + '\r\n')


def privmsg(msg, s):
    send('PRIVMSG #cmsc491 :'+msg+'\r\n', s)


def send(cmd, s):
    s.send(cmd)


def connect():
    server = input('Enter a server name: ')
    port = input('Enter a port #: ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((server, port))
    send(nick(), s)
    send(user(), s)
    return s


def increment(r, s):
    msg = r.split(' ')
    print(msg[4])
    num = int(msg[4])
    num += 1
    privmsg('Incremented ' + str(num), s)


if __name__ == '__main__':
    socket = connect()
    time.sleep(5)
    join(socket)
    while 1:
	try:
            reply = socket.recv(2048)
            if reply.find("PING") != -1:
            	pong(socket)
            if reply.find("!IncrementMe") != -1:
                increment(reply, socket)
	except KeyboardInterrupt:
		privmsg('cy@', socket)
		sys.exit()	
