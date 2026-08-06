import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# =========================================================
# CONFIG & STATE
# =========================================================

st.set_page_config(
    page_title="Sea View Apartments & Suites | Ammoudara, Crete",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
balcony = get_image("balcony.jpg")
livingroom = get_image("livingroom.jpg")
bedroom = get_image("bedroom.jpg")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    .stApp { background: #faf9f6; color: #222222; }
    .block-container { max-width: 1400px; padding-top: 25px; padding-bottom: 60px; padding-left: 5%; padding-right: 5%; }
    #MainMenu, footer { visibility: hidden; }

    h1, h2, h3 { font-family: Georgia, "Times New Roman", serif !important; color: #173b43 !important; font-weight: 400 !important; }
    h1 { font-size: 3.3rem !important; }
    h2 { font-size: 2.3rem !important; }
    h3 { font-size: 1.5rem !important; }
    p { color: #555555; line-height: 1.8; }
    hr { border: none; border-top: 1px solid #e5e0d8; margin-top: 40px; margin-bottom: 40px; }

    .stLinkButton > a {
        background: #173b43 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.7rem 1.4rem !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        display: inline-block !important;
        text-align: center !important;
    }
    .stLinkButton > a:hover { background: #285b64 !important; }

    [data-testid="stMetric"] { background: white; border: 1px solid #ebe7df; border-radius: 4px; padding: 18px; }
    .section-label { color: #a0784c; font-size: 11px; font-weight: 700; letter-spacing: 0.16em; margin-bottom: 8px; }

    .room-card {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# NAVBAR
# =========================================================

nav_left, nav_center, nav_right = st.columns([2.2, 2.2, 1], gap="medium")

with nav_left:
    st.markdown("### SEA VIEW HOTEL & APARTMENTS")
    st.caption("AMMOUDARA · CRETE (23 ROOMS & SUITES)")

with nav_center:
    st.markdown(
        """
        <div style="text-align:center; padding-top:15px; color:#666666; font-size:13px; letter-spacing:0.04em;">
            ROOMS · DIRECT BOOKING · LOCATION
        </div>
        """,
        unsafe_allow_html=True,
    )

with nav_right:
    st.link_button("AIRBNB LISTING", AIRBNB_URL_1, use_container_width=True)

st.divider()

# =========================================================
# HERO & DIRECT SEARCH BAR
# =========================================================

hero_left, hero_right = st.columns([1.1, 0.9], gap="large")

with hero_left:
    st.markdown('<div class="section-label">AMMOUDARA · HERAKLION · CRETE</div>', unsafe_allow_html=True)
    st.title("Your Seaside Escape in Crete.")
    st.write(
        """
        Welcome to Sea View Apartments. Featuring 23 comfortable, fully-equipped rooms 
        and apartments just 50 meters from Ammoudara beach. Book directly with us for 
        the best rates or view selected units on Airbnb.
        """
    )

    # Φόρμα Γρήγορου Ελέγχου Διαθεσιμότητας
    st.subheader("Direct Reservation Request")
    with st.form("quick_search"):
        col_d1, col_d2, col_g = st.columns(3)
        with col_d1:
            check_in = st.date_input("Check-in", datetime.now())
        with col_d2:
            check_out = st.date_input("Check-out", datetime.now() + timedelta(days=3))
        with col_g:
            guests = st.number_input("Guests", min_value=1, max_value=6, value=2)

        search_submit = st.form_submit_button("CHECK DIRECT AVAILABILITY", use_container_width=True)
        if search_submit:
            st.success(
                f"Request received for {guests} guests ({check_in.strftime('%d/%m')} - {check_out.strftime('%d/%m')}). Please complete your details in the booking section below!")

with hero_right:
    if hotel:
        st.image(hotel, use_container_width=True)

st.divider()

# =========================================================
# ROOM TYPES & ACCOMMODATION (23 ROOMS CONCEPT)
# =========================================================

st.markdown('<div class="section-label">ACCOMMODATION</div>', unsafe_allow_html=True)
st.header("Explore Our Rooms & Apartments")
st.write("We offer 23 private units tailored for couples, families, and solo travelers.")

# Κατηγορία 1: Sea View Apartments (Τα 2 που βρίσκονται στο Airbnb)
col_r1_img, col_r1_txt = st.columns([1, 1.2], gap="large")
with col_r1_img:
    if balcony:
        st.image(balcony, use_container_width=True, caption="Sea View Apartment")

with col_r1_txt:
    st.subheader("1. Premium Sea View Apartment")
    st.write("Spacious 1-bedroom apartment with a living room, full kitchen, and panoramic Cretan sea view.")
    st.markdown("• **Capacity:** Up to 3 guests | • **Size:** 45 m² | • **Distance to beach:** 50m")

    btn_c1, btn_c2 = st.columns(2)
    with btn_c1:
        st.link_button("BOOK ON AIRBNB", AIRBNB_URL_1, use_container_width=True)
    with btn_c2:
        if st.button("BOOK DIRECTLY (BEST PRICE)", key="btn_direct_1", use_container_width=True):
            st.info(
                "Fill in the Direct Booking form at the bottom of the page to lock in the best rate without platform fees!")

st.write("")

# Κατηγορία 2: Standard Double / Twin Rooms (Τα υπόλοιπα δωμάτια)
col_r2_img, col_r2_txt = st.columns([1, 1.2], gap="large")
with col_r2_img:
    if bedroom:
        st.image(bedroom, use_container_width=True, caption="Standard Double Room")

with col_r2_txt:
    st.subheader("2. Standard Double & Twin Rooms (21 Units)")
    st.write("Comfortable private rooms featuring air conditioning, private balcony, Wi-Fi, and fridge.")
    st.markdown("• **Capacity:** 2 guests | • **Size:** 25 m² | • **Balcony / Garden View**")
    if st.button("REQUEST DIRECT BOOKING", key="btn_direct_2", use_container_width=True):
        st.info("Scroll down to our Direct Booking Form or send us a message to check availability!")

st.divider()

# =========================================================
# DIRECT BOOKING FORM SECTION
# =========================================================

st.markdown('<div class="section-label">DIRECT RESERVATION</div>', unsafe_allow_html=True)
st.header("Book Directly With Us & Save")

st.write(
    "By booking directly with Kostas & Maria, you avoid third-party service fees and secure the best available rate for any of our 23 rooms.")

form_col, info_col = st.columns([1.3, 1], gap="large")

with form_col:
    with st.form("hotel_direct_booking", clear_on_submit=True):
        st.subheader("Reservation Request Form")

        full_name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone / WhatsApp *")

        c_in, c_out = st.columns(2)
        with c_in:
            date_in = st.date_input("Arrival Date", datetime.now() + timedelta(days=1))
        with c_out:
            date_out = st.date_input("Departure Date", datetime.now() + timedelta(days=5))

        r_type = st.selectbox("Preferred Room Type", [
            "Premium Sea View Apartment (Airbnb Listed)",
            "Standard Double Room",
            "Twin Room with Balcony",
            "Family Suite"
        ])

        notes = st.text_area("Special Requests / Questions")

        submit_booking = st.form_submit_button("SUBMIT RESERVATION REQUEST", use_container_width=True)

        if submit_booking:
            if full_name and email and phone:
                st.success(
                    "Thank you! Your booking request has been received. Kostas & Maria will contact you within 2 hours to confirm availability and pricing.")
            else:
                st.error("Please fill in all required fields (*).")

with info_col:
    st.subheader("Direct Booking Benefits")
    st.markdown(
        """
        ✔ **Best Rate Guarantee:** No platform commission fees.  
        ✔ **Flexible Check-in:** Personalized service upon arrival.  
        ✔ **Direct Communication:** Speak straight with your hosts.  
        ✔ **Free Parking & High-Speed Wi-Fi** included.  
        """
    )
    st.divider()
    st.write("**Contact Hosts Directly:**")
    st.write("📍 Ammoudara, Heraklion, Crete")
    st.write("📧 info@seaviewammoudara.com")
    st.write("📞 +30 690 000 0000")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#777777;">
        <b>SEA VIEW HOTEL & APARTMENTS (23 UNITS)</b><br>
        Ammoudara · Heraklion · Crete · Hosted by Kostas & Maria<br>
        © 2026 Sea View Apartments. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)