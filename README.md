# 🍵 Assam Tourism Guide Agent

An AI-powered tourism assistant for Assam, India — built with **Google ADK** and connected to **Google Search via MCP (Model Context Protocol)**. Deployed on **Google Cloud Run**.

## 🗺️ What It Does

Users can ask questions like:
- *"What are the top places to visit in Assam?"*
- *"Tell me about Kaziranga National Park"*
- *"Plan a trip from Guwahati to Majuli"*
- *"Best tea gardens to visit near Jorhat?"*

The agent fetches **live data from Google Search** via MCP and generates a rich, grounded travel guide response.

## 🏗️ Architecture

```
User → ADK Agent (Cloud Run)
           ↓  MCP
     Google Search Tool
           ↓
     Real-time Web Data (via Vertex AI)
```

## 📁 Project Structure

```
assam-tourism-agent/
├── assam_tourism_agent/
│   ├── agent.py          # ADK agent definition
│   └── __init__.py       # Module init
├── main.py               # FastAPI entrypoint
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container config
├── .env.example          # Environment variable template
└── README.md
```

## 🚀 Setup & Deployment

### Prerequisites
- Google Cloud project with billing enabled
- Vertex AI API enabled
- `gcloud` CLI installed and authenticated

### Step 1: Clone & Configure

```bash
git clone https://github.com/leo-leo-691/assam-tourism-agent.git
cd assam-tourism-agent
cp .env.example .env
# Fill in your values in .env
```

### Step 2: Enable Vertex AI API

```bash
gcloud services enable aiplatform.googleapis.com --project YOUR_PROJECT_ID
```

### Step 3: Deploy to Cloud Run

```bash
export PROJECT_ID=your_gcp_project_id
export REGION=us-central1

gcloud run deploy assam-tourism-agent \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_CLOUD_PROJECT=$PROJECT_ID,GOOGLE_CLOUD_LOCATION=us-central1,GOOGLE_GENAI_USE_VERTEXAI=TRUE \
  --project $PROJECT_ID
```

### Step 4: Get Your Cloud Run URL

After deployment, you'll get a URL like:
```
https://assam-tourism-agent-xxxxxxxx-uc.a.run.app
```

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID |
| `GOOGLE_CLOUD_LOCATION` | GCP region (e.g. us-central1) |
| `GOOGLE_GENAI_USE_VERTEXAI` | Set to TRUE to use Vertex AI |

## 🧪 Example Queries

- "What are the best wildlife sanctuaries in Assam?"
- "Top tourist spots in Guwahati"
- "Tell me about Majuli island"
- "Tea garden experiences near Dibrugarh"
- "How to get to Kaziranga from Jorhat?"

## 🌐 Live Demo

```
https://assam-tourism-agent-882158419848.us-central1.run.app
```

## 📌 Tech Stack

- **Google ADK** — Agent framework
- **MCP (Model Context Protocol)** — Tool integration standard
- **Google Search Tool** — Real-time web data retrieval
- **Gemini 2.5 Flash (Vertex AI)** — LLM
- **FastAPI + Uvicorn** — Web server
- **Google Cloud Run** — Serverless deployment

## 🙏 Credits

Built as part of the Google Gen AI Academy APAC Edition 2026
