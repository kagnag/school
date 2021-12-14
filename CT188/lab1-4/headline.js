const headlineContent = [
  {
    title: "Bánh flan sữa chua - sự kết hợp hoàn hảo",
    photo: "./images/trangchu/headline/headline1.jpg",
  },
  {
    title: "Sữa chua làm từ sữa dê - đậm đà hương vị khó quên",
    photo: "./images/trangchu/headline/headline2.jpg",
  },
  {
    title: "Thưởng thức sữa chua theo cách của bạn",
    photo: "./images/trangchu/headline/headline3.jpg",
  },
];
$(document).ready(function () {
  let html = "";
  const headline = $("#headline");
  headlineContent.forEach(function (item, index) {
    html += `<div>
        <span>
        <h3>${item.title}</h3>
        </span>
        <img src="${item.photo}"/>
        </div>`;
  });
  headline.html(html);
  const headlineChild = $("#headline>div");
  let f = headlineChild[0];
  let s = headlineChild[1];
  let t = headlineChild[2];
  const arr = [f, s, t];
  $(s).hide();
  $(t).hide();
  setInterval(() => {
    $(arr[0]).hide();
    $(arr[1]).fadeIn(1000);
    console.log(arr);
    f = arr.shift();
    arr.push(f);
  }, 5000);
});
