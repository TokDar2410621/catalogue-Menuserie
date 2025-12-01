// Configuration API pour DKbois
// Ce fichier centralise toutes les interactions avec le backend Django

// URL de base de l'API (à adapter selon l'environnement)
const API_BASE_URL = 'http://localhost:3000/api';

// Fonction utilitaire pour faire des requêtes API
const apiRequest = async (endpoint, options = {}) => {
    const url = `${API_BASE_URL}${endpoint}`;

    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.status} ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error(`Error fetching ${endpoint}:`, error);
        throw error;
    }
};

// Fonctions API pour chaque ressource
export const API = {
    // Projets
    projects: {
        list: (lang = 'fr', filters = {}) => {
            const params = new URLSearchParams({ lang, ...filters });
            return apiRequest(`/projects/?${params}`);
        },
        featured: (lang = 'fr') => {
            return apiRequest(`/projects/featured/?lang=${lang}`);
        },
        detail: (slug, lang = 'fr') => {
            return apiRequest(`/projects/${slug}/?lang=${lang}`);
        }
    },

    // Services
    services: {
        list: (lang = 'fr') => {
            return apiRequest(`/services/?lang=${lang}`);
        },
        detail: (slug, lang = 'fr') => {
            return apiRequest(`/services/${slug}/?lang=${lang}`);
        }
    },

    // Témoignages
    testimonials: {
        list: (lang = 'fr') => {
            return apiRequest(`/testimonials/?lang=${lang}`);
        }
    },

    // Équipe
    team: {
        list: (lang = 'fr') => {
            return apiRequest(`/team/?lang=${lang}`);
        }
    },

    // Timeline
    timeline: {
        list: (lang = 'fr') => {
            return apiRequest(`/timeline/?lang=${lang}`);
        }
    },

    // Valeurs
    values: {
        list: (lang = 'fr') => {
            return apiRequest(`/values/?lang=${lang}`);
        }
    },

    // FAQs
    faqs: {
        list: (lang = 'fr') => {
            return apiRequest(`/faqs/?lang=${lang}`);
        }
    },

    // Contact
    contact: {
        submit: (data) => {
            return apiRequest('/contact/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        }
    }
};

// Export de l'URL de base pour usage direct si nécessaire
export { API_BASE_URL };
