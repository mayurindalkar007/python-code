# Tower of Hanoi is a very famous game.
# In this game there are 3 pegs and N number of disks placed one over the other in decreasing size.
# The objective of this game is to move the disks one by one from the first peg to the last peg.
# And there is only ONE condition, we can not place a bigger disk on top of a smaller disk.

def tower_of_hanoi(number_of_disks, start_peg, aux_peg, end_peg):
	if number_of_disks == 1:
		print('Move from {} to {}'.format(start_peg, end_peg))	
	else:
		tower_of_hanoi(number_of_disks - 1, start_peg, end_peg, aux_peg)
		tower_of_hanoi(1, start_peg, aux_peg, end_peg)
		tower_of_hanoi(number_of_disks - 1, aux_peg, start_peg, end_peg)

if __name__ == '__main__':
	N = int(raw_input('Enter number of disks = '))
	tower_of_hanoi(N, 'A', 'B', 'C')
