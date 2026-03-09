import pandas as pd


class LeadScoringAgent:

    def __init__(self):
        pass

    def calculate_score(self, lead):

        score = 0
        reasons = []

        if lead["demo_requested"]:
            score += 25
            reasons.append("Lead requested a demo which shows high interest")

        if lead["registration"]:
            score += 15
            reasons.append("Lead completed registration")

        if lead["enquiry_call_whatsapp"]:
            score += 15
            reasons.append("Lead contacted through call or WhatsApp")

        if lead["lead_referral"]:
            score += 20
            reasons.append("Lead came through referral which usually converts better")

        if lead["lead_event"]:
            score += 10
            reasons.append("Lead generated from event marketing")

        if lead["price_comparison"]:
            score += 10
            reasons.append("Lead is actively comparing pricing with competitors")

        if lead["lead_call"]:
            score += 5
            reasons.append("Lead interacted through sales call")

        # recency score
        days = lead["enquiry_from_days"]

        if days <= 3:
            score += 10
            reasons.append("Recent enquiry within last 3 days")

        elif days <= 10:
            score += 5
            reasons.append("Moderately recent enquiry")

        score = min(score, 100)

        action = self.next_best_action(score)

        return {
            "lead_score": score,
            "explanation": reasons,
            "next_best_action": action
        }

    def next_best_action(self, score):

        if score >= 80:
            return "Immediately schedule sales call and close the deal"

        elif score >= 50:
            return "Send product demo and follow up with customer"

        elif score >= 30:
            return "Send educational emails and nurture the lead"

        else:
            return "Add lead to long-term marketing campaign"
