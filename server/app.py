from config import app, migrate
from rich import print
from datetime import datetime
from models import db
from db_utils import (
    get_all_job_applications,
    find_job_app_by_id,
    add_job_application,
    delete_job_application_by_id,
    get_all_companies,
    find_company_by_id,
    add_company,
    delete_company_by_id,
    get_or_create_company,
    update_company_by_id,
    update_job_application_by_id,
)


# Helper function to validate date format
def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        print(
            "[red]Invalid date format. Please enter a date in the format YYYY-MM-DD.[/red]"
        )
        return False


# Helper function to validate input is a number
def validate_number(input):
    if not input.isdigit():
        print("[red]Invalid input. Please enter a number.[/red]")
        return False
    return True


# Helper function to validate input is not empty
def validate_not_empty(input):
    if not input:
        print("[red]Invalid input. Please enter a non-empty value.[/red]")
        return False
    return True


# Display main menu options
def main_menu():
    print("[bold magenta]Welcome to the Job Application Manager![/bold magenta]")
    print(
        "[bold magenta]Here, you can manage your job applications and potential employers.[/bold magenta]\n"
    )
    while True:
        print("[bold yellow]Main Menu[/bold yellow]")
        print("[bold cyan]1.[/bold cyan] Manage job applications")
        print("[bold cyan]2.[/bold cyan] Manage companies")
        print("[bold cyan]3.[/bold cyan] Exit")
        choice = input("Please choose an option: ")

        if choice == "1":
            manage_job_applications()
        elif choice == "2":
            manage_companies()
        elif choice == "3":
            print("[bold green]Goodbye![/bold green]")
            break
        else:
            print("[red]Invalid option. Please try again.[/red]")


# Manage job applications
def manage_job_applications():
    while True:
        print("\n[bold yellow]Job Applications Menu[/bold yellow]")
        display_all_job_applications()  # Display all job applications
        print("[bold cyan]1.[/bold cyan] Update a job application")
        print("[bold cyan]2.[/bold cyan] Add a new job application")
        print("[bold cyan]3.[/bold cyan] Delete a job application")
        print("[bold cyan]4.[/bold cyan] Go back to main menu")
        choice = input("Please choose an option: ")

        if choice == "1":
            update_job_app()  # Call update function
            display_all_job_applications()  # Display updated list
        elif choice == "2":
            create_new_job_app()
            display_all_job_applications()  # Display updated list
        elif choice == "3":
            delete_job_app()
            display_all_job_applications()  # Display updated list
        elif choice == "4":
            break
        else:
            print("[red]Invalid option. Please try again.[/red]")


# Manage companies
def manage_companies():
    while True:
        print("\n[bold yellow]Companies Menu[/bold yellow]")
        display_all_companies()  # Display all companies
        print("[bold cyan]1.[/bold cyan] Update a company")
        print("[bold cyan]2.[/bold cyan] Add a new company")
        print("[bold cyan]3.[/bold cyan] Delete a company")
        print("[bold cyan]4.[/bold cyan] Go back to main menu")
        choice = input("Please choose an option: ")

        if choice == "1":
            update_company()  # Call update function
            display_all_companies()  # Display updated list
        elif choice == "2":
            create_new_company()
            display_all_companies()  # Display updated list
        elif choice == "3":
            delete_company()
            display_all_companies()  # Display updated list
        elif choice == "4":
            break
        else:
            print("[red]Invalid option. Please try again.[/red]")


# Display all companies
def display_all_companies():
    companies = get_all_companies()
    for company in companies:
        print(
            f"[bold cyan]Id:[/bold cyan] {company.id} | [bold cyan]Name:[/bold cyan] {company.name} | [bold cyan]Industry:[/bold cyan] {company.industry} | [bold cyan]Notes:[/bold cyan] {company.notes} | [bold cyan]Created at:[/bold cyan] {company.created_at} | [bold cyan]Last updated:[/bold cyan] {company.updated_at}"
        )


# Choose company by ID
def choose_company_by_id():
    search_id = input("Enter the ID of the company you want to view or update: ")
    try:
        company = find_company_by_id(int(search_id))
        if company is None:
            print("[red]No company found with this ID. Please try again.[/red]")
        else:
            print(
                f"Id: {company.id} | Name: {company.name} | Industry: {company.industry} | Notes: {company.notes} | Created at: {company.created_at} | Last updated: {company.updated_at}"
            )
    except ValueError:
        print("[red]Invalid input. Please enter a number[/red]")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Update company
def update_company():
    company_id = input("Enter the ID of the company to update: ")
    if not validate_number(company_id):
        return
    company_name = input("Enter the new company name: ")
    if not validate_not_empty(company_name):
        return
    industry = input("Enter the new industry: ")
    if not validate_not_empty(industry):
        return
    notes = input("Enter the new notes: ")
    if not validate_not_empty(notes):
        return

    try:
        updated_company = update_company_by_id(
            company_id, company_name, industry, notes
        )
        print(f"Updated company: {updated_company}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Create a new company
def create_new_company():
    company_name = input("Enter the company name: ")
    if not validate_not_empty(company_name):
        return
    industry = input("Enter the industry: ")
    if not validate_not_empty(industry):
        return
    notes = input("Enter any notes: ")
    if not validate_not_empty(notes):
        return

    try:
        new_company = add_company(company_name, industry, notes)
        print(f"Added new company: {new_company}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Delete a company
def delete_company():
    company_id = input("Enter the ID of the company to delete: ")
    try:
        delete_company_by_id(company_id)
        print(f"Deleted company with ID {company_id}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Display all job applications
def display_all_job_applications():
    job_apps = get_all_job_applications()
    for job_application in job_apps:
        company_name = (
            job_application.company.name if job_application.company else "No company"
        )
        print(
            f"[bold cyan]Id:[/bold cyan] {job_application.id} | [bold cyan]Title:[/bold cyan] {job_application.job_title} | [bold cyan]Status:[/bold cyan] {job_application.status} | [bold cyan]Company:[/bold cyan] {company_name} | [bold cyan]Notes:[/bold cyan] {job_application.notes} | [bold cyan]Date applied:[/bold cyan] {job_application.date_applied} | [bold cyan]Created at:[/bold cyan] {job_application.created_at} | [bold cyan]Last updated:[/bold cyan] {job_application.updated_at}"
        )


# Choose job application by ID
def choose_job_app_by_id():
    search_id = input(
        "Enter the ID of the job application you want to view or update: "
    )
    try:
        job_app = find_job_app_by_id(int(search_id))
        if job_app is None:
            print("[red]No job application found with this ID. Please try again.[/red]")
        else:
            print(
                f"Id: {job_app.id} | Title: {job_app.job_title} | Status: {job_app.status} | Notes: {job_app.notes} | Created at: {job_app.created_at} | Last updated: {job_app.updated_at}"
            )
    except ValueError:
        print("[red]Invalid input. Please enter a number.[/red]")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Update status of job application
def update_job_app():
    job_app_id = input("Enter the ID of the job application to update: ")
    if not validate_number(job_app_id):
        return
    job_title = input("Enter the new job title: ")
    if not validate_not_empty(job_title):
        return
    status = input("Enter the new status: ")
    if not validate_not_empty(status):
        return
    company_name = input("Enter the new company name: ")
    if not validate_not_empty(company_name):
        return
    notes = input("Enter the new notes: ")
    if not validate_not_empty(notes):
        return
    date_applied = input("Enter the new date you applied (YYYY-MM-DD): ")
    if not validate_date_format(date_applied):
        return

    try:
        company_id = get_or_create_company(company_name)
        updated_job_app = update_job_application_by_id(
            job_app_id, job_title, status, company_id, notes, date_applied
        )
        print(f"Updated job application: {updated_job_app}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Create a new job application
def create_new_job_app():
    job_title = input("Enter the job title: ")
    if not validate_not_empty(job_title):
        return
    status = input("Enter the status: ")
    if not validate_not_empty(status):
        return
    company_name = input("Enter the company name: ")
    if not validate_not_empty(company_name):
        return
    notes = input("Enter any notes: ")
    if not validate_not_empty(notes):
        return
    date_applied = input("Enter the date you applied (YYYY-MM-DD): ")
    if not validate_date_format(date_applied):
        return

    try:
        company_id = get_or_create_company(company_name)
        new_job_app = add_job_application(
            job_title, status, company_id, notes, date_applied
        )
        print(f"Added new job application: {new_job_app}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Delete a job application
def delete_job_app():
    job_app_id = input("Enter the ID of the job application to delete: ")
    try:
        delete_job_application_by_id(job_app_id)
        print(f"Deleted job application with ID {job_app_id}")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")


# Main function
if __name__ == "__main__":
    with app.app_context():
        migrate.init_app(app, db)
        main_menu()
