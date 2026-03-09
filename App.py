from fastapi import FastAPI
from lead_scoring import LeadScoringAgent

app = FastAPI()

agent = LeadScoringAgent()

@app.get("/")
def home():
    return {"message": "AI Lead Scoring Assistant Agent is running"}

@app.post("/score-lead")
def score_lead(lead: dict):

    result = agent.calculate_score(lead)

    return {
        "Lead Score": result["lead_score"],
        "Explanation": result["explanation"],
        "Next Best Action": result["next_best_action"]
    }
