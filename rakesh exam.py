exam=str(input('enter the day rakesh had to written the organic chemistry exam:'))
if exam=="monday":
	print("he can go to organic chemistry exam in these day")
	time=int(input('enter the time rakesh had started:'))
	if time<10:
		print('he can go to exam in the given time')
		hall_ticket=str(input('enter rakesh had taken his hall ticket or not:'))
		if hall_ticket=='yes':
			print('you can allowed to the center')
			room_number=int(input('enter the room number of rakesh'))
			if room_number<=16:
				print('he can enter room 16')
			elif room_number==18:
				print('he can enter in between 17-19 room')
			else:
				print('he enter the room number 20')
		else:
			print('you are not allowed to the cemter')
	
	else:
		print('he cannot go to exam in the gibmve time')
	
else:
		print('there is no organic chemistry exam in these day')
		