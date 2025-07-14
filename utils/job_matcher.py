import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_with_jobs(resume_text, top_n=5):
    jobs_df = pd.read_csv("data/sample_jobs.csv")
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(jobs_df["description"].tolist() + [resume_text])
    scores = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()
    top_matches = jobs_df.iloc[scores.argsort()[-top_n:][::-1]]
    return top_matches[["title", "company", "description"]].to_dict(orient="records")
