// Function to toggle the navigation menu
const showMenu = (toggleId, navId) => {
    const toggleButton = document.getElementById(toggleId);
    const navMenu = document.getElementById(navId);

    if (toggleButton && navMenu) {
        toggleButton.addEventListener('click', () => {
            console.log('Toggle button clicked');
            navMenu.classList.toggle('show');
        });
    } else {
        console.error(`Element with ID ${toggleId} or ${navId} not found.`);
    }
};

// Initialize the menu toggle functionality
showMenu('toggle', 'menu');

// Handle navigation link activation and menu closing
const navLinks = document.querySelectorAll('.link');

function linkAction(event) {
    console.log('Navigation link clicked');
    navLinks.forEach(link => link.classList.remove('active'));
    event.currentTarget.classList.add('active');

    const navMenu = document.getElementById('menu');
    if (navMenu) {
        navMenu.classList.remove('show');
    } else {
        console.error('Element with ID menu not found.');
    }
}

// Attach click event listeners to navigation links
navLinks.forEach(link => link.addEventListener('click', linkAction));

// Handle click events for place links to open images
const placeLinks = document.querySelectorAll('.place-link');

placeLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        
        const imageSrc = link.getAttribute('data-image-src');
        if (imageSrc) {
            console.log('Opening image:', imageSrc);
            window.open(imageSrc, '_blank');
        } else {
            console.error('data-image-src attribute not found on link.');
        }
    });
});

// Initialize the carousel slideshow
document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll('.carousel-slide');
    let currentSlide = 0;

    if (slides.length === 0) {
        console.warn('No slides found for the carousel.');
        return;
    }

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    // Initialize the first slide
    showSlide(currentSlide);

    // Set the interval for the slideshow (e.g., 5 seconds)
    setInterval(nextSlide, 5000);
});
