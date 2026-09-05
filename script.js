const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('nav-scrolled');
    } else {
        navbar.classList.remove('nav-scrolled');
    }
});

let cartCount = 0;
const cartBadges = document.querySelectorAll('.cart-badge');
const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');

addToCartBtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (navigator.vibrate) navigator.vibrate(50);
        
        const icon = this.querySelector('i');
        if (icon) {
            icon.classList.remove('fa-plus');
            icon.classList.add('fa-check');
            this.classList.add('bg-green-500');
            this.classList.remove('from-primary', 'to-primaryLight');
            
            setTimeout(() => {
                icon.classList.remove('fa-check');
                icon.classList.add('fa-plus');
                this.classList.remove('bg-green-500');
                this.classList.add('from-primary', 'to-primaryLight');
            }, 1500);
        }

        cartCount++;
        cartBadges.forEach(badge => {
            badge.innerText = cartCount;
            badge.style.transform = 'scale(1.4)';
            setTimeout(() => badge.style.transform = 'scale(1)', 200);
        });
    });
});

const categoryBtns = document.querySelectorAll('.category-scroll button');
categoryBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        categoryBtns.forEach(b => {
            b.classList.remove('bg-gradient-to-r', 'from-primary', 'to-primaryLight', 'text-white', 'shadow-md');
            b.classList.add('bg-white', 'text-darkbrown');
            b.classList.remove('border-primary');
            b.classList.add('border-gray-200');
        });
        this.classList.remove('bg-white', 'text-darkbrown', 'border-gray-200');
        this.classList.add('bg-gradient-to-r', 'from-primary', 'to-primaryLight', 'text-white', 'shadow-md', 'border-primary');
    });
});
