function checkKeySearch(e) {
  var key = event.which | event.keyCode;
  if (key == 32) {
    doSearch();
  }
}

function doSearch() {
  var frm = document.forms["frm-search"];
  if (frm.words.value.length > 0) frm.submit();
}

function showSearch() {
  var url = new URL(window.location);
  var ws = url.searchParams.get("words");
  document.getElementById("searchDetail").innerHTML =
    "<h1>Từ khoá tìm kiếm</h1> <b>" + ws + "</b>";
}

// bai tap 2
function loginValidate(frm) {
  var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  if (emailReg.test(frm.email.value) == false) {
    alert("Vui lòng nhập lại email hợp lệ");
    frm.email.focus();
    return false;
  }
  if (frm.psw.value.length < 8) {
    alert("Mật khẩu có tối thiểu 8 ký tự");
    frm.psw.focus();
    return false;
  }

  alert("Đã gửi dữ liệu!");
  return true;
}

function registerValidate(frm) {
  var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  if (emailReg.test(frm.email.value) == false) {
    alert("Vui lòng nhập lại email hợp lệ");
    frm.email.focus();
    return false;
  }
  if (frm.psw.value.length < 8) {
    alert("Mật khẩu có tối thiểu 8 ký tự");
    frm.psw.focus();
    return false;
  }
  if (frm.psw2.value.length < 8) {
    alert("Mật khẩu có tối thiểu 8 ký tự");
    frm.psw2.focus();
    return false;
  }
  if (frm.psw.value.length != frm.psw2.value.length) {
    alert("Mật khẩu và Nhập lại mật khẩu phải giống nhau");
    frm.psw.focus();
    return false;
  }
  alert("Đã gửi dữ liệu!");
  return true;
}

var itemList = {
  sp001: {
    name: "Sữa Chua Vị Kiwi",
    price: 21000,
    photo: "images/sanpham/kiwi.jpg",
  },
  sp002: {
    name: "Sữa Chua Vị Xoài",
    price: 22000,
    photo: "images/sanpham/mango.jpg",
  },
  sp003: {
    name: "Sữa Chua Vị Dưa lưới",
    price: 23000,
    photo: "images/sanpham/cantaloupe.jpg",
  },
  sp004: {
    name: "Sữa Chua Vị Mâm Xôi",
    price: 24000,
    photo: "images/sanpham/blackberry.jpg",
  },
  sp005: {
    name: "Sữa Chua Vị Dâu Tây",
    price: 25000,
    photo: "images/sanpham/strawberry.jpg",
  },
  sp006: {
    name: "Sữa Chua Vị Việt Quất",
    price: 26000,
    photo: "images/sanpham/blueberry.jpg",
  },
  sp007: {
    name: "Sữa Chua Vị Bưởi",
    price: 27000,
    photo: "images/sanpham/grapes.jpg",
  },
  sp008: {
    name: "Sữa Chua Vị Táo Xanh",
    price: 28000,
    photo: "images/sanpham/green-apple.jpg",
  },
  sp009: {
    name: "Sữa Chua Vị Dứa",
    price: 29000,
    photo: "images/sanpham/pineapple.jpg",
  },
};

function addCart(code) {
  var number = parseInt(document.getElementById(code).value);
  var name = itemList[code].name;
  if (number == 0) return;
  if (typeof localStorage[code] === "undefined") {
    window.localStorage.setItem(code, number);
  } else {
    var current = parseInt(window.localStorage.getItem(code));
    if (current + number > 100) {
      window.localStorage.setItem(code, 100);
      alert(
        "Mỗi mặt hàng chỉ có thể đặt 100 sản phẩm cho mỗi đơn hàng. Bạn đã đặt 100 sản phẩm"
      );
      return;
    } else window.localStorage.setItem(code, current + number);
  }
  alert(
    "Đã cập nhật sản phẩm" +
      name +
      " với số lượng " +
      number +
      " vào giỏ hàng. Số lượng sản phẩm là..." +
      number
  );
}

function openCart() {
  window.location.href = "donhang.html";
}

function showCart() {
  var formatter = new Intl.NumberFormat("vi-VN", {
    style: "currency",
    currency: "VND",
  });
  var container = document
    .getElementById("cartDetail")
    .getElementsByTagName("tbody")[0];
  container.innerHTML = "";
  var sum = 0;
  totalPreTax = 0;
  discountRate = getDiscountRate();
  taxRate = 0;
  discount = 0;
  tax = 0;
  for (var i = 0; i < window.localStorage.length; i++) {
    if (typeof itemList[localStorage.key(i)] === "undefined") continue;
    var tr = document.createElement("tr");
    photoCell = document.createElement("td");
    nameCell = document.createElement("td");
    priceCell = document.createElement("td");
    numberCell = document.createElement("td");
    photoCell = document.createElement("td");
    removeCell = document.createElement("td");
    removeLink = document.createElement("a");
  }
}
