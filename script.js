$(function () {
    var socket = io.connect();

    socket.on('hey', function(msg){
        console.debug(msg)
    });
});