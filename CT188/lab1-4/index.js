const frm_search = document.getElementById("frm_search");
const btnSubmit = document.getElementById("btnSubmit");
const inpSearch = document.getElementById("search");

frm_search.addEventListener("submit", (e) => {
  e.preventDefault();
  const value = inpSearch.value;
  if (value.length > 0) {
    frm_search.submit();
  }
});
function itemSaved(cartItems, id) {
  // let x = JSON.parse(cartItem);
  const arr = [];
  cartItems.forEach((value) => {
    arr.push(value.id);
  });
  return arr.indexOf(id);
}
function cartItemsSaved(id, quantity) {
  const cartItems = JSON.parse(localStorage.getItem("cartItems"));

  if (!cartItems) {
    localStorage.setItem(
      "cartItems",
      JSON.stringify([{ id, quantity: parseInt(quantity) }])
    );
  } else {
    const index = itemSaved(cartItems, id);
    if (index !== -1) {
      let newQuan = parseInt(cartItems[index].quantity);
      newQuan += parseInt(quantity);
      cartItems[index].quantity = newQuan;
      localStorage.setItem("cartItems", JSON.stringify(cartItems));
    } else {
      const item = { id, quantity: parseInt(quantity) };
      cartItems.push(item);
      localStorage.setItem("cartItems", JSON.stringify(cartItems));
    }
  }
}
function addCart(item) {
  const quantity = document.getElementById(item).value;
  cartItemsSaved(item, quantity);
}

const cart = document.getElementById("btnCart");
cart.addEventListener("click", () => {
  window.location.href = "./giohang.html";
});
function removeItem(id) {
  const cartItems = JSON.parse(localStorage.getItem("cartItems"));
  const arr = [];
  cartItems.forEach((value) => {
    arr.push(value.id);
  });
  const index = arr.indexOf(id);
  cartItems.splice(index, 1);
  localStorage.setItem("cartItems", JSON.stringify(cartItems));
  location.reload();
}
