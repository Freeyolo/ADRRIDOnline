$(document).ready(function() {
    $('#TabellA').DataTable({
        autoWidth: false,
        paging: true,
        searching: true,
        ordering: false,
        responsive: true,
        language: {
            search: "Søk i tabellen:", // Replace "Search" label with "Søk i tabellen"
            lengthMenu: "Vis _MENU_ rader",
            info: "Viser side _PAGE_ av _PAGES_",
            infoFiltered: "(filtrert fra _MAX_ rader)",
            infoEmpty: "Ingen treff",
            zeroRecords: "Ingen treff - beklager",
        },
    });
    // Add placeholder text to the search input field
    $('.dataTables_filter input').attr('placeholder', 'Skriv for å søke...');
});