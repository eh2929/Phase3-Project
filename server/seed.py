from config import db, app
from models import *
from datetime import datetime

if __name__ == "__main__":
    with app.app_context():

        print("Clearing out tables...")

        Job_application.query.delete()
        Companies.query.delete()

        print("Seeding companies table...")

        companies = [
            Companies(name="Google", industry="Tech"),
            Companies(name="Meta", industry="Tech"),
            Companies(name="Amazon", industry="Tech"),
            Companies(name="Meijer", industry="Retail"),
            Companies(name="Walmart", industry="Retail"),
            Companies(name="Microsoft", industry="Tech"),
            Companies(name="Apple", industry="Tech"),
            Companies(name="Tesla", industry="Automotive"),
            Companies(name="Netflix", industry="Entertainment"),
            Companies(name="Spotify", industry="Entertainment"),
        ]

        db.session.add_all(companies)
        db.session.commit()

        print("Seeding job applications table...")

        job_applications = [
            Job_application(
                job_title="Software Engineer",
                date_applied=datetime.strptime("2022-01-01", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[0].id,
            ),
            Job_application(
                job_title="Back-end Developer",
                date_applied=datetime.strptime("2022-01-02", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[1].id,
            ),
            Job_application(
                job_title="Front-end Developer",
                date_applied=datetime.strptime("2022-01-03", "%Y-%m-%d"),
                status="Rejected",
                company_id=companies[2].id,
            ),
            Job_application(
                job_title="Full-stack Developer",
                date_applied=datetime.strptime("2022-01-04", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[3].id,
            ),
            Job_application(
                job_title="Associate",
                date_applied=datetime.strptime("2022-01-05", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[4].id,
            ),
            Job_application(
                job_title="Data Scientist",
                date_applied=datetime.strptime("2022-01-06", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[5].id,
            ),
            Job_application(
                job_title="Product Manager",
                date_applied=datetime.strptime("2022-01-07", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[6].id,
            ),
            Job_application(
                job_title="UX Designer",
                date_applied=datetime.strptime("2022-01-08", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[7].id,
            ),
            Job_application(
                job_title="DevOps Engineer",
                date_applied=datetime.strptime("2022-01-09", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[8].id,
            ),
            Job_application(
                job_title="QA Engineer",
                date_applied=datetime.strptime("2022-01-10", "%Y-%m-%d"),
                status="Applied",
                company_id=companies[9].id,
            ),
        ]

        db.session.add_all(job_applications)
        db.session.commit()
