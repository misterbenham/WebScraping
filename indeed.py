from requests_html import HTMLSession


def get_data(s, url):
    r = s.get(url)
    return r.html.find('div.job_seen_beacon')


def parse_html(html):
    job = {
        'title': html.find('h2 > a')[0].text
    }
    return job


def main():
    session = HTMLSession()
    url = 'https://uk.indeed.com/jobs?q=python+developer&l=London'

    jobs = (get_data(session, url))

    for job in jobs:
        print(parse_html(job))


if __name__ == '__main__':
    main()
