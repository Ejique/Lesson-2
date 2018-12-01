def check_lines(line1, line2):
	if type(line1)!=str or type(line2)!=str:
		return "0"
	if line2==line1:
		return "1"
	if len(line2)<=len(line1):
		return "2"
	if line1!='learn':
		return "3"

result=check_lines("line1","learn5")
print(result)