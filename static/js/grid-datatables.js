function getGridWrapper(tableName) {
  return document.querySelector(`#${tableName}_wrapper`);
}

function addOrRemoveScroll(grid, limitWidth) {
  const className = "overflow-auto";
  grid.clientWidth < limitWidth
    ? grid.classList.add(className)
    : grid.classList.remove(className);
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
      addOrRemoveScroll(gridWrapper, 600);
      break;
    case "gridPatient":
      addOrRemoveScroll(gridWrapper, 600);
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

function initDataTable(grids) {
  // Initialize Datatable according to the grid name
  const pathName = "/static/assets/datatables/pt_br.json";

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
              order: [[1, "asc"]],
              columns: [
                {
                  name: "name",
                  data: 1,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/medicine/detail/${row[0]}/">${data}</a>`;
                  },
                },
                { name: "description", data: 2 },
                { name: "batch", data: 3 },
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
                  render: function (data, type, row, meta) {
                    const editMsg = gettext("Edit");
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
                  render: function (data, type, row, meta) {
                    const deactivateMsg = gettext("Deactivate");
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
                {
                  searchable: false,
                  render: function (data, type, row, meta) {
                    const historyMsg = gettext("History");
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${historyMsg}">
                            <a href="#" class="btn btn-info btn-xs"
                              data-title="${historyMsg}" aria-label="${historyMsg}">
                                <span class="fa fa-history"></span>
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
              order: [[1, "asc"]],
              columns: [
                {
                  name: "name",
                  data: 1,
                  render: function (data, type, row, meta) {
                    return `<a href="/medicines/patient/detail/${row[0]}/">${data}</a>`;
                  },
                },
                { name: "cpf", data: 2 },
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
                  render: function (data, type, row, meta) {
                    const editMsg = gettext("Edit");
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
                  render: function (data, type, row, meta) {
                    const deactivateMsg = gettext("Deactivate");
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
                {
                  searchable: false,
                  render: function (data, type, row, meta) {
                    const historyMsg = gettext("History");
                    return `
                      <td>
                        <p class="d-flex justify-content-center m-auto" data-placement="middle" data-toggle="tooltip"
                          title="${historyMsg}">
                            <a href="#" class="btn btn-info btn-xs"
                              data-title="${historyMsg}" aria-label="${historyMsg}">
                                <span class="fa fa-history"></span>
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
  const grids = ["gridMedicine", "gridPatient"];

  initDataTable(grids);
});
