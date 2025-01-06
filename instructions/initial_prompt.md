# Sports Betting Line Movement Tracker

## Overview
A full-stack application to track and visualize sports betting line movements using The Odds API (v4). The application consists of a Python backend and React frontend.

## Project Goals
- Track and visualize line movements across different sportsbooks
- Store historical odds data efficiently
- Provide real-time updates when odds change
- Allow users to compare odds across different sportsbooks
- Support multiple sports and betting markets

## Backend Architecture

### Directory Structure
```
backend/
├── src/
│   ├── api/
│   │   ├── odds_api/      # The Odds API integration
│   │   └── routes/        # FastAPI endpoints
│   ├── models/            # Pydantic models and database models
│   ├── services/          # Business logic
│   └── utils/             # Helper functions
├── tests/
└── config/               # Configuration management
```

### Technical Requirements
- **Framework**: FastAPI for REST API
- **Caching**: Redis for efficient data caching
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Real-time**: WebSocket support for live updates
- **API Management**: Rate limiting for The Odds API
- **Data Validation**: Pydantic models
- **Code Quality**: Python best practices and type hints

## Frontend Architecture

### Directory Structure
```
frontend/
├── src/
│   ├── components/        # Reusable UI components
│   ├── pages/            # Page components
│   ├── services/         # API service layer
│   ├── hooks/            # Custom React hooks
│   └── utils/            # Helper functions
└── tests/
```

### Technical Requirements
- **Language**: TypeScript for type safety
- **Styling**: TailwindCSS for responsive design
- **Visualization**: Recharts for line movement graphs
- **Real-time**: WebSocket client integration
- **State Management**: React Query for data fetching/caching
- **Error Handling**: Comprehensive error and loading states

## Implementation Strategy
1. Set up backend structure and core functionality
2. Abstract The Odds API complexity
3. Create clean, documented endpoints
4. Implement frontend components
5. Integrate real-time updates
6. Add visualization features