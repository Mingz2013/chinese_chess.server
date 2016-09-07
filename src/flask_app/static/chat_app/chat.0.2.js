/**
 * Created by zhaojm on 9/7/16.
 */


var socket = io.connect('http://localhost');
socket.on('news', function (data) {
    console.log(data);
    socket.emit('my other event', {my: 'data'});
});