List = [] 
for i in range(0,5):
	num=int(input())
	List.append(num)
num6 = int(input())
print(List)
print('['+str(List[0])+', '+str(List[1])+', '+str(List[2])+']')
print('['+str(List[-2])+', '+str(List[-1])+']')
print('The number', num6 ,'appears', List.count(num6) ,'time(s) in the list.')
