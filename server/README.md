ikhasi-server
=============

HTML CODE

```javscript
var socket = io.connect('http://localhost:6543');
socket.on('content', function (data) {
  console.log(data);
  socket.emit('my other event', { my: 'data' });
});
```
