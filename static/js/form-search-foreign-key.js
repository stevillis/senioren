function findForeignKey(form, model) {
  const id_model = "#id_" + model;
  const selectorModel = id_model + "-TOTAL_FORMS";
  const indexModel = $(selectorModel).val();
  const tableModel = $(id_model + "-__prefix__-DELETE")
    .parents("table")
    .clone();

  tableModel.find(":input").each(function () {
    for (const attr of ["name", "id"])
      $(form).attr(attr, $(form).attr(attr).replace("__prefix__", indexModel));
  });

  tableModel.insertBefore($(form));
  $(selectorModel).val(parseInt($(selectorModel).val()) + 1);
  tableModel.slideDown();
}

(function ($) {
  $("#form-crud").click(function () {
    findForeignKey(this, "patient");
    findForeignKey(this, "nursing_professional");
  });
})($);
