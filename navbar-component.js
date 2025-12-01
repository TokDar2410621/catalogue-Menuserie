export function createNavbar(activePage = 'home') {
    const navbar = document.createElement('header');
    navbar.id = 'navbar';
    navbar.className = 'fixed w-full top-0 z-50 transition-all duration-300 bg-white shadow-sm border-b border-oak/10';

    navbar.innerHTML = `
        <div class="container mx-auto px-6 h-20 flex items-center justify-between transition-all duration-300 max-w-7xl" id="navbar-container">
            <!-- Logo -->
            <a href="index.html" class="flex items-center gap-3 group">
                <img src="image/Création sans titre.svg" alt="DKbois Logo" class="h-24 w-auto object-contain group-hover:opacity-80 transition-opacity">
            </a>

            <!-- Desktop Navigation -->
            <nav class="hidden md:flex items-center gap-10">
                <a href="index.html" class="nav-link ${activePage === 'home' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.home">Accueil</a>
                <a href="about.html" class="nav-link ${activePage === 'about' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.about">À Propos</a>
                <a href="services.html" class="nav-link ${activePage === 'services' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.services">Services</a>
                <a href="portfolio.html" class="nav-link ${activePage === 'portfolio' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.portfolio">Réalisations</a>
                <a href="contact.html" class="nav-link ${activePage === 'contact' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.contact">Contact</a>
            </nav>

            <!-- Actions -->
            <div class="hidden md:flex items-center gap-6">
                <button id="lang-toggle" class="font-serif text-oak hover:text-gold transition-colors px-2 font-bold text-base">EN</button>
                <a href="contact.html" class="bg-gradient-to-r from-walnut to-oak text-white px-7 py-2.5 rounded-sm font-serif hover:brightness-110 hover:scale-105 transition-all duration-300" data-i18n="cta.quote">Devis gratuit</a>
            </div>

            <!-- Mobile Menu Button -->
            <button id="mobile-menu-btn" class="md:hidden text-walnut">
                <i data-lucide="menu"></i>
            </button>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="fixed inset-0 bg-walnut z-40 transform translate-x-full transition-transform duration-300 flex flex-col items-center justify-center space-y-8 text-white md:hidden">
            <button id="close-menu-btn" class="absolute top-6 right-6 text-white/80 hover:text-gold">
                <i data-lucide="x" size="32"></i>
            </button>
            <a href="index.html" class="mobile-link text-2xl font-serif" data-i18n="nav.home">Accueil</a>
            <a href="about.html" class="mobile-link text-2xl font-serif" data-i18n="nav.about">À Propos</a>
            <a href="services.html" class="mobile-link text-2xl font-serif" data-i18n="nav.services">Services</a>
            <a href="portfolio.html" class="mobile-link text-2xl font-serif" data-i18n="nav.portfolio">Réalisations</a>
            <a href="contact.html" class="mobile-link text-2xl font-serif" data-i18n="nav.contact">Contact</a>
            <div class="flex items-center gap-4 mt-8">
                <button id="mobile-lang-toggle" class="text-gold font-serif text-xl font-bold">EN</button>
            </div>
        </div>
    `;

    return navbar;
}

export function initNavbar(activePage = 'home') {
    const navbarPlaceholder = document.getElementById('navbar-placeholder');
    if (navbarPlaceholder) {
        const navbar = createNavbar(activePage);
        navbarPlaceholder.replaceWith(navbar);
    }

    // Mobile menu functionality
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    if (mobileMenuBtn && mobileMenu && closeMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.remove('translate-x-full');
        });

        closeMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
        });

        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
            });
        });
    }
}
