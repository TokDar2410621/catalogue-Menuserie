import { translations, filterOptions } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';
import { initComponents } from './components.js';
import { API } from './api-config.js';

let currentLang = 'fr';
let allProjects = [];
const d = document;

const keyPath = path => path.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || path;
const updateContent = () => d.querySelectorAll('[data-i18n]').forEach(el => el.innerHTML = keyPath(el.dataset.i18n));

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

const setupLanguage = async () => {
    currentLang = new URLSearchParams(window.location.search).get('lang') || 'fr';
    d.documentElement.lang = currentLang;
    const langToggle = d.getElementById('lang-toggle');
    if (langToggle) langToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    const mobileLangToggle = d.getElementById('mobile-lang-toggle');
    if (mobileLangToggle) mobileLangToggle.textContent = currentLang === 'fr' ? 'EN' : 'FR';
    updateContent();
    updateLinkHrefs();
    initFilters();
    await loadProjects();
};

const switchLanguage = () => {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    const url = new URL(window.location);
    url.searchParams.set('lang', currentLang);
    window.history.pushState({}, '', url);
    setupLanguage();
};

const populateSelect = (select, options, type) => {
    if (!select) return;
    select.innerHTML = `<option value="all">${keyPath('portfolio_page.filters.' + type)}</option>`;
    options.forEach(opt => select.innerHTML += `<option value="${opt.value}">${opt.label[currentLang]}</option>`);
};

const initFilters = () => {
    populateSelect(d.getElementById('filter-category'), filterOptions.category, 'category');
    populateSelect(d.getElementById('filter-type'), filterOptions.type, 'type');
    populateSelect(d.getElementById('filter-material'), filterOptions.material, 'material');
};

function resolveImageUrl(url) {
    if (!url) return '';
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('//')) return url;
    return url.startsWith('/') ? url : `/${url}`;
}

const loadProjects = async () => {
    const grid = d.getElementById('projects-grid');
    const emptyState = d.getElementById('empty-state');
    if (grid) grid.innerHTML = `<p class="col-span-full text-center text-walnut/60 py-12">${currentLang === 'fr' ? 'Chargement…' : 'Loading…'}</p>`;
    if (emptyState) emptyState.classList.add('hidden');

    try {
        const response = await API.projects.list(currentLang);
        allProjects = response.results || response;
        applyFilters();
    } catch (error) {
        console.error('Failed to load projects:', error);
        if (grid) grid.innerHTML = `<p class="col-span-full text-center text-red-600 py-12">${currentLang === 'fr' ? 'Erreur de chargement' : 'Loading error'}</p>`;
    }
};

const applyFilters = () => {
    const filters = {
        category: d.getElementById('filter-category')?.value || 'all',
        type: d.getElementById('filter-type')?.value || 'all',
        material: d.getElementById('filter-material')?.value || 'all',
    };
    const filtered = allProjects.filter(p =>
        Object.keys(filters).every(key => filters[key] === 'all' || p[key] === filters[key])
    );
    renderGrid(filtered);
};

const renderGrid = (projects) => {
    const grid = d.getElementById('projects-grid');
    const emptyState = d.getElementById('empty-state');
    if (!grid) return;
    grid.innerHTML = '';

    if (projects.length === 0) {
        if (emptyState) emptyState.classList.remove('hidden');
        return;
    }
    if (emptyState) emptyState.classList.add('hidden');

    projects.forEach(p => {
        const card = d.createElement('a');
        card.href = `project.html?id=${p.slug}&lang=${currentLang}`;
        card.className = 'project-card group block bg-white rounded-sm overflow-hidden shadow-sm hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1';
        const firstImage = resolveImageUrl((p.images || [])[0]);
        const tag = (p.tags || [])[0] || '';
        card.innerHTML = `
            <div class="relative h-64 overflow-hidden">
                <img data-src="${firstImage}" alt="${p.title} - ${p.category} en menuiserie et ébénisterie sur mesure par DKBOIS à Yaoundé, Cameroun" class="lazy w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                <div class="absolute inset-0 bg-black/20 group-hover:bg-black/0 transition-colors"></div>
                ${tag ? `<div class="absolute top-4 left-4"><span class="bg-white/90 text-oak text-xs font-bold px-2 py-1 rounded-sm uppercase tracking-widest">${tag}</span></div>` : ''}
            </div>
            <div class="p-6">
                <h3 class="font-serif font-bold text-xl text-walnut mb-2 group-hover:text-oak transition-colors">${p.title}</h3>
                <p class="text-walnut/60 text-sm line-clamp-2">${p.short_desc || ''}</p>
                <div class="mt-4 pt-4 border-t border-oak/10 flex justify-between items-center text-xs text-oak">
                    <span class="uppercase tracking-wider">${currentLang === 'fr' ? 'Voir détails' : 'View details'}</span>
                    <i data-lucide="arrow-right" class="w-4 h-4 transform group-hover:translate-x-1 transition-transform"></i>
                </div>
            </div>`;
        grid.appendChild(card);
    });

    lazyLoadImages();
    lucide.createIcons();
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

    d.querySelectorAll('.filter-select').forEach(sel => sel.addEventListener('change', applyFilters));
    d.getElementById('reset-filters')?.addEventListener('click', () => {
        d.querySelectorAll('.filter-select').forEach(sel => sel.value = 'all');
        applyFilters();
    });
};

d.addEventListener('DOMContentLoaded', () => {
    initComponents('portfolio');
    setupLanguage();
    setupInteractions();
    lucide.createIcons();
    UXEnhancements.runEnhancements();
});
