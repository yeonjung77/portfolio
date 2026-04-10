// Toggle project detail sections
function toggleDetail(id) {
    const detail = document.getElementById(id);
    const btn = detail.previousElementSibling.querySelector('.project-toggle');

    if (detail.hidden) {
        detail.hidden = false;
        btn.textContent = 'Hide Details';
    } else {
        detail.hidden = true;
        btn.textContent = 'View Details';
    }
}

// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
