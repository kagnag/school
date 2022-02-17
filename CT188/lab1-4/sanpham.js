import { type, product, vn } from "./productList.js";

const article = document.getElementsByTagName("article");
const articleElement = article[0];
const section = (section) => {
    return `<section>${section}</section>`
}
const appendProduct = () => {
    const div = document.createElement("div");
    const h1 = document.createElement("h1");
    const keyType = Object.keys(type);
    let h12 = "";
    keyType.forEach(value => {
        const name = vn[value];
        h1.innerText = name;
        h12 += `<h1>${name}</h1>`
        let div1 = '';
        type[value].forEach(value => {
            const product1 = product[value];
            div1 += `<div>
            <img src="${product1.image}" alt="" />
            <h2>${product1.name}</h2>
            ${product1.des} <a href="#">Xem chi tiết</a>

            <span>
              Số Lượng:
              <input id="${value}"type="number" max="100" min="0" value="1" />
              <button onclick="addCart('${value}')" >Đặt hàng</button>
            </span>
            </div>`
        })
        const section1 = section(div1);
        h12 += section1;
    })
    articleElement.innerHTML = h12;
}

appendProduct();