import sublime, sublime_plugin, subprocess
import threading
from socketIO_client import SocketIO
import Queue

class ikhasiEvents(sublime_plugin.EventListener):
	pending = 0
	def __init__(self):
		self.queue = Queue.Queue()
		ikhasiThread(self.queue).start()

	def on_modified(self, view):
		self.pending = self.pending + 1
		sublime.set_timeout(lambda: self.pushContent(view), 1000)

	# TODO need to send cursor location updates at least periodically
	def on_cursor_position_change(self, view):
		self.socketIO.emit('cursor', ['x','y'])

	# TODO needs to send only the lambda and position
	def pushContent(self, view):
		self.pending = self.pending - 1
		if self.pending == 0:
			content = view.substr(sublime.Region(0, view.size()))
			self.queue.put(content)

class ikhasiThread(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__ (self)
		self.host = "127.0.0.1"
		self.port = 6543
		self.queue = queue

	def run(self):
		while True:
			print self.queue.qsize()

			
			content = self.queue.get(True)
			t = threading.Thread(self.sendData(content))
			t.start()

	def sendData(self, content):
		socketIO = SocketIO(self.host, self.port)
		print "!!!!"
		socketIO.emit('push', content)  
		self.queue.task_done()