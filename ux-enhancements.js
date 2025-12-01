// UX Enhancements - Common functionality for all pages
// Import this file in all page JS files

export const UXEnhancements = {
    // Scroll to top button
    initScrollToTop() {
        const scrollBtn = document.createElement('button');
        scrollBtn.id = 'scroll-to-top';
        scrollBtn.innerHTML = '<i data-lucide="arrow-up"></i>';
        scrollBtn.className = 'fixed bottom-8 right-8 bg-oak text-white w-12 h-12 rounded-full shadow-lg flex items-center justify-center opacity-0 pointer-events-none transition-all duration-300 hover:bg-gold hover:scale-110 z-50';
        scrollBtn.setAttribute('aria-label', 'Retour en haut');
        document.body.appendChild(scrollBtn);

        // Show/hide on scroll
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            const scrolled = window.pageYOffset > 400;

            if (scrolled) {
                scrollBtn.classList.remove('opacity-0', 'pointer-events-none');
                scrollBtn.classList.add('opacity-100', 'pointer-events-auto');
            } else {
                scrollBtn.classList.add('opacity-0', 'pointer-events-none');
                scrollBtn.classList.remove('opacity-100', 'pointer-events-auto');
            }
        });

        // Smooth scroll to top
        scrollBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        // Reinitialize lucide icons for the new button
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    },

    // Smooth scroll for anchor links
    initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href === '#' || href === '') return;

                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    const offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 100;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    },

    // Enhanced image loading with skeleton
    enhanceImageLoading() {
        const lazyImages = document.querySelectorAll('img.lazy');
        lazyImages.forEach(img => {
            // Add skeleton background
            img.style.backgroundColor = '#e5e7eb';
            img.style.backgroundImage = 'linear-gradient(90deg, #e5e7eb 0%, #f3f4f6 50%, #e5e7eb 100%)';
            img.style.backgroundSize = '200% 100%';
            img.style.animation = 'shimmer 1.5s infinite';

            // Add loaded class when image loads
            img.addEventListener('load', () => {
                img.style.backgroundColor = 'transparent';
                img.style.backgroundImage = 'none';
                img.style.animation = 'none';
                img.classList.add('image-loaded');
            });
        });
    },

    // Add ripple effect to buttons
    addRippleEffect() {
        document.querySelectorAll('button, .btn, a[class*="bg-"]').forEach(element => {
            element.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;

                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.classList.add('ripple');

                this.style.position = 'relative';
                this.style.overflow = 'hidden';
                this.appendChild(ripple);

                setTimeout(() => ripple.remove(), 600);
            });
        });
    },

    // Improve focus visibility for accessibility
    enhanceFocusStates() {
        // Add visible focus ring to interactive elements
        const style = document.createElement('style');
        style.textContent = `
            a:focus-visible, button:focus-visible, input:focus-visible, textarea:focus-visible, select:focus-visible {
                outline: 3px solid #D4AF37 !important;
                outline-offset: 2px !important;
            }

            .nav-link:focus-visible {
                outline: 2px solid #D4AF37 !important;
                outline-offset: 4px !important;
            }
        `;
        document.head.appendChild(style);
    },

    // Add loading indicator for page transitions
    addPageLoadingIndicator() {
        const loader = document.createElement('div');
        loader.id = 'page-loader';
        loader.className = 'fixed top-0 left-0 w-full h-1 bg-gold z-[100] transform scale-x-0 origin-left transition-transform duration-300';
        document.body.appendChild(loader);

        // Show loader on page navigation
        document.querySelectorAll('a[href$=".html"]').forEach(link => {
            link.addEventListener('click', () => {
                loader.style.transform = 'scaleX(1)';
            });
        });

        // Hide loader when page loads
        window.addEventListener('load', () => {
            loader.style.transform = 'scaleX(0)';
        });
    },

    // Improve mobile menu interactions
    enhanceMobileMenu() {
        const mobileMenu = document.getElementById('mobile-menu');
        if (!mobileMenu) return;

        // Add swipe to close functionality
        let touchStartX = 0;
        let touchEndX = 0;

        mobileMenu.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        mobileMenu.addEventListener('touchend', e => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        }, { passive: true });

        function handleSwipe() {
            if (touchEndX > touchStartX + 50) {
                // Swipe right to close
                mobileMenu.classList.add('translate-x-full');
            }
        }

        // Trap focus inside mobile menu when open
        const focusableElements = mobileMenu.querySelectorAll('a, button');
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        mobileMenu.addEventListener('keydown', e => {
            if (e.key !== 'Tab') return;

            if (e.shiftKey && document.activeElement === firstElement) {
                e.preventDefault();
                lastElement.focus();
            } else if (!e.shiftKey && document.activeElement === lastElement) {
                e.preventDefault();
                firstElement.focus();
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('translate-x-full')) {
                mobileMenu.classList.add('translate-x-full');
            }
        });
    },

    // Add scroll progress indicator
    addScrollProgress() {
        const progressBar = document.createElement('div');
        progressBar.id = 'scroll-progress';
        progressBar.className = 'fixed top-0 left-0 h-1 bg-gradient-to-r from-oak via-gold to-oak z-[60] transition-all duration-150';
        progressBar.style.width = '0%';
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', () => {
            const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (window.pageYOffset / windowHeight) * 100;
            progressBar.style.width = scrolled + '%';
        });
    },

    // Add entrance animations for cards
    addCardAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('card-visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.team-card, .service-card, .portfolio-item, .value-item').forEach(card => {
            card.classList.add('card-animate');
            observer.observe(card);
        });
    },

    // Initialize all enhancements
    init() {
        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.runEnhancements());
        } else {
            this.runEnhancements();
        }
    },

    runEnhancements() {
        this.initScrollToTop();
        this.initSmoothScroll();
        this.enhanceImageLoading();
        this.addRippleEffect();
        this.enhanceFocusStates();
        this.addPageLoadingIndicator();
        this.enhanceMobileMenu();
        this.addScrollProgress();
        this.addCardAnimations();
    }
};

// Auto-initialize if not imported as module
if (typeof window !== 'undefined' && !window.UX_MANUAL_INIT) {
    UXEnhancements.init();
}
