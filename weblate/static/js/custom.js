$(function() {
    $('#dropdownMenuUpload').click(function () {

        // Send the data using post
        var posting = $.post('https://wishcam.com/update-pot', {
            component: '{{ object.subproject.slug }}',
            lang: '{{ object.language.code }}'
        });
        $(this).html(
            '<i class="fa fa-refresh fa-spin fa-fw"></i>' +
            '<span class="sr-only">Loading...</span>' +
            'Nalagam...');

        $(this).attr("disabled", true);

        // Put the results in a div
        posting.done(function (data) {
            if (data.status) {
                $('#dropdownMenuUpload').html('<i class="fa fa-check" aria-hidden="true"></i> Uspešno posodobljeno');
            } else {
                $('#dropdownMenuUpload').html('<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> Napaka:' + data.error);
            }
        });

    });
});