$(document).ready(function () {
    let selectedChoices = [];

    // Handle choice selection
    $(document).on('click', '.choice', function () {
        const id = $(this).data('id');
        var img = this.querySelector('img');

        if (selectedChoices.includes(id)) {
            selectedChoices = selectedChoices.filter(x => x !== id);
            img.classList.remove('selected');
        } else {
            selectedChoices.push(id);
            img.classList.add('selected');
        }
    });

    // Handle quiz submission
    $(document).on('click', '.submit_btn', function () {
        if (selectedChoices.length === 0) {
            alert('Please select an answer.');
            return;
        }

        const solutions = $(this).data('solutions');
        const isCorrect = selectedChoices.every(choiceId => {
            return solutions.includes(choiceId);
        });
        const scored = (isCorrect && selectedChoices.length === solutions.length);

        // Display Feedback
        if (scored) {
            alert('Your answer is correct!');
        } else {
            alert('Your answer is incorrect!');
        }

        $.ajax({
            type: 'POST',
            url: "/submit",
            data: { scored: scored },
            success: function(response) {
                window.location.href = "/quiz";
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

})