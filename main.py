import matplotlib.pyplot as plt
def nmoid(n, x):
	a = 1 + n**(-1 * x)
	b = 1 / a
	print(f"The nmoid of {x} in base {n} is equal to {b}")

def visualize(n):
	x_axis = []
	y_axis = []
	for i in range(-50, 50):
		x_axis.append(i)
		y_axis.append(nmoid(n, i))
	plt.plot(x_axis, y_axis)
	plt.xlabel("Values for N")
	plt.ylabel("Nmoids of N")
	ticks = [t * 0.1 for t in range(0, 11)]
	plt.xticks(range(-50, 54, 4))
	plt.yticks(ticks)
	plt.show()

def choose(cho):
	x_value = float(input("Enter a value to be nmoid-	ed."))
	n_value = float(input("Enter a base value."))
	if(cho==1):
		nmoid(n_value, x_value)
	elif(cho==2):
		visualize(n_value)
	else:
		new_choice = int(input("Unknown input. Please try again.\n"))
		choose(new_choice)
choice = int(input("Welcome to nmoid interface. Choose the function you want to use:\n1-Find nmoid-ed of a number.\n2-Visualize nmoid's of values between -50 and 50 with n value you choose.\n"))
choose(choice)
