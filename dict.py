from tkinter import X


key_list = ['agr1', 'age', 'ave','eer','tyu','ttyu','wsx','tdf','qqw','rrg']
value_list = [21,27,25,30,28,37,32,24,27,60]
# print(len(key_list))
# print(len(value_list))
# dict_from_list = dict(zip(key_list, value_list))
dict_list = {key_list[i]: value_list[i] for i in range(len(value_list))}


# print(dict_from_list)
# print(dict_from_list2)
print(dict_list.items())
# print(sorted(dict_from_list2.items()))

# https://zhuanlan.zhihu.com/p/344230384
# sorted函数，sorted(iterable,key,reverse)，sorted一共有iterable,key,reverse这三个参数。
# items()方法将字典的元素转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
# （如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。
Res=sorted(dict_list.items(),key=lambda a:a[0])
Result=sorted(dict_list.items(),key=lambda x:x[1])
print(Res)
print(Result)
# print(len(Result))
# print(Result[0])
# print(Result[0][0])


# for key in sorted(dict_from_list2.keys()):
#     print(key, dict_from_list2[key],end=', ')
# print('\n-----')
# for key in sorted(dict_from_list2.items()):
#     print(key[0], key[1])