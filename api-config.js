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
            // Try to get error details from response
            let errorMessage = `API Error: ${response.status} ${response.statusText}`;
            try {
                const errorData = await response.json();
                if (errorData.message || errorData.error) {
                    errorMessage = errorData.message || errorData.error;
                }
            } catch (e) {
                // Response is not JSON, use default error message
            }
            throw new Error(errorMessage);
        }

        // DELETE requests return 204 No Content
        if (response.status === 204 || options.method === 'DELETE') {
            return { message: 'Operation successful' };
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
        },
        create: (data) => {
            return apiRequest('/projects/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (slug, data) => {
            return apiRequest(`/projects/${slug}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (slug) => {
            return apiRequest(`/projects/${slug}/`, {
                method: 'DELETE'
            });
        }
    },

    // Services
    services: {
        list: (lang = 'fr') => {
            return apiRequest(`/services/?lang=${lang}`);
        },
        detail: (slug, lang = 'fr') => {
            return apiRequest(`/services/${slug}/?lang=${lang}`);
        },
        create: (data) => {
            return apiRequest('/services/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (slug, data) => {
            return apiRequest(`/services/${slug}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (slug) => {
            return apiRequest(`/services/${slug}/`, {
                method: 'DELETE'
            });
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
    },

    // Upload
    upload: {
        image: async (file) => {
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await fetch(`${API_BASE_URL}/upload/`, {
                    method: 'POST',
                    body: formData
                    // Don't set Content-Type header, browser will set it with boundary
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || 'Upload failed');
                }

                return await response.json();
            } catch (error) {
                console.error('Upload error:', error);
                throw error;
            }
        }
    }
};

// Export de l'URL de base pour usage direct si nécessaire
export { API_BASE_URL };
