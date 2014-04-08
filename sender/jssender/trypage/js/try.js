var sendDweet= function (devicename, command) {
	// body...
}

var commandExecuter = {
	"up": sendDweet(name,"up"),
	"dn": sendDweet(name,"down"),
	"lt": sendDweet(name,"left"),
	"rt": sendDweet(name,"right"),
	"st": sendDweet(name,"stop")
};
//w=119,a=97,s=115,d=100,x=120

$(document).keydown(function(e){
	if((e.which == 119) || (e.which == 38)){
		$('#up').click();
		alert("Up");
		return e.preventDefault();
	}
	if( (e.which == 97) || (e.which == 37)){
		$('#left').click();
		alert("left");
		return e.preventDefault();
	}
	if((e.which == 115) || (e.which == 40)){
		$('#down').click();
		alert("down");
		return e.preventDefault();
	}
	if((e.which == 100) || (e.which == 39)){
		$('#right').click();
		alert("right");
		return e.preventDefault();
	}
	if((e.keyCode == 120)){
		$('#stop').click();
		alert("stop");
		return e.preventDefault();
	}
});

$(document).keypress(function(e){
	if((e.which == 119) ){
		$('#up').click();
		alert("Up");
		return e.preventDefault();
	}
	if( (e.which == 97) ){
		$('#left').click();
		alert("left");
		return e.preventDefault();
	}
	if((e.which == 115) ){
		$('#down').click();
		alert("down");
		return e.preventDefault();
	}
	if((e.which == 100) ){
		$('#right').click();
		alert("right");
		return e.preventDefault();
	}
	if((e.keyCode == 120)){
		$('#stop').click();
		alert("stop");
		return e.preventDefault();
	}
});

