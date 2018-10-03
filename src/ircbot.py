import socket
import time


def join(s):
    s.send("JOIN #cmsc491 \r\n")


def user():
    cmd = "USER tim.lin 0 * :Tim.Lin \r\n"
    return cmd


def nick():
    cmd = "NICK dg79418\r\n"
    return cmd


def pong(s):
    s.send('PONG: ' + '\r\n')


def privmsg(msg, s):
    send(msg, s)


def send(cmd, s):
    s.send(cmd)


def connect():
    server = '127.0.0.1'
    port = '6667'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server, port))
        send(nick(), s)
        send(user(), s)
    return s


def increment(r, s):
    msg = r.split(' ')
    num = msg[1]
    num += 1
    privmsg('!IncrementMe ' + num, s)


if __name__ == '__main__':
    socket = connect()
    time.sleep(5)
    join(socket)
    while 1:
        reply = socket.recv(2048)
        if reply.find("PING") != -1:
            pong(socket)
        if reply.find("!IncrementMe") != -1:
            increment(reply, socket)
