
// load bar to the next LVl
var articles = $('#articles_count').text();
var percent, text;
count_articles(articles);
function count_articles(articles){
    if(articles <= 20){
        percent= Math.floor((articles*100)/20);
        text = percent + '%';
    }else if (articles > 20 && articles < 50){
        articles -=20;
        percent = Math.floor((articles*100)/30);
        text = percent + '%' ;
    }else if (articles > 50)  {
        text = "THE LAST LVL";
    }
    $('.progress-bar').attr('style', 'width:'+ percent + "%").text(text);
}
// load bar to the next LVl