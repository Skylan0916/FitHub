$(document).ready(function(){

    // Selecting a specific learning section
    $(document).on('click', '.muscle_group', function() {
        const id = $(this).data('id');
        window.location.href = `/learn/${id}/0`;
    });

    // Completion of a learning section
    $('.complete_btn').on('click', function() {
        const section = $(this).data('id');

        $.ajax({
            type: 'POST',
            url: '/learn',
            data: { completed_section: section },
            success: function(response) {
                // console.log(section)
                window.location.href = '/learn';
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

})