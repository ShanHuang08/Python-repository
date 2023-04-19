<<<<<<< HEAD
import json
with open('C:/Users/shan_huang/Python/Banks.json','r',encoding="utf-8") as jsonfile:
    jdata=json.load(jsonfile)
    # data=json.loads(jsonfile.read())
    # data=json.dumps(jdata)
    print(type(jdata)) #<class 'dict'> 字典要用名子
    print(type(jdata['Items'])) #<class 'list'> 列表要用數字
    print(type(jdata['Items'][0])) #<class 'dict'>
    print(type(jdata['Items'][0]['code'])) #<class 'str'>
    print(type(jdata['Items'][0]['name'])) #<class 'str'>

    
print(jdata['Pager']['Total'], type(jdata['Pager']['Total'])) #191 int
print(len(jdata['Items']), type(len(jdata['Items']))) #191 int
print(jdata['Items'][0:3])
print(jdata['Items'][0]['code'])
print(jdata['Items'][1]['name'])

=======
import json
with open('C:/Users/shan_huang/Python/Banks.json','r',encoding="utf-8") as jsonfile:
    jdata=json.load(jsonfile)
    # data=json.loads(jsonfile.read())
    # data=json.dumps(jdata)
    print(type(jdata)) #<class 'dict'> 字典要用名子
    print(type(jdata['Items'])) #<class 'list'> 列表要用數字
    print(type(jdata['Items'][0])) #<class 'dict'>
    print(type(jdata['Items'][0]['code'])) #<class 'str'>
    print(type(jdata['Items'][0]['name'])) #<class 'str'>

    
print(jdata['Pager']['Total'], type(jdata['Pager']['Total'])) #191 int
print(len(jdata['Items']), type(len(jdata['Items']))) #191 int
print(jdata['Items'][0:3])
print(jdata['Items'][0]['code'])
print(jdata['Items'][1]['name'])

>>>>>>> 8ed83d2505d4355229a31d2a06788e31225895b9
