from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.startupjobs.cz/nabidky').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', class_='divider-top')
for job in jobs:
    job_name = job.find(
        'h3', class_='home-hot-offers-name font-weight-normal').text
    job_location = job.find(
        'p', class_='d-inline dot-before-sm-down dot-before-primary mb-0 mr-1 dot-before-hot').text

    print(f"Job name: {job_name.strip()}")
    print(f"Location: {job_location.strip()}")

    print(' ')
