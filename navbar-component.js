export function createNavbar(activePage = 'home') {
    const navbar = document.createElement('header');
    navbar.id = 'navbar';
    navbar.className = 'fixed w-full top-0 z-50 transition-all duration-300 bg-white shadow-sm border-b border-oak/10';

    navbar.innerHTML = `
        <div class="container mx-auto px-6 h-20 flex items-center justify-between transition-all duration-300 max-w-7xl" id="navbar-container">
            <a href="index.html" class="flex items-center gap-3 group">
                <img src="image/Création sans titre.svg" alt="DKBOIS - Menuiserie et Ébénisterie d'Excellence à Yaoundé, Cameroun" class="h-24 w-auto object-contain group-hover:opacity-80 transition-opacity">
            </a>

            <nav class="hidden md:flex items-center gap-10">
                <a href="index.html" class="nav-link ${activePage === 'home' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.home">Accueil</a>
                <a href="about.html" class="nav-link ${activePage === 'about' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.about">À Propos</a>
                <a href="services.html" class="nav-link ${activePage === 'services' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.services">Services</a>
                <a href="portfolio.html" class="nav-link ${activePage === 'portfolio' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.portfolio">Réalisations</a>
                <a href="contact.html" class="nav-link ${activePage === 'contact' ? 'active' : ''} text-sm font-medium uppercase tracking-wider hover:text-oak transition-colors" data-i18n="nav.contact">Contact</a>
            </nav>

            <div class="hidden md:flex items-center gap-6">
                <button id="lang-toggle" class="font-serif text-oak hover:text-gold transition-colors px-2 font-bold text-base">EN</button>
                <a href="contact.html" class="bg-gradient-to-r from-walnut to-oak text-white px-7 py-2.5 rounded-sm font-serif hover:brightness-110 hover:scale-105 transition-all duration-300" data-i18n="cta.quote">Devis gratuit</a>
            </div>

            <button id="mobile-menu-btn" class="md:hidden text-walnut p-2 focus:outline-none z-50 relative" aria-label="Ouvrir le menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
            </button>
        </div>

        <div id="mobile-menu" class="fixed inset-0 bg-walnut z-[60] transform translate-x-full transition-transform duration-300 md:hidden flex flex-col">
            
            <button id="close-menu-btn" class="absolute top-6 right-6 text-white/80 hover:text-white transition-colors p-2 focus:outline-none" aria-label="Fermer le menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="pointer-events-none"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg>
            </button>

            <div class="flex flex-col items-center justify-center h-full space-y-8 text-white w-full overflow-y-auto">
                <a href="index.html" class="mobile-link text-2xl font-serif hover:text-gold transition-colors" data-i18n="nav.home">Accueil</a>
                <a href="about.html" class="mobile-link text-2xl font-serif hover:text-gold transition-colors" data-i18n="nav.about">À Propos</a>
                <a href="services.html" class="mobile-link text-2xl font-serif hover:text-gold transition-colors" data-i18n="nav.services">Services</a>
                <a href="portfolio.html" class="mobile-link text-2xl font-serif hover:text-gold transition-colors" data-i18n="nav.portfolio">Réalisations</a>
                <a href="contact.html" class="mobile-link text-2xl font-serif hover:text-gold transition-colors" data-i18n="nav.contact">Contact</a>
                
                <div class="flex items-center gap-4 mt-8 pt-8 border-t border-white/20 w-48 justify-center">
                    <button id="mobile-lang-toggle" class="text-gold font-serif text-xl font-bold hover:text-white transition-colors">EN</button>
                </div>
            </div>
        </div>
    `;

    return navbar;
}

export function initNavbar(activePage = 'home') {
    const navbarPlaceholder = document.getElementById('navbar-placeholder');
    if (!navbarPlaceholder) return;

    const navbar = createNavbar(activePage);
    navbarPlaceholder.replaceWith(navbar);

    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    // Fonction pour gérer l'ouverture/fermeture et le scroll
const toggleMenu = (show) => {
    if (show) {
        const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
        document.body.style.paddingRight = `${scrollbarWidth}px`;
        document.body.style.overflow = 'hidden';
        mobileMenu.classList.remove('translate-x-full');
    } else {
        mobileMenu.classList.add('translate-x-full');
        document.body.style.overflow = '';
        document.body.style.paddingRight = '';
    }
};

    if (mobileMenuBtn && mobileMenu && closeMenuBtn) {
        mobileMenuBtn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleMenu(true);
        });

        closeMenuBtn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleMenu(false);
        });

        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                toggleMenu(false);
            });
        });
        
        // Fermer si on appuie sur Echap
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('translate-x-full')) {
                toggleMenu(false);
            }
        });
    }
}