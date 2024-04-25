$(document).ready(function(){
    $(document).on('click', function(){
        $('.home-container').addClass('hidden');

        setTimeout(function(){
            window.location.href = "/learn";
        }, 1000);
    });
});