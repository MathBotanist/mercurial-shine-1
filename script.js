$(function () {
    var socket = io.connect();

    //sockets
    socket.on('connect', () => {
        console.log('connected: '+socket.connected);
        socket.emit('hello', 'world')
      });

    socket.on('hey', function(msg){
        console.log(msg)
        ctx.font = "30px Arial";
        ctx.fillText(msg['text'], msg['x'], msg['y']);
    });

    function send_command(command){
        socket.emit('command', command)
    }

    //game
    var canvas = document.getElementById("game_canvas");
    var ctx = canvas.getContext("2d");

    canvas.addEventListener('keydown', this.get_key, false);

    function get_key(key){
        var key_code = key.keyCode;

        console.log(key_code)

        if(key_code == 87){
            send_command('moveup')
        }
    }
});