import { product } from "./productList.js";
const cartItems = JSON.parse(localStorage.getItem("cartItems"));
const tBody = document.getElementById("tableBd");
function numberWithCommas(x) {
  var parts = x.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  return parts.join(".");
}
function getDiscountRate() {
  const date = new Date();
  const weekDay = date.getDate();
  const hours = date.getHours();
  const totalMins = hours * 60 + date.getMinutes();
  if (
    weekDay >= 1 &&
    weekDay <= 3 &&
    ((totalMins >= 420 && totalMins <= 660) ||
      (totalMins >= 780 && totalMins <= 1020))
  )
    return 0.1;
  return 0;
}

let xxx = "";
let sum = 0;
cartItems.forEach((value) => {
  const item = product[value.id];
  xxx += `<tr>
    <td><img src="${item.image}" width="100px" height="100px"/></td>
    <td>${item.name}</td>
    <td>${value.quantity}</td>
    <td>${item.price}</td>
    <td>${item.price * value.quantity}</td>
    <td><button onclick="removeItem('${
      value.id
    }')"><i class="fa fa-trash"></i></button></td>
    </tr>`;
  sum += value.quantity * item.price;
});
xxx += `<tr>
<td colspan="6" style="text-align: right; padding: 5px 10px">Tổng thành tiền (A) = ${numberWithCommas(
  sum
)} đ</td>
</tr>`;
xxx += `<tr>
<td colspan="6" style="text-align: right; padding: 5px 10px">Chiết khấu (B) = ${getDiscountRate()} * A = ${
  getDiscountRate() * sum
} đ</td>
</tr>`;

xxx += `<tr>
<td colspan="6" style="text-align: right; padding: 5px 10px">Thuế (C) = 10% * (A-B)= ${
  (10 * (sum - getDiscountRate() * sum)) / 100
} đ</td>
</tr>`;

xxx += `<tr>
<td colspan="6" style="text-align: right; padding: 5px 10px">Tổng đơn hàng (D) = A - B + C= ${numberWithCommas(
  sum + (10 * (sum - getDiscountRate() * sum)) / 100 - getDiscountRate() * sum
)} đ</td>
</tr>`;
tBody.innerHTML = xxx;
