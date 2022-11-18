n=5
# for i in range(n+1):
#     if i == 1:
#         print('  '*(n-i)+'*'*i)
#     if i > 1:
#         print('  '*(n-i)+'*   '*i)

# 字串對齊: https://zhuanlan.zhihu.com/p/51436239
# ljust(), rjust(),  center()

Digit=1
Sum=0
for i in range(n+1):
    if i == 1: #1
        print('  '*(n-i)+str(Digit)*i)
        Digit+=2
    if i > 1:
        for j in range(i):
            Sum+=Digit
            if j == 0:
                print('  '*(n-i)+(str(Digit))+'  ',end='') #i=2 Digit加2次
            elif j > 0 and Digit < 10:
                print('  '+(str(Digit))+'  ',end='')
            elif j > 0 and Digit >= 10:
                print(' '+(str(Digit))+'  ',end='')
            Digit+=2 
        print()
# print(Sum)