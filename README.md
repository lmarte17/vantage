# Sports Betting Line Movement Tracker

A full-stack application to track and visualize sports betting line movements using The Odds API (v4).

## Features
- Track and visualize line movements across different sportsbooks
- Store historical odds data
- Real-time updates for odds changes
- Cross-sportsbook odds comparison
- Support for multiple sports and betting markets

## Project Structure
- `/backend` - FastAPI backend server
- `/frontend` - React TypeScript frontend

## Setup Instructions

### Backend
1. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Run the server:
```bash
uvicorn src.main:app --reload
```

### Frontend
1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm run dev
```

## Technologies Used
- Backend: FastAPI, PostgreSQL, Redis, SQLAlchemy
- Frontend: React, TypeScript, TailwindCSS, Recharts
