$('.slider-main').owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    mouseDrag: false,
    autoplay: true,
    autoWidth: false,
    // animateOut: 'fadeIn',
    autoplayTimeout: 6500,
    smartSpeed: 450,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

// country-list

jQuery(document).ready(function ($) {
    'use strict';
    $('.country-list').owlCarousel({
        margin: 30,
        loop: true,
        center: false,
        items: 4,
        autoplay: true,
        dots: false,
        nav: true,
        autoplayTimeout: 8500,
        smartSpeed: 450,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1170: {
                items: 4
            }
        }
    });
});

//testimonials

jQuery(document).ready(function ($) {
    'use strict';
    $('.client-feedback').owlCarousel({
        margin: 30,
        loop: true,
        center: false,
        items: 3,
        autoplay: true,
        dots: false,
        nav: true,
        autoplayTimeout: 7500,
        smartSpeed: 450,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1170: {
                items: 3
            }
        }
    });
    var owl = $('.owl-carousel');
    $('.video-block').on('click', function () {
        owl.trigger('stop.owl.autoplay');
    });
});

// counter

$(document).ready(function () {
    // code from https://code.mukto.info/counter-up-with-a-simple-jquery/
    // Create new intersection observer
    var observer = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                $(entry.target)
                    .prop('Counter', 0)
                    .animate(
                        {
                            Counter: $(entry.target).text()
                        },
                        {
                            duration: 4000,
                            easing: 'swing',
                            step: function (now) {
                                $(entry.target).text(Math.ceil(now));
                            }
                        }
                    );
                observer.unobserve(entry.target);
            }
        });
    });

    $('.counterup').each(function () {
        observer.observe(this);
    });
});

// sticky-nav

window.addEventListener('scroll', function () {
    const nav = document.querySelector('nav');
    nav.classList.toggle('sticky', window.scrollY > 200);
});

//aos
AOS.init();
