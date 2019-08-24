var taskId;
var uniqueId;
var statusInterval;
var url;
var siteUrl = {
    1: 'http://www.inven.co.kr/board/maple/2587?p=',
    2: 'http://www.inven.co.kr/board/maple/2299?p='
};
var selectedCategory;

$(document).ready(function(){
    $(document).on('click', '#start-crawl', function(){
        selectedCategory = $('#site-select option:selected').val();
        for(k in siteUrl){
            if(k === selectedCategory){
                url = siteUrl[k]
            }
        }
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is working...');
        $.ajax({
            url: '/api/crawl/',
            type: 'POST',
            data: {
                'url': url,
            },
            success: crawlSuccess,
            error: crawlFail,
        })
    });

    $(document).on('click', '#show-data', function(){
        selectedCategory = $('#site-select option:selected').val();
        $.ajax({
            url: '/api/showdata/',
            type: 'GET',
            data: {
                'category': selectedCategory
            },
            success: showData,
            error: showDataFail
        })
    });
});

function checkCrawlStatus(taskId, uniqueId){
    $.ajax({
        url: '/api/crawl/?task_id='+taskId+'&unique_id='+uniqueId+'/',
        type: 'GET',
        success: showCrawledData,
        error: showCrawledDataFail,
    })
}

function crawlSuccess(data){
    taskId = data.task_id;
    uniqueId = data.unique_id;
    statusInterval = setInterval(function() {checkCrawlStatus(taskId, uniqueId);}, 2000);
}

function crawlFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showCrawledData(data){
    if (data.status){
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is ' + data.status + ' ... ' + 'After crawling, the results are returned');
    }else{
        clearInterval(statusInterval);
        $('#progress').attr("class", "alert alert-primary");
        $('#progress').html('crawling is finished!');
        var list = data.data;
        var html = '';
        for(var i=0; i<list.length; i++){
            html += `
                <tr>
                    <th scope="row">`+ (i + 1) +`</th>
                    <td width="20%"><a href="`+ list[i].url +`">`+ list[i].title +`</td>
                    <td>`+ list[i].contents +`</td>
                    <td>`+ list[i].views +`</td>
                    <td>`+ list[i].recommends +`</td>
                    <td>`+ list[i].published_date +`</td>
                </tr>
            `;
        }
        $('#board').html(html);
    }
}

function showCrawledDataFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showData(data){
    var list = data.data;
    var html = '';
    for(var i=0; i<list.length; i++){
        html += `
            <tr>
                <th scope="row">`+ (i + 1) +`</th>
                <td width="20%"><a href="`+ list[i].url +`">`+ list[i].title +`</td>
                <td>`+ list[i].contents +`</td>
                <td>`+ list[i].views +`</td>
                <td>`+ list[i].recommends +`</td>
                <td>`+ list[i].published_date +`</td>
            </tr>
        `;
    }
    $('#progress').attr("class", "");
    $('#progress').empty();
    $('#board').html(html);
}

function showDataFail(data){
    $('#progress').attr("class", "alert alert-danger");
    $('#progress').html(data.responseJSON.error);
    $('#board').empty();
}
