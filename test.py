#!/usr/bin/python3

from bs4 import BeautifulSoup
import mechanicalsoup


class Job():
    """
    This class initialises the job object.
    """

    def __init__(self):
        self.keyword = ""
        self.location = ""
        self.title = ""
        # self.radius = ""
        self.link = ""
        # self.salary = ""
        self.job_type = ""
        # #self.json = ""
        self.date_posted = ""
        # self.valid_through = ""
        self.hiring_organisation_name = ""
        # self.hiring_city = ""
        # self.hiring_region = ""
        # self.hiring_contact = ""
        # self.hiring_reference = ""
        # self.job_id = ""
        #self.description = ""

browser = mechanicalsoup.StatefulBrowser(soup_config={'features': 'lxml'})

url = 'https://weworkremotely.com'
browser.open(url)
browser.select_form('form[action="/remote-jobs/search"]')
    
keyword = 'devops'
browser["term"] = keyword

# url = 'https://www.geezjobs.com'
# browser.open(url)
# browser.select_form('form[action="https://www.geezjobs.com/search"]')

# soup = BeautifulSoup('lxml')
#web_page_html = web_page.soup
# form = web_page_html.select("form")[0]
# form.select(".input-group")[0]["value"] = 'law'
# form.select(".input-group")[1]["value"] = 'addis ababa'
# browser["search"] = "it"
# browser["city"] = "Addis Ababa"

# search_result_page = browser.submit(form, web_page.url)
search_result_page = browser.submit_selected()

# find total search results pages
get_search_result_page = browser.get(search_result_page.url)
print(get_search_result_page.url)

browser.open(search_result_page.url)
# print(browser.page)
job_list = []
search_result_page_html = search_result_page.soup
search_results = browser.page.select('.jobs')

for job_post in search_results:
    for a in job_post.select('a'):
            new_job = Job()
            new_job.keyword = keyword
            new_job.link = a["href"]
            location = a.find('span', class_='region company')
            job_title = a.find('span', class_='title')
            if job_title:
                new_job.title = job_title.text
            if location:
                new_job.location = location.text
            post_date = a.find('time')
            if post_date:
                new_job.date_posted = post_date.text
            company_class = a.find_all('span', class_='company')
            for i in company_class:
                    # print(company_class[2])
                    job_type = company_class[1]
                    if job_type:
                        new_job.job_type =job_type.text
            company_name = a.select_one('.company')
            # company_name = company_class_list[0]
            if company_name:
                new_job.hiring_organisation_name = company_name.text
            
            if new_job.title:
                job_list.append(new_job)

#driver.quit()
browser.close()

for job in job_list:
    print('Job Title: ' + job.title+',','Location: ' + job.location +',', 'Date Posted: ' + job.date_posted+',', 'Company name: ' + job.hiring_organisation_name+',', 'Job Type: ' + job.job_type)
    # print(job.link)