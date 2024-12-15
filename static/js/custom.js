// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


//-- Display messages for 5 sec -->

document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.auto-close-alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show'); // Remove the 'show' class to hide the alert
            alert.classList.add('fade'); // Add 'fade' class to smoothly fade it out
            // Remove from DOM
            setTimeout(() => {
                alert.remove(); //  remove the alert from the DOM
            }, 500); // for css transmition
        }, 5000); // Time in milliseconds (5000 ms = 5 seconds)
    });
});

//-- Book Table Link -->
    
document.getElementById('bookTableLink').onclick = function (event) {
    event.preventDefault(); // Prevent default link behavior
    if (window.userIsAuthenticated === 'true') { // Check string equality for true
        // Redirect to the booking page if user is authenticated
        window.location.href = window.bookingPageUrl;
    } else {
        // Show the registration prompt modal if user is not authenticated
        $('#registrationPromptModal').modal('show');
    }
};
    