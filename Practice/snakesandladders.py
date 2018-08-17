"""kk"""
p1 = 0
p2 = 0
n = 0
print('Welcome to snakes and ladders game')
print('________________________________________________')
import random
def dice(n):
	roll = int(input('roll the dice'))
	if roll > 1 and roll < 6:
		roll = roll + n
	return roll
def snakes_or_ladders(n):
	ladders = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:100}
	snakes = {98:78,95:75,93:73,87:24,64:60,62:19,56:53,49:11,48:26,16:6}
	if n in ladders.keys():
		print('LADDER!!')
		print('________________________________________________')
		n = ladders[n]
	elif n in snakes.keys():
		print('SNAKE!!!')
		print('________________________________________________')
		n = snakes[n]
	return n
while p1 < 100 or p2 < 100:
	print('Player1 turn')
	p1 = dice(p1)
	p1 = snakes_or_ladders(p1)
	print('Player1 is at : ', p1, '   Player2 is at : ', p2)
	print('________________________________________________')
	if p1>99:
		print('Player1 is the winner!!')
		break
	print('Player2 turn')
	p2 = dice(p2)
	p2 = snakes_or_ladders(p2)
	print('Player1 is at :', p1, '   Player2 is at : ', p2)
	print('________________________________________________')
	if p2>99:
		print('Player2 is the winner!!!')
		break
