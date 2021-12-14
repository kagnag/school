var adsVerEffect = (w) => {
  $("#adscontainer").addClass("adstopcontainer container");
  $("#adscontainer").css("width", Math.round(w) - 20);
  $("span#adstext").addClass("adstoptext adstext");
  $("span#adstext").css("top", $("#adscontainer").height());
  $("span#adstext").animate(
    { top: `-=${$("#adscontainer").height() + $("span#adstext").height()}` },
    30000,
    adsVerEffect
  );
};

var adsHorEffect = () => {
  $("#adscontainer").addClass("adsleftcontainer container");
  $(".container h2").css({
    margin: 0,
    "line-height": "50px",
  });
  $("#adscontainer").css("left", $("main").position().left);
  $("#adscontainer").css("width", $("main").width());
  $("span#adstext").addClass("adslefttext adstext");
  $("span#adstext").css("left", $("#adscontainer").width());
  $("span#adstext").animate(
    { left: `-=${$("#adscontainer").width() + $("span#adstext").width()}` },
    30000,
    adsHorEffect
  );
};

var headlineContent = [
  {
    title: "Bánh flan sữa chua - sự kết hợp hoàn hảo",
    photo: "images/trangchu/headline/headline1.jpg",
  },
  {
    title: "Sữa chua làm từ sữa dê - đậm đà hương vị khó quên",
    photo: "images/trangchu/headline/headline2.jpg",
  },
  {
    title: "Thưởng thức sữa chua theo cách của bạn",
    photo: "images/trangchu/headline/headline3.jpg",
  },
];

var headlineDataInit = () => {
  headlineContent.forEach((e) => {
    let featuredPrdDiv = $("<div></div>")
      .append($("<span></span>").append($("<h3></h3>").text(e.title)))
      .append($("<img></img>").attr("src", e.photo));

    $("#headline").append(featuredPrdDiv);
  });
};

$(document).ready(() => {
  var d = new Date();
  var ads =
    "Khách hàng có ngày sinh trong tháng " +
    d.getMonth() +
    " sẽ được tặng 2 phần sữa chua dâu cho đơn hàng đầu tiên trong tháng.";
  $("footer").append(
    "<div id='adscontainer'><span id='adstext'><h2>" +
      ads +
      "</h2></span></div>"
  );

  var w = ($(window).width() - $("main").width()) / 2;
  if (w >= 200) adsVerEffect(w);
  else adsHorEffect();

  headlineDataInit();

  $("#headline > div").each((i, e) => {
    if (i > 0) $(e).hide();
  });

  setInterval(() => {
    var firstElement = $("#headline > div:first-child");
    firstElement.hide();
    firstElement.next().fadeIn(1000);
    firstElement.appendTo($("#headline"));
  }, 5000);
});
