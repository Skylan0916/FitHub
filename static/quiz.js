let submitted = false;

// Remove the submit button, and add two new buttons
function updateButtons(scored, answer){
    $('.submit_btn').remove();

    var feedbackButton = $('<button>', {
        class: 'feedback_btn button',
        text: 'Feedback',
        click: function() {
            displayFeedback(scored, answer);
        }
    });

    var nextButton = $('<button>', {
        class: 'next_btn button',
        text: 'Next',
        click: function() {
            submit(scored);
        }
    });

    $('#btn-contatiner').append(feedbackButton);
    $('#btn-contatiner').append(nextButton);
}

// Disable choice selection and animation
function disableSelection(){
    submitted = true;

    $(".choice").each(function() {
        this.classList.remove("choice");
    });
}

// Submit the quiz results asynchronously via AJAX
function submit(scored) {
    $.ajax({
        type: "POST",
        url: "/submit",
        data: { scored: scored },
        success: function(response) {
            window.location.href = "/quiz";
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}

// Display the feedback and submit the result upon exiting
function displayFeedback(scored, answer) {
    const title = scored ? "Correct" : "Incorrect";
    const color = scored ? "#AFE1AF" : "#FAA0A0";

    const result = new Popup({
        title: title,
        content: answer,
        borderRadius: "2rem",
        backgroundColor: color,
        showImmediately: true
    });
}

// Display the specified content
function display(content) {
    const result = new Popup({
        hideTitle: true,
        content: content,
        borderRadius: "2rem",
        backgroundColor: "#D3D3D3",
        showImmediately: true
    });
}

$(document).ready(function () {
    let selectedChoices = [];

    // Handle choice selection
    $(document).on("click", ".choice", function () {
        if (submitted) {
            return;
        }

        const id = $(this).data("id");
        const solutions = $(this).data("solutions");
        var img = this.querySelector("img");
    
        // Deselect all other choices if it's not a multiple choice question
        if (solutions.length === 1) {
            $(".choice").each(function() {
                const otherId = $(this).data("id");
                if (otherId !== id && selectedChoices.includes(otherId)) {
                    selectedChoices = selectedChoices.filter(x => x !== otherId);
                    this.querySelector("img").classList.remove("selected");
                }
            });
        }
    
        if (selectedChoices.includes(id)) {
            selectedChoices = selectedChoices.filter(x => x !== id);
            img.classList.remove("selected");
        } else {
            selectedChoices.push(id);
            img.classList.add("selected");
        }
    });

    // Handle quiz submission
    $(document).on("click", ".submit_btn", function () {
        if (selectedChoices.length === 0) {
            display("Please select at least one answer");
            return;
        }

        const solutions = $(this).data("solutions");
        const answer = $(this).data("answer");

        const isCorrect = selectedChoices.every(choiceId => {
            return solutions.includes(choiceId);
        });
        const scored = (isCorrect && selectedChoices.length === solutions.length);

        disableSelection();
        updateButtons(scored, answer);
        displayFeedback(scored, answer);
    });

    // Hint
    $(document).on("click", ".hint", function () {
        const hint = $(this).data("hint");
        console.log(hint)
        display(hint);
    });

})