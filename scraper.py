from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.jobstack.it/it-jobs?positiontype=1&isDetail=0').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'jobposts-item')
for job in jobs:
    job_name = job.find('h3').text
    description = job.find('div', class_ = 'jobposts-item_intro').text
    company_name = job.find('span', class_ = 'jobposts-item_company icontext').text
    job_location = job.find('span', class_ = 'jobposts-item_location icontext').text.replace(' ','')
    job_pay = job.find('span', class_ = 'jobposts-item_salary icontext').text

    # print(job_name)
    # print(descritpion)
    # print(company_name)
    # print(job_location)
    # print(job_pay)
    print(f'''
    Job name: {job_name}
    Company name: {company_name}
    Description: {description}
    Location: {job_location}
    Wage: {job_pay}
    ''')

    print(' ')
