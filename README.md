# Financial Health Assessment Tool for SMEs

## Problem Statement

Small and Medium Enterprises (SMEs) often struggle to understand their financial health due to the lack of structured analytics, expert financial advice, and easy-to-use decision-support tools. Business owners who are not from a finance background need a clear, reliable, and actionable system to evaluate their financial performance, risks, and growth opportunities.

This project addresses that need by building a **Financial Health Assessment Platform** that analyzes financial data, evaluates risk and creditworthiness, performs industry benchmarking, forecasts cash flow, and generates AI-driven recommendations.

---

## Solution Overview

The **Financial Health Assessment Tool** is a full-stack web application that allows SMEs to upload financial data and receive a comprehensive analysis of their business health.

The platform:
- Processes structured financial data
- Computes key financial metrics
- Evaluates financial risk and creditworthiness
- Compares performance against industry benchmarks
- Forecasts future cash flow
- Generates AI-powered insights and recommendations
- Presents results through a clean, visual dashboard

The system is designed with **scalability, modularity, and real-world feasibility** in mind.

---

## Core Features Implemented

### 1. Financial Data Ingestion
- Upload financial data using **CSV or XLSX**
- Validates uploaded files
- Prepares data for downstream analysis using pandas

---

### 2. Financial Metrics Analysis
Automatically calculates:
- Revenue
- Expenses
- Profit
- Profit Margin
- Cash Flow Ratio

These metrics form the foundation for all further analysis.

---

### 3. Financial Health Scoring
- Generates a numerical **financial health score**
- Classifies risk level as **Low / Medium / High**
- Rule-based and explainable scoring logic

---

### 4. Creditworthiness Evaluation
- Determines loan eligibility
- Identifies potential financial risk flags
- Designed to mirror real-world bank/NBFC evaluation criteria

---

### 5. Industry Benchmarking
- Compares business performance with industry standards
- Currently supports **Retail** industry
- Evaluates:
  - Profit margin status
  - Cash flow health status

---

### 6. Cash Flow Forecasting
- Predicts expected cash flow for upcoming months
- Helps with liquidity and working capital planning
- Modular design allows future use of advanced forecasting models

---

### 7. AI-Powered Financial Insights
- Generates business-friendly insights using a Large Language Model
- Produces:
  - Executive summary
  - Key financial risks
  - Cost optimization suggestions
  - Recommended financial products
  - Actionable next steps
- Designed for **non-finance business owners**

---

### 8. Interactive Dashboard
Built using **React.js**, the dashboard includes:
- KPI cards
- Revenue vs Expense bar chart
- Profit distribution pie chart
- Cash flow forecast line chart
- Credit and benchmark indicators
- AI advisor insights panel

---

### 9. Database Integration
- Uses **PostgreSQL** for secure and persistent data storage
- Stores:
  - Financial assessments
  - Forecast results
  - AI insights
- Schema supports future expansion

---

## Technology Stack

### Backend
- FastAPI
- Python
- pandas
- SQLAlchemy
- PostgreSQL

### Frontend
- React.js
- Axios
- Chart libraries for visualization

### AI Layer
- LLM integration via **Ollama (local inference)**
- Architecture compatible with OpenAI GPT / Claude

---

## System Architecture
React Frontend
|
| REST API
v
FastAPI Backend
|
├── Data Ingestion
├── Metrics Engine
├── Financial Scoring
├── Credit Evaluation
├── Industry Benchmarking
├── Cash Flow Forecasting
└── AI Insights Generator
|
PostgreSQL Database

This layered architecture ensures clean separation of concerns and future scalability.

---

## Supported Inputs

- CSV (Implemented)
- XLSX (Implemented)
- PDF (Text-based exports – planned)

---

## Compliance with Problem Requirements

| Requirement | Status |
|------------|--------|
| Financial data analysis | Implemented |
| Risk & credit evaluation | Implemented |
| Cost optimization insights | Implemented |
| Financial forecasting | Implemented |
| Industry benchmarking | Implemented |
| AI-generated recommendations | Implemented |
| PostgreSQL database | Implemented |
| React-based visualization | Implemented |
| Banking / GST APIs | Planned |
| Multilingual output | Planned |
| Data encryption | Planned (production-ready design) |

---

## Limitations & Future Scope

The following features are intentionally planned for future phases:
- GST returns API integration
- Banking and payment gateway APIs (max 2)
- Automated bookkeeping
- Investor-ready PDF reports
- Multilingual support (Hindi & regional languages)
- Encryption at rest and enhanced compliance controls

The current system architecture fully supports these additions.

---
## How to Run the Project

### Backend
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn backend.app.main:app --reload



