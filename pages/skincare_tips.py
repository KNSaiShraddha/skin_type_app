import streamlit as st

st.set_page_config(page_title="Skincare Tips", page_icon="💡")

st.title("💡 Skincare Tips")
st.markdown("#### 🧘‍♀️ Healthy skin starts from within 🌟")

if "skin_type" not in st.session_state or not st.session_state["skin_type"]:
    st.warning("⚠️ Skin type not detected. Please analyze your skin on the Home page first.")
    st.stop()

skin_type = st.session_state["skin_type"]

st.markdown(f"### ✨ Personalized Tips for **{skin_type}** Skin")
st.markdown("---")

# Tips based on skin type
if skin_type == "normal":
    st.subheader("🧴 DIY Remedies")
    st.markdown("- Use raw honey as a mild face mask once a week.")
    st.markdown("- Aloe vera gel can maintain hydration and soothe skin.")
    st.subheader("🥗 Diet Tips")
    st.markdown("- Eat a balanced diet with fresh fruits and vegetables.")
    st.markdown("- Stay hydrated and avoid excessive sugar.")

elif skin_type == "oily":
    st.subheader("🧴 DIY Remedies")
    st.markdown("- Apply diluted tea tree oil on acne-prone areas.")
    st.markdown("- Use multani mitti (Fuller's Earth) face mask 1–2 times a week.")
    st.subheader("🥗 Diet Tips")
    st.markdown("- Avoid deep-fried and oily foods.")
    st.markdown("- Include zinc-rich foods like pumpkin seeds and lentils.")
    st.markdown("- Limit dairy and high-glycemic foods.")

elif skin_type == "dry":
    st.subheader("🧴 DIY Remedies")
    st.markdown("- Use mashed banana or avocado with honey as a face mask.")
    st.markdown("- Apply coconut oil or almond oil before bed.")
    st.subheader("🥗 Diet Tips")
    st.markdown("- Include healthy fats like nuts, seeds, and olive oil.")
    st.markdown("- Drink at least 8 glasses of water daily.")

elif skin_type == "Combination":
    st.subheader("🧴 DIY Remedies")
    st.markdown("- Use rose water to balance oily and dry areas.")
    st.markdown("- Apply a yogurt + honey face mask once a week.")
    st.subheader("🥗 Diet Tips")
    st.markdown("- Focus on a variety of fruits and vegetables.")
    st.markdown("- Stay consistent with hydration and avoid extreme diets.")

st.markdown("---")
st.markdown("### 💡 _Healthy skin starts from within!_ 🧡")

st.page_link("pages/skincare_routine.py", label="🧼 View Day & Night Routine", icon="🧼")
st.page_link("pages/skincare_actives.py", label="🧴 View Skincare Actives", icon="🧴")

# ---------------------------- Custom Background Color ---------------------------- #
st.markdown("""
    <style>
        body {
            background-color: #fce4ec;
        }
        .stApp {
            background-color: #fce4ec;
        }
    </style>
""", unsafe_allow_html=True)
