from flask import render_template, request
from sqlalchemy import or_
from job_func.models import Job
from job_func import app, db
from job_func import job_search
from job_func.forms import JobSearchForm
from datetime import datetime, date
today = datetime.now().strftime('%Y-%m-%d') + ' 00:00:00'


@app.route("/")
@app.route('/Search')
def search():
    form = JobSearchForm()
    return render_template('search_jobs.html', title='Search Jobs', form=form)


@app.route('/get_jobs', methods=['POST', 'GET'])
def get_jobs():
    jobs = []
    if request.method == 'POST':
        search = request.form
        keyword = search["keyword"]
        jobs = job_search(keyword)

        db.create_all()
        for job in jobs:
            job = Job(**job)
            link_exist = Job.query.filter_by(link=job.link).first()
            if link_exist:
                pass
            else:
                db.session.add(job)
        db.session.commit()

        jobs = Job.query.filter(or_((Job.search_keyword == keyword), Job.title.like('%Keyword%')))

        return render_template('job_results.html', title='Job Results',
                               job_results=jobs)
