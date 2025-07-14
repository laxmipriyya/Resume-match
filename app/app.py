from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_resume
from utils.job_matcher import match_resume_with_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    matches = []
    if request.method == "POST":
        file = request.files["resume"]
        resume_text = extract_text_from_resume(file)
        matches = match_resume_with_jobs(resume_text)
    return render_template("index.html", matches=matches)

if __name__ == "__main__":
    app.run(debug=True)
