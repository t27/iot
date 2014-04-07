var sendDweet= function (var devicename, var command) {
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
$().keypress(function(e){
	if(e.keyCode == 119){
		$('#up').click();
		return e.preventDefault();
	}
	if(e.keyCode == 97){
		$('#left').click();
		return e.preventDefault();
	}
	if(e.keyCode == 115){
		$('#down').click();
		return e.preventDefault();
	}
	if(e.keyCode == 100){
		$('#right').click();
		return e.preventDefault();
	}
	if(e.keyCode == 120){
		$('#stop').click();
		return e.preventDefault();
	}
});

