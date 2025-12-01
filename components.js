import { initNavbar } from './navbar-component.js';
import { initFooter } from './footer-component.js';

// Initialiser tous les composants
export function initComponents(activePage = 'home') {
    initNavbar(activePage);
    initFooter();
}

// Export des fonctions individuelles si besoin
export { initNavbar, initFooter };
