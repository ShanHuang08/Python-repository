import time
# UnboundLocalError: local variable 'username' referenced before assignment

username = 'abc'
def ErrorA():
    print(username) # "abc"
    username = 'ABC' 

def ErrorB(grade):
	if grade > 80:
		username = "A"
	elif grade > 70:
		username = "B"
	elif grade > 60:
		username = "C"
	elif grade > 50:
		username = "D"
	return username

# IndexError: list index out of range
TestList=['A','B','C'] #012
TestList2=['A','B'] #01
def ErrorC():
	TestList.reverse()
	List=[]
	for i in range(len(TestList)):
		List.append(TestList2[i])
	return List

def ErrorD(Num):
		return print(TestList[Num])

def timecal():
	print(time.time())


if __name__=='__main__':
    # ErrorA()
	# print(ErrorB(36))
	# ErrorC()
	# ErrorD(3)
	timecal()

