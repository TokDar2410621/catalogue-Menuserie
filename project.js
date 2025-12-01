import { translations, allProjectsData } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';

let currentLang = 'fr';
const d = document;

const keyPath = path => path.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || path;

const updateContent = () => {
    d.querySelectorAll('[data-i18n]').forEach(el => el.innerHTML = keyPath(el.dataset.i18n));
};

const setupLanguage = () => {
    currentLang = new URLSearchParams(window.location.search).get('lang') || 'fr';
    d.documentElement.lang = currentLang;
    updateContent();
};

const renderProject = (project) => {
    if (!project) {
        d.body.innerHTML = '<h1>Project not found</h1>';
        return;
    }
    
    d.title = `${project.title[currentLang]} - DKbois`;
    d.querySelector('meta[name="description"]').content = project.shortDesc[currentLang];

    d.getElementById('project-hero').src = project.images[0];
    d.getElementById('project-title').textContent = project.title[currentLang];
    d.getElementById('project-subtitle').textContent = project.shortDesc[currentLang];
    d.getElementById('project-tags').innerHTML = project.tags.map(t => `<span class="bg-gold/90 text-walnut text-xs font-bold px-3 py-1 rounded-sm uppercase tracking-wider">${t}</span>`).join('');
    d.getElementById('project-desc').textContent = project.fullDesc[currentLang];
    d.getElementById('project-challenge').textContent = project.challenge[currentLang];

    d.getElementById('spec-material').textContent = project.material.charAt(0).toUpperCase() + project.material.slice(1);
    d.getElementById('spec-duration').textContent = project.specs.duration[currentLang];
    d.getElementById('spec-location').textContent = project.specs.location;
    d.getElementById('spec-finish').textContent = project.specs.finish[currentLang];
    
    const gallery = d.getElementById('project-gallery');
    gallery.innerHTML = project.images.map(img => `
        <div class="relative aspect-[4/3] overflow-hidden rounded-sm cursor-pointer group" onclick="openLightbox('${img}')">
            <img src="${img}" alt="Project image" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
                <i data-lucide="maximize" class="w-8 h-8 text-white"></i>
            </div>
        </div>`).join('');
    
    d.getElementById('back-to-portfolio').href = `portfolio.html?lang=${currentLang}`;
    d.getElementById('contact-link').href = `contact.html?lang=${currentLang}`;
    d.querySelector('header a').href = `index.html?lang=${currentLang}`;

    lucide.createIcons();
};

window.openLightbox = (src) => {
    const lb = d.getElementById('lightbox');
    d.getElementById('lightbox-img').src = src;
    lb.classList.remove('hidden');
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
            d.body.style.overflow = '';
        }, 300);
    };

    closeBtn.addEventListener('click', closeLightbox);
    lb.addEventListener('click', (e) => e.target === lb && closeLightbox());
    d.addEventListener('keydown', (e) => e.key === 'Escape' && closeLightbox());
};

d.addEventListener('DOMContentLoaded', () => {
    setupLanguage();
    const projectId = new URLSearchParams(window.location.search).get('id');
    const project = allProjectsData.find(p => p.id === projectId);
    renderProject(project);
    setupLightbox();
    UXEnhancements.runEnhancements();
});
