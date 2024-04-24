$(document).ready(function () {

    // Handle learning section selection
    $(document).on("click", ".muscle-group", function () {
        const id = $(this).data("id");
        window.location.href = `/learn/${id}/0`;
    });

    // Handle learning section completion
    $(".complete-btn").on("click", function () {
        const section = $(this).data("id");

        $.ajax({
            type: "POST",
            url: "/complete",
            data: { section: section },
            success: function (response) {
                window.location.href = "/learn";
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    // Apply the grayscale filter and completion icon to the completed sections
    $(".image").each(function() {
        const completed = $(this).data("completed");
        console.log(completed)
        if (completed === "True") {
            $(this).css("filter", "grayscale(100%)");

            const completeIcon = $("<img>", {
                class: "complete-icon",
                src: "https://cdn0.iconfinder.com/data/icons/shift-free/32/Complete_Symbol-512.png"
            });
            $(this).closest(".muscle-group").append(completeIcon);
        }
    });

})