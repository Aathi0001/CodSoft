// Day/Night Mode Toggle
const dayNightToggle = document.querySelector('.day-night');
const body = document.body;

dayNightToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        dayNightToggle.querySelector('i').classList.remove('fa-moon');
        dayNightToggle.querySelector('i').classList.add('fa-sun');
    } else {
        dayNightToggle.querySelector('i').classList.remove('fa-sun');
        dayNightToggle.querySelector('i').classList.add('fa-moon');
    }
});

const nav = document.querySelector(".nav"),
      navList = nav.querySelectorAll("li"),
      totalNavList = navList.length,
      allSection = document.querySelectorAll(".section"),
      totalSection = allSection.length;

// Add click event listener to navigation links
for (let i = 0; i < totalNavList; i++) {
    const link = navList[i].querySelector("a");
    link.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent default anchor behavior

        const targetId = this.getAttribute("href").split("#")[1];

        // Check if the target section is already active
        if (this.classList.contains("active") && targetId === 'home') {
            return; // If "Home" is already active, do nothing
        }

        removeBackSection();
        for (let j = 0; j < totalNavList; j++) {
            if (navList[j].querySelector("a").classList.contains("active")) {
                addBackSection(j);
            }
            navList[j].querySelector("a").classList.remove("active");
        }
        this.classList.add("active");
        showSection(this);

        // Update URL hash and scroll
        if (targetId === 'home') {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            setTimeout(() => {
                window.location.hash = 'home';
            }, 300); // Adjust the delay if needed
        } else {
            window.location.hash = targetId;
        }

        // Automatically close the sidebar if the width is less than 1200px
        if (window.innerWidth < 1200) {
            asideSectionToggleBtn();
        }
    });
}

function removeBackSection() {
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.remove("back-section");
    }
}

function addBackSection(num) {
    allSection[num].classList.add("back-section");
}

function showSection(element) {
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.remove("active");
    }
    const target = element.getAttribute("href").split("#")[1];
    document.querySelector("#" + target).classList.add("active");
}

function updateNav(element) {
    const target = element.getAttribute("href").split("#")[1];
    for (let i = 0; i < totalNavList; i++) {
        const link = navList[i].querySelector("a");
        link.classList.remove("active");
        if (target === link.getAttribute("href").split("#")[1]) {
            link.classList.add("active");
        }
    }
}

document.querySelector(".hire-me").addEventListener("click", function() {
    const sectionIndex = this.getAttribute("data-section-index");
    showSection(this);
    updateNav(this);
    removeBackSection();
    addBackSection(sectionIndex);
});

const navTogglerBtn = document.querySelector(".nav-toggler"),
      aside = document.querySelector(".aside");

navTogglerBtn.addEventListener("click", () => {
    asideSectionToggleBtn();
});

function asideSectionToggleBtn() {
    aside.classList.toggle("open");
    navTogglerBtn.classList.toggle("open");
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.toggle("open");
    }
    
    // Adjust padding based on the sidebar state
    adjustSectionPadding();
}

// Adjust padding based on the sidebar state and screen size
function adjustSectionPadding() {
    if (window.innerWidth < 1200) {
        // Mobile view or smaller screens
        for (let i = 0; i < totalSection; i++) {
            if (aside.classList.contains("open")) {
                allSection[i].style.padding = "0 30px"; // Padding with sidebar open
            } else {
                allSection[i].style.padding = "0 30px"; // Padding with sidebar closed
            }
        }
    } else {
        // Larger screens
        for (let i = 0; i < totalSection; i++) {
            if (aside.classList.contains("open")) {
                allSection[i].style.padding = "0 30px 0 300px"; // Padding with sidebar open
            } else {
                allSection[i].style.padding = "0 30px"; // Padding with sidebar closed
            }
        }
    }
}

// Auto close sidebar on resize and adjust padding
window.addEventListener('resize', () => {
    if (window.innerWidth < 1200) {
        closeToggleBar();
    }
    adjustSectionPadding(); // Adjust padding on resize
});

// Function to close the toggle bar
function closeToggleBar() {
    if (aside.classList.contains('open')) {
        aside.classList.remove('open');
        navTogglerBtn.classList.remove('open');
        adjustSectionPadding(); // Adjust padding when closing
    }
}

// Initial check on page load
window.addEventListener('load', () => {
    const targetId = "home"; // Always set the targetId to "home" on page load

    // Scroll to the home section on page load
    window.location.hash = targetId; // Update the URL hash to #home
    setTimeout(() => {
        document.querySelector("#home").scrollIntoView({ behavior: "smooth" });
    }, 0); // Delay to ensure hash update

    // Update the navigation to highlight home as active
    const homeNavLink = document.querySelector('.nav a[href="#home"]');
    if (homeNavLink) {
        updateNav(homeNavLink);
    }

    // Ensure the home section is active
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.remove("active");
        if (allSection[i].id === targetId) {
            allSection[i].classList.add("active");
        }
    }

    if (window.innerWidth < 1200) {
        closeToggleBar();
    }

    // Adjust section padding on page load
    adjustSectionPadding();
});

// Update navigation on scroll
window.addEventListener('scroll', () => {
    let currentSectionId = '';
    
    allSection.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        if (window.scrollY >= sectionTop - 50 && window.scrollY < sectionTop + sectionHeight - 50) {
            currentSectionId = section.getAttribute('id');
        }
    });
    
    const navLinks = nav.querySelectorAll('a');
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(currentSectionId)) {
            link.classList.add('active');
        }
    });
});
