import { translations } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';
import { initComponents } from './components.js';

let currentLang = 'fr';
const d = document;

const mathurinData = {
    photos: [
        // Photos professionnelles en costume
        'image/atelier-images/proprietaire-costume-assis-planches-atelier.jpg',
        'image/atelier-images/proprietaire-costume-assis-planches-atelier-02.jpg',
        // Photos assis dans l'atelier
        'image/atelier-images/proprietaire-atelier-assis-planches-bois-01.jpg',
        'image/atelier-images/proprietaire-atelier-assis-planches-bois-02.jpg',
        // Artisan à l'atelier
        'image/atelier-images/artisan-a-latelier.jpg',
        'image/atelier-images/artisan-avec-porte.jpg',
        'image/atelier-images/artisans-avec-porte.jpg',
        // Selfies avec réalisations
        'image/atelier-images/artisan-selfie-commode-orange-tiroirs.jpg',
        'image/atelier-images/artisan-selfie-porte-lamelles-horizontales.jpg',
        // Installation plafond
        'image/atelier-images/artisan-installation-plafond-bois-chevron.jpg',
        'image/atelier-images/artisan-installation-plafond-bois-chevron-02.jpg',
        // Équipe avec réalisation
        'image/atelier-images/equipe-artisant-meuble-chausure.jpg'
    ]
};

const keyPath = path => path.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || path;

const updateContent = () => {
    d.querySelectorAll('[data-i18n]').forEach(el => {
        const translation = keyPath(el.dataset.i18n);
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
        } catch (e) { /* ignore */ }
    });
};

const setupLanguage = () => {
    const urlParams = new URLSearchParams(window.location.search);
    currentLang = ['fr', 'en'].includes(urlParams.get('lang')) ? urlParams.get('lang') : 'fr';
    d.documentElement.lang = currentLang;

    const langToggle = d.getElementById('lang-toggle');
    const mobileLangToggle = d.getElementById('mobile-lang-toggle');
    if (langToggle) langToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    if (mobileLangToggle) mobileLangToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';

    updateContent();
    updateLinkHrefs();
    renderBioContent();
    renderPhilosophy();
};

const switchLanguage = () => {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    const url = new URL(window.location);
    url.searchParams.set('lang', currentLang);
    window.history.pushState({}, '', url);
    setupLanguage();
    lucide.createIcons();
};

const renderBioContent = () => {
    const container = d.getElementById('bio-content');
    if (!container) return;

    const paragraphs = keyPath('mathurin_page.bio_paragraphs');
    container.innerHTML = paragraphs.map(p => `<p>${p}</p>`).join('');
};

const renderPhotoGallery = () => {
    const gallery = d.getElementById('photo-gallery');
    if (!gallery) return;

    gallery.innerHTML = mathurinData.photos.map((photo, index) => `
        <div class="relative aspect-[4/3] overflow-hidden rounded-sm cursor-pointer group shadow-lg hover:shadow-xl transition-shadow" onclick="openLightbox('${photo}')">
            <img data-src="${photo}"
                 alt="Mathurin Defehe dans son atelier DKBOIS à Yaoundé - Photo ${index + 1} - Maître artisan menuisier ébéniste au travail, Cameroun"
                 class="lazy w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
                <i data-lucide="maximize" class="w-8 h-8 text-white"></i>
            </div>
        </div>
    `).join('');

    lazyLoadImages();
};

const renderPhilosophy = () => {
    const container = d.getElementById('philosophy-content');
    if (!container) return;

    const values = keyPath('mathurin_page.philosophy_values');
    container.innerHTML = values.map(val => `
        <div class="text-center space-y-4">
            <div class="w-20 h-20 mx-auto bg-white/10 rounded-full flex items-center justify-center text-gold mb-4 border border-white/20">
                <i data-lucide="${val.icon}" class="w-10 h-10"></i>
            </div>
            <h3 class="text-xl font-serif font-bold">${val.title}</h3>
            <p class="text-white/70 leading-relaxed">${val.description}</p>
        </div>
    `).join('');
};

window.openLightbox = (src) => {
    const lb = d.getElementById('lightbox');
    const lbImg = d.getElementById('lightbox-img');
    lbImg.src = src;
    lbImg.alt = 'Mathurin Defehe - Maître artisan DKBOIS dans son atelier de menuiserie et ébénisterie à Yaoundé, Cameroun';
    lb.classList.remove('hidden');
    lb.classList.add('flex');
    setTimeout(() => lb.classList.remove('opacity-0'), 10);
    d.body.style.overflow = 'hidden';
};

const setupLightbox = () => {
    const lb = d.getElementById('lightbox');
    const closeBtn = d.getElementById('lightbox-close');

    const closeLightbox = () => {
        lb.classList.add('opacity-0');
        setTimeout(() => {
            lb.classList.add('hidden');
            lb.classList.remove('flex');
            d.body.style.overflow = '';
        }, 300);
    };

    closeBtn.addEventListener('click', closeLightbox);
    lb.addEventListener('click', (e) => e.target === lb && closeLightbox());
    d.addEventListener('keydown', (e) => e.key === 'Escape' && closeLightbox());
};

const lazyLoadImages = () => {
    const lazyImages = d.querySelectorAll('img.lazy');
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                obs.unobserve(img);
            }
        });
    }, { rootMargin: "200px" });
    lazyImages.forEach(img => observer.observe(img));
};

const setupInteractions = () => {
    d.getElementById('lang-toggle')?.addEventListener('click', switchLanguage);
    d.getElementById('mobile-lang-toggle')?.addEventListener('click', switchLanguage);
};

const initGSAP = () => {
    gsap.registerPlugin(ScrollTrigger);

    d.querySelectorAll('.animate-up').forEach(el => {
        gsap.fromTo(el,
            { opacity: 0, y: 30 },
            { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out', delay: parseFloat(el.style.animationDelay) || 0 }
        );
    });

    d.querySelectorAll('.reveal-section').forEach(section => {
        gsap.from(section, {
            opacity: 0,
            y: 50,
            duration: 1,
            ease: 'power3.out',
            scrollTrigger: {
                trigger: section,
                start: 'top 85%',
                toggleActions: 'play none none none'
            }
        });
    });
};

d.addEventListener('DOMContentLoaded', () => {
    // Initialize navbar and footer
    initComponents('mathurin');

    setupLanguage();
    renderPhotoGallery();
    setupInteractions();
    setupLightbox();
    lucide.createIcons();
    initGSAP();
    lazyLoadImages();
    UXEnhancements.runEnhancements();
});
