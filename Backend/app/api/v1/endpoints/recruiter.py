# app/api/v1/endpoints/recruiter.py

from fastapi import APIRouter, Depends, HTTPException
from app.db.session import bots_collection
from app.schemas.bot import Bot
from app.api.v1.deps import get_current_user
from app.schemas.user import User
from typing import List
from bson import ObjectId
from pydantic import BaseModel

# Import the Global Index for Semantic Search
from app.core.rag_pipeline import GlobalRecruiterIndex

router = APIRouter()

class SearchRequest(BaseModel):
    query: str

@router.post("/search")
async def search_candidates(
    search_request: SearchRequest,  # Fixed: Match the class name defined above
    current_user: User = Depends(get_current_user) # Fixed: Type as User model
):
    if current_user.role != "recruiter":
        raise HTTPException(status_code=403, detail="Only recruiters can search candidates")

    if not search_request.query.strip():
        return []

    try:
        # 1. Initialize Index and Run Vector Search
        # Note: This returns a list of ID strings (e.g. ['60d5...', '60d6...'])
        global_index = GlobalRecruiterIndex()
        matching_bot_ids = global_index.semantic_search(search_request.query, k=10)

        if not matching_bot_ids:
            return []

        # 2. Fetch Full Documents from MongoDB
        # We need to convert string IDs to ObjectIds for the DB query
        bot_object_ids = [ObjectId(bid) for bid in matching_bot_ids]
        
        candidates_cursor = bots_collection.find({"_id": {"$in": bot_object_ids}})
        candidates = await candidates_cursor.to_list(100)

        # 3. Format the results safely
        formatted_results = []
        
        # Helper map to preserve search order (relevance)
        candidates_map = {str(c["_id"]): c for c in candidates}

        for bid in matching_bot_ids:
            res = candidates_map.get(bid)
            if not res:
                continue

            # --- FIX: Use .get() to avoid 'skills' KeyError ---
            skills_list = res.get("skills", [])
            
            # Ensure skills is actually a list (handle None or strings)
            if not isinstance(skills_list, list):
                skills_list = [] 

            formatted_results.append({
                "id": str(res["_id"]),
                "name": res.get("name", "Unknown Candidate"),
                # 'score' might not be available from Mongo, 
                # usually vector engines return it separately. 
                # For now we can omit it or set a default.
                "match_score": 0, 
                "skills": skills_list,  # Safe access
                "summary": res.get("summary", "No summary available."),
                "experience_years": res.get("experience_years", 0)
            })
            
        return formatted_results

    except Exception as e:
        print(f"Search Error: {str(e)}") # Print to console for debugging
        raise HTTPException(status_code=500, detail=f"Error performing semantic search: {str(e)}")