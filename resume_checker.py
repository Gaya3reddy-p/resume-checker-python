def load_text(filename):
    with open(filename, "r") as file:
        return file.read().lower()

resume = load_text("resume.txt")
job = load_text("job_description.txt")

resume_words = set(resume.split())
job_words = set(job.split())

matched = resume_words.intersection(job_words)
match_percent = (len(matched) / len(job_words)) * 100

print(f"Resume Match Percentage: {match_percent:.2f}%")
