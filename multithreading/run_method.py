import threading

class MyThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def run(self):
		print('Running thread {}'.format(self.threadID))
		
	def execute_function(self):
		print('Execute')

if __name__ == '__main__':
	t1 = MyThread(1, 'thread1')	
	t2 = MyThread(2, 'thread2')

	t1.start()
	t2.start()
