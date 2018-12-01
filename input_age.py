def count_age(a):	
	if a <= 7:
		otvet = 'welcome to the kindergarden'
	elif 7<a<=17:
		otvet = 'welcome to the school'
	elif 17<a<=23:
		otvet = 'welcome to the institute'
	elif a>23: 
		otvet = 'run for job'
	return otvet

a = int(input("input your age, please "))		
print(count_age(a))