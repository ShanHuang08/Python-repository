key_list = ['agr1', 'cge', 'ave','eer','tyu','ttyu','wsx','tdf','qqw','rrg']
key2_list = ['方法', '字典','为了','这里','的意','思则','取元','参数','应的','比较']
value_list = [21,27,25,30,28,37,32,24,27,60]

# key跟key2陣列內容結合
for i in range(len(key_list)):
    key_list[i]=key_list[i]+' ('+key2_list[i]+')'
print(key_list)

# dict_from_list = dict(zip(key_list, value_list))
dict_list = {key_list[i]: value_list[i] for i in range(len(value_list))}


# print(dict_list)
print(dict_list.items())
print(sorted(dict_list.items()))

# sorted函数，sorted(iterable,key,reverse)，sorted一共有iterable,key,reverse这三个参数。
# items()方法将字典的元素转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
# （如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。
Res=sorted(dict_list.items(),key=lambda a:a[0])
Result=sorted(dict_list.items(),key=lambda x:x[1])

List=[]
for i in range(len(dict_list)-1,-1,-1):
    for j in range(2):
        # print(Result[i][j],end=' ')
        List.append(Result[i][j])
print(List)
# print(len(List)) #20
# print(type(len(List))) #int

for k in range(len(List)//2):
    print(f'{List[0+2*k]}:{List[1+2*k]}')


