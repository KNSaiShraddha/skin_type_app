import streamlit as st

st.set_page_config(page_title="Skincare Actives", layout="wide", page_icon="🧴")

st.markdown("<h1 style='color:#ff6f61;'>🧴 Personalized Skincare Actives</h1>", unsafe_allow_html=True)

if "skin_type" not in st.session_state or not st.session_state["skin_type"]:
    st.warning("⚠️ Skin type not detected. Please analyze your skin on the Home page first.")
    st.stop()

skin_type = st.session_state["skin_type"]

actives_with_descriptions = {
    "normal": [
        ("Niacinamide", "Balances oil and improves skin texture."),
        ("Hyaluronic Acid", "Hydrates and plumps the skin."),
        ("Vitamin C", "Brightens and protects from free radicals."),
        ("Ceramides", "Strengthens the skin barrier."),
        ("Peptides", "Boosts collagen and firms skin.")
    ],
    "oily": [
        ("Salicylic Acid", "Exfoliates pores and treats acne."),
        ("Niacinamide", "Controls oil and reduces redness."),
        ("Zinc PCA", "Regulates sebum and calms inflammation."),
        ("Retinol", "Unclogs pores and reduces breakouts."),
        ("Tea Tree Oil", "Antibacterial and helps with acne.")
    ],
    "Combination": [
        ("Niacinamide", "Balances oil and soothes the skin."),
        ("Hyaluronic Acid", "Provides hydration without heaviness."),
        ("Lactic Acid", "Gently exfoliates dry areas."),
        ("Green Tea Extract", "Soothes irritation and controls oil."),
        ("Alpha Arbutin", "Fades dark spots and evens skin tone.")
    ],
    "dry": [
        ("Hyaluronic Acid", "Deeply hydrates and plumps."),
        ("Ceramides", "Rebuilds and protects skin barrier."),
        ("Squalane", "Nourishes and locks in moisture."),
        ("Panthenol", "Soothes and moisturizes dry skin."),
        ("Shea Butter", "Provides intense moisture and softness.")
    ]
}

st.subheader(f"✨ Recommended Actives for **{skin_type}** Skin")
st.markdown("---")

for i, (active, desc) in enumerate(actives_with_descriptions[skin_type], 1):
    st.markdown(f"**{i}. {active}** – {desc}")

st.markdown("---")
st.page_link("pages/skincare_tips.py", label="💡 View Skincare Tips")
st.page_link("pages/skincare_routine.py", label="🧼 View Routine")

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

