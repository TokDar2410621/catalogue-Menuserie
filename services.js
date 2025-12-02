import { translations, detailedServicesData } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';
import { initComponents } from './components.js';

let currentLang = 'fr';
const d = document;

const updateContent = () => {
    d.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        el.innerHTML = key.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || key;
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
    currentLang = new URLSearchParams(window.location.search).get('lang') || 'fr';
    d.documentElement.lang = currentLang;
    const langToggle = d.getElementById('lang-toggle');
    if (langToggle) langToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    const mobileLangToggle = d.getElementById('mobile-lang-toggle');
    if (mobileLangToggle) mobileLangToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    updateContent();
    updateLinkHrefs();
    renderPageContent();
};

const switchLanguage = () => {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    const url = new URL(window.location);
    url.searchParams.set('lang', currentLang);
    window.history.pushState({}, '', url);
    setupLanguage();
    lucide.createIcons();
    initGSAP();
};

const renderServices = () => {
    const container = d.getElementById('services-container');
    if (!container) return;
    container.innerHTML = detailedServicesData.map((service, index) => {
        const bgClass = index % 2 !== 0 ? 'bg-white border-y border-oak/10' : 'bg-offwhite';
        const directionClass = index % 2 === 0 ? 'lg:flex-row' : 'lg:flex-row-reverse';
        return `
        <section id="${service.anchor}" class="service-section py-16 lg:py-24 ${bgClass} scroll-mt-24 relative z-10">
            <div class="container mx-auto px-6">
                <div class="flex flex-col ${directionClass} gap-12 lg:gap-16 items-start">
                    <div class="lg:w-7/12 space-y-8">
                        <div class="flex items-center gap-4 text-oak"><i data-lucide="${service.icon}" class="w-8 h-8"></i><span class="font-serif italic text-lg tracking-wider">0${index + 1}</span></div>
                        <h2 class="text-4xl md:text-5xl font-serif font-bold text-walnut">${service.title[currentLang]}</h2>
                        <p class="text-walnut/80 leading-relaxed text-lg">${service.description[currentLang]}</p>
                        <div class="py-6 border-t border-b border-oak/10">
                            <h3 class="font-serif font-bold text-walnut mb-4 text-lg">Prestations incluses</h3>
                            <ul class="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-3">
                                ${service.subServices.map(sub => `<li class="flex items-center gap-3 text-walnut/70"><i data-lucide="check" class="w-4 h-4 text-gold"></i>${sub[currentLang]}</li>`).join('')}
                            </ul>
                        </div>
                        <div class="flex flex-wrap gap-6 items-center">
                            <div>
                                <h3 class="font-serif font-bold text-walnut mb-4 text-lg" data-i18n="services_page.process_title"></h3>
                                <div class="flex gap-4 md:gap-8">
                                    ${service.process.map(step => `<div class="text-center"><div class="w-12 h-12 bg-oak/10 rounded-full flex items-center justify-center text-oak font-bold text-lg mb-2">${step.step}</div><p class="text-xs text-walnut/60">${step.title[currentLang]}</p></div>`).join('')}
                                </div>
                            </div>
                            <div class="bg-oak/5 p-4 rounded-sm">
                                <span class="block text-xs text-oak font-bold uppercase tracking-wider" data-i18n="services_page.delay_title"></span>
                                <span class="font-serif text-lg text-walnut">${service.timeframe[currentLang]}</span>
                            </div>
                        </div>
                    </div>
                    <div class="lg:w-5/12 w-full lg:pl-8">
                        <div class="space-y-4">
                            <div class="h-80 rounded-sm overflow-hidden shadow-md group"><img data-src="${service.images[0]}" alt="${service.title[currentLang]}" class="lazy w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"></div>
                            <div class="grid grid-cols-2 gap-4">
                                <div class="h-40 rounded-sm overflow-hidden shadow-sm group"><img data-src="${service.images[1]}" alt="Detail 1" class="lazy w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"></div>
                                <div class="h-40 rounded-sm overflow-hidden shadow-sm group"><img data-src="${service.images[2]}" alt="Detail 2" class="lazy w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"></div>
                            </div>
                            <div class="text-right"><span class="font-serif italic text-oak/60 text-sm" data-i18n="services_page.gallery_title"></span></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>`;
    }).join('');
    updateContent();
};

const renderQuickLinks = () => {
    const container = d.getElementById('service-quick-links');
    if (!container) return;
    container.innerHTML = detailedServicesData.map(s => `<a href="#${s.anchor}" class="px-4 py-2 border border-white/30 text-offwhite hover:border-gold hover:text-gold transition-colors rounded-sm text-sm uppercase tracking-widest">${s.title[currentLang]}</a>`).join('');
};

const renderPageContent = () => {
    renderServices();
    renderQuickLinks();
    lazyLoadImages();
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
    // Mobile menu is handled by navbar-component.js
    d.getElementById('lang-toggle')?.addEventListener('click', switchLanguage);
    d.getElementById('mobile-lang-toggle')?.addEventListener('click', switchLanguage);
};

const initGSAP = () => {
    gsap.registerPlugin(ScrollTrigger);
    d.querySelectorAll('.animate-up').forEach(el => {
        gsap.fromTo(el, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out', delay: parseFloat(el.style.animationDelay) || 0 });
    });
    d.querySelectorAll('.service-section').forEach(section => {
        const content = section.querySelector('.lg\\:w-7\\/12');
        const gallery = section.querySelector('.lg\\:w-5\\/12');
        if (content) gsap.from(content, { opacity: 0, x: -30, duration: 1, scrollTrigger: { trigger: section, start: 'top 70%' } });
        if (gallery) gsap.from(gallery, { opacity: 0, x: 30, duration: 1, delay: 0.2, scrollTrigger: { trigger: section, start: 'top 70%' } });
    });
};

d.addEventListener('DOMContentLoaded', () => {
    // Initialiser navbar et footer
    initComponents('services');

    setupLanguage();
    setupInteractions();
    lucide.createIcons();
    initGSAP();
    UXEnhancements.runEnhancements();
});
