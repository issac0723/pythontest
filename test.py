#print("Hello World")
List = [] 
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
List.append(num1)
List.append(num2)
List.append(num3)
List.append(num4)
List.append(num5)
print(List)
print('['+str(List[0])+', '+str(List[1])+', '+str(List[2])+']')
print('['+str(List[-2])+', '+str(List[-1])+']')
print('The number', num6 ,'appears', List.count(num6) ,'time(s) in the list.')
print('test')
