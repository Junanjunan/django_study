function ajaxRender(){
    // const body = document.querySelector("body")
    const html = document.querySelector("html")
    $.ajax({
        url: '/ajax-test',
        method: 'GET',
        success: function (data) {
            // body.innerHTML = data.contents;
            html.innerHTML = data.contents;
            console.log(data.status);
        }
    });
}