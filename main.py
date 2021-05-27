import random, string, time


def send_msg(msg):
    nick = 'random:'  # must be unique (can be in any language)
    passwd = (''.join(random.choice(string.ascii_lowercase) for _ in range(256)) + ':')
    passwd_two = ':Please scan my body form:'
    passwd_three = ':Please check my current location:'

    print(nick + passwd + passwd_two + passwd_three + msg)

    reg_msg(msg)


def reg_msg(msg):
    file_object = open('test.db', 'a')
    file_object.write(str(time.time()) + ":" + str(msg))
    file_object.close()


def conversation_loop():
    send_msg(input())
    reg_msg(input())

    conversation_loop()


conversation_loop()
