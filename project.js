import { translations } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';
import { API } from './api-config.js';
import { initComponents } from './components.js';

let currentLang = 'fr';
let currentProject = null;
const d = document;

// Legacy English code translations. New projects store French labels
// directly so values are displayed as-is via the fallback below.
const MATERIAL_LABELS = {
    fr: { oak: 'Chêne', walnut: 'Noyer', maple: 'Érable' },
    en: { oak: 'Oak', walnut: 'Walnut', maple: 'Maple', 'Chêne': 'Oak', 'Noyer': 'Walnut', 'Érable': 'Maple' },
};

const keyPath = path => path.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || path;

const updateContent = () => {
    d.querySelectorAll('[data-i18n]').forEach(el => el.innerHTML = keyPath(el.dataset.i18n));
};

const setupLanguage = () => {
    currentLang = new URLSearchParams(window.location.search).get('lang') || 'fr';
    d.documentElement.lang = currentLang;
    updateContent();
};

// Resolve image URL : absolute (Cloudinary) → as-is, relative legacy paths → prefix with /
function resolveImageUrl(url) {
    if (!url) return '';
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('//')) return url;
    return url.startsWith('/') ? url : `/${url}`;
}

const showError = (message) => {
    d.body.innerHTML = `
        <div class="min-h-screen flex flex-col items-center justify-center px-6 text-center">
            <div class="font-serif text-6xl text-oak mb-4">404</div>
            <h1 class="font-serif text-3xl text-walnut mb-4">${message}</h1>
            <a href="portfolio.html?lang=${currentLang}" class="mt-4 inline-flex items-center gap-2 bg-oak text-white px-6 py-3 font-serif hover:bg-gold transition-colors">
                ← ${currentLang === 'fr' ? 'Retour au portfolio' : 'Back to portfolio'}
            </a>
        </div>`;
};

const renderProject = (project) => {
    currentProject = project;

    const title = project.title || '';
    const shortDesc = project.short_desc || '';
    const fullDesc = project.full_desc || '';
    const challenge = project.challenge || '';
    const specs = project.specs || {};
    const images = (project.images || []).map(resolveImageUrl);
    const tags = project.tags || [];

    d.title = `${title} - DKbois`;
    const metaDesc = d.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.content = shortDesc;

    const heroImg = d.getElementById('project-hero');
    heroImg.src = images[0] || '';
    heroImg.alt = `${title} - Projet de menuiserie et ébénisterie sur mesure DKBOIS à Yaoundé, Cameroun`;

    d.getElementById('project-title').textContent = title;
    d.getElementById('project-subtitle').textContent = shortDesc;
    d.getElementById('project-tags').innerHTML = tags.map(t =>
        `<span class="bg-gold/90 text-walnut text-xs font-bold px-3 py-1 rounded-sm uppercase tracking-wider">${t}</span>`
    ).join('');
    d.getElementById('project-desc').textContent = fullDesc;
    d.getElementById('project-challenge').textContent = challenge;

    const materialLabel = MATERIAL_LABELS[currentLang]?.[project.material] || project.material || '';
    d.getElementById('spec-material').textContent = materialLabel;
    d.getElementById('spec-duration').textContent = specs.duration || '—';
    d.getElementById('spec-location').textContent = specs.location || '—';
    d.getElementById('spec-finish').textContent = specs.finish || '—';

    const gallery = d.getElementById('project-gallery');
    gallery.innerHTML = images.map((img, index) => `
        <div class="relative aspect-[4/3] overflow-hidden rounded-sm cursor-pointer group" onclick="openLightbox('${img}')">
            <img src="${img}" alt="${title} - Photo ${index + 1} - Réalisation DKBOIS Yaoundé" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
                <i data-lucide="maximize" class="w-8 h-8 text-white"></i>
            </div>
        </div>`).join('');

    const contactLink = d.getElementById('contact-link');
    if (contactLink) contactLink.href = `contact.html?lang=${currentLang}`;

    lucide.createIcons();
};

const loadProject = async (slug) => {
    try {
        const project = await API.projects.detail(slug, currentLang);
        renderProject(project);
    } catch (error) {
        console.error('Project load error:', error);
        showError(currentLang === 'fr' ? 'Projet introuvable' : 'Project not found');
    }
};

window.openLightbox = (src) => {
    const lb = d.getElementById('lightbox');
    const lbImg = d.getElementById('lightbox-img');
    lbImg.src = src;
    lbImg.alt = `Agrandissement - Réalisation DKBOIS`;
    lb.classList.remove('hidden');
    setTimeout(() => lb.classList.remove('opacity-0'), 10);
    d.body.style.overflow = 'hidden';
};

const setupLightbox = () => {
    const lb = d.getElementById('lightbox');
    const closeBtn = d.getElementById('lightbox-close');
    if (!lb || !closeBtn) return;

    const closeLightbox = () => {
        lb.classList.add('opacity-0');
        setTimeout(() => {
            lb.classList.add('hidden');
            d.body.style.overflow = '';
        }, 300);
    };

    closeBtn.addEventListener('click', closeLightbox);
    lb.addEventListener('click', (e) => e.target === lb && closeLightbox());
    d.addEventListener('keydown', (e) => e.key === 'Escape' && closeLightbox());
};

d.addEventListener('DOMContentLoaded', () => {
    initComponents('portfolio');
    setupLanguage();

    // Accept either ?id=<slug> (legacy) or ?slug=<slug>
    const params = new URLSearchParams(window.location.search);
    const slug = params.get('slug') || params.get('id');

    if (!slug) {
        showError(currentLang === 'fr' ? 'Aucun projet spécifié' : 'No project specified');
        return;
    }

    loadProject(slug);
    setupLightbox();
    UXEnhancements.runEnhancements();
});
