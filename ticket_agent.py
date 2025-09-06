# app.py
from typing import Dict, List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel

# ----- Data models -----

class Customer(BaseModel):
    name: str
    vip_status: bool
    location: Tuple[int, int]  # (x, y)
    credit_card: str

class Concert(BaseModel):
    name: str
    booking_center_location: Tuple[int, int]  # (x, y)

class TicketingRequest(BaseModel):
    customers: List[Customer]
    concerts: List[Concert]
    priority: Dict[str, str] = {}  # credit_card -> concert_name

# ----- App -----

app = FastAPI(
    title="Ticketing Agent 2025",
    version="1.0.0",
    description="Scores concerts per customer and returns the best pick."
)

def latency_points_from_squared_distance(d2: int) -> int:
    # Inferred from the example in the brief:
    # (1,1)->(0,0): d2=2 -> 30
    # (1,1)->(3,3): d2=8 -> 20
    # (1,1)->(5,5): d2=32 -> 0
    if d2 <= 4:        # distance <= 2
        return 30
    elif d2 <= 16:     # 2 < distance <= 4
        return 20
    else:
        return 0

@app.post("/ticketing-agent", tags=["ticketing"])
def ticketing_agent(payload: TicketingRequest) -> Dict[str, str]:
    result: Dict[str, str] = {}

    # O(#customers × #concerts) ~ 1000 × 100 = 100k checks (well within 10s limit and constraints). :contentReference[oaicite:2]{index=2}
    for cust in payload.customers:
        best_concert_name = None
        best_score = None
        best_d2 = None

        for con in payload.concerts:
            dx = cust.location[0] - con.booking_center_location[0]
            dy = cust.location[1] - con.booking_center_location[1]
            d2 = dx*dx + dy*dy

            score = 0

            # Factor 1: VIP (+100 to all concerts if true). :contentReference[oaicite:3]{index=3}
            if cust.vip_status:
                score += 100

            # Factor 2: Credit card priority (+50 if this card maps to this concert). :contentReference[oaicite:4]{index=4}
            if payload.priority.get(cust.credit_card) == con.name:
                score += 50

            # Factor 3: Latency (up to +30, tiered by distance). :contentReference[oaicite:5]{index=5}
            score += latency_points_from_squared_distance(d2)

            # Deterministic tie-breakers: higher score, then smaller distance, then name
            if (best_score is None
                or score > best_score
                or (score == best_score and (best_d2 is None or d2 < best_d2))
                or (score == best_score and d2 == best_d2 and (best_concert_name is None or con.name < best_concert_name))):
                best_score = score
                best_d2 = d2
                best_concert_name = con.name

        result[cust.name] = best_concert_name

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:ticketing_agent", host="0.0.0.0", port=8000, reload=True)
