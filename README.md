# Conversational Learning Assessment

A web-based adaptive assessment system for evaluating student understanding in statistics using Claude AI.

## Architecture

### Backend (`backend/app.py`)
- **Framework**: Flask
- **Port**: 3001 (localhost only)
- **Features**:
  - Claude AI integration for adaptive questioning
  - Conversation history management
  - Data collection to `backend/data/conversation.json`
  - PDF support via Anthropic Files API
  
### Frontend (`frontend/public/index.html`)
- **Type**: Static HTML/CSS/JavaScript
- **Port**: 3000 (served via Python HTTP server)
- **Features**:
  - Real-time chat interface
  - Conversation persistence
  - Responsive design

### Data Storage
All conversation data is automatically saved to:
- `backend/data/history.json` - Current session history
- `backend/data/conversation.json` - Master log of all conversations (for analytics)

## Setup

### 1. Install Dependencies

```bash
cd ~/Desktop/conversational-assessment
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 2. Configure Environment

Create `backend/.env` with your Anthropic API key:

```bash
cp backend/.env.example backend/.env
```

Then edit `backend/.env` and add:
```
ANTHROPIC_API_KEY=your_api_key_here
```

Get your API key from: https://console.anthropic.com/

### 3. Update PDF Path (Optional)

In `backend/app.py`, update the `PDF_PATH` variable to point to your course material PDF.

## Running Locally

### Start Backend
```bash
cd ~/Desktop/conversational-assessment
source .venv/bin/activate
python backend/app.py
```

### Start Frontend (in a new terminal)
```bash
cd ~/Desktop/conversational-assessment/frontend/public
python3 -m http.server 3000
```

### Access the App
Open your browser and go to: **http://localhost:3000/index.html**

## API Endpoints

### POST `/api/start`
- Initializes assessment conversation
- Returns: `{"reply": "Opening question from Claude"}`

### POST `/api/chat`
- Continues conversation with student answer
- Body: `{"answer": "student response"}`
- Returns: `{"reply": "Claude's response"}`

### POST `/api/history`
- Retrieves current session chat history
- Returns: `{"history": [...]}`

### POST `/api/clear`
- Clears current session and starts fresh
- Returns: `{"status": "cleared"}`

### GET `/api/conversation-log`
- Gets master log of all conversations (admin use)
- Returns: `{"logs": [{"timestamp": "...", "role": "...", "text": "..."}]}`

## Data Collection

All conversations are automatically logged to `backend/data/conversation.json`:

```json
[
  {
    "timestamp": "2026-06-11T14:30:00.123456",
    "role": "user",
    "text": "Student's answer"
  },
  {
    "timestamp": "2026-06-11T14:30:05.654321",
    "role": "assistant",
    "text": "Claude's response"
  }
]
```

## Development Notes

- Frontend automatically detects localhost environment and connects to `http://localhost:3001`
- In production, the frontend serves from `/convo/` and the backend is at `/convo/api/`
- CORS is enabled for local development
- Flask debug mode is enabled for development convenience

## Stop Services

```bash
pkill -f "python.*app.py"
pkill -f "http.server"
```

## Next Steps

- Customize the system prompt in `backend/app.py` for your course
- Add more validation and error handling
- Implement authentication if needed
- Set up database for persistent storage of conversation logs
