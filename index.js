var app = require('express')();
var http = require('http').Server(app);

app.get('/', function(req, res){
	res.sendfile('index.html');
});

http.listen(3000,function(){
	console.log('Listening on *:3000');
});
