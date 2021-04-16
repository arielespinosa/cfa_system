var TableScienceWork = function () {

    var initTablePonencys = function () {

        $('#tbl_ponencys tfoot th').each( function () {
            var title = $(this).text();

            if(title.length > 0){
                $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
            }
        } );

        var table = $('#tbl_ponencys');

        // begin first table
        table.DataTable({
             pageLength: 15,
                "lengthMenu": [
                    [5, 15, 20, -1],
                    [5, 15, 20, "Todos"]
                ],
                responsive: true,
                dom: '<"html5buttons"B>lTfgitp',
                ajax: '/piloto/ponency_realized/',
                "columnDefs": [
                    {
                        'orderable': false,
                        'targets': [0]
                    },
                ],
                language: {
                    aria: {
                        "sortAscending": ": activate to sort column ascending",
                        "sortDescending": ": activate to sort column descending"
                    },
                    "emptyTable": "No hay datos en la tabla",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                    "infoEmpty": "No se encontraron registros",
                    "infoFiltered": "(filtered1 from _MAX_ total records)",
                    "lengthMenu": "Mostrar _MENU_",
                    "search": "Buscar:",
                    "zeroRecords": "No se encontraron resultados",
                    "paginate": {
                        "previous":"Anterior",
                        "next": "Próximo",
                        "last": "Último",
                        "first": "Primero"
                    }
                },

                buttons: [
                    {extend: 'copy'},
                    {extend: 'csv'},
                    {extend: 'excel', title: 'ExampleFile'},
                    {extend: 'pdf', title: 'ExampleFile'},
                    {extend: 'print',
                     customize: function (win){
                            $(win.document.body).addClass('white-bg');
                            $(win.document.body).css('font-size', '10px');

                            $(win.document.body).find('table')
                                    .addClass('compact')
                                    .css('font-size', 'inherit');
                    }
                    }
                ],

            initComplete: function () {
            // Apply the search
                this.api().columns().every( function () {
                    var that = this;

                    $( 'input', this.footer() ).on( 'keyup change clear', function () {
                        if ( that.search() !== this.value ) {
                            that
                                .search( this.value )
                                .draw();
                        }
                    } );
                } );
            }
        });

        var tableWrapper = jQuery('#tbl_ponencys_wrapper');

        table.find('.group-checkable').change(function () {
            var set = jQuery(this).attr("data-set");
            var checked = jQuery(this).is(":checked");
            jQuery(set).each(function () {
                if (checked) {
                    $(this).prop("checked", true);
                    $(this).parents('tr').addClass("active");
                } else {
                    $(this).prop("checked", false);
                    $(this).parents('tr').removeClass("active");
                }
            });
        });

        table.on('change', 'tbody tr .checkboxes', function () {
            $(this).parents('tr').toggleClass("active");
        });
    }

    var initTableThesis = function () {

            $('#tbl_thesis tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_thesis');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/thesis/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_thesis_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }

    var initTableServices = function () {

            $('#tbl_services tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_services');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/services/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_services_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }

    var initTableProjects = function () {

            $('#tbl_projects tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_projects');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/projects/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_projects_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }

    var initTableArticles = function () {

            $('#tbl_articles tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_articles');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/articles/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_articles_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }

    var initTableBooks = function () {

            $('#tbl_books tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_books');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/books/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_books_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }

    var initTableResults = function () {

            $('#tbl_results tfoot th').each( function () {
                var title = $(this).text();

                if(title.length > 0){
                    $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
                }
            } );

            var table = $('#tbl_results');

            // begin first table
            table.DataTable({
                 pageLength: 15,
                    "lengthMenu": [
                        [5, 15, 20, -1],
                        [5, 15, 20, "Todos"]
                    ],
                    responsive: true,
                    dom: '<"html5buttons"B>lTfgitp',
                    ajax: '/piloto/results/',
                    "columnDefs": [
                        {
                            'orderable': false,
                            'targets': [0]
                        },
                    ],
                    language: {
                        aria: {
                            "sortAscending": ": activate to sort column ascending",
                            "sortDescending": ": activate to sort column descending"
                        },
                        "emptyTable": "No hay datos en la tabla",
                        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                        "infoEmpty": "No se encontraron registros",
                        "infoFiltered": "(filtered1 from _MAX_ total records)",
                        "lengthMenu": "Mostrar _MENU_",
                        "search": "Buscar:",
                        "zeroRecords": "No se encontraron resultados",
                        "paginate": {
                            "previous":"Anterior",
                            "next": "Próximo",
                            "last": "Último",
                            "first": "Primero"
                        }
                    },

                    buttons: [
                        {extend: 'copy'},
                        {extend: 'csv'},
                        {extend: 'excel', title: 'ExampleFile'},
                        {extend: 'pdf', title: 'ExampleFile'},
                        {extend: 'print',
                         customize: function (win){
                                $(win.document.body).addClass('white-bg');
                                $(win.document.body).css('font-size', '10px');

                                $(win.document.body).find('table')
                                        .addClass('compact')
                                        .css('font-size', 'inherit');
                        }
                        }
                    ],

                initComplete: function () {
                // Apply the search
                    this.api().columns().every( function () {
                        var that = this;

                        $( 'input', this.footer() ).on( 'keyup change clear', function () {
                            if ( that.search() !== this.value ) {
                                that
                                    .search( this.value )
                                    .draw();
                            }
                        } );
                    } );
                }
            });

            var tableWrapper = jQuery('#tbl_results_wrapper');

            table.find('.group-checkable').change(function () {
                var set = jQuery(this).attr("data-set");
                var checked = jQuery(this).is(":checked");
                jQuery(set).each(function () {
                    if (checked) {
                        $(this).prop("checked", true);
                        $(this).parents('tr').addClass("active");
                    } else {
                        $(this).prop("checked", false);
                        $(this).parents('tr').removeClass("active");
                    }
                });
            });

            table.on('change', 'tbody tr .checkboxes', function () {
                $(this).parents('tr').toggleClass("active");
            });
        }


    return {

        init: function () {
            if (!jQuery().dataTable) {
                return;
            }

            initTablePonencys();
            initTableThesis();
            initTableServices();
            initTableProjects();
            initTableArticles();
            initTableBooks();
            initTableResults();

        }

    };

}();


jQuery(document).ready(function() {
    TableScienceWork.init();
});
