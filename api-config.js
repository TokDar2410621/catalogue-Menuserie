// Configuration API pour DKbois
// Ce fichier centralise toutes les interactions avec le backend Django

// URL de base de l'API (détection automatique de l'environnement)
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:3000/api'
    : 'https://carefree-heart-production-ec3a.up.railway.app/api';

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
        },
        create: (data) => {
            return apiRequest('/testimonials/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (id, data) => {
            return apiRequest(`/testimonials/${id}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (id) => {
            return apiRequest(`/testimonials/${id}/`, {
                method: 'DELETE'
            });
        }
    },

    // Équipe
    team: {
        list: (lang = 'fr') => {
            return apiRequest(`/team/?lang=${lang}`);
        },
        create: (data) => {
            return apiRequest('/team/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (id, data) => {
            return apiRequest(`/team/${id}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (id) => {
            return apiRequest(`/team/${id}/`, {
                method: 'DELETE'
            });
        }
    },

    // Timeline
    timeline: {
        list: (lang = 'fr') => {
            return apiRequest(`/timeline/?lang=${lang}`);
        },
        create: (data) => {
            return apiRequest('/timeline/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (id, data) => {
            return apiRequest(`/timeline/${id}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (id) => {
            return apiRequest(`/timeline/${id}/`, {
                method: 'DELETE'
            });
        }
    },

    // Valeurs
    values: {
        list: (lang = 'fr') => {
            return apiRequest(`/values/?lang=${lang}`);
        },
        create: (data) => {
            return apiRequest('/values/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (id, data) => {
            return apiRequest(`/values/${id}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (id) => {
            return apiRequest(`/values/${id}/`, {
                method: 'DELETE'
            });
        }
    },

    // FAQs
    faqs: {
        list: (lang = 'fr') => {
            return apiRequest(`/faqs/?lang=${lang}`);
        },
        create: (data) => {
            return apiRequest('/faqs/', {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        update: (id, data) => {
            return apiRequest(`/faqs/${id}/`, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        delete: (id) => {
            return apiRequest(`/faqs/${id}/`, {
                method: 'DELETE'
            });
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
