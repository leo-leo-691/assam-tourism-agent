# 🍵 Assam Tourism Guide Agent

An AI-powered tourism assistant for Assam, India — built with **Google ADK** and connected to **Google Maps via MCP (Model Context Protocol)**. Deployed on **Google Cloud Run**.

## 🗺️ What It Does

Users can ask questions like:
- *"What are the top places to visit in Assam?"*
- *"Tell me about Kaziranga National Park"*
- *"Plan a trip from Guwahati to Majuli"*
- *"Best tea gardens to visit near Jorhat?"*

The agent fetches **live data from Google Maps** via an MCP server and generates a rich, grounded travel guide response.

## 🏗️ Architecture

```
User → ADK Agent (Cloud Run)
           ↓  MCP (SSE)
     Google Maps MCP Server (Cloud Run)
           ↓
     Google Maps Places API
```

## 📁 Project Structure

```
assam-tourism-agent/
├── agent.py          # ADK agent definition
├── main.py           # FastAPI entrypoint
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container config
├── .env.example      # Environment variable template
└── README.md
```

## 🚀 Setup & Deployment

### Prerequisites
- Google Cloud project with billing enabled
- Google Maps API key
- Maps MCP server deployed (from Codelab 1)
- `gcloud` CLI installed and authenticated

### Step 1: Clone & Configure

```bash
git clone <your-repo-url>
cd assam-tourism-agent
cp .env.example .env
# Fill in your values in .env
```

### Step 2: Run Locally

```bash
pip install -r requirements.txt
source .env  # or set env vars manually
adk web      # starts local dev server
```

Visit `http://localhost:8000` and start chatting!

### Step 3: Deploy to Cloud Run

```bash
# Set your project
export PROJECT_ID=your_gcp_project_id
export REGION=us-central1

# Build and push container
gcloud builds submit --tag gcr.io/$PROJECT_ID/assam-tourism-agent

# Deploy to Cloud Run
gcloud run deploy assam-tourism-agent \
  --image gcr.io/$PROJECT_ID/assam-tourism-agent \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_key,MAPS_MCP_URL=your_mcp_url \
  --port 8080
```

### Step 4: Get Your Cloud Run URL

After deployment, you'll get a URL like:
```
https://assam-tourism-agent-xxxxxxxx-uc.a.run.app
```

Use this as your **submission link**.

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Gemini API key for ADK |
| `MAPS_MCP_URL` | URL of your deployed Maps MCP server (SSE endpoint) |
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID |

## 🧪 Example Queries

- "What are the best wildlife sanctuaries in Assam?"
- "Top tourist spots in Guwahati"
- "Tell me about Majuli island"
- "Tea garden experiences near Dibrugarh"
- "How to get to Kaziranga from Jorhat?"

## 📌 Tech Stack

- **Google ADK** — Agent framework
- **MCP (Model Context Protocol)** — Tool integration standard
- **Google Maps Places API** — Live location data
- **Gemini 2.0 Flash** — LLM
- **FastAPI + Uvicorn** — Web server
- **Google Cloud Run** — Serverless deployment

## 🙏 Credits

Built as part of the Google ADK + MCP hackathon/workshop track.
