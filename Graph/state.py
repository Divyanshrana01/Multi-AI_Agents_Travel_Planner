from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import MessagesState


class TravelState(MessagesState):
    """Shared state for the travel agent graph.

    Inherits `messages` from MessagesState (with add-message reducer).
    """

    origin: str
    destination: str
    departure_date: str
    return_date: str
    num_travelers: int
    budget: str
    interests: list[str]

    flight_options: list[dict]
    selected_flight: dict
    hotel_options: list[dict]
    selected_hotel: dict
    activities: list[dict]
    weather_info: dict
    itinerary: str

    next_agent: Literal[
        "flight_agent",
        "hotel_agent",
        "activities_agent",
        "itinerary_agent",
        "FINISH",
    ]
