
message = 'hello,world'
message = message.replace('world','hello')
print(message)

message_list = ['hello', 'world']
message_str = message_list[0] + ',' + message_list[1]
new_message = message_str.replace(message_list[1], message_list[0])
print(new_message)