import streamlit as st
from agent import narrator_agent, monster_agent, item_agent

st.set_page_config(page_title="🎮 Game Master Agent")
st.title("🧙 Fantasy Adventure Game")

player_choice = st.text_input("What would you like to do?", placeholder="e.g., explore, fight, rest")

if st.button("Continue") and player_choice:
    with st.spinner("Your story unfolds..."):
        story = narrator_agent(player_choice)
        st.subheader("📜 Story:")
        st.write(story)

        if "monster" in story.lower():
            battle = monster_agent()
            st.subheader("⚔ Battle:")
            st.write(battle)

        reward = item_agent()
        st.subheader("🎁 Reward:")
        st.write(reward)