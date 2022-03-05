# -*- coding: utf-8 -*-
"""
This code web scrapes job listings and exports a csv file.
"""

from datetime import date
import job_func.get_jobs
import pandas as pd


def job_search(keyword):

    jobs = []

    # Call the get_job_list function
    jobs_list = job_func.get_jobs.get_job_list(keyword)
    
    today = date.today()
    today = today.strftime('%Y%m%d')

    # convert lists of jobs to dictionary and create a dataframe
    df = pd.DataFrame([job.as_dict() for job in jobs_list])

    print(df)

    file_name = f'job_searches_{today}_JobsList.csv'
    print(file_name)
    df.to_csv(file_name, sep=',', index=False) #convert/export dataframe to csv

    # create a new job object to map to db model
    for j in jobs_list:

        job = {
            'search_keyword': j.search_keyword,
            'search_location': j.search_location,
            'title': j.title,
            'job_type': j.job_type,
            'link': j.link,
            'date_added': j.date_added,
            'date_posted': j.date_posted,
            'hiring_organisation': j.hiring_organisation
        }
        jobs.append(job)


    return jobs
