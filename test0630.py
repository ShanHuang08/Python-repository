
#字串交換
class MyLibrary():
    def MySolution():
        message = 'hello,world'
        List = message.split(',')
        message_1 = List[0].replace(List[0], List[1])
        message_2 = List[1].replace(List[1], List[0])

        new_message = message_1 + ',' + message_2
        print(new_message)


    def ChatGPT():
        message = 'hello,world'
        index = message.index(',')  # 找到逗號的索引位置

        new_message = message[index + 1:] + ',' + message[:index]

        print(new_message)


