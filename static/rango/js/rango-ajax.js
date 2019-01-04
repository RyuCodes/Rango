$(document).ready(function(){
  $("#likes").click(function(){
      var catid;
      catid = $(this).attr("data-catid");
      //$.get only exists in the full version of jQuery.  Slim version will show error
      // response from get request will go in as data
      $.get("/rango/like_category/", {category_id: catid}, function(data){
        $("#like_count").html(data);
        $("#likes").hide();
      });
  });

  // returns render html as data, which passes into id=cats
  // div is updated with a new category list.html overwriting everything in the div
  $('#suggestion').keyup(function(){
    var query;
    query = $(this).val();
    $.get("/rango/suggest_category/", {suggestion: query}, function (data){
      $('#cats').html(data);
    });
  });

  // For auto-add; look for defined class "rango-addpage"
  $(".rango-addpage").click(function(){
    var cat_id, title, url;
    var test_val;
    catid = $(this).attr("data-catid");
    title = $(this).attr("data-title");
    url = $(this).attr("data-url");

    $.get("/rango/auto_add_page/", {category_id: catid, title: title, url: url}, function(data){
        $("#page-display").html(data);
    });

  });

});
