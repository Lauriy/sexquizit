$(document).ready(function () {
    $('#generate-link').submit(function (e) {
        var pk1 = $('#pk1').val();
        var pk2 = $('#pk2').val();

        if (pk1 == null && pk2 == null) {
            return;
        }

        var url = '/compare';
        if (pk1) {
            url += '/' + encodeURIComponent(pk1);
        }
        if (pk2) {
            url += '/' + encodeURIComponent(pk2);
        }

        window.location = url;

        e.preventDefault();
    });
});

