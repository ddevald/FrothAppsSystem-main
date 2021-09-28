function add(e) {
    var tr = $(".milestone-title")[0].parentNode.cloneNode(true);
    var tb = $(".milestone-title")[0].parentNode.parentNode;
    // tb.appendChild(tr);
    if(tb.rows.length >= 6) {
        $(e).parent().hide();
    }
    $(".milestone-title").last().parent().after(tr);
}