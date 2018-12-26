import os
import threading

def square_num(num):
	print('In square method')
	print('Proces id is {}'.format(os.getpid()))
	print('Thread name is {}'.format(threading.current_thread().name))
	print('Square of num is {}'.format(num*num))

def cube_thread(num):
	print('In cube method')
	print('Proces id is {}'.format(os.getpid()))
	print('Thread name is {}'.format(threading.current_thread().name))
	print('Cube of num is {}'.format(num*num*num))

if __name__ == '__main__':
	print('Proces id is {}'.format(os.getpid()))
	#print("Main thread name: {}".format(threading.main_thread().name()))
	t1 = threading.Thread(target=square_num, args=(2,))
	t2 = threading.Thread(target=cube_thread, args=(3,))
	t1.start()
	t2.start()
	t1.join() # Wait thread t1 to compleate its execution
	t2.join()	
