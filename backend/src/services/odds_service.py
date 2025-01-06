import os
import httpx
from typing import List, Optional
from backend.src.models.sport import Sport
from fastapi import HTTPException


def get_active_sports(all_sports: bool = False) -> List[Sport]:
    api_key = os.getenv("ODDS_API_KEY", "")
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing Odds API key")

    base_url = "https://api.the-odds-api.com/v4/sports"
    params = {
        "apiKey": api_key,
        "all": str(all_sports).lower()
    }

    try:
        response = httpx.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        sports_data = response.json()
        return [Sport(**sport) for sport in sports_data]
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=f"Error fetching sports: {exc}")