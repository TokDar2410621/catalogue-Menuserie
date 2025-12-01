"""
API Testing Script for DKbois Backend

This script tests all API endpoints to verify they work correctly.
Run this after starting the development server.

Usage:
    python test_api.py
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'


def test_endpoint(name, url, method='GET', data=None, lang='fr'):
    """Test a single API endpoint"""
    print(f"\nTesting: {name}")
    print(f"URL: {url}")

    try:
        params = {'lang': lang}
        if method == 'GET':
            response = requests.get(url, params=params)
        elif method == 'POST':
            response = requests.post(url, json=data, params=params)

        print(f"Status: {response.status_code}")

        if response.status_code in [200, 201]:
            print("Success!")
            if response.status_code == 200:
                result = response.json()
                # Show first result if it's a list
                if isinstance(result, dict) and 'results' in result:
                    print(f"Count: {result.get('count', 'N/A')}")
                    if result['results']:
                        print(f"First item: {json.dumps(result['results'][0], indent=2, ensure_ascii=False)[:200]}...")
                elif isinstance(result, list):
                    print(f"Count: {len(result)}")
                    if result:
                        print(f"First item: {json.dumps(result[0], indent=2, ensure_ascii=False)[:200]}...")
                else:
                    print(f"Result: {json.dumps(result, indent=2, ensure_ascii=False)[:200]}...")
        else:
            print(f"Error: {response.text}")

        return response.status_code in [200, 201]

    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to server. Make sure the dev server is running:")
        print("  python manage.py runserver")
        return False
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False


def main():
    """Run all API tests"""
    print("=" * 70)
    print("DKbois Backend API Testing")
    print("=" * 70)
    print("\nMake sure the development server is running:")
    print("  python manage.py runserver\n")

    results = []

    # Test Projects
    results.append(test_endpoint(
        "Projects List (French)",
        f"{BASE_URL}/projects/",
        lang='fr'
    ))

    results.append(test_endpoint(
        "Projects List (English)",
        f"{BASE_URL}/projects/",
        lang='en'
    ))

    results.append(test_endpoint(
        "Projects - Filtered by Category",
        f"{BASE_URL}/projects/?category=kitchen",
        lang='fr'
    ))

    results.append(test_endpoint(
        "Projects - Featured Only",
        f"{BASE_URL}/projects/featured/",
        lang='fr'
    ))

    results.append(test_endpoint(
        "Project Detail",
        f"{BASE_URL}/projects/cuisine-haussmannienne/",
        lang='fr'
    ))

    # Test Services
    results.append(test_endpoint(
        "Services List",
        f"{BASE_URL}/services/",
        lang='fr'
    ))

    results.append(test_endpoint(
        "Service Detail",
        f"{BASE_URL}/services/menuiserie-interieure/",
        lang='en'
    ))

    # Test Testimonials
    results.append(test_endpoint(
        "Testimonials List",
        f"{BASE_URL}/testimonials/",
        lang='fr'
    ))

    # Test Team
    results.append(test_endpoint(
        "Team Members List",
        f"{BASE_URL}/team/",
        lang='fr'
    ))

    # Test Timeline
    results.append(test_endpoint(
        "Timeline Events",
        f"{BASE_URL}/timeline/",
        lang='fr'
    ))

    # Test Values
    results.append(test_endpoint(
        "Company Values",
        f"{BASE_URL}/values/",
        lang='fr'
    ))

    # Test FAQs
    results.append(test_endpoint(
        "FAQs List",
        f"{BASE_URL}/faqs/",
        lang='fr'
    ))

    # Test Contact Submission
    contact_data = {
        'firstname': 'Test',
        'lastname': 'User',
        'email': 'test@example.com',
        'phone': '0123456789',
        'project_type': 'cabinetry',
        'budget': '5000-15000',
        'description': 'This is a test contact submission',
        'gdpr_consent': True
    }

    results.append(test_endpoint(
        "Contact Form Submission",
        f"{BASE_URL}/contact/",
        method='POST',
        data=contact_data,
        lang='fr'
    ))

    # Summary
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    print(f"Failed: {total - passed}/{total}")

    if passed == total:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. Check the output above for details.")

    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
