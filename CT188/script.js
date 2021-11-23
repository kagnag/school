function lienhe(frm) {
  var emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  if (emailReg.test(email.value) == false) {
    /*mã xử lý dữ liệu không hợp lệ*/
    return false;
  }
  if (psw.value.length < 8) {
    /*mã xử lý dữ liệu không hợp lệ*/
    return false;
  }
  if (hoten.value.length < 4) {
    /*mã xử lý dữ liệu không hợp lệ*/
    return false;
  }
  if (lienhe.value.length < 10) {
    /*mã xử lý dữ liệu không hợp lệ*/
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

function sanpham(frm) {
  if (typeof localStorage[code] === "undefined") {
    window.localStorage.setItem(code, number);
  }
  window.localStorage.setItem(code, 100);
  number = parseInt(document.getElementById(code).value);
  current = parseInt(window.localStorage.getItem(code));
  window.localStorage.setItem(code, current + number);
}
