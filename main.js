import { translations } from './data.js';
import { API } from './api-config.js';
import { UXEnhancements } from './ux-enhancements.js';
import { initComponents } from './components.js';

let currentLang = 'fr';
const d = document;

const updateContent = () => {
    d.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const translation = key.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || key;
        el.innerHTML = translation;
    });
};

const updateLinkHrefs = () => {
    d.querySelectorAll('a[href]').forEach(link => {
        try {
            const url = new URL(link.href, window.location.origin);
            if (url.hostname === window.location.hostname && url.pathname.endsWith('.html')) {
                url.searchParams.set('lang', currentLang);
                link.href = url.toString();
            }
        } catch (e) {
        }
    });
};

const setupLanguage = () => {
    const urlParams = new URLSearchParams(window.location.search);
    const langParam = urlParams.get('lang');
    const browserLang = navigator.language.split('-')[0];
    currentLang = ['fr', 'en'].includes(langParam) ? langParam : (['fr', 'en'].includes(browserLang) ? browserLang : 'fr');

    d.documentElement.lang = currentLang;
    updateContent();
    updateLinkHrefs();

    const langToggle = d.getElementById('lang-toggle');
    const mobileLangToggle = d.getElementById('mobile-lang-toggle');
    if (langToggle) langToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    if (mobileLangToggle) mobileLangToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
};

const switchLanguage = () => {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    const url = new URL(window.location);
    url.searchParams.set('lang', currentLang);
    window.history.pushState({}, '', url);
    setupLanguage();

    // Recharger les données avec la nouvelle langue
    renderServices();
    renderPortfolio();
    renderTestimonials();
    // lucide.createIcons() est appelé dans chaque fonction render
};

const renderServices = async () => {
    const grid = d.getElementById('services-grid');
    if (!grid) return;

    // État de chargement
    grid.innerHTML = `
        <div class="col-span-full flex justify-center items-center py-20">
            <div class="animate-spin rounded-full h-12 w-12 border-4 border-oak border-t-gold"></div>
        </div>
    `;

    try {
        const response = await API.services.list(currentLang);
        const services = response.results || response;

        if (!services || services.length === 0) {
            grid.innerHTML = `
                <div class="col-span-full text-center py-20">
                    <i data-lucide="inbox" class="w-16 h-16 text-oak/30 mx-auto mb-4"></i>
                    <p class="text-walnut/70">Aucun service disponible pour le moment.</p>
                </div>
            `;
            lucide.createIcons();
            return;
        }

        grid.innerHTML = services.map(s => `
            <div class="service-card bg-white p-8 rounded-sm border border-oak/10 hover:border-gold/30 group relative overflow-hidden">
                <div class="relative z-10">
                    <div class="w-12 h-12 mb-6 text-oak group-hover:text-gold transition-colors">
                        <i data-lucide="${s.icon}"></i>
                    </div>
                    <h3 class="font-serif font-bold text-xl mb-3 text-walnut">${s.title}</h3>
                    <p class="text-walnut/70 text-sm leading-relaxed">${s.description}</p>
                </div>
            </div>
        `).join('');

        lucide.createIcons();
    } catch (error) {
        console.error('Error loading services:', error);

        grid.innerHTML = `
            <div class="col-span-full text-center py-20 space-y-4">
                <i data-lucide="wifi-off" class="w-16 h-16 text-oak/30 mx-auto"></i>
                <p class="text-walnut/80 text-lg">Impossible de charger les services</p>
                <p class="text-walnut/60 text-sm">Vérifiez votre connexion internet</p>
                <button onclick="location.reload()"
                        class="mt-4 bg-oak text-white px-6 py-2 rounded-sm hover:bg-gold transition-colors inline-flex items-center gap-2">
                    <i data-lucide="refresh-cw" class="w-4 h-4"></i>
                    <span>Réessayer</span>
                </button>
            </div>
        `;
        lucide.createIcons();
    }
};

const renderPortfolio = async () => {
    const grid = d.getElementById('portfolio-grid');
    if (!grid) return;

    // État de chargement
    grid.innerHTML = `
        <div class="col-span-full flex justify-center items-center py-20">
            <div class="animate-spin rounded-full h-12 w-12 border-4 border-oak border-t-gold"></div>
        </div>
    `;

    try {
        const response = await API.projects.featured(currentLang);
        const projects = response.results || response;

        if (!projects || projects.length === 0) {
            grid.innerHTML = `
                <div class="col-span-full text-center py-20">
                    <i data-lucide="inbox" class="w-16 h-16 text-oak/30 mx-auto mb-4"></i>
                    <p class="text-walnut/70">Aucun projet disponible pour le moment.</p>
                </div>
            `;
            lucide.createIcons();
            return;
        }

        grid.innerHTML = projects.map((p, index) => {
            // Ajouter des variations de taille comme dans l'original
            const sizes = ['col-span-1', 'col-span-1 lg:col-span-2', 'col-span-1'];
            const size = sizes[index % sizes.length];

            // Assurer qu'on a une image valide
            const imageUrl = (p.images && p.images.length > 0) ? p.images[0] : (p.image || '');

            if (!imageUrl) {
                console.warn(`Project ${p.title} has no image`);
                return '';
            }

            return `
                <a href="project.html?id=${p.slug}&lang=${currentLang}" class="portfolio-item relative overflow-hidden rounded-sm group cursor-pointer ${size} h-64 md:h-80 bg-gray-200">
                    <img data-src="${imageUrl}" alt="${p.title} - ${p.category} en menuiserie et ébénisterie sur mesure par DKBOIS à Yaoundé, Cameroun" class="lazy w-full h-full object-cover object-center">
                    <div class="portfolio-overlay absolute inset-0 flex flex-col justify-end p-6">
                        <span class="text-gold-contrast text-xs font-serif tracking-widest uppercase mb-1 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">${p.category}</span>
                        <h3 class="text-white font-serif text-2xl font-bold transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300 delay-75">${p.title}</h3>
                    </div>
                </a>
            `;
        }).join('');

        lazyLoadImages();
    } catch (error) {
        console.error('Error loading portfolio:', error);

        grid.innerHTML = `
            <div class="col-span-full text-center py-20 space-y-4">
                <i data-lucide="wifi-off" class="w-16 h-16 text-oak/30 mx-auto"></i>
                <p class="text-walnut/80 text-lg">Impossible de charger le portfolio</p>
                <p class="text-walnut/60 text-sm">Vérifiez votre connexion internet</p>
                <button onclick="location.reload()"
                        class="mt-4 bg-oak text-white px-6 py-2 rounded-sm hover:bg-gold transition-colors inline-flex items-center gap-2">
                    <i data-lucide="refresh-cw" class="w-4 h-4"></i>
                    <span>Réessayer</span>
                </button>
            </div>
        `;
        lucide.createIcons();
    }
};

const renderTestimonials = async () => {
    const track = d.getElementById('testimonial-track');
    const dotsContainer = d.getElementById('testimonial-dots');
    if (!track || !dotsContainer) return;

    // État de chargement
    track.innerHTML = `
        <div class="w-full flex justify-center items-center py-20">
            <div class="animate-spin rounded-full h-12 w-12 border-4 border-white/20 border-t-gold"></div>
        </div>
    `;

    try {
        const response = await API.testimonials.list(currentLang);
        const testimonials = response.results || response;

        if (!testimonials || testimonials.length === 0) {
            track.innerHTML = `
                <div class="w-full text-center py-20">
                    <i data-lucide="inbox" class="w-16 h-16 text-white/30 mx-auto mb-4"></i>
                    <p class="text-white/70">Aucun témoignage disponible pour le moment.</p>
                </div>
            `;
            lucide.createIcons();
            return;
        }

        track.innerHTML = testimonials.map(t => `
            <div class="w-full flex-shrink-0 px-4">
                <div class="bg-white/10 p-8 md:p-12 rounded-sm backdrop-blur-sm border border-white/5 text-center flex flex-col items-center">
                    <img data-src="${t.image}" alt="${t.name} - ${t.role} - Témoignage client satisfait des services de menuiserie et ébénisterie DKBOIS à Yaoundé, Cameroun" class="lazy w-16 h-16 rounded-full object-cover border-2 border-gold/50 mb-6">
                    <div class="flex justify-center gap-1 text-gold-contrast mb-6">
                        ${Array(t.stars).fill('<i data-lucide="star" class="w-5 h-5 fill-current"></i>').join('')}
                    </div>
                    <p class="font-serif text-xl md:text-2xl italic mb-8 leading-relaxed text-white/90">"${t.text}"</p>
                    <div class="font-sans">
                        <span class="block font-bold text-gold-contrast uppercase tracking-wider text-sm">${t.name}</span>
                        <span class="block text-xs text-white/50 mt-1">${t.role}</span>
                    </div>
                </div>
            </div>
        `).join('');

        dotsContainer.innerHTML = testimonials.map((_, i) => `
            <button aria-label="Go to slide ${i + 1}" class="w-3 h-3 rounded-full bg-white/20 hover:bg-gold transition-colors ${i === 0 ? 'bg-gold' : ''}" data-index="${i}"></button>
        `).join('');

        lucide.createIcons();
        lazyLoadImages();
        setupCarousel(testimonials.length);
    } catch (error) {
        console.error('Error loading testimonials:', error);

        track.innerHTML = `
            <div class="w-full text-center py-20 space-y-4">
                <i data-lucide="wifi-off" class="w-16 h-16 text-white/30 mx-auto"></i>
                <p class="text-white/80 text-lg">Impossible de charger les témoignages</p>
                <p class="text-white/60 text-sm">Vérifiez votre connexion internet</p>
                <button onclick="location.reload()"
                        class="mt-4 bg-gold text-walnut px-6 py-2 rounded-sm hover:bg-gold-hover transition-colors inline-flex items-center gap-2">
                    <i data-lucide="refresh-cw" class="w-4 h-4"></i>
                    <span>Réessayer</span>
                </button>
            </div>
        `;
        lucide.createIcons();
    }
};

const setupCarousel = (count) => {
    let currentIndex = 0;
    const track = d.getElementById('testimonial-track');
    const dots = d.querySelectorAll('#testimonial-dots button');
    if (!track || dots.length === 0) return;

    const updateSlide = (index) => {
        track.style.transform = `translateX(-${index * 100}%)`;
        dots.forEach((dot, i) => {
            dot.classList.toggle('bg-gold', i === index);
            dot.classList.toggle('bg-white/20', i !== index);
        });
        currentIndex = index;
    };

    dots.forEach(dot => dot.addEventListener('click', () => updateSlide(parseInt(dot.dataset.index))));
    setInterval(() => updateSlide((currentIndex + 1) % count), 5000);
};

const setupInteractions = () => {
    const navbar = d.getElementById('navbar');
    const navbarContainer = d.getElementById('navbar-container');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-md');
            navbarContainer.classList.remove('h-24');
            navbarContainer.classList.add('h-20');
        } else {
            navbar.classList.remove('shadow-md');
            navbarContainer.classList.add('h-24');
            navbarContainer.classList.remove('h-20');
        }
    });

    // Language toggle only - mobile menu is handled by navbar-component.js
    d.getElementById('lang-toggle')?.addEventListener('click', switchLanguage);
    d.getElementById('mobile-lang-toggle')?.addEventListener('click', switchLanguage);
};

const lazyLoadImages = () => {
    const lazyImages = d.querySelectorAll('img.lazy');
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    }, { rootMargin: "0px 0px 200px 0px" });
    lazyImages.forEach(img => observer.observe(img));
};

const initGSAP = () => {
    gsap.registerPlugin(ScrollTrigger);
    gsap.to('.parallax-bg', {
        yPercent: 30,
        ease: 'none',
        scrollTrigger: { trigger: '#home', start: 'top top', end: 'bottom top', scrub: true }
    });
    d.querySelectorAll('.animate-up').forEach(el => {
        gsap.fromTo(el, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out', delay: parseFloat(el.style.animationDelay) || 0 });
    });
    d.querySelectorAll('.reveal-section').forEach(section => {
        gsap.from(section, { opacity: 0, y: 50, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: section, start: 'top 85%', toggleActions: 'play none none none' } });
    });
    // Animations GSAP pour services et portfolio DÉSACTIVÉES pour éviter les problèmes d'invisibilité
    // setTimeout(() => {
    //     gsap.from('.service-card', { opacity: 0, y: 30, stagger: 0.1, duration: 0.8, ease: 'power2.out', scrollTrigger: { trigger: '#services-grid', start: 'top 85%' } });
    //     gsap.from('.portfolio-item', { opacity: 0, scale: 0.95, stagger: 0.1, duration: 0.8, ease: 'power2.out', scrollTrigger: { trigger: '#portfolio-grid', start: 'top 80%' } });
    // }, 100);
};

d.addEventListener('DOMContentLoaded', async () => {
    // Initialiser navbar et footer
    initComponents('home');

    setupLanguage();

    // Charger toutes les données depuis l'API
    await Promise.all([
        renderServices(),
        renderPortfolio(),
        renderTestimonials()
    ]);

    lucide.createIcons();
    setupInteractions();
    initGSAP();
    lazyLoadImages();
    UXEnhancements.runEnhancements();
});
