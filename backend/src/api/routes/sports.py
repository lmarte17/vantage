from fastapi import APIRouter, Query
from typing import List
from backend.src.services.odds_service import get_active_sports
from backend.src.models.sport import Sport

router = APIRouter()

@router.get("/sports", response_model=List[Sport])
def read_sports(all_sports: bool = Query(False, description="Set to true to retrieve all sports")):
    """
    Return a list of sports data retrieved from The Odds API.
    If 'all_sports' is set to true, it retrieves both in-season and out-of-season.
    Otherwise, only in-season sports are returned.
    """
    return get_active_sports(all_sports=all_sports)