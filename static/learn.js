$(document).ready(function(){

    // Handle learning section selection
    $(document).on('click', '.muscle_group', function() {
        const id = $(this).data('id');
        window.location.href = `/learn/${id}/0`;
    });

    // Handle learning section completion
    $('.complete_btn').on('click', function() {
        const section = $(this).data('id');

        $.ajax({
            type: 'POST',
            url: '/complete',
            data: { section: section },
            success: function(response) {
                window.location.href = '/learn';
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

})