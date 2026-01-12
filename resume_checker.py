import csv

def load_resume_from_csv(filename):
    text = ""
    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            text += row["text"].lower() + " "
    return text

def load_text(filename):
    with open(filename, "r") as file:
        return file.read().lower()

resume = load_resume_from_csv("resume.csv")
job = load_text("job_description.txt")

resume_words = set(resume.split())
job_words = set(job.split())

if len(job_words) == 0:
    print("Job description is empty.")
else:
    matched = resume_words.intersection(job_words)
    match_percent = (len(matched) / len(job_words)) * 100
    print(f"Resume Match Percentage: {match_percent:.2f}%")

