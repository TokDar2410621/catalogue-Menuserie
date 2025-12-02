import { translations, timelineData, teamData, valuesData } from './data.js';
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
    currentLang = ['fr', 'en'].includes(urlParams.get('lang')) ? urlParams.get('lang') : 'fr';
    d.documentElement.lang = currentLang;
    const langToggle = d.getElementById('lang-toggle');
    const mobileLangToggle = d.getElementById('mobile-lang-toggle');
    if (langToggle) langToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
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

const renderTimeline = () => {
    const container = d.getElementById('timeline-container');
    if (!container) return;
    container.innerHTML = timelineData.map((item, index) => {
        const sideClass = index % 2 === 0 ? 'md:text-right md:pr-12' : 'md:pl-12';
        const itemClass = index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse';
        return `
        <div class="timeline-item flex ${itemClass} items-start mb-12">
            <div class="md:w-1/2 w-full pl-8 md:pl-0 ${sideClass}">
                <p class="font-serif text-2xl text-gold">${item.year}</p>
                <h3 class="text-2xl font-serif font-bold text-walnut mt-1 mb-2">${item.title[currentLang]}</h3>
                <p class="text-walnut/70 leading-relaxed">${item.desc[currentLang]}</p>
            </div>
            <div class="absolute left-4 md:left-1/2 top-1 w-4 h-4 mt-1 bg-offwhite border-2 border-gold rounded-full z-10 -translate-x-1/2"></div>
        </div>`;
    }).join('');
};

const renderFounder = () => {
    const container = d.getElementById('founder-content');
    if (!container || teamData.length === 0) return;

    const founder = teamData[0]; // First member is the founder
    container.innerHTML = `
        <div class="bg-white rounded-sm shadow-lg overflow-hidden border border-oak/10">
            <div class="grid md:grid-cols-2 gap-0">
                <div class="relative h-96 md:h-auto overflow-hidden">
                    <img data-src="${founder.image}" alt="${founder.name} - ${founder.role[currentLang]} de DKBOIS, expert en menuiserie et ébénisterie à Yaoundé, Cameroun avec ${founder.exp} ans d'expérience"
                         class="lazy w-full h-full object-cover object-center">
                    <div class="absolute inset-0 bg-gradient-to-t from-walnut/80 via-walnut/20 to-transparent"></div>
                </div>
                <div class="p-8 md:p-12 flex flex-col justify-center">
                    <div class="mb-6">
                        <p class="text-gold font-serif text-sm uppercase tracking-widest mb-2">${founder.role[currentLang]}</p>
                        <h3 class="font-serif font-bold text-3xl md:text-4xl text-walnut mb-2">${founder.name}</h3>
                        <div class="flex items-center gap-2 text-oak">
                            <i data-lucide="briefcase" class="w-4 h-4"></i>
                            <span class="text-sm">${founder.exp} ${currentLang === 'fr' ? "ans d'expérience" : "years of experience"}</span>
                        </div>
                    </div>
                    <div class="mb-6 p-4 bg-offwhite/50 border-l-4 border-gold rounded">
                        <p class="font-serif italic text-walnut/80 text-lg leading-relaxed">"${founder.quote[currentLang]}"</p>
                    </div>
                    ${founder.bio ? `
                        <div class="text-walnut/70 leading-relaxed space-y-3">
                            ${founder.bio[currentLang].split('\n\n').map(para => `<p>${para}</p>`).join('')}
                        </div>
                    ` : ''}
                </div>
            </div>
        </div>
    `;
};

const renderTeam = () => {
    const grid = d.getElementById('team-grid');
    if (!grid) return;

    // Render team members excluding the founder (skip first member)
    const teamMembers = teamData.slice(1);
    grid.innerHTML = teamMembers.map(member => `
        <div class="team-card group text-center">
            <div class="relative h-72 w-full overflow-hidden rounded-sm mb-4">
                <img data-src="${member.image}" alt="${member.name} - ${member.role[currentLang]} chez DKBOIS, artisan menuisier et ébéniste à Yaoundé, Cameroun" class="lazy w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
                <div class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent flex items-end justify-center p-4 opacity-0 group-hover:opacity-100 transition-opacity">
                    <p class="text-white font-serif italic text-sm text-center">"${member.quote[currentLang]}"</p>
                </div>
            </div>
            <h3 class="font-serif font-bold text-xl text-walnut">${member.name}</h3>
            <p class="text-oak text-sm uppercase tracking-wider">${member.role[currentLang]}</p>
        </div>`
    ).join('');
};

const renderValues = () => {
    const grid = d.getElementById('values-grid');
    if (!grid) return;
    grid.innerHTML = valuesData.map(val => `
        <div class="value-item text-center">
            <div class="w-20 h-20 mx-auto bg-white/10 rounded-full flex items-center justify-center text-gold mb-6 border border-white/20">
                <i data-lucide="${val.icon}" class="w-8 h-8"></i>
            </div>
            <h3 class="text-xl font-serif font-bold text-white mb-3">${val.title[currentLang]}</h3>
            <p class="text-white/60 text-sm leading-relaxed">${val.desc[currentLang]}</p>
        </div>`
    ).join('');
};

const renderPageContent = () => {
    renderTimeline();
    renderFounder();
    renderTeam();
    renderValues();
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
    d.querySelectorAll('.reveal-section').forEach(section => {
        gsap.from(section, { opacity: 0, y: 50, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: section, start: 'top 85%', toggleActions: 'play none none none' } });
    });
    gsap.from('.timeline-item', { opacity: 0, x: -30, stagger: 0.2, duration: 0.8, scrollTrigger: { trigger: '#timeline-container', start: 'top 70%' } });
    gsap.from('#founder-content', { opacity: 0, y: 40, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: '#founder-content', start: 'top 80%', toggleActions: 'play none none none' } });
    gsap.from('.team-card', { opacity: 0, y: 30, stagger: 0.15, duration: 0.8, scrollTrigger: { trigger: '#team-grid', start: 'top 80%' } });
    gsap.from('.value-item', { opacity: 0, y: 40, stagger: 0.15, duration: 0.8, scrollTrigger: { trigger: '#values-grid', start: 'top 80%' } });
};

d.addEventListener('DOMContentLoaded', () => {
    // Initialiser navbar et footer
    initComponents('about');

    setupLanguage();
    setupInteractions();
    lucide.createIcons();
    initGSAP();
    UXEnhancements.runEnhancements();
});
