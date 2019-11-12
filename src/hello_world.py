message = " hello Message "
print (message.title())
print (message.upper())
print (message.lower())
print (message.lstrip())

motors =[]
motors.append("Honda")
print (motors)
motors.append("Toyota")
motors.append("Chevy")
print (motors)
popedmotor = motors.pop()
print (popedmotor)
motors.append("Ford")
motors[0]="Chevy"

for motor in motors:
	print (motor)


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

for a,b in alien_0.items():
	print ('\nkey:' + a)
	print ('\nvalue:' + str(b))


unconfirmed_users = ['alice','brian','candance']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print ("Verify user: " + current_user.title())
	confirmed_users.append(current_user)
print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print (confirmed_user.title())

numbers = list(range(1,6))
print(numbers)
for number in numbers:
	print(number)