
// load bar to the next LVl
var articles = $('#articles_count').text();
var procent
if(articles <= 20){
    procent = Math.floor((articles*100)/20);
    $('.progress-bar').attr('style', 'width:'+ procent + "%").text(procent + "%");
}else if (articles > 20 && articles < 50){
    articles -=20;
	procent = Math.floor((articles*100)/30);
	$('.progress-bar').attr('style', 'width:'+ procent + "%").text(procent + "%");
}else  {
	$('.progress-bar').attr('style', 'width:100%').text("THE LAST LVL");
}
// load bar to the next LVl