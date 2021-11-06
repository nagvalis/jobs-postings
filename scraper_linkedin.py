from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Prague%2C%20Prague%2C%20Czechia&geoId=103973174&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all(
    'div', class_='base-search-card__info')
for job in jobs:
    post_date = job.find('time', class_='job-search-card__listdate').text
    job_name = job.find('h3', class_='base-search-card__title').text
    company_name = job.find('a', class_='hidden-nested-link').text
    job_location = job.find('span', class_='job-search-card__location').text

    print(f"Job name: {job_name.strip()}")
    print(f"Company name: {company_name.strip()}")
    print(f"Location: {job_location.strip()}")
    print(f"Post date: {post_date.strip()}")

    print(' ')
