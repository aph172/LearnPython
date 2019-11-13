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
	print (motor + '\n')


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#add new key/value
alien_0['x_position'] = 10
alien_0['y_position'] = 20

for a,b in alien_0.items():
	print ('\nkey:' + a)
	print ('\nvalue:' + str(b))

print (alien_0['color'])

del alien_0['y_position']
print (alien_0)

for mykey in sorted(alien_0.keys()):
    print ('\nKey: ' + mykey)

for myvalue in alien_0.values():
    print ('\nValue: ' + str(myvalue))

unconfirmed_users = ['alice','brian','candance']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print ("Verify user: " + current_user.title())
	confirmed_users.append(current_user)
print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    if confirmed_user == 'alice':
        print (confirmed_user.upper())
    else:
	    print (confirmed_user.title())

numbers = list(range(1,6))
print(numbers)
for number in numbers:
	print(number)

#tuple
dimensions = (20, 30)
print ('print dimension')
print (dimensions[0])
print (dimensions [1])
for dimension in dimensions:
    print (dimension)

banned_users = ['andrew', 'michael', 'mary']
print ('already banned users' + str(banned_users))
new_user = input('please type in a new user name: ')
if new_user in banned_users:
   print (new_user + 'is in the banned list')
else:
   banned_users.append(new_user)
print ('new banned user list' + str(banned_users))