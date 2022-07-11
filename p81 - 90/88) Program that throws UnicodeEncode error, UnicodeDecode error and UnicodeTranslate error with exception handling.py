# UnicodeEncode error handling
try:
    u = 'é'
    print("Integer value for é: ", ord(u))
    print("Converting the encoded value of é to Integer Equivalent: ", chr(233))
    print("UNICODE Representation of é: ", u.encode('utf-8'))
    print("ASCII Representation of é: ", u.encode('ascii'))


except UnicodeEncodeError as msg1:
    print(msg1)


finally:
    print("End1")


# UnicodeDecode error handling
try:
    with open('sample.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()

        print(lines)

    raise UnicodeTranslateError

except UnicodeDecodeError as msg2:
    print(msg2)


finally:
    print('End2')


# UnicodeTranslate error handling
try:
    with open('sample.txt', 'r', encoding='UTF-32') as f:
        lines = f.readlines()

        print(lines)


except Exception as msg3:
    print(msg3)


finally:
    print('End3')
