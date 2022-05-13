function getGridWrapper(tableName) {
    return document.querySelector(`#${tableName}_wrapper`);
}

function addOrRemoveScroll(grid, limitWidth) {
    const className = 'overflow-auto';
    grid.clientWidth < limitWidth ? grid.classList.add(className) : grid.classList.remove(className);
}

function drag(tableName) {
    /* https://codepen.io/thenutz/pen/VwYeYEE */
    let isDown = false;
    let startX;
    let scrollLeft;
    const grid = getGridWrapper(tableName);

    grid.addEventListener('mousedown', (e) => {
        isDown = true;
        grid.classList.add('active');
        startX = e.pageX - grid.offsetLeft;
        scrollLeft = grid.scrollLeft;
    });

    grid.addEventListener('mouseleave', () => {
        isDown = false;
        grid.classList.remove('active');
    });

    grid.addEventListener('mouseup', () => {
        isDown = false;
        grid.classList.remove('active');
    });

    grid.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - grid.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        grid.scrollLeft = scrollLeft - walk;
    });
}

function addTableResizeEvent(tableName) {
    const table = $(`#${tableName}`);

    table.on('column-sizing.dt', function (e, settings) {
        handleTableResizeEvent(tableName);
    });

    table.on('init.dt', function (e, settings) {
        handleTableResizeEvent(tableName);
        drag(tableName);
    });
}

function handleTableResizeEvent(tableName) {
    // Add horizontal scrollbar to grid
    const gridWrapper = getGridWrapper(tableName);
    switch (tableName) {
        case 'gridMedicine':
            addOrRemoveScroll(gridWrapper, 600);
            break;
    }
}

function initDataTable(grids) {
    // Initialize Datatable according to the grid name
    const pathName = '/static/assets/datatables/pt_br.json';

    grids.forEach(gridName => {
        const grid = document.querySelector(`#${gridName}`);

        if (grid) {
            const gridSize = grid.rows[0].cells.length;

            const orderable = false;
            const actionColumns = [
                gridSize - 1, // History
                gridSize - 2, // Deactivate
                gridSize - 3, // Edit
            ];
            const searching = false;
            const responsive = true;

            switch (gridName) {
                case 'gridMedicine':
                    $(`#${gridName}`).DataTable({
                        columnDefs: [
                            {
                                orderable: orderable,
                                targets: actionColumns,
                            },
                            {
                                width: '15%',
                                targets: 0, // Name
                            },
                            {
                                width: '30%',
                                targets: 1, // Description
                            },
                            {
                                width: '10%',
                                targets: 2, // Batch
                            },
                            {
                                width: '5%',
                                targets: 3, // Expiration Date
                            },
                            {
                                width: '0%',
                                targets: 4, // Stock Quantity
                            },
                            {
                                width: '0%',
                                targets: 5, // Edit
                            },
                            {
                                width: '0%',
                                targets: 6, // Deactivate
                            },
                            {
                                width: '0%',
                                targets: 7, // History
                            },
                        ],
                        language: {
                            url: pathName
                        },
                        searching: searching,
                        responsive: responsive,
                    });

                    addTableResizeEvent(gridName);
                    break;
            }
        }
    });
}

window.addEventListener('DOMContentLoaded', event => {
    const grids = [
        'gridMedicine',
    ]

    initDataTable(grids);
});
