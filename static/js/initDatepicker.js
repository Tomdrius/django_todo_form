document.addEventListener('DOMContentLoaded', function() {
    const dueDateInput = document.getElementById('due-date-input');
    new Datepicker(dueDateInput, {
        autohide: true,
        format: 'yyyy-mm-dd'
    });
});