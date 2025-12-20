import requests

requests.request('GET', 'https://example.domain', verify=True) # Noncompliant
requests.get('https://example.domain', verify=True) # Noncompliant
