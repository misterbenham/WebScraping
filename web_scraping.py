from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.cv-library.co.uk/python-jobs-in-london?us=1').text
soup = BeautifulSoup(html_text, 'lxml')
# job = soup.find('div', class_='results__item')
jobs = soup.find_all('li', class_='results__item')
try:
    for job in jobs:
        job_title = job.find('h2', class_='job__title').text.strip()
        company_name = job.find('a', class_='job__company-link').text.replace(' ', '')
        location = job.find('span', class_='job__details-location').text.strip()
        salary = job.find('dd', class_='job__details-value salary').text

        print(job_title)
        print(company_name)
        print(location)
        print(salary)
        print()
except AttributeError as ae:
    print()




