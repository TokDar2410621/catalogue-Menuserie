export function createFooter() {
    const footer = document.createElement('footer');
    footer.className = 'bg-white pt-20 border-t border-oak/10';

    footer.innerHTML = `
        <div class="container mx-auto px-6 pb-12 max-w-7xl">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16">
                <!-- Brand -->
                <div class="space-y-6">
                    <a href="index.html" class="flex items-center gap-2 group">
                         <img src="image/Création sans titre.svg" alt="DKbois Logo" class="h-24 w-auto object-contain group-hover:opacity-80 transition-all">
                    </a>
                    <p class="text-walnut/70 text-sm leading-relaxed" data-i18n="footer.about"></p>
                    <div class="flex gap-4 text-oak">
                        <a href="#" aria-label="Instagram"><i data-lucide="instagram" class="w-5 h-5 hover:text-gold transition-colors" aria-hidden="true"></i></a>
                        <a href="#" aria-label="Facebook"><i data-lucide="facebook" class="w-5 h-5 hover:text-gold transition-colors" aria-hidden="true"></i></a>
                        <a href="#" aria-label="LinkedIn"><i data-lucide="linkedin" class="w-5 h-5 hover:text-gold transition-colors" aria-hidden="true"></i></a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div>
                    <h3 class="font-serif font-bold text-walnut mb-6" data-i18n="footer.links"></h3>
                    <ul class="space-y-3 text-sm text-walnut/80">
                        <li><a href="index.html" class="hover:text-oak transition-colors" data-i18n="nav.home"></a></li>
                        <li><a href="about.html" class="hover:text-oak transition-colors" data-i18n="nav.about"></a></li>
                        <li><a href="mathurin-defehe.html" class="hover:text-gold transition-colors font-serif" data-i18n="nav.mathurin"></a></li>
                        <li><a href="services.html" class="hover:text-oak transition-colors" data-i18n="nav.services"></a></li>
                        <li><a href="portfolio.html" class="hover:text-oak transition-colors" data-i18n="nav.portfolio"></a></li>
                        <li><a href="contact.html" class="hover:text-oak transition-colors" data-i18n="nav.contact"></a></li>
                    </ul>
                </div>

                <!-- Contact -->
                <div>
                    <h3 class="font-serif font-bold text-walnut mb-6" data-i18n="footer.contact"></h3>
                    <ul class="space-y-4 text-sm text-walnut/80">
                        <li class="flex gap-3">
                            <i data-lucide="map-pin" class="w-5 h-5 text-oak flex-shrink-0 mt-1" aria-hidden="true"></i>
                            <span>Yaoundé, Quartier Mendong<br>Cameroun</span>
                        </li>
                        <li class="flex gap-3">
                            <i data-lucide="phone" class="w-5 h-5 text-oak flex-shrink-0 mt-1" aria-hidden="true"></i>
                            <a href="tel:+237694469929" class="hover:text-gold transition-colors">+237 6 94 46 99 29</a>
                        </li>
                        <li class="flex gap-3">
                            <i data-lucide="mail" class="w-5 h-5 text-oak flex-shrink-0 mt-1" aria-hidden="true"></i>
                            <a href="mailto:contact@dkbois.cm" class="hover:text-gold transition-colors">contact@dkbois.cm</a>
                        </li>
                    </ul>
                </div>

                <!-- Newsletter -->
                <div>
                    <h3 class="font-serif font-bold text-walnut mb-6">Newsletter</h3>
                    <p class="text-sm text-walnut/70 mb-4">Recevez nos actualités et nos conseils.</p>
                     <form id="mailchimp-form" class="flex">
                        <input type="email" placeholder="Votre email" class="w-full bg-white border border-oak/20 py-2 px-3 text-sm focus:outline-none focus:border-gold rounded-l-sm" required>
                        <button type="submit" class="bg-oak text-white px-3 hover:bg-gold transition-colors rounded-r-sm" aria-label="S'inscrire à la newsletter"><i data-lucide="arrow-right" class="w-4 h-4" aria-hidden="true"></i></button>
                    </form>
                </div>
            </div>

            <div class="border-t border-oak/10 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center text-xs text-walnut/60">
                <p>&copy; 2024 DKbois. <span data-i18n="footer.rights"></span></p>
                <div class="flex gap-6 mt-4 md:mt-0">
                    <a href="#" class="hover:text-oak">Mentions Légales</a>
                    <a href="#" class="hover:text-oak">Politique de confidentialité</a>
                </div>
            </div>
        </div>
    `;

    return footer;
}

export function initFooter() {
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        const footer = createFooter();
        footerPlaceholder.replaceWith(footer);
    }
}
