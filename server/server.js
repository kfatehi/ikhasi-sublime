var io = require('socket.io').listen(6543);
// io.set('log level', 1);


io.sockets.on('connection', function (socket) {
  socket.on('push', function (data) { 
   	socket.broadcast.emit("outgoing_delta", data);
  });
});



