$(document).ready(() => {
  const date = new Date();
  const month = date.getMonth() + 1;
  const ads = `Khách hàng có ngày sinh trong tháng ${month}
    sẽ được tặng 2 phần sữa chua dâu cho đơn hàng đầu tiên trong
    tháng.`;
  $("footer").append(
    `<div id='adscontainer'><span id='adstext'><h2> ${ads} </h2></span ></div >`
  );
  const W = $("main").width() / 2;

  if (W >= 700) {
    adsTopEffect();
  } else {
    adsLeftEffect();
  }
  function adsLeftEffect() {
    $("#adscontainer").addClass("adsleftcontainer container");
    $("#adscontainer").css("left", $("main").position().left);
    $("#adscontainer").css("width", $("main").width());
    $("#adstext").addClass("adslefttext adstext");
    $("#adstext").css("left", $("#adscontainer").width());
    $("#adstext").animate(
      {
        left: 0,
      },
      3000,
      adsLeftEffect
    );
  }
  function adsTopEffect() {
    $("#adscontainer").addClass(" adstopcontainer container");
    $("#adscontainer").css("width", W / 5);
    $("#adstext").addClass("adstoptext adstext");
    $("#adstext").css("top", -$("#adscontainer").height() / 5);
    $("#adstext").animate(
      {
        top: $("#adscontainer").height() + $("#adstext").height(),
      },
      30000,
      adsTopEffect
    );
  }
});
