$(document).ready(function() {
   $(".site-btn").hide();
	$('.game').mouseover(function(){
		let id = this.getAttribute('id');
		$('.a'+id).show(1000).mouseout(function(){
		$('.a'+id).hide(1000);
   });
   })
   setInterval(function(){
   	for(let i = 1;i<7;i++){
   		$(".a" + i).hide(2000);
	}
	},20000);
});
