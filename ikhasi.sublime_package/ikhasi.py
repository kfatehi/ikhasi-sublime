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

	def pushContent(self, view):
		self.pending = self.pending - 1
		if self.pending == 0:
			self.queue.put(view.substr(sublime.Region(0, view.size())))

class ikhasiThread(threading.Thread):
	def __init__(self, queue):
		self.queue = queue
		threading.Thread.__init__ (self)

	def run(self):
		while True:
			content = self.queue.get()
			t = threading.Thread(self.sendData(content))
			t.start()

	def sendData(self, content):
		host = "127.0.0.1"
		port = 6543
		socketIO = SocketIO(host, port)
		socketIO.emit('push', content)
		self.queue.task_done()


