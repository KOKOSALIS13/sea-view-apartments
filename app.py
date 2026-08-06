import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# =========================================================
# CONFIG & STATE
# =========================================================

st.set_page_config(
    page_title="Sea View Hotel & Apartments | Ammoudara, Crete",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "apartment_slide" not in st.session_state:
    st.session_state.apartment_slide = 0

if "sea_slide" not in st.session_state:
    st.session_state.sea_slide = 0

AIRBNB_URL_1 = "https://www.airbnb.gr/rooms/559151340688341474"
MAPS_URL = "https://www.google.com/maps/search/Ammoudara+Heraklion+Crete"

# =========================================================
# PATHS & CACHED IMAGE LOADER
# =========================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


@st.cache_data(show_spinner=False)
def load_image_cached(path_str):
    path = Path(path_str)
    if path.exists():
        try:
            return Image.open(path)
        except Exception:
            return None
    return None


def get_image(filename):
    return load_image_cached(str(IMAGE_DIR / filename))


# Load Images
hotel = get_image("hotel.jpg")

sea = get_image("sea.jpg")
sea1 = get_image("sea1.jpg")
seaview = get_image("seaview.jpg")
seabynight = get_image("seabynight.jpg")

balcony = get_image("balcony.jpg")
livingroom = get_image("livingroom.jpg")
livingroom1 = get_image("livingroom1.jpg")
livingroom2 = get_image("livingroom2.jpg")

bedroom = get_image("bedroom.jpg")
bedroom1 = get_image("bedroom1.jpg")
bedroom2 = get_image("bedroom2.jpg")

kitchen = get_image("kitchen.jpg")
bathroom = get_image("bathroom.jpg")
bathroom1 = get_image("bathroom1.jpg")

# =========================================================
# LUXURY CORPORATE CSS DESIGN
# =========================================================

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>
    /* 1. Global Luxury Dark Slate Background */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b1c1e !important;
        background-image: 
            radial-gradient(at 50% 0%, rgba(26, 54, 58, 0.5) 0px, transparent 75%),
            radial-gradient(at 100% 100%, rgba(15, 33, 36, 0.8) 0px, transparent 50%) !important;
        background-attachment: fixed !important;
        color: #e2e8e8 !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    .block-container {
        max-width: 1320px;
        padding-top: 20px;
        padding-bottom: 80px;
        padding-left: 5%;
        padding-right: 5%;
    }

    #MainMenu, footer { visibility: hidden; }

    /* 2. Corporate Luxury Typography */
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        color: #f4e8c1 !important;
        font-weight: 500 !important;
        letter-spacing: 0.04em !important;
    }

    h1 { font-size: 3.4rem !important; line-height: 1.15 !important; }
    h2 { font-size: 2.2rem !important; margin-bottom: 20px !important; border-bottom: 1px solid rgba(212, 175, 55, 0.2); padding-bottom: 10px; }
    h3 { font-size: 1.4rem !important; }

    p, label, span { color: #b8c5c5; line-height: 1.8; font-size: 14px; font-weight: 300; }

    hr {
        border: none;
        border-top: 1px solid rgba(212, 175, 55, 0.15);
        margin-top: 45px;
        margin-bottom: 45px;
    }

    /* 3. Luxury Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: rgba(18, 38, 41, 0.8);
        padding: 8px 12px;
        border-radius: 40px;
        border: 1px solid rgba(212, 175, 55, 0.2);
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 30px;
        color: #b8c5c5 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
        padding: 0 24px !important;
        background-color: transparent !important;
        border: none !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #d4af37 !important;
        color: #0b1c1e !important;
        font-weight: 600 !important;
    }

    /* 4. Luxury Cards & Components */
    .corporate-card {
        background: rgba(18, 38, 41, 0.75) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        border-radius: 12px;
        padding: 30px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .corporate-card:hover {
        border-color: #d4af37 !important;
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(212, 175, 55, 0.08);
    }

    .card-title {
        font-family: 'Cinzel', serif;
        color: #f4e8c1;
        font-size: 20px;
        margin-bottom: 12px;
    }

    /* 5. Metrics */
    [data-testid="stMetric"] {
        background: rgba(18, 38, 41, 0.75) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        border-radius: 10px;
        padding: 18px;
        text-align: center;
    }

    [data-testid="stMetricLabel"] { color: #d4af37 !important; font-size: 11px !important; letter-spacing: 0.12em; text-transform: uppercase; }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-family: 'Cinzel', serif;
        font-size: 2.1rem !important;
    }

    /* 6. Premium Buttons */
    .stLinkButton > a, .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%) !important;
        color: #0b1c1e !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.7rem 1.6rem !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
    }

    .stLinkButton > a:hover, .stButton > button:hover {
        background: linear-gradient(135deg, #f4e8c1 0%, #d4af37 100%) !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4) !important;
        transform: translateY(-2px);
    }

    /* 7. Forms */
    [data-testid="stForm"] {
        background: rgba(15, 33, 36, 0.85) !important;
        border: 1px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 12px;
        padding: 30px;
    }

    .section-label {
        color: #d4af37;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# BRAND HEADER & NAVBAR
# =========================================================

head_col1, head_col2 = st.columns([3, 1])

with head_col1:
    st.markdown('<div class="section-label">LUXURY HOSPITALITY GROUP</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:0; border:none;'>SEA VIEW HOTEL & RESIDENCES</h2>", unsafe_allow_html=True)
    st.caption("AMMOUDARA, HERAKLION, CRETE · 23 BOUTIQUE UNITS")

with head_col2:
    st.write("")
    st.link_button("VERIFY ON AIRBNB", AIRBNB_URL_1, use_container_width=True)

st.divider()

# =========================================================
# MAIN TABBED INTERFACE
# =========================================================

tab_overview, tab_rooms, tab_experience, tab_reviews, tab_booking = st.tabs([
    "OVERVIEW",
    "SUITES & ROOMS",
    "EXPERIENCE & LOCATION",
    "GUEST REVIEWS",
    "DIRECT RESERVATIONS"
])

# ---------------------------------------------------------
# TAB 1: OVERVIEW
# ---------------------------------------------------------
with tab_overview:
    hero_l, hero_r = st.columns([1.1, 0.9], gap="large")

    with hero_l:
        st.markdown('<div class="section-label">WELCOME TO SEA VIEW</div>', unsafe_allow_html=True)
        st.title("Refined Seaside Living in Crete.")
        st.write(
            """
            Situated 50 meters from the coastline of Ammoudara, Sea View Hotel & Residences 
            offers an exclusive collection of 23 fully serviced apartments. Combining high-end 
            architectural comfort with authentic Cretan hospitality.
            """
        )

        st.markdown(
            """
            • **23 Premium Units** with private balconies & panoramic views  
            • **Prime Location** 50m from beach & 10 mins from Heraklion city center  
            • **Tailored Hospitality** managed directly by Kostas & Maria  
            • **Best Rate Guarantee** for direct reservations
            """
        )

    with hero_r:
        if hotel:
            st.image(hotel, use_container_width=True)

    st.write("")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("ACCOMMODATION", "23 Suites")
    with m2: st.metric("BEACH DISTANCE", "50 Metres")
    with m3: st.metric("GUEST RATING", "4.68 / 5.0")
    with m4: st.metric("LOCATION", "Ammoudara")

# ---------------------------------------------------------
# TAB 2: SUITES & ROOMS
# ---------------------------------------------------------
with tab_rooms:
    st.markdown('<div class="section-label">ACCOMMODATION PORTFOLIO</div>', unsafe_allow_html=True)
    st.header("Designed for Ultimate Comfort")

    apartment_images = [
        (name, img) for name, img in [
            ("Master Living Space", livingroom),
            ("Executive Suite Area", livingroom1),
            ("Lounge Area", livingroom2),
            ("Primary Bedroom", bedroom),
            ("Guest Bedroom", bedroom1),
            ("Suite Bedroom", bedroom2),
            ("Kitchenette", kitchen),
            ("En-Suite Bathroom", bathroom),
            ("Bathroom Suite", bathroom1),
            ("Private Sea View Balcony", balcony),
        ] if img is not None
    ]

    if apartment_images:
        current_apartment = st.session_state.apartment_slide
        apt_name, apt_img = apartment_images[current_apartment]

        r_col1, r_col2 = st.columns([1.4, 0.86], gap="large")

        with r_col1:
            st.image(apt_img, use_container_width=True)
            st.caption(f"{apt_name} — Image {current_apartment + 1} of {len(apartment_images)}")

            p_btn, _, n_btn = st.columns([1, 4, 1])
            with p_btn:
                if st.button("← PREV", key="apt_p"):
                    st.session_state.apartment_slide = (current_apartment - 1) % len(apartment_images)
                    st.rerun()
            with n_btn:
                if st.button("NEXT →", key="apt_n"):
                    st.session_state.apartment_slide = (current_apartment + 1) % len(apartment_images)
                    st.rerun()

        with r_col2:
            st.markdown(
                """
                <div class="corporate-card">
                    <div class="card-title">Suite Specifications</div>
                    <p style="color:#b8c5c5;">Each of our 23 residences is engineered to meet corporate and vacation standards alike.</p>
                    <hr style="margin:15px 0;">
                    <p><b>Executive Amenities:</b></p>
                    <p>✔ High-Speed Wi-Fi (Dedicated Access)</p>
                    <p>✔ Independent Climate Control</p>
                    <p>✔ Fully Equipped Kitchenette</p>
                    <p>✔ Private Balcony with Sea/Mountain View</p>
                    <p>✔ Soundproof Windows & Secure Access</p>
                    <p>✔ On-Site Complimentary Parking</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------------------------------------
# TAB 3: EXPERIENCE & LOCATION
# ---------------------------------------------------------
with tab_experience:
    st.markdown('<div class="section-label">LOCATION & CRETE</div>', unsafe_allow_html=True)
    st.header("The Ideal Gateway to Heraklion")

    loc_left, loc_right = st.columns([1, 1], gap="large")

    with loc_left:
        st.write(
            """
            Ammoudara offers a unique blend of serene coastal atmosphere while maintaining 
            immediate connectivity to Heraklion's business district, international airport, and seaport.
            """
        )

        st.markdown(
            """
            <div class="corporate-card">
                <div class="card-title">Key Distances & Connectivity</div>
                <p>📍 <b>Ammoudara Beach:</b> 50 m (1 min walk)</p>
                <p>🏛️ <b>Heraklion City Center:</b> 6.0 km (10 mins drive)</p>
                <p>✈️ <b>Heraklion Airport (HER):</b> 11.0 km (14 mins drive)</p>
                <p>🏺 <b>Palace of Knossos:</b> 12.0 km (15 mins drive)</p>
                <p>🍽️ <b>Fine Dining & Markets:</b> 100 m (Walking distance)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.link_button("OPEN IN GOOGLE MAPS", MAPS_URL, use_container_width=True)

    with loc_right:
        map_data = {"lat": [35.3400], "lon": [25.0800]}
        st.map(map_data, latitude="lat", longitude="lon", zoom=14)

# ---------------------------------------------------------
# TAB 4: GUEST REVIEWS
# ---------------------------------------------------------
with tab_reviews:
    st.markdown('<div class="section-label">CLIENT TESTIMONIALS</div>', unsafe_allow_html=True)
    st.header("Trusted by Travelers Worldwide")

    rev1, rev2 = st.columns(2, gap="large")

    with rev1:
        st.markdown(
            """
            <div class="corporate-card">
                <div style="color:#d4af37; font-size:16px;">★ ★ ★ ★ ★</div>
                <p style="font-style:italic; font-size:16px; margin-top:15px; color:#ffffff;">
                    “Exceptional standards. The sea view from the executive suite balcony was breathtaking. Extremely clean, professional management, and ideal location.”
                </p>
                <p style="text-transform:uppercase; font-size:11px; color:#d4af37; margin-top:20px; letter-spacing:0.1em;">
                    — Obada · Verified Guest
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with rev2:
        st.markdown(
            """
            <div class="corporate-card">
                <div style="color:#d4af37; font-size:16px;">★ ★ ★ ★ ★</div>
                <p style="font-style:italic; font-size:16px; margin-top:15px; color:#ffffff;">
                    “Quiet, impeccably maintained apartments with high-speed internet. Perfectly situated near the beach and top-rated restaurants.”
                </p>
                <p style="text-transform:uppercase; font-size:11px; color:#d4af37; margin-top:20px; letter-spacing:0.1em;">
                    — Véronique · Verified Guest
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# TAB 5: DIRECT RESERVATIONS
# ---------------------------------------------------------
with tab_booking:
    st.markdown('<div class="section-label">DIRECT BOOKING PORTAL</div>', unsafe_allow_html=True)
    st.header("Reserve Your Residence Directly")

    st.write(
        "Secure preferred corporate rates, complimentary room upgrades upon availability, and direct host coordination.")

    b_form, b_info = st.columns([1.3, 0.9], gap="large")

    with b_form:
        with st.form("corporate_booking_form"):
            st.subheader("Booking Request")

            fn = st.text_input("Full Name *")
            em = st.text_input("Corporate / Personal Email *")
            ph = st.text_input("Phone Number (with country code) *")

            d_col1, d_col2 = st.columns(2)
            with d_col1:
                cin = st.date_input("Check-In Date", datetime.now() + timedelta(days=1))
            with d_col2:
                cout = st.date_input("Check-Out Date", datetime.now() + timedelta(days=5))

            suite_type = st.selectbox("Residence Category", [
                "Executive Sea View Apartment",
                "Standard Double Suite",
                "Twin Balcony Room",
                "Family Suite (2-Bedroom)"
            ])

            req = st.text_area("Special Requests / Corporate Billing Requirements")

            sub = st.form_submit_button("SUBMIT DIRECT RESERVATION")
            if sub:
                if fn and em and ph:
                    st.success(
                        "Your reservation request has been transmitted. Our management team (Kostas & Maria) will respond within 2 hours.")
                else:
                    st.error("Please complete all required fields (*).")

    with b_info:
        st.markdown(
            """
            <div class="corporate-card">
                <div class="card-title">Management Desk</div>
                <p><b>Hosts:</b> Kostas & Maria</p>
                <p><b>Property:</b> Sea View Hotel & Apartments</p>
                <p><b>Address:</b> Ammoudara, Heraklion, Crete, Greece</p>
                <hr style="margin:15px 0;">
                <p><b>Direct Booking Guarantees:</b></p>
                <p>✔ 0% Commission Surcharge</p>
                <p>✔ Priority Check-in Flexibility</p>
                <p>✔ Direct Access to Management</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# CORPORATE FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:20px 0;">
        <div style="font-family:'Cinzel', serif; color:#f4e8c1; font-size:20px; letter-spacing:0.08em;">SEA VIEW HOTEL & RESIDENCES</div>
        <p style="font-size:12px; color:#777777; margin-top:8px;">
            Ammoudara · Heraklion · Crete · Greece | Managed by Kostas & Maria<br>
            © 2026 Sea View Hotel Group. All rights reserved.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)