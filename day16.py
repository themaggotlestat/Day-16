careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
    {"career": "IT Support", "salary": 18, "remote": False}
]

minimum_salary = int(input("What is your minimum salary?"))

def find_high_paying_jobs(careers, minimum_salary):
    matching_jobs = []
    for job in careers:
        if job["salary"] >= minimum_salary:
            matching_jobs.append(job)
    return matching_jobs


def show_jobs(jobs):
    for job in jobs:
        print(job["career"])


jobs = find_high_paying_jobs(careers, minimum_salary)

show_jobs(jobs)