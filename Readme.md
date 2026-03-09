# AI Powered Lead Scoring Assistant Agent

This project implements a simple AI-powered Lead Scoring System that can be integrated inside a CRM system to help sales teams prioritize leads.

## Problem

Sales teams receive many leads but not all leads are equally valuable.  
This system automatically scores leads based on engagement signals and recommends the next best action.

## Features

- Lead Score from 0 to 100
- Explanation for why the score was assigned
- Suggests next best action for sales team
- API ready for CRM integration

## Input Data

Each lead contains the following attributes:

- Demo Requested
- Registration
- Enquiry via Call or WhatsApp
- Enquiry From Date
- Plan Pricing Comparison
- Lead through Events
- Lead through Call
- Lead through Referral

## How It Works

1. Lead attributes are passed to the API
2. Scoring engine evaluates lead intent signals
3. System generates score
4. Explanation and recommended action are returned

## Example Output
Lead Name: Rahul Sharma
Lead Score: 95 (Hot)

Why?
• Demo requested
• WhatsApp enquiry
• Checked pricing
• Recent lead

Next Best Action:
Call immediately and schedule demo.
