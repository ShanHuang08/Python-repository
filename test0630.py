message = ['hello', 'world']
print('no replace()')
for i in message:
    print(i, end=' ')
print()
print('----------')

message_str = message[0] + ',' + message[1]
new_message = message_str.replace(message[0], message[0])
print('has replace()')
print(new_message)