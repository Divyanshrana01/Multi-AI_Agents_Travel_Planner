import streamlit as st
from datetime import date, timedelta

st.set_page_config(
    page_title="AI Travel Agent",
    page_icon="🌍",
    layout="wide",
)

# --- Sidebar: Trip Details ---
with st.sidebar:
    st.header("Trip Details")

    origin = st.text_input("From", placeholder="e.g. New York")
    destination = st.text_input("To", placeholder="e.g. Paris")

    col1, col2 = st.columns(2)
    with col1:
        departure_date = st.date_input("Departure", value=date.today() + timedelta(days=7))
    with col2:
        return_date = st.date_input("Return", value=date.today() + timedelta(days=14))

    num_travelers = st.number_input("Travelers", min_value=1, max_value=20, value=1)
    budget = st.selectbox("Budget", ["Budget", "Mid-range", "Luxury"])
    interests = st.multiselect(
        "Interests",
        ["Culture", "Adventure", "Food", "Nightlife", "Family-friendly", "Nature", "Shopping", "Relaxation"],
    )

    if st.button("Plan My Trip", use_container_width=True, type="primary"):
        if not origin or not destination:
            st.warning("Please enter both origin and destination.")
        else:
            trip_request = (
                f"Plan a trip from {origin} to {destination}, "
                f"departing {departure_date} and returning {return_date}, "
                f"for {num_travelers} traveler(s). "
                f"Budget: {budget}. "
                f"Interests: {', '.join(interests) if interests else 'general'}."
            )
            st.session_state.messages.append({"role": "user", "content": trip_request})
            # TODO: invoke the LangGraph travel agent here
            # response = graph.invoke({"messages": [("user", trip_request)], ...})
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Got it! I'll plan your **{budget.lower()}** trip from **{origin}** to **{destination}** "
                           f"({departure_date} - {return_date}) for {num_travelers} traveler(s).\n\n"
                           f"Interests: {', '.join(interests) if interests else 'general'}.\n\n"
                           f"*Agent integration coming soon — connect the LangGraph supervisor to get live results.*",
            })
            st.rerun()

# --- Main area: Chat ---
st.title("AI Travel Agent")
st.caption("Plan your perfect trip with AI-powered flight, hotel, and activity recommendations.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI travel agent. Fill in your trip details in the sidebar and click **Plan My Trip**, or just chat with me below."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask me anything about your trip..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # TODO: route through LangGraph supervisor
    # response = graph.invoke({"messages": st.session_state.messages, ...})
    reply = "Thanks for your message! Once the LangGraph agents are wired up, I'll be able to search flights, hotels, activities, and build your full itinerary."
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
