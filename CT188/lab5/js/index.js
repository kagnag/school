function numberWithCommas(x) {
  var parts = x.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  return parts.join(".");
}
$(document).ready(() => {
  // $("#loaded").addClass("loaded");
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  const lanSelectors = $(".langSelector");
  const vn = lanSelectors[0];
  const us = lanSelectors[1];
  $(vn).on("click", () => {
    setLang("vi-VN");
  });
  $(us).on("click", () => {
    setLang("en-US");
  });
  function setLang(lang) {
    localStorage.setItem("lang", lang);
    location.reload();
  }
  function getLang() {
    const lang = localStorage.getItem("lang");
    const objectKeys = Object.keys(labels);
    objectKeys.forEach((value) => {
      $(`#${value}`)
        .html(labels[value][lang])
        .attr("title", labels[value][lang]);
    });
    const data = [];
    courseList.forEach((value) => {
      data.push({
        ...value,
        startDate: new Date(value.startDate).toLocaleDateString(lang),
        endDate: new Date(value.endDate).toLocaleDateString(lang),
        name: value.name[lang],
        fee: numberWithCommas(value.fee[lang]),
        checkbox: `<div class="bg-success text-center width"><i class="far fa-check-square"></i></div>`,
      });
    });
    $("#table").bootstrapTable({
      columns: [
        {
          field: "code",
          title: labels["COURSES_CODE"][lang],
        },
        {
          field: "name",
          title: labels["COURSES_NAME"][lang],
        },
        {
          field: "startDate",
          title: labels["COURSES_STARTDATE"][lang],
        },
        {
          field: "endDate",
          title: labels["COURSES_ENDDATE"][lang],
        },
        {
          field: "fee",
          title: labels["COURSES_FEE"][lang],
        },
        {
          field: "checkbox",
          title: "",
        },
      ],
      data,
    });
  }
  getLang();
});
