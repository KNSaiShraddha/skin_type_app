import streamlit as st

st.set_page_config(page_title="Skincare Routine", page_icon="🧼")

st.title("🧼 Skincare Routine")
st.markdown("#### 🌞 Day & 🌙 Night Routine Based on Your Skin Type")

if "skin_type" not in st.session_state or not st.session_state["skin_type"]:
    st.warning("⚠️ Skin type not detected. Please analyze your skin on the Home page first.")
    st.stop()

skin_type = st.session_state["skin_type"]
st.markdown(f"### 🧬 Routine for **{skin_type}** Skin")
st.markdown("---")

# Routines...
if skin_type == "normal":
    st.subheader("🌞 Day Routine")
    st.markdown("- **Cleanser**: Gentle foaming cleanser")
    st.markdown("- **Toner**: Rose water or hydrating toner")
    st.markdown("- **Serum**: Vitamin C (brightening & antioxidant)")
    st.markdown("- **Moisturizer**: Lightweight cream with **Hyaluronic Acid**")
    st.markdown("- **Sunscreen**: SPF 30+ broad spectrum")

    st.subheader("🌙 Night Routine")
    st.markdown("- **Cleanser**: Same as day")
    st.markdown("- **Toner**: Hydrating toner")
    st.markdown("- **Serum**: Niacinamide or Peptides")
    st.markdown("- **Moisturizer**: Ceramide-rich cream")

elif skin_type == "oily":
    st.subheader("🌞 Day Routine")
    st.markdown("- **Cleanser**: Salicylic Acid-based gel cleanser")
    st.markdown("- **Toner**: Witch hazel (alcohol-free)")
    st.markdown("- **Serum**: Niacinamide (oil control & calming)")
    st.markdown("- **Moisturizer**: Gel-based with **Zinc PCA**")
    st.markdown("- **Sunscreen**: Mattifying SPF 50")

    st.subheader("🌙 Night Routine")
    st.markdown("- **Cleanser**: Same as day")
    st.markdown("- **Toner**: BHA-based toner")
    st.markdown("- **Treatment**: Retinol (use 2–3x/week if beginner)")
    st.markdown("- **Moisturizer**: Oil-free night gel")

elif skin_type == "dry":
    st.subheader("🌞 Day Routine")
    st.markdown("- **Cleanser**: Cream-based cleanser with Glycerin")
    st.markdown("- **Toner**: Alcohol-free hydrating toner")
    st.markdown("- **Serum**: Hyaluronic Acid + Vitamin E")
    st.markdown("- **Moisturizer**: Rich cream with **Ceramides or Squalane**")
    st.markdown("- **Sunscreen**: Hydrating SPF 30+")

    st.subheader("🌙 Night Routine")
    st.markdown("- **Cleanser**: Same as day")
    st.markdown("- **Toner**: Hydrating toner")
    st.markdown("- **Serum**: Peptides or Panthenol")
    st.markdown("- **Moisturizer**: Thick cream or sleeping mask")

elif skin_type == "Combination":
    st.subheader("🌞 Day Routine")
    st.markdown("- **Cleanser**: Gel cleanser (gentle) for all zones")
    st.markdown("- **Toner**: Balancing toner with Green Tea Extract")
    st.markdown("- **Serum**: Niacinamide (balances T-zone + soothes)")
    st.markdown("- **Moisturizer**: Light lotion for oily areas, cream for dry areas")
    st.markdown("- **Sunscreen**: Broad spectrum, non-comedogenic SPF")

    st.subheader("🌙 Night Routine")
    st.markdown("- **Cleanser**: Same as day")
    st.markdown("- **Toner**: Calming or balancing toner")
    st.markdown("- **Serum**: Alpha Arbutin or mild exfoliants")
    st.markdown("- **Moisturizer**: Mix light and rich creams as needed")

st.markdown("---")
st.info("⚠️ Always perform a **patch test** before using any new product.")
st.markdown("🩺 This is a **general recommendation**. If you have persistent or serious skin issues, **consult a certified dermatologist**.")

st.page_link("pages/skincare_tips.py", label="💡 View Skincare Tips", icon="💡")
st.page_link("pages/skincare_actives.py", label="🧴 View Skincare Actives", icon="🧴")
if "skin_type" in st.session_state:
    st.page_link("main.py", label="⬅️ Back to Skin Analysis", icon="🔍")


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



