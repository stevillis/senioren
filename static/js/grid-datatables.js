function getGridWrapper(tableName) {
  return document.querySelector(`#${tableName}_wrapper`);
}

function addOrRemoveScroll(grid, minLimitWidth) {
  const className = "overflow-auto";
  grid.clientWidth < minLimitWidth ?
    grid.classList.add(className) :
    grid.classList.remove(className);
}

function drag(tableName) {
  /* https://codepen.io/thenutz/pen/VwYeYEE */
  let isDown = false;
  let startX;
  let scrollLeft;
  const grid = getGridWrapper(tableName);

  grid.addEventListener("mousedown", (e) => {
    isDown = true;
    grid.classList.add("active");
    startX = e.pageX - grid.offsetLeft;
    scrollLeft = grid.scrollLeft;
  });

  grid.addEventListener("mouseleave", () => {
    isDown = false;
    grid.classList.remove("active");
  });

  grid.addEventListener("mouseup", () => {
    isDown = false;
    grid.classList.remove("active");
  });

  grid.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - grid.offsetLeft;
    const walk = (x - startX) * 3; //scroll-fast
    grid.scrollLeft = scrollLeft - walk;
  });
}

function addTableResizeEvent(tableName) {
  const table = $(`#${tableName}`);

  table.on("column-sizing.dt", function (e, settings) {
    handleTableResizeEvent(tableName);
  });

  table.on("init.dt", function (e, settings) {
    handleTableResizeEvent(tableName);
    drag(tableName);
  });
}

function handleTableResizeEvent(tableName) {
  // Add horizontal scrollbar to grid
  const gridWrapper = getGridWrapper(tableName);
  switch (tableName) {
    case "gridMedicine":
    case "gridPatient":
    case "gridNursingProfessional":
    case "gridMedicalEvaluation":
    case "gridMedication":
      addOrRemoveScroll(gridWrapper, 768);
      break;
  }
}

function padTo2Digits(num) {
  return num.toString().padStart(2, "0");
}

function formatDate(date) {
  return [
    padTo2Digits(date.getDate()),
    padTo2Digits(date.getMonth() + 1),
    date.getFullYear(),
  ].join("/");
}

function formatDateTime(date) {
  const day = padTo2Digits(date.getDate());
  const month = padTo2Digits(date.getMonth() + 1);
  const year = date.getFullYear();
  const hours = padTo2Digits(date.getHours());
  const minutes = padTo2Digits(date.getMinutes());
  const seconds = padTo2Digits(date.getSeconds());

  return `${[day, month, year].join("/")} ${hours}:${minutes}:${seconds}`;
}

function initDataTable(grids) {
  // Initialize Datatable according to the grid name
  const pathName = "/static/assets/datatables/pt_br.json";

  const deactivateMsg = "Inativar";
  const editMsg = "Editar";

  grids.forEach((gridName) => {
    const grid = document.querySelector(`#${gridName}`);

    if (grid) {
      switch (gridName) {
        case "gridMedicine":
          $(document).ready(function () {
            const host = document.location.origin;
            $(`#${gridName}`).DataTable({
              serverSide: true,
              sAjaxSource: `${host}/medicines/medicine/data/`,
              order: [
                [1, "asc"]
              ],
              columns: [{
                  name: "name",
                  data: 1,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/medicine/detail/${row[0]}/">${data}</a>`;
                  },
                },
                {
                  name: "description",
                  data: 2
                },
                {
                  name: "batch",
                  data: 3
                },
                {
                  name: "expiration_date",
                  data: 4,
                  searchable: false,
                  render: function (data, type, row, meta) {
                    const date = `${row[4]}T00:00:00`;
                    return `${formatDate(new Date(date))}`;
                  },
                },
                {
                  name: "stock_qty",
                  data: 5,
                  searchable: false,
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${editMsg}">
                            <a href="/medicines/medicine/update/${row[0]}/" class="btn btn-warning btn-xs"
                              data-title="${editMsg}" aria-label="${editMsg}">
                                <span class="fa fa-edit"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${deactivateMsg}">
                            <a href="/medicines/medicine/deactivate/${row[0]}/" class="btn btn-danger btn-xs"
                              data-title="${deactivateMsg}" aria-label="${deactivateMsg}">
                                <span class="fa fa-trash"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
              ],
              language: {
                url: pathName,
              },
              searching: true,
              responsive: true,
            });
          });
          addTableResizeEvent(gridName);
          break;
        case "gridPatient":
          $(document).ready(function () {
            const host = document.location.origin;
            $(`#${gridName}`).DataTable({
              serverSide: true,
              sAjaxSource: `${host}/medicines/patient/data/`,
              order: [
                [1, "asc"]
              ],
              columns: [{
                  name: "name",
                  data: 1,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/patient/detail/${row[0]}/">${data}</a>`;
                  },
                },
                {
                  name: "cpf",
                  data: 2
                },
                {
                  name: "birth_date",
                  data: 3,
                  searchable: false,
                  render: function (data, type, row, meta) {
                    const date = `${row[3]}T00:00:00`;
                    return `${formatDate(new Date(date))}`;
                  },
                },
                {
                  name: "phone",
                  data: 4,
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${editMsg}">
                            <a href="/medicines/patient/update/${row[0]}/" class="btn btn-warning btn-xs"
                              data-title="${editMsg}" aria-label="${editMsg}">
                                <span class="fa fa-edit"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${deactivateMsg}">
                            <a href="/medicines/patient/deactivate/${row[0]}/" class="btn btn-danger btn-xs"
                              data-title="${deactivateMsg}" aria-label="${deactivateMsg}">
                                <span class="fa fa-trash"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
              ],
              language: {
                url: pathName,
              },
              searching: true,
              responsive: true,
            });
          });
          addTableResizeEvent(gridName);
          break;
        case "gridNursingProfessional":
          $(document).ready(function () {
            const host = document.location.origin;
            $(`#${gridName}`).DataTable({
              serverSide: true,
              sAjaxSource: `${host}/medicines/nursing-professional/data/`,
              order: [
                [1, "asc"]
              ],
              columns: [{
                  name: "name",
                  data: 1,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/nursing-professional/detail/${row[0]}/">${data}</a>`;
                  },
                },
                {
                  name: "coren",
                  data: 2
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${editMsg}">
                            <a href="/medicines/nursing-professional/update/${row[0]}/" class="btn btn-warning btn-xs"
                              data-title="${editMsg}" aria-label="${editMsg}">
                                <span class="fa fa-edit"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${deactivateMsg}">
                            <a href="/medicines/nursing-professional/deactivate/${row[0]}/" class="btn btn-danger btn-xs"
                              data-title="${deactivateMsg}" aria-label="${deactivateMsg}">
                                <span class="fa fa-trash"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
              ],
              language: {
                url: pathName,
              },
              searching: true,
              responsive: true,
            });
          });
          addTableResizeEvent(gridName);
          break;
        case "gridMedicalEvaluation":
          $(document).ready(function () {
            const host = document.location.origin;
            $(`#${gridName}`).DataTable({
              serverSide: true,
              sAjaxSource: `${host}/medicines/medical-evaluation/data/`,
              order: [
                [1, "asc"]
              ],
              columns: [{
                  name: "patient",
                  data: 5,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/medical-evaluation/detail/${row[0]}/">${data}</a>`;
                  },
                },
                {
                  name: "schedule",
                  data: 1,
                  render: function (data, type, row, meta) {
                    const date = `${row[1]}`;
                    return `${formatDateTime(new Date(date))}`;
                  },
                },
                {
                  name: "hurt_pressure",
                  data: 2
                },
                {
                  name: "glucose",
                  data: 3
                },
                {
                  name: "observation",
                  data: 4
                },
                {
                  name: "nursing_professional",
                  data: 6
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${editMsg}">
                            <a href="/medicines/medical-evaluation/update/${row[0]}/" class="btn btn-warning btn-xs"
                              data-title="${editMsg}" aria-label="${editMsg}">
                                <span class="fa fa-edit"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${deactivateMsg}">
                            <a href="/medicines/medical-evaluation/deactivate/${row[0]}/" class="btn btn-danger btn-xs"
                              data-title="${deactivateMsg}" aria-label="${deactivateMsg}">
                                <span class="fa fa-trash"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
              ],
              language: {
                url: pathName,
              },
              searching: true,
              responsive: true,
            });
          });
          addTableResizeEvent(gridName);
          break;
        case "gridMedication":
          $(document).ready(function () {
            const host = document.location.origin;
            $(`#${gridName}`).DataTable({
              serverSide: true,
              sAjaxSource: `${host}/medicines/medication/data/`,
              order: [
                [1, "desc"]
              ],
              columns: [{
                  name: "schedule",
                  data: 1,
                  render: function (data, type, row, meta) {
                    const date = `${row[1]}`;
                    return `${formatDateTime(new Date(date))}`;
                  },
                },
                {
                  name: "patient",
                  data: 2,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/medication/detail/${row[0]}/">${data}</a>`;
                  },
                },
                // {name: "medicine", data: 2},
                {
                  name: "nursing_professional",
                  data: 3
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${editMsg}">
                            <a href="/medicines/medication/update/${row[0]}/" class="btn btn-warning btn-xs"
                              data-title="${editMsg}" aria-label="${editMsg}">
                                <span class="fa fa-edit"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
                {
                  searchable: false,
                  orderable: false,
                  render: function (data, type, row, meta) {
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${deactivateMsg}">
                            <a href="/medicines/medication/deactivate/${row[0]}/" class="btn btn-danger btn-xs"
                              data-title="${deactivateMsg}" aria-label="${deactivateMsg}">
                                <span class="fa fa-trash"></span>
                            </a>
                        </p>
                    </td>
                    `;
                  },
                },
              ],
              language: {
                url: pathName,
              },
              searching: true,
              responsive: true,
            });
          });
          addTableResizeEvent(gridName);
          break;
      }
    }
  });
}

window.addEventListener("DOMContentLoaded", (event) => {
  const grids = [
    "gridMedicine",
    "gridPatient",
    "gridNursingProfessional",
    "gridMedicalEvaluation",
    "gridMedication",
  ];

  initDataTable(grids);
});