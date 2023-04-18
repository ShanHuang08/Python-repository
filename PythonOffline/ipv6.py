import random
# from sklearn.datasets import load_boston
# import pandas as pd

def AI_generate_ipv6():
    ipv6_blocks = []
    for i in range(8):
        ipv6_blocks.append('{:04x}'.format(random.randint(0, 0xffff)))
    ipv6_str = ':'.join(ipv6_blocks)
    return ipv6_str

if __name__=='__main__':
    print(AI_generate_ipv6())
# print(AI_generate_ipv6())



# boston = load_boston()
# print(boston.keys())
# print(boston['filename'])

# {:04x} 是一種 Python 格式化字串的方法，其中 : 代表著要進行格式化的動作，0 代表要在不足四個字元時使用 0 進行填充，4 代表要使用四個字元，x 代表要使用十六進位表示。

# 例如，'{:04x}'.format(15) 會輸出 000f，因為 15 的十六進位表示為 0f，而 :{04x} 的格式指令要求四個字元，因此在 0 前面填充了兩個 0。 :x = 16進位, :d = 10進位. :o = 8進位

# random.randint(0, 0xffff) 則是使用 Python 的 random 模組中的 randint 函式，產生介於 0 到 65535 之間的一個隨機整數。
# 由於 IPv6 位址每個區塊使用十六進位表示，因此這個隨機整數的範圍需要是 0 到 0xffff（也就是十六進位下的 0x0000 到 0xffff）。