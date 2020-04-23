$(document).ready(function() {
   $(".site-btn").hide();
	$('.game').click(function(){
		let id = this.getAttribute('id');
		$('.a'+id).show(2000);
   });
   setInterval(function(){
   	for(let i = 1;i<7;i++){
   		$(".a" + i).hide(2000);
	}
	},10000);
});