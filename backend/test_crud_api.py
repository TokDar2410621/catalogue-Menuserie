"""
Test script for CRUD operations on Projects and Services API endpoints.
Run this from the backend directory with Django server running on port 3000.

Usage: python test_crud_api.py
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:3000/api"
HEADERS = {"Content-Type": "application/json"}


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_response(response):
    """Pretty print API response"""
    print(f"Status: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except:
        print(f"Response: {response.text}")
    print("-" * 80)


def test_project_crud():
    """Test full CRUD operations for Projects"""
    print_section("TESTING PROJECT CRUD OPERATIONS")

    # CREATE - POST /api/projects/
    print("\n1. CREATE PROJECT (POST /api/projects/)")
    project_data = {
        "title_fr": "Cuisine Test API",
        "title_en": "Test API Kitchen",
        "category": "kitchen",
        "type": "creation",
        "material": "oak",
        "short_desc_fr": "Description courte de test",
        "short_desc_en": "Short test description",
        "full_desc_fr": "Description complète de test pour la cuisine moderne.",
        "full_desc_en": "Full test description for modern kitchen.",
        "challenge_fr": "Défi de test",
        "challenge_en": "Test challenge",
        "duration_fr": "2 semaines",
        "duration_en": "2 weeks",
        "location": "Yaoundé",
        "finish_fr": "Vernis mat",
        "finish_en": "Matte varnish",
        "tags": ["Test", "API", "Cuisine"],
        "images": ["image/test-kitchen.jpg"],
        "featured": True,
        "order": 100
    }

    response = requests.post(f"{BASE_URL}/projects/", json=project_data, headers=HEADERS)
    print_response(response)

    if response.status_code == 201:
        created_project = response.json().get('data', response.json())
        project_slug = created_project.get('slug')
        print(f"✓ Project created with slug: {project_slug}")

        # READ - GET /api/projects/{slug}/
        print("\n2. READ PROJECT (GET /api/projects/{slug}/)")
        response = requests.get(f"{BASE_URL}/projects/{project_slug}/?lang=fr")
        print_response(response)

        # READ LIST - GET /api/projects/
        print("\n3. READ PROJECT LIST (GET /api/projects/)")
        response = requests.get(f"{BASE_URL}/projects/?lang=en")
        print_response(response)

        # UPDATE - PUT /api/projects/{slug}/
        print(f"\n4. UPDATE PROJECT (PUT /api/projects/{project_slug}/)")
        update_data = project_data.copy()
        update_data['title_fr'] = "Cuisine Test API Modifiée"
        update_data['title_en'] = "Modified Test API Kitchen"
        update_data['slug'] = project_slug  # Include slug in update
        update_data['featured'] = False
        update_data['order'] = 101

        response = requests.put(f"{BASE_URL}/projects/{project_slug}/", json=update_data, headers=HEADERS)
        print_response(response)

        # PARTIAL UPDATE - PATCH /api/projects/{slug}/
        print(f"\n5. PARTIAL UPDATE PROJECT (PATCH /api/projects/{project_slug}/)")
        patch_data = {
            "featured": True,
            "order": 99
        }
        response = requests.patch(f"{BASE_URL}/projects/{project_slug}/", json=patch_data, headers=HEADERS)
        print_response(response)

        # DELETE - DELETE /api/projects/{slug}/
        print(f"\n6. DELETE PROJECT (DELETE /api/projects/{project_slug}/)")
        response = requests.delete(f"{BASE_URL}/projects/{project_slug}/")
        print_response(response)

        # VERIFY DELETION
        print(f"\n7. VERIFY DELETION (GET /api/projects/{project_slug}/)")
        response = requests.get(f"{BASE_URL}/projects/{project_slug}/")
        print_response(response)
        if response.status_code == 404:
            print("✓ Project successfully deleted")
    else:
        print("✗ Failed to create project, skipping further tests")


def test_service_crud():
    """Test full CRUD operations for Services"""
    print_section("TESTING SERVICE CRUD OPERATIONS")

    # CREATE - POST /api/services/
    print("\n1. CREATE SERVICE (POST /api/services/)")
    service_data = {
        "service_id": f"test-service-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "icon": "hammer",
        "title_fr": "Service Test API",
        "title_en": "Test API Service",
        "description_fr": "Description de test pour le service API.",
        "description_en": "Test description for API service.",
        "sub_services": {
            "fr": ["Sous-service 1", "Sous-service 2"],
            "en": ["Sub-service 1", "Sub-service 2"]
        },
        "process_steps": {
            "fr": [
                {"step": 1, "title": "Consultation", "description": "Discussion initiale"},
                {"step": 2, "title": "Conception", "description": "Création du design"}
            ],
            "en": [
                {"step": 1, "title": "Consultation", "description": "Initial discussion"},
                {"step": 2, "title": "Design", "description": "Design creation"}
            ]
        },
        "timeframe_fr": "2-4 semaines",
        "timeframe_en": "2-4 weeks",
        "images": ["image/test-service.jpg"],
        "order": 100,
        "is_active": True
    }

    response = requests.post(f"{BASE_URL}/services/", json=service_data, headers=HEADERS)
    print_response(response)

    if response.status_code == 201:
        created_service = response.json().get('data', response.json())
        service_slug = created_service.get('slug')
        print(f"✓ Service created with slug: {service_slug}")

        # READ - GET /api/services/{slug}/
        print("\n2. READ SERVICE (GET /api/services/{slug}/)")
        response = requests.get(f"{BASE_URL}/services/{service_slug}/?lang=fr")
        print_response(response)

        # READ LIST - GET /api/services/
        print("\n3. READ SERVICE LIST (GET /api/services/)")
        response = requests.get(f"{BASE_URL}/services/?lang=en&show_all=true")
        print_response(response)

        # UPDATE - PUT /api/services/{slug}/
        print(f"\n4. UPDATE SERVICE (PUT /api/services/{service_slug}/)")
        update_data = service_data.copy()
        update_data['title_fr'] = "Service Test API Modifié"
        update_data['title_en'] = "Modified Test API Service"
        update_data['slug'] = service_slug  # Include slug in update
        update_data['is_active'] = False
        update_data['order'] = 101

        response = requests.put(f"{BASE_URL}/services/{service_slug}/", json=update_data, headers=HEADERS)
        print_response(response)

        # PARTIAL UPDATE - PATCH /api/services/{slug}/
        print(f"\n5. PARTIAL UPDATE SERVICE (PATCH /api/services/{service_slug}/)")
        patch_data = {
            "is_active": True,
            "order": 99
        }
        response = requests.patch(f"{BASE_URL}/services/{service_slug}/", json=patch_data, headers=HEADERS)
        print_response(response)

        # DELETE - DELETE /api/services/{slug}/
        print(f"\n6. DELETE SERVICE (DELETE /api/services/{slug}/)")
        response = requests.delete(f"{BASE_URL}/services/{service_slug}/")
        print_response(response)

        # VERIFY DELETION
        print(f"\n7. VERIFY DELETION (GET /api/services/{service_slug}/)")
        response = requests.get(f"{BASE_URL}/services/{service_slug}/")
        print_response(response)
        if response.status_code == 404:
            print("✓ Service successfully deleted")
    else:
        print("✗ Failed to create service, skipping further tests")


def test_error_handling():
    """Test error handling for validation"""
    print_section("TESTING ERROR HANDLING")

    # Test duplicate slug
    print("\n1. TEST DUPLICATE PROJECT (should fail)")
    project_data = {
        "slug": "cuisine-moderne",  # Assuming this exists
        "title_fr": "Test Duplicate",
        "title_en": "Test Duplicate",
        "category": "kitchen",
        "type": "creation",
        "material": "oak",
        "short_desc_fr": "Test",
        "short_desc_en": "Test",
        "full_desc_fr": "Test",
        "full_desc_en": "Test"
    }
    response = requests.post(f"{BASE_URL}/projects/", json=project_data, headers=HEADERS)
    print_response(response)

    # Test missing required fields
    print("\n2. TEST MISSING REQUIRED FIELDS (should fail)")
    invalid_project = {
        "title_fr": "Test Incomplete"
    }
    response = requests.post(f"{BASE_URL}/projects/", json=invalid_project, headers=HEADERS)
    print_response(response)


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("  CRUD API TEST SUITE")
    print("  Testing Django REST API endpoints for Projects and Services")
    print("  Server: http://localhost:3000/api")
    print("=" * 80)

    try:
        # Check if API is accessible
        response = requests.get(f"{BASE_URL}/projects/")
        if response.status_code != 200:
            print(f"\n✗ Error: API not accessible at {BASE_URL}")
            print("  Make sure Django server is running: py -3.13 manage.py runserver 3000")
            return
    except requests.exceptions.ConnectionError:
        print(f"\n✗ Error: Cannot connect to API at {BASE_URL}")
        print("  Make sure Django server is running: py -3.13 manage.py runserver 3000")
        return

    # Run tests
    test_project_crud()
    test_service_crud()
    test_error_handling()

    print("\n" + "=" * 80)
    print("  TEST SUITE COMPLETED")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
