import { API, API_BASE_URL } from './api-config.js';

// Global state
let currentUser = null;
let authToken = null;
let uploadedProjectImages = [];
let uploadedServiceImages = [];

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initializeAdmin();
    lucide.createIcons();
});

// Initialize admin
function initializeAdmin() {
    // Check if user is logged in
    authToken = localStorage.getItem('adminToken');

    if (authToken) {
        showAdminDashboard();
        loadDashboardData();
    } else {
        showLoginScreen();
    }

    // Setup event listeners
    setupEventListeners();
}

// Show/Hide screens
function showLoginScreen() {
    document.getElementById('login-screen').classList.remove('hidden');
    document.getElementById('admin-dashboard').classList.add('hidden');
}

function showAdminDashboard() {
    document.getElementById('login-screen').classList.add('hidden');
    document.getElementById('admin-dashboard').classList.remove('hidden');
    lucide.createIcons();
}

// Event listeners
function setupEventListeners() {
    // Login form
    document.getElementById('login-form').addEventListener('submit', handleLogin);

    // Logout button
    document.getElementById('logout-btn').addEventListener('click', handleLogout);

    // Sidebar navigation
    document.querySelectorAll('.sidebar-link').forEach(link => {
        link.addEventListener('click', function() {
            const section = this.dataset.section;
            switchSection(section);
        });
    });

    // Form submissions
    document.getElementById('project-form').addEventListener('submit', handleProjectSubmit);
    document.getElementById('service-form').addEventListener('submit', handleServiceSubmit);

    // Image uploads
    document.getElementById('project-image-files').addEventListener('change', handleProjectImageUpload);
    document.getElementById('service-image-files').addEventListener('change', handleServiceImageUpload);
}

// Login handler
async function handleLogin(e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorDiv = document.getElementById('login-error');

    // For demo purposes - simple authentication
    // TODO: Replace with actual Django authentication
    if (username === 'admin' && password === 'admin') {
        authToken = 'demo-token-' + Date.now();
        localStorage.setItem('adminToken', authToken);
        currentUser = { username: 'admin' };

        showAdminDashboard();
        loadDashboardData();
    } else {
        errorDiv.textContent = 'Nom d\'utilisateur ou mot de passe incorrect';
        errorDiv.classList.remove('hidden');
    }
}

// Logout handler
function handleLogout() {
    localStorage.removeItem('adminToken');
    authToken = null;
    currentUser = null;
    showLoginScreen();
}

// Switch sections
window.switchSection = function(sectionName) {
    // Update sidebar active state
    document.querySelectorAll('.sidebar-link').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.section === sectionName) {
            link.classList.add('active');
        }
    });

    // Show selected section
    document.querySelectorAll('.section-content').forEach(section => {
        section.classList.remove('active');
    });

    const targetSection = document.getElementById(`section-${sectionName}`);
    if (targetSection) {
        targetSection.classList.add('active');

        // Load data for specific sections
        switch(sectionName) {
            case 'projects':
                loadProjects();
                break;
            case 'services':
                loadServices();
                break;
            case 'contact':
                loadMessages();
                break;
        }
    }

    lucide.createIcons();
}

// Load dashboard data
async function loadDashboardData() {
    try {
        // Load statistics
        const [projects, services, testimonials, messages] = await Promise.all([
            API.projects.list('fr'),
            API.services.list('fr'),
            API.testimonials.list('fr'),
            // Messages endpoint might not exist, use empty array if fails
            API.contact ? fetch(`${API_BASE_URL}/contact/`).then(r => r.ok ? r.json() : {results: []}).catch(() => ({results: []})) : Promise.resolve({results: []})
        ]);

        // Update statistics
        document.getElementById('stat-projects').textContent = projects.results?.length || projects.length || 0;
        const featuredCount = projects.results?.filter(p => p.featured).length || projects.filter(p => p.featured).length || 0;
        document.getElementById('stat-projects-featured').textContent = featuredCount;

        document.getElementById('stat-services').textContent = services.results?.length || services.length || 0;
        const activeServices = services.results?.filter(s => s.is_active).length || services.filter(s => s.is_active).length || 0;
        document.getElementById('stat-services-active').textContent = activeServices;

        document.getElementById('stat-testimonials').textContent = testimonials.results?.length || testimonials.length || 0;

        const messagesData = messages.results || messages || [];
        document.getElementById('stat-messages').textContent = messagesData.length;
        const unreadCount = messagesData.filter(m => !m.is_read).length;
        document.getElementById('stat-messages-unread').textContent = unreadCount;

        // Load recent messages
        loadRecentMessages(messagesData.slice(0, 5));

    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

// Load recent messages for dashboard
function loadRecentMessages(messages) {
    const container = document.getElementById('recent-messages');

    if (messages.length === 0) {
        container.innerHTML = '<p class="text-walnut/40 text-sm">Aucun message</p>';
        return;
    }

    container.innerHTML = messages.map(msg => `
        <div class="p-3 bg-offwhite rounded-lg hover:bg-oak/5 transition-colors cursor-pointer" onclick="switchSection('contact')">
            <div class="flex items-center justify-between mb-1">
                <span class="font-medium text-walnut text-sm">${msg.firstname} ${msg.lastname}</span>
                <span class="${msg.is_read ? 'badge-success' : 'badge-warning'} badge">${msg.is_read ? 'Lu' : 'Non lu'}</span>
            </div>
            <p class="text-xs text-walnut/60 truncate">${msg.description}</p>
        </div>
    `).join('');
}

// Load projects
async function loadProjects() {
    const tbody = document.getElementById('projects-table');
    tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-walnut/40">Chargement...</td></tr>';

    try {
        const response = await API.projects.list('fr');
        const projects = response.results || response;

        if (projects.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-walnut/40">Aucun projet</td></tr>';
            return;
        }

        tbody.innerHTML = projects.map(project => `
            <tr class="table-row border-b border-oak/5">
                <td class="px-6 py-4">
                    <div class="flex items-center gap-3">
                        ${project.images && project.images[0] ?
                            `<img src="${project.images[0]}" alt="${project.title}" class="w-12 h-12 object-cover rounded-lg">` :
                            '<div class="w-12 h-12 bg-oak/10 rounded-lg"></div>'
                        }
                        <div>
                            <div class="font-medium text-walnut">${project.title}</div>
                            <div class="text-xs text-walnut/60">${project.slug}</div>
                        </div>
                    </div>
                </td>
                <td class="px-6 py-4 text-sm text-walnut">${project.category}</td>
                <td class="px-6 py-4 text-sm text-walnut">${project.type}</td>
                <td class="px-6 py-4">
                    <span class="${project.featured ? 'badge-success' : 'badge'}">${project.featured ? 'Oui' : 'Non'}</span>
                </td>
                <td class="px-6 py-4">
                    <div class="flex items-center gap-2">
                        <button class="p-2 text-oak hover:bg-oak/10 rounded transition-colors" onclick="editProject('${project.slug}')">
                            <i data-lucide="edit" class="w-4 h-4"></i>
                        </button>
                        <button class="p-2 text-red-600 hover:bg-red-50 rounded transition-colors" onclick="deleteProject('${project.slug}')">
                            <i data-lucide="trash-2" class="w-4 h-4"></i>
                        </button>
                    </div>
                </td>
            </tr>
        `).join('');

        lucide.createIcons();

    } catch (error) {
        console.error('Error loading projects:', error);
        tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-red-600">Erreur de chargement</td></tr>';
    }
}

// Load services
async function loadServices() {
    const tbody = document.getElementById('services-table');
    tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-walnut/40">Chargement...</td></tr>';

    try {
        const response = await API.services.list('fr');
        const services = response.results || response;

        if (services.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-walnut/40">Aucun service</td></tr>';
            return;
        }

        tbody.innerHTML = services.map(service => `
            <tr class="table-row border-b border-oak/5">
                <td class="px-6 py-4">
                    <div class="font-medium text-walnut">${service.title}</div>
                    <div class="text-xs text-walnut/60">${service.slug}</div>
                </td>
                <td class="px-6 py-4">
                    <i data-lucide="${service.icon}" class="w-5 h-5 text-oak"></i>
                </td>
                <td class="px-6 py-4">
                    <span class="${service.is_active ? 'badge-success' : 'badge-danger'}">${service.is_active ? 'Actif' : 'Inactif'}</span>
                </td>
                <td class="px-6 py-4 text-sm text-walnut">${service.order}</td>
                <td class="px-6 py-4">
                    <div class="flex items-center gap-2">
                        <button class="p-2 text-oak hover:bg-oak/10 rounded transition-colors" onclick="editService('${service.slug}')">
                            <i data-lucide="edit" class="w-4 h-4"></i>
                        </button>
                        <button class="p-2 text-red-600 hover:bg-red-50 rounded transition-colors" onclick="deleteService('${service.slug}')">
                            <i data-lucide="trash-2" class="w-4 h-4"></i>
                        </button>
                    </div>
                </td>
            </tr>
        `).join('');

        lucide.createIcons();

    } catch (error) {
        console.error('Error loading services:', error);
        tbody.innerHTML = '<tr><td colspan="5" class="px-6 py-8 text-center text-red-600">Erreur de chargement</td></tr>';
    }
}

// Load messages
async function loadMessages() {
    const tbody = document.getElementById('messages-table');
    tbody.innerHTML = '<tr><td colspan="6" class="px-6 py-8 text-center text-walnut/40">Chargement...</td></tr>';

    try {
        // Try to fetch messages - this endpoint might not be accessible
        const response = await fetch('http://localhost:3000/api/contact/', {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });

        if (!response.ok) {
            throw new Error('Cannot access messages endpoint');
        }

        const data = await response.json();
        const messages = data.results || data || [];

        if (messages.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" class="px-6 py-8 text-center text-walnut/40">Aucun message</td></tr>';
            return;
        }

        tbody.innerHTML = messages.map(msg => `
            <tr class="table-row border-b border-oak/5">
                <td class="px-6 py-4">
                    <div class="font-medium text-walnut">${msg.firstname} ${msg.lastname}</div>
                    <div class="text-xs text-walnut/60">${msg.phone || 'N/A'}</div>
                </td>
                <td class="px-6 py-4 text-sm text-walnut">${msg.email}</td>
                <td class="px-6 py-4 text-sm text-walnut">${msg.project_type}</td>
                <td class="px-6 py-4 text-sm text-walnut/60">${new Date(msg.created_at).toLocaleDateString('fr-FR')}</td>
                <td class="px-6 py-4">
                    <span class="${msg.is_read ? 'badge-success' : 'badge-warning'}">${msg.is_read ? 'Lu' : 'Non lu'}</span>
                </td>
                <td class="px-6 py-4">
                    <div class="flex items-center gap-2">
                        <button class="p-2 text-oak hover:bg-oak/10 rounded transition-colors" onclick="viewMessage(${msg.id})">
                            <i data-lucide="eye" class="w-4 h-4"></i>
                        </button>
                        <button class="p-2 text-red-600 hover:bg-red-50 rounded transition-colors" onclick="deleteMessage(${msg.id})">
                            <i data-lucide="trash-2" class="w-4 h-4"></i>
                        </button>
                    </div>
                </td>
            </tr>
        `).join('');

        lucide.createIcons();

    } catch (error) {
        console.error('Error loading messages:', error);
        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="px-6 py-8 text-center">
                    <div class="text-walnut/60 mb-2">
                        <i data-lucide="alert-circle" class="w-8 h-8 mx-auto mb-2"></i>
                    </div>
                    <p class="text-walnut/60">Les messages ne sont pas accessibles depuis cette interface.</p>
                    <p class="text-walnut/40 text-sm mt-2">Utilisez l'interface Django Admin à l'adresse: <a href="http://localhost:3000/admin/" class="text-oak hover:underline" target="_blank">http://localhost:3000/admin/</a></p>
                </td>
            </tr>
        `;
        lucide.createIcons();
    }
}

// Modal functions
window.openModal = function(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) {
        // Clear form for new items
        if (type === 'project') {
            document.getElementById('project-form').reset();
            document.getElementById('project-id').value = '';
        } else if (type === 'service') {
            document.getElementById('service-form').reset();
            document.getElementById('service-id').value = '';
        }

        modal.classList.add('active');
        lucide.createIcons();
    }
}

window.closeModal = function(type) {
    const modal = document.getElementById(`modal-${type}`);
    if (modal) {
        modal.classList.remove('active');

        // Clear form on close
        if (type === 'project') {
            document.getElementById('project-form').reset();
            document.getElementById('project-id').value = '';
            uploadedProjectImages = [];
            document.getElementById('project-image-previews').innerHTML = '';
            document.getElementById('project-upload-status').textContent = '';
        } else if (type === 'service') {
            document.getElementById('service-form').reset();
            document.getElementById('service-id').value = '';
            uploadedServiceImages = [];
            document.getElementById('service-image-previews').innerHTML = '';
            document.getElementById('service-upload-status').textContent = '';
        }
    }
}

// CRUD Operations
window.editProject = async function(slug) {
    try {
        // Load project data
        const project = await API.projects.detail(slug, 'fr');

        // Populate form
        document.getElementById('project-id').value = slug;
        document.getElementById('project-slug').value = project.slug || '';
        document.getElementById('project-title-fr').value = project.title_fr || '';
        document.getElementById('project-title-en').value = project.title_en || '';
        document.getElementById('project-category').value = project.category || 'kitchen';
        document.getElementById('project-type').value = project.type || 'creation';
        document.getElementById('project-material').value = project.material || '';
        document.getElementById('project-short-desc-fr').value = project.short_desc_fr || '';
        document.getElementById('project-short-desc-en').value = project.short_desc_en || '';
        document.getElementById('project-full-desc-fr').value = project.full_desc_fr || '';
        document.getElementById('project-full-desc-en').value = project.full_desc_en || '';
        document.getElementById('project-location').value = project.location || '';
        document.getElementById('project-duration-fr').value = project.duration_fr || '';
        document.getElementById('project-duration-en').value = project.duration_en || '';
        document.getElementById('project-images').value = (project.images || []).join(', ');
        document.getElementById('project-tags').value = (project.tags || []).join(', ');
        document.getElementById('project-featured').checked = project.featured || false;
        document.getElementById('project-order').value = project.order || 0;

        // Open modal directly without resetting
        const modal = document.getElementById('modal-project');
        modal.classList.add('active');
        lucide.createIcons();
    } catch (error) {
        console.error('Error loading project:', error);
        alert('❌ Erreur de chargement: ' + error.message);
    }
}

window.deleteProject = async function(slug) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce projet?')) {
        try {
            await API.projects.delete(slug);
            alert('✅ Projet supprimé avec succès!');
            loadProjects(); // Refresh list
        } catch (error) {
            console.error('Error deleting project:', error);
            alert('❌ Erreur de suppression: ' + error.message);
        }
    }
}

window.editService = async function(slug) {
    try {
        // Load service data
        const service = await API.services.detail(slug, 'fr');

        // Populate form
        document.getElementById('service-id').value = slug;
        document.getElementById('service-service-id').value = service.service_id || '';
        document.getElementById('service-slug').value = service.slug || '';
        document.getElementById('service-icon').value = service.icon || '';
        document.getElementById('service-title-fr').value = service.title_fr || '';
        document.getElementById('service-title-en').value = service.title_en || '';
        document.getElementById('service-description-fr').value = service.description_fr || '';
        document.getElementById('service-description-en').value = service.description_en || '';
        document.getElementById('service-timeframe-fr').value = service.timeframe_fr || '';
        document.getElementById('service-timeframe-en').value = service.timeframe_en || '';

        // Handle sub-services
        if (service.sub_services) {
            const subServicesFr = service.sub_services.fr || [];
            const subServicesEn = service.sub_services.en || [];
            document.getElementById('service-sub-services-fr').value = subServicesFr.join(', ');
            document.getElementById('service-sub-services-en').value = subServicesEn.join(', ');
        }

        document.getElementById('service-images').value = (service.images || []).join(', ');
        document.getElementById('service-is-active').checked = service.is_active !== false;
        document.getElementById('service-order').value = service.order || 0;

        // Open modal directly without resetting
        const modal = document.getElementById('modal-service');
        modal.classList.add('active');
        lucide.createIcons();
    } catch (error) {
        console.error('Error loading service:', error);
        alert('❌ Erreur de chargement: ' + error.message);
    }
}

window.deleteService = async function(slug) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce service?')) {
        try {
            await API.services.delete(slug);
            alert('✅ Service supprimé avec succès!');
            loadServices(); // Refresh list
        } catch (error) {
            console.error('Error deleting service:', error);
            alert('❌ Erreur de suppression: ' + error.message);
        }
    }
}

window.viewMessage = function(id) {
    console.log('View message:', id);
    alert('Fonction de visualisation en cours de développement');
}

window.deleteMessage = function(id) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce message?')) {
        console.log('Delete message:', id);
        alert('Fonction de suppression en cours de développement');
    }
}

// Helper function to remove empty string values from form data
function cleanFormData(data) {
    const cleaned = {};
    for (const [key, value] of Object.entries(data)) {
        // Keep the value if it's not an empty string
        // Keep false, 0, empty arrays, and objects
        if (value !== '' || typeof value === 'boolean' || typeof value === 'number' || Array.isArray(value) || (typeof value === 'object' && value !== null)) {
            cleaned[key] = value;
        }
    }
    return cleaned;
}

// Form submission handlers
async function handleProjectSubmit(e) {
    e.preventDefault();

    const projectId = document.getElementById('project-id').value;
    const isEdit = projectId && projectId !== '';

    const formData = {
        title_fr: document.getElementById('project-title-fr').value.trim(),
        featured: document.getElementById('project-featured').checked,
        order: parseInt(document.getElementById('project-order').value) || 0
    };

    // Add optional fields only if they have values
    const slug = document.getElementById('project-slug').value.trim();
    if (slug) formData.slug = slug;

    const titleEn = document.getElementById('project-title-en').value.trim();
    if (titleEn) formData.title_en = titleEn;

    const category = document.getElementById('project-category').value;
    if (category) formData.category = category;

    const type = document.getElementById('project-type').value;
    if (type) formData.type = type;

    const material = document.getElementById('project-material').value.trim();
    if (material) formData.material = material;

    const shortDescFr = document.getElementById('project-short-desc-fr').value.trim();
    if (shortDescFr) formData.short_desc_fr = shortDescFr;

    const shortDescEn = document.getElementById('project-short-desc-en').value.trim();
    if (shortDescEn) formData.short_desc_en = shortDescEn;

    const fullDescFr = document.getElementById('project-full-desc-fr').value.trim();
    if (fullDescFr) formData.full_desc_fr = fullDescFr;

    const fullDescEn = document.getElementById('project-full-desc-en').value.trim();
    if (fullDescEn) formData.full_desc_en = fullDescEn;

    const location = document.getElementById('project-location').value.trim();
    if (location) formData.location = location;

    const durationFr = document.getElementById('project-duration-fr').value.trim();
    if (durationFr) formData.duration_fr = durationFr;

    const durationEn = document.getElementById('project-duration-en').value.trim();
    if (durationEn) formData.duration_en = durationEn;

    // Parse images (comma-separated) and merge with uploaded images
    const imagesText = document.getElementById('project-images').value.trim();
    const manualImages = imagesText ? imagesText.split(',').map(img => img.trim()).filter(img => img) : [];
    formData.images = [...uploadedProjectImages, ...manualImages];

    // Parse tags (comma-separated)
    const tagsText = document.getElementById('project-tags').value.trim();
    formData.tags = tagsText ? tagsText.split(',').map(tag => tag.trim()).filter(tag => tag) : [];

    try {
        let response;
        if (isEdit) {
            // Update existing project
            response = await API.projects.update(projectId, formData);
            alert('✅ Projet mis à jour avec succès!');
        } else {
            // Create new project
            response = await API.projects.create(formData);
            alert('✅ Projet créé avec succès!');
        }

        console.log('Project response:', response);

        closeModal('project');
        document.getElementById('project-form').reset();
        uploadedProjectImages = [];
        document.getElementById('project-image-previews').innerHTML = '';
        loadProjects(); // Refresh list

    } catch (error) {
        console.error('Error submitting project:', error);
        alert('❌ Erreur: ' + error.message);
    }
}

async function handleServiceSubmit(e) {
    e.preventDefault();

    const serviceId = document.getElementById('service-id').value;
    const isEdit = serviceId && serviceId !== '';

    const formData = {
        title_fr: document.getElementById('service-title-fr').value.trim(),
        is_active: document.getElementById('service-is-active').checked,
        order: parseInt(document.getElementById('service-order').value) || 0
    };

    // Add optional fields only if they have values
    const serviceIdField = document.getElementById('service-service-id').value.trim();
    if (serviceIdField) formData.service_id = serviceIdField;

    const slug = document.getElementById('service-slug').value.trim();
    if (slug) formData.slug = slug;

    const icon = document.getElementById('service-icon').value.trim();
    if (icon) formData.icon = icon;

    const titleEn = document.getElementById('service-title-en').value.trim();
    if (titleEn) formData.title_en = titleEn;

    const descriptionFr = document.getElementById('service-description-fr').value.trim();
    if (descriptionFr) formData.description_fr = descriptionFr;

    const descriptionEn = document.getElementById('service-description-en').value.trim();
    if (descriptionEn) formData.description_en = descriptionEn;

    const timeframeFr = document.getElementById('service-timeframe-fr').value.trim();
    if (timeframeFr) formData.timeframe_fr = timeframeFr;

    const timeframeEn = document.getElementById('service-timeframe-en').value.trim();
    if (timeframeEn) formData.timeframe_en = timeframeEn;

    // Parse sub-services (comma-separated)
    const subServicesFr = document.getElementById('service-sub-services-fr').value.trim();
    const subServicesEn = document.getElementById('service-sub-services-en').value.trim();
    const subServicesFrArray = subServicesFr ? subServicesFr.split(',').map(s => s.trim()).filter(s => s) : [];
    const subServicesEnArray = subServicesEn ? subServicesEn.split(',').map(s => s.trim()).filter(s => s) : [];

    // Only add sub_services if at least one language has values
    if (subServicesFrArray.length > 0 || subServicesEnArray.length > 0) {
        formData.sub_services = {
            fr: subServicesFrArray,
            en: subServicesEnArray
        };
    }

    // Parse images (comma-separated) and merge with uploaded images
    const imagesText = document.getElementById('service-images').value.trim();
    const manualImages = imagesText ? imagesText.split(',').map(img => img.trim()).filter(img => img) : [];
    formData.images = [...uploadedServiceImages, ...manualImages];

    try {
        let response;
        if (isEdit) {
            // Update existing service
            response = await API.services.update(serviceId, formData);
            alert('✅ Service mis à jour avec succès!');
        } else {
            // Create new service
            response = await API.services.create(formData);
            alert('✅ Service créé avec succès!');
        }

        console.log('Service response:', response);

        closeModal('service');
        document.getElementById('service-form').reset();
        uploadedServiceImages = [];
        document.getElementById('service-image-previews').innerHTML = '';
        loadServices(); // Refresh list

    } catch (error) {
        console.error('Error submitting service:', error);
        alert('❌ Erreur: ' + error.message);
    }
}

// Image upload handlers
async function handleProjectImageUpload(e) {
    const files = Array.from(e.target.files);
    if (files.length === 0) return;

    const statusEl = document.getElementById('project-upload-status');
    const previewEl = document.getElementById('project-image-previews');

    statusEl.textContent = `Téléversement de ${files.length} image(s)...`;

    try {
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            statusEl.textContent = `Téléversement ${i + 1}/${files.length}...`;

            const response = await API.upload.image(file);
            uploadedProjectImages.push(response.url);

            // Add preview
            const previewDiv = document.createElement('div');
            previewDiv.className = 'relative group';
            previewDiv.innerHTML = `
                <img src="/media/${response.url}" class="w-full h-20 object-cover rounded border border-oak/20">
                <button type="button" onclick="removeProjectImage('${response.url}')"
                        class="absolute top-1 right-1 bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            `;
            previewEl.appendChild(previewDiv);
            lucide.createIcons();
        }

        statusEl.textContent = `✅ ${files.length} image(s) téléversée(s)`;
        e.target.value = ''; // Reset file input

    } catch (error) {
        console.error('Upload error:', error);
        statusEl.textContent = `❌ Erreur: ${error.message}`;
    }
}

async function handleServiceImageUpload(e) {
    const files = Array.from(e.target.files);
    if (files.length === 0) return;

    const statusEl = document.getElementById('service-upload-status');
    const previewEl = document.getElementById('service-image-previews');

    statusEl.textContent = `Téléversement de ${files.length} image(s)...`;

    try {
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            statusEl.textContent = `Téléversement ${i + 1}/${files.length}...`;

            const response = await API.upload.image(file);
            uploadedServiceImages.push(response.url);

            // Add preview
            const previewDiv = document.createElement('div');
            previewDiv.className = 'relative group';
            previewDiv.innerHTML = `
                <img src="/media/${response.url}" class="w-full h-20 object-cover rounded border border-oak/20">
                <button type="button" onclick="removeServiceImage('${response.url}')"
                        class="absolute top-1 right-1 bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            `;
            previewEl.appendChild(previewDiv);
            lucide.createIcons();
        }

        statusEl.textContent = `✅ ${files.length} image(s) téléversée(s)`;
        e.target.value = ''; // Reset file input

    } catch (error) {
        console.error('Upload error:', error);
        statusEl.textContent = `❌ Erreur: ${error.message}`;
    }
}

// Remove image functions
window.removeProjectImage = function(url) {
    const index = uploadedProjectImages.indexOf(url);
    if (index > -1) {
        uploadedProjectImages.splice(index, 1);
    }
    // Refresh preview
    renderProjectImagePreviews();
}

window.removeServiceImage = function(url) {
    const index = uploadedServiceImages.indexOf(url);
    if (index > -1) {
        uploadedServiceImages.splice(index, 1);
    }
    // Refresh preview
    renderServiceImagePreviews();
}

function renderProjectImagePreviews() {
    const previewEl = document.getElementById('project-image-previews');
    previewEl.innerHTML = uploadedProjectImages.map(url => `
        <div class="relative group">
            <img src="/media/${url}" class="w-full h-20 object-cover rounded border border-oak/20">
            <button type="button" onclick="removeProjectImage('${url}')"
                    class="absolute top-1 right-1 bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
        </div>
    `).join('');
    lucide.createIcons();
}

function renderServiceImagePreviews() {
    const previewEl = document.getElementById('service-image-previews');
    previewEl.innerHTML = uploadedServiceImages.map(url => `
        <div class="relative group">
            <img src="/media/${url}" class="w-full h-20 object-cover rounded border border-oak/20">
            <button type="button" onclick="removeServiceImage('${url}')"
                    class="absolute top-1 right-1 bg-red-600 text-white rounded-full w-6 h-6 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
        </div>
    `).join('');
    lucide.createIcons();
}
