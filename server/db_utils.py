from models import db, Job_application, Companies
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime


def get_all_companies():
    return db.session.query(Companies).all()


def find_company_by_id(id):
    return db.session.query(Companies).get(id)


def update_company_by_id(company_id, company_name, industry, notes):
    company = Companies.query.get(company_id)
    if company is None:
        return None

    company.name = company_name
    company.industry = industry
    company.notes = notes

    db.session.commit()

    return company


def get_all_job_applications():
    return db.session.query(Job_application).all()


def find_job_app_by_id(id):
    return db.session.get(Job_application, id)


def update_job_application_by_id(
    job_app_id, job_title, status, company_id, notes, date_applied
):
    job_app = Job_application.query.get(job_app_id)
    if job_app is None:
        return None
    job_app.job_title = job_title
    job_app.status = status
    job_app.company_id = company_id
    job_app.notes = notes
    job_app.date_applied = datetime.strptime(date_applied, "%Y-%m-%d")
    db.session.commit()
    return job_app


def add_job_application(job_title, status, company_id, notes, date_applied):
    new_job_app = Job_application(
        job_title=job_title,
        status=status,
        company_id=company_id,
        notes=notes,
        date_applied=datetime.strptime(date_applied, "%Y-%m-%d"),
    )
    db.session.add(new_job_app)
    db.session.commit()
    return new_job_app


def add_company(name, industry, notes):
    new_company = Companies(name=name, industry=industry, notes=notes)
    db.session.add(new_company)
    db.session.commit()
    return new_company


def get_or_create_company(company_name):
    try:
        company = db.session.query(Companies).filter_by(name=company_name).one()
    except NoResultFound:
        company = Companies(name=company_name)
        db.session.add(company)
        db.session.commit()
    return company.id


def delete_job_application_by_id(id):
    job_app = db.session.query(Job_application).get(id)
    if job_app is None:
        print(f"No job application found with ID {id}")
        return
    db.session.delete(job_app)
    db.session.commit()
    print(f"Deleted job application with ID {id}")


def delete_company_by_id(company_id):
    try:
        company = db.session.query(Companies).get(company_id)
        if company is None:
            print(f"No company found with ID {company_id}")
            return
        db.session.delete(company)
        db.session.commit()
        print(f"Deleted company with ID {company_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
