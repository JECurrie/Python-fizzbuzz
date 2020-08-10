#Clear the screen
import os
os.system('cls')

count = 0

#number = [1,2,3,4,5,6,7,8,9,10]

while (count < 100):
	count += 1

	if (count % 3 == 0) and (count % 5 == 0):
		print("%s - fizzbuzz" % count)
	elif (count % 3 == 0):
	    print("%s - fizz" % count)
	elif (count % 5 == 0):
		print("%s - buzz" % count)
	else:
		print(count)	

		


