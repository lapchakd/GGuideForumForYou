
// load bar to the next LVl
var articles = $('#articles_count').text();
var percent;
count_articles(articles);
function count_articles(articles){
    if(articles <= 20){
        percent = Math.floor((articles*100)/20);
    }else if (articles > 20 && articles < 50){
        articles -=20;
        percent = Math.floor((articles*100)/30);
    }else if (articles > 50)  {
        $('.progress-bar').attr('style', 'width:100%').text("THE LAST LVL");
        return;
    }
    $('.progress-bar').attr('style', 'width:'+ percent + "%").text(percent + "%");
}
// load bar to the next LVl