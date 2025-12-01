import { translations, faqData } from './data.js';
import { UXEnhancements } from './ux-enhancements.js';
import { initComponents } from './components.js';

let currentLang = 'fr';
const d = document;

const keyPath = path => path.split('.').reduce((acc, part) => acc && acc[part], translations[currentLang]) || path;
const updateContent = () => d.querySelectorAll('[data-i18n]').forEach(el => { el.innerHTML = keyPath(el.dataset.i18n); });

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
    renderFAQ();
    renderFormOptions();
};

const switchLanguage = () => {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    const url = new URL(window.location);
    url.searchParams.set('lang', currentLang);
    window.history.pushState({}, '', url);
    setupLanguage();
    lucide.createIcons();
};

const renderFAQ = () => {
    const container = d.getElementById('faq-container');
    if (!container) return;
    container.innerHTML = faqData.map(item => `
        <div class="border border-oak/10 rounded-sm overflow-hidden faq-item">
            <button class="w-full flex justify-between items-center p-5 text-left bg-offwhite/30 hover:bg-white transition-colors" onclick="toggleFAQ(this)">
                <span class="font-serif font-bold text-walnut group-hover:text-oak text-lg">${item.question[currentLang]}</span>
                <i data-lucide="chevron-down" class="w-5 h-5 text-oak transition-transform duration-300"></i>
            </button>
            <div class="max-h-0 overflow-hidden transition-all duration-500 ease-in-out bg-white">
                <p class="p-5 text-walnut/70 leading-relaxed border-t border-oak/5">${item.answer[currentLang]}</p>
            </div>
        </div>`).join('');
};

const renderFormOptions = () => {
    const projectTypes = ['type_interior', 'type_cabinetry', 'type_restoration', 'type_fitting', 'type_other'];
    const select = d.getElementById('project-type-select');
    if(select) {
        select.innerHTML = `<option value="" disabled selected>${keyPath('contact_page.form.select_option')}</option>`;
        projectTypes.forEach(type => select.innerHTML += `<option value="${type}">${keyPath('contact_page.form.'+type)}</option>`);
    }

    const budgetOptions = ['budget_1', 'budget_2', 'budget_3'];
    const budgetContainer = d.getElementById('budget-options');
    if(budgetContainer) {
        budgetContainer.innerHTML = budgetOptions.map((opt, i) => `
            <label class="cursor-pointer"><input type="radio" name="budget" value="${opt}" class="peer sr-only">
            <span class="block px-4 py-2 border border-oak/30 rounded-sm text-sm text-walnut/70 peer-checked:bg-oak peer-checked:text-white peer-checked:border-oak transition-all">${keyPath('contact_page.form.'+opt)}</span></label>
        `).join('');
    }
};

window.toggleFAQ = (btn) => {
    const content = btn.nextElementSibling;
    const item = btn.parentElement;
    const wasOpen = item.classList.contains('open');

    d.querySelectorAll('.faq-item.open').forEach(openItem => {
        if (openItem !== item) {
            openItem.classList.remove('open');
            openItem.querySelector('div').style.maxHeight = null;
            openItem.querySelector('i').style.transform = 'rotate(0deg)';
        }
    });

    if (wasOpen) {
        item.classList.remove('open');
        content.style.maxHeight = null;
        btn.querySelector('i').style.transform = 'rotate(0deg)';
    } else {
        item.classList.add('open');
        content.style.maxHeight = content.scrollHeight + "px";
        btn.querySelector('i').style.transform = 'rotate(180deg)';
    }
};

const setupForm = () => {
    const form = d.getElementById('contact-form');
    if (!form) return;
    
    d.getElementById('file-upload').addEventListener('change', (e) => {
        d.getElementById('file-name').textContent = e.target.files.length > 0 ? e.target.files[0].name : '';
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const statusBox = d.getElementById('form-status');
        const btn = form.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.innerHTML = `<span class="animate-pulse">...</span>`;

        setTimeout(() => {
            btn.disabled = false;
            btn.innerHTML = keyPath('cta.send');
            statusBox.textContent = keyPath('contact_page.success_message');
            statusBox.className = 'block p-3 rounded-sm text-sm font-bold bg-green-100 text-green-800';
            form.reset();
            d.getElementById('file-name').textContent = '';
        }, 1500);
    });
};

const setupInteractions = () => {
    const menuBtn = d.getElementById('mobile-menu-btn');
    const closeBtn = d.getElementById('close-menu-btn');
    const mobileMenu = d.getElementById('mobile-menu');
    const toggleMenu = () => mobileMenu.classList.toggle('translate-x-full');
    if(menuBtn) menuBtn.addEventListener('click', toggleMenu);
    if(closeBtn) closeBtn.addEventListener('click', toggleMenu);
    d.querySelectorAll('.mobile-link').forEach(l => l.addEventListener('click', toggleMenu));

    d.getElementById('lang-toggle')?.addEventListener('click', switchLanguage);
    d.getElementById('mobile-lang-toggle')?.addEventListener('click', switchLanguage);
};

d.addEventListener('DOMContentLoaded', () => {
    // Initialiser navbar et footer
    initComponents('contact');

    setupLanguage();
    setupInteractions();
    setupForm();
    lucide.createIcons();
    gsap.from('.animate-up', { y: 30, opacity: 0, duration: 0.5, stagger: 0.1, ease: 'power3.out' });
    UXEnhancements.runEnhancements();
});
