# -*- coding: utf-8 -*-
"""

This module gets job summaries and details from website.
"""

import mechanicalsoup


jobs = []

class Job():
    """
    A job object.
    """

    def __init__(self):
        self.search_keyword = ""
        self.search_location = ""
        self.title = ""
        self.job_type = ""
        self.link = ""
        self.date_added = None
        self.date_posted = ""
        self.hiring_organisation = ""

    def as_dict(self):
        return {
            'search_keyword': self.search_keyword,
            'search_location': self.search_location,
            'title': self.title,
            'job_type':self.job_type,
            'link':self.link,
            'date_added': self.date_added,
            'date_posted': self.date_posted,
            'hiring_organisation': self.hiring_organisation
            }

def get_job_list(keyword):
    """
    This function takes keyword as argument.
    It returns a list of job objects.
    """

    browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'})

    url = 'https://weworkremotely.com'
    browser.open(url)
    browser.select_form('form[action="/remote-jobs/search"]')

    browser["term"] = keyword

    search_result_page = browser.submit_selected()

    get_search_result_page = browser.get(search_result_page.url)
    search_result_page_html = search_result_page.soup
    browser.open(search_result_page.url)



    search_results = browser.page.select('.jobs')

    for job_post in search_results:
        for a in job_post.select('a'):
                new_job = Job()
                new_job.search_keyword = keyword
                new_job.link = a["href"]
                location = a.find('span', class_='region company')
                job_title = a.find('span', class_='title')
                if job_title:
                    new_job.title = job_title.text
                if location:
                    new_job.search_location = location.text
                post_date = a.find('time')
                if post_date:
                    new_job.date_posted = post_date.text
                company_class = a.find_all('span', class_='company')
                for i in company_class:
                        job_type = company_class[1]
                        if job_type:
                            new_job.job_type =job_type.text
                company_name = a.select_one('.company')
                # company_name = company_class_list[0]
                if company_name:
                    new_job.hiring_organisation = company_name.text
                
                if new_job.title:
                    jobs.append(new_job)


    browser.close()

    return jobs
