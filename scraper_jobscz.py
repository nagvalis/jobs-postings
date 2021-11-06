from bs4 import BeautifulSoup
import requests
import time

# # makes user write a part of name of the job and parses through the list
# showing the written name
print('Write a part of the job name')
searchfor_job = input('<')
print(f'Filtering out {searchfor_job}')


def find_jobs():
    html_text = requests.get(
        'https://www.jobs.cz/prace/praha/datovy-analytik/?language-skill=en&locality%5Bradius%5D=0').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='grid__item e-8--palm e-13 e-23--desk')
    for index, job in enumerate(jobs):
        job_name = job.find('h3', class_='search-list__main-info__title').text
        company_name = job.find(
            'span', class_='search-list__secondary-info--label').text
        job_location = job.find(
            'span', class_='search-list__secondary-info--label').text
        post_date = job.find(
            'div', class_='search-list__status__data').text
        job_info = job.div.h3.a['href']
        if searchfor_job in job_name:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Job name: {job_name.strip()}\n")
                f.write(f"Company name: {company_name.strip()}\n")
                f.write(f"Location: {job_location.strip()}\n")
                f.write(f"Post date: {post_date.strip()}\n")
                f.write(f"More info: {job_info}\n")
            print(f'File saved: {index}')


print(' ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'Refreshes every {time_wait} minutes..')
        time.sleep(time_wait * 60)
