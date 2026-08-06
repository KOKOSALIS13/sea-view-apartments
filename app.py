import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# =========================================================
# CONFIG & STATE
# =========================================================

st.set_page_config(
    page_title="Sea View Hotel & Apartments | Ammoudara, Crete",
    page_icon="🌊",
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
# AESTHETIC DESIGN WITH WARM SUN FADE BACKGROUND
# =========================================================

st.markdown(
    """
    <!-- Google Fonts import for Aesthetic Serif & Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>
    /* 1. Fine Grain & Warm Sun Fade Aesthetic Background */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #f6f3ee !important;
        background-image: 
            radial-gradient(at 90% 10%, rgba(228, 213, 196, 0.45) 0px, transparent 50%),
            radial-gradient(at 10% 90%, rgba(210, 222, 220, 0.35) 0px, transparent 50%) !important;
        background-attachment: fixed !important;
        color: #2b2b2b !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 25px;
        padding-bottom: 90px;
        padding-left: 6%;
        padding-right: 6%;
    }

    #MainMenu, footer { visibility: hidden; }

    /* 2. Editorial Typography */
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #1f3a3d !important;
        font-weight: 500 !important;
        letter-spacing: -0.01em !important;
    }

    h1 { font-size: 3.8rem !important; line-height: 1.08 !important; }
    h2 { font-size: 2.6rem !important; margin-bottom: 24px !important; }
    h3 { font-size: 1.6rem !important; }

    p, label, span { color: #525252; line-height: 1.85; font-size: 14.5px; font-weight: 300; }

    hr {
        border: none;
        border-top: 1px solid #e5dfd5;
        margin-top: 55px;
        margin-bottom: 55px;
    }

    /* 3. Glassmorphic Aesthetic Cards & Hover Effects */
    .feature-box, .review-box {
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(8px);
        border: 1px solid #ece6dc !important;
        border-radius: 16px;
        padding: 34px;
        transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.015);
        min-height: 200px;
    }

    .feature-box:hover, .review-box:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 32px rgba(31, 58, 61, 0.07);
        border-color: #d1b89d !important;
        background: #ffffff !important;
    }

    .feature-icon { font-size: 24px; margin-bottom: 14px; opacity: 0.85; }
    .feature-title { color: #1f3a3d; font-family: 'Cormorant Garamond', serif; font-size: 22px; margin-bottom: 10px; font-weight: 500; }
    .feature-text { color: #666666; line-height: 1.75; font-size: 14px; font-weight: 300; }

    .host-box {
        background: #1f3a3d !important;
        border-radius: 16px;
        padding: 40px;
        color: white !important;
        box-shadow: 0 14px 30px rgba(31, 58, 61, 0.12);
    }
    .host-title { color: white !important; font-family: 'Cormorant Garamond', serif; font-size: 28px; margin-bottom: 16px; font-weight: 400; }
    .host-text { color: #e1e9e9 !important; line-height: 1.85; font-size: 15px; font-weight: 300; }

    .review-stars { color: #c27d66; font-size: 15px; letter-spacing: 3px; }
    .review-quote { color: #3d3d3d; font-size: 18px; line-height: 1.85; font-style: italic; margin-top: 16px; font-family: 'Cormorant Garamond', serif; }
    .review-author { color: #888888; font-size: 12px; margin-top: 22px; letter-spacing: 0.05em; text-transform: uppercase; }

    /* 4. Minimal Aesthetic Metrics */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(8px);
        border: 1px solid #ece6dc !important;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.015);
        text-align: center;
    }

    [data-testid="stMetricLabel"] { color: #888888 !important; font-size: 12px !important; letter-spacing: 0.06em; text-transform: uppercase; }

    [data-testid="stMetricValue"] {
        color: #1f3a3d !important;
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.3rem !important;
        font-weight: 500;
    }

    /* 5. Minimalist Buttons */
    .stLinkButton > a, .stButton > button {
        background: #1f3a3d !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 0.75rem 1.8rem !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        letter-spacing: 0.08em !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(31, 58, 61, 0.1) !important;
    }

    .stLinkButton > a:hover, .stButton > button:hover {
        background: #c27d66 !important;
        color: #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(194, 125, 102, 0.25) !important;
    }

    /* 6. Form Styling */
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        border: 1px solid #ece6dc !important;
        border-radius: 16px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
    }

    .section-label {
        color: #c27d66;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .gallery-title { font-family: 'Cormorant Garamond', serif; color: #1f3a3d; font-size: 22px; margin-top: 14px; margin-bottom: 2px; }
    .gallery-counter { color: #999999; font-size: 11px; letter-spacing: 0.08em; margin-bottom: 14px; }

    .footer-title { font-family: 'Cormorant Garamond', serif; color: #1f3a3d; font-size: 26px; }
    .footer-text { color: #888888; line-height: 1.8; font-size: 13px; }

    @media (max-width: 768px) {
        .block-container { padding-left: 5%; padding-right: 5%; padding-top: 15px; }
        h1 { font-size: 2.5rem !important; }
        h2 { font-size: 1.9rem !important; }
        .feature-box, .review-box { min-height: auto; }
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
        <div style="text-align:center; padding-top:15px; color:#777777; font-size:12px; letter-spacing:0.08em; text-transform:uppercase;">
            STAY · GALLERY · DIRECT BOOKING · LOCATION
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
                f"Request received for {guests} guests ({check_in.strftime('%d/%m')} - {check_out.strftime('%d/%m')}). Please complete your details below!")

with hero_right:
    if hotel:
        st.image(hotel, use_container_width=True)

# =========================================================
# QUICK STATS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Accommodation", "23 Rooms")
with c2:
    st.metric("Beach Distance", "50 m")
with c3:
    st.metric("Guest Rating", "4.68 / 5")
with c4:
    st.metric("Host Experience", "5 years")

# =========================================================
# EXPERIENCE
# =========================================================

st.divider()

st.markdown('<div class="section-label">THE EXPERIENCE</div>', unsafe_allow_html=True)
st.header("A quiet place beside the Cretan sea.")

experience_left, experience_right = st.columns([1.1, 1], gap="large")

with experience_left:
    st.write(
        """
        Located in Ammoudara, just outside Heraklion,
        our hotel and apartments combine the simplicity of a private
        stay with the beauty of the Cretan coastline.
        """
    )
    st.write(
        """
        Enjoy your morning coffee on the balcony, walk to
        the beach in just a few minutes and discover
        restaurants, cafés, supermarkets and local shops
        close to your stay.
        """
    )
    st.write(
        """
        Whether you are visiting Crete for a few days or
        staying longer, our goal is simple:

        **make you feel comfortable, relaxed and welcome.**
        """
    )

with experience_right:
    if balcony:
        st.image(balcony, caption="Sea view from the balcony", use_container_width=True)

# =========================================================
# WHY STAY
# =========================================================

st.divider()

st.markdown('<div class="section-label">WHY STAY WITH US</div>', unsafe_allow_html=True)
st.header("Everything you need for a relaxing stay.")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">🌊</div>
            <div class="feature-title">By the sea</div>
            <div class="feature-text">
                Approximately 50 metres from the beach,
                perfect for morning walks, swimming and
                relaxing beside the Cretan coast.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with f2:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">🌅</div>
            <div class="feature-title">Beautiful views</div>
            <div class="feature-text">
                Enjoy views of the sea and surrounding
                landscape from the apartment and balcony.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with f3:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">🚗</div>
            <div class="feature-title">Free parking</div>
            <div class="feature-text">
                Convenient free parking makes arriving by
                car and exploring Crete easier.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# ALL APARTMENT & ROOM PHOTOS SLIDESHOW
# =========================================================

st.divider()

st.markdown('<div class="section-label">PHOTO GALLERY</div>', unsafe_allow_html=True)
st.header("Simple. Comfortable. Authentic.")

apartment_images = [
    (name, img) for name, img in [
        ("Living room", livingroom),
        ("Living room view 2", livingroom1),
        ("Living room view 3", livingroom2),
        ("Bedroom", bedroom),
        ("Bedroom view 2", bedroom1),
        ("Bedroom view 3", bedroom2),
        ("Kitchen", kitchen),
        ("Bathroom", bathroom),
        ("Bathroom view 2", bathroom1),
        ("Balcony", balcony),
    ] if img is not None
]

if apartment_images:
    current_apartment = st.session_state.apartment_slide
    apartment_name, apartment_image = apartment_images[current_apartment]

    gallery_left, gallery_right = st.columns([1.35, 0.85], gap="large")

    with gallery_left:
        st.image(apartment_image, use_container_width=True)
        st.markdown(
            f"""
            <div class="gallery-title">{apartment_name}</div>
            <div class="gallery-counter">{current_apartment + 1} / {len(apartment_images)}</div>
            """,
            unsafe_allow_html=True,
        )

        selected_apt = st.radio(
            "Select Apartment Photo",
            options=range(len(apartment_images)),
            index=current_apartment,
            format_func=lambda i: f"📷 {i + 1}",
            horizontal=True,
            key="apt_radio",
            label_visibility="collapsed"
        )
        if selected_apt != current_apartment:
            st.session_state.apartment_slide = selected_apt
            st.rerun()

    with gallery_right:
        st.subheader("A comfortable home in Ammoudara")
        st.write(
            """
            Our 23 rooms & apartments offer comfortable bedrooms,
            living areas, fully equipped kitchens or mini-fridges, and private
            balconies with sea or mountain views.
            """
        )
        st.markdown(
            """
            **Room Amenities & Features:**

            • Double or Twin beds  
            • Private balcony or terrace  
            • Air conditioning  
            • Free High-Speed Wi-Fi  
            • Private bathroom with shower  
            • Kitchen / Mini-fridge  
            • Washing machine access  
            • Free on-site parking  
            • Sea and mountain views
            """
        )

    apartment_prev, apartment_spacer, apartment_next = st.columns([1, 4, 1])

    with apartment_prev:
        if st.button("← Previous", key="apartment_previous", use_container_width=True):
            st.session_state.apartment_slide = (current_apartment - 1) % len(apartment_images)
            st.rerun()

    with apartment_next:
        if st.button("Next →", key="apartment_next", use_container_width=True):
            st.session_state.apartment_slide = (current_apartment + 1) % len(apartment_images)
            st.rerun()

# =========================================================
# CRETE / SEA SLIDESHOW
# =========================================================

st.divider()

st.markdown('<div class="section-label">CRETE</div>', unsafe_allow_html=True)
st.header("The sea is part of the stay.")

sea_images = [
    (name, img) for name, img in [
        ("Ammoudara beach", sea),
        ("The Cretan coastline", sea1),
        ("Sea view", seaview),
        ("Ammoudara by night", seabynight),
    ] if img is not None
]

if sea_images:
    current_sea = st.session_state.sea_slide
    sea_name, sea_image = sea_images[current_sea]

    sea_gallery_left, sea_gallery_right = st.columns([1.35, 0.85], gap="large")

    with sea_gallery_left:
        st.image(sea_image, use_container_width=True)
        st.markdown(
            f"""
            <div class="gallery-title">{sea_name}</div>
            <div class="gallery-counter">{current_sea + 1} / {len(sea_images)}</div>
            """,
            unsafe_allow_html=True,
        )

        selected_sea = st.radio(
            "Select Sea Photo",
            options=range(len(sea_images)),
            index=current_sea,
            format_func=lambda i: f"🌊 {i + 1}",
            horizontal=True,
            key="sea_radio",
            label_visibility="collapsed"
        )
        if selected_sea != current_sea:
            st.session_state.sea_slide = selected_sea
            st.rerun()

    with sea_gallery_right:
        st.subheader("Discover Ammoudara")
        st.write(
            """
            From the beach just a short walk away to the
            beautiful Cretan coastline, the sea is always
            close during your stay.
            """
        )
        st.write(
            """
            Enjoy a morning swim, an afternoon by the sea
            or a relaxing evening watching the coastline.
            """
        )

    sea_prev, sea_spacer, sea_next = st.columns([1, 4, 1])

    with sea_prev:
        if st.button("← Previous", key="sea_previous", use_container_width=True):
            st.session_state.sea_slide = (current_sea - 1) % len(sea_images)
            st.rerun()

    with sea_next:
        if st.button("Next →", key="sea_next", use_container_width=True):
            st.session_state.sea_slide = (current_sea + 1) % len(sea_images)
            st.rerun()

# =========================================================
# HOSTS
# =========================================================

st.divider()

st.markdown('<div class="section-label">YOUR HOSTS</div>', unsafe_allow_html=True)
st.header("A warm welcome from Kostas & Maria.")

host_left, host_right = st.columns([1.1, 1], gap="large")

with host_left:
    st.subheader("Feel at home in Crete.")
    st.write(
        """
        We are Kostas and Maria, and we are happy to welcome
        you to Ammoudara.
        """
    )
    st.write(
        """
        We believe that a good holiday is about more than
        simply having a place to sleep. It is about feeling
        comfortable, knowing that someone is there if you
        need anything and enjoying the destination at your
        own pace.
        """
    )
    st.write(
        """
        We are always happy to help with recommendations,
        directions or anything that can make your stay
        easier and more enjoyable.
        """
    )

with host_right:
    st.markdown(
        """
        <div class="host-box">
            <div class="host-title">Feel at home in Crete.</div>
            <div class="host-text">
                Personal hospitality, local knowledge and
                a relaxed seaside atmosphere — from two
                hosts who genuinely want you to enjoy
                your time in Crete.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# REVIEWS
# =========================================================

st.divider()

st.markdown('<div class="section-label">GUEST REVIEWS</div>', unsafe_allow_html=True)
st.header("What our guests say.")

r1, r2 = st.columns(2, gap="large")

with r1:
    st.markdown(
        """
        <div class="review-box">
            <div class="review-stars">★ ★ ★ ★ ★</div>
            <div class="review-quote">
                “The location was unbeatable. Waking up with
                a sea view made the whole trip feel special.
                The apartment was clean, comfortable and
                exactly as described.”
            </div>
            <div class="review-author">— Obada · Guest</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with r2:
    st.markdown(
        """
        <div class="review-box">
            <div class="review-stars">★ ★ ★ ★ ★</div>
            <div class="review-quote">
                “Very clean, quiet, with a large balcony and
                beautiful sea view. The beach and restaurants
                are just a short walk away.”
            </div>
            <div class="review-author">— Véronique · Guest</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# LOCATION
# =========================================================

st.divider()

st.markdown('<div class="section-label">LOCATION</div>', unsafe_allow_html=True)
st.header("The sea is close. Heraklion is closer than you think.")

location_left, location_right = st.columns([1, 1.15], gap="large")

with location_left:
    st.write(
        """
        Located in Ammoudara, just outside Heraklion,
        our hotel and apartments offer a relaxed seaside atmosphere
        while keeping you close to the city.
        """
    )
    st.write(
        """
        The beach is approximately **50 metres away**.
        Restaurants, cafés, supermarkets and local shops
        are all within easy walking distance.
        """
    )
    st.write(
        """
        Ammoudara is also a convenient base for exploring
        Heraklion, Knossos and the rest of Crete.
        """
    )

    st.subheader("Perfect for exploring Crete")
    st.write(
        """
        • 🏖️ Ammoudara Beach — approximately 50 m  
        • 🏛️ Heraklion city centre — a short drive away  
        • 🏺 Knossos Archaeological Site — easy access by car  
        • 🍽️ Restaurants & cafés — within walking distance  
        • 🛒 Supermarkets & shops — nearby  
        • 🚗 Free parking — available
        """
    )

    st.link_button("OPEN LOCATION IN GOOGLE MAPS", MAPS_URL)

with location_right:
    st.subheader("Find us in Ammoudara")
    st.write("Ammoudara · Heraklion · Crete")

    map_data = {
        "lat": [35.3400],
        "lon": [25.0800],
    }
    st.map(map_data, latitude="lat", longitude="lon", zoom=14)

# Highlights
st.write("")
l1, l2, l3, l4 = st.columns(4)

with l1:
    st.metric("Beach", "50 m", "Walking distance")
with l2:
    st.metric("Area", "Ammoudara", "Heraklion")
with l3:
    st.metric("Nearby", "Restaurants", "Cafés & shops")
with l4:
    st.metric("Parking", "FREE", "Available")

# =========================================================
# FAQ SECTION
# =========================================================

st.divider()

st.markdown('<div class="section-label">QUESTIONS & ANSWERS</div>', unsafe_allow_html=True)
st.header("Frequently Asked Questions")

faq1, faq2 = st.columns(2, gap="large")

with faq1:
    with st.expander("🕒 What are the Check-in and Check-out times?"):
        st.write(
            "Standard check-in is from 15:00 onwards, and check-out is until 11:00 AM. Flexible timing can be arranged upon request.")

    with st.expander("🚌 Is public transport available nearby?"):
        st.write(
            "Yes! A public bus stop is located just a short walk away with regular routes connecting to Heraklion city center, the port, and the airport.")

with faq2:
    with st.expander("📶 Is Wi-Fi suitable for remote work?"):
        st.write(
            "Yes, we provide fast and reliable private Wi-Fi suitable for video calls, streaming, and remote work.")

    with st.expander("🛒 Are grocery stores and restaurants nearby?"):
        st.write(
            "Supermarkets, bakeries, tavernas, and cafés are all within 2 to 5 minutes walking distance from the accommodation.")

# =========================================================
# DIRECT BOOKING FORM SECTION (ALL 23 ROOMS)
# =========================================================

st.divider()

st.markdown('<div class="section-label">DIRECT RESERVATION</div>', unsafe_allow_html=True)
st.header("Book Directly With Us & Save")

st.write(
    "By booking directly with Kostas & Maria, you avoid third-party service fees and secure the best available rate for any of our 23 rooms & apartments.")

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

        r_type = st.selectbox("Preferred Accommodation Type", [
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
                    "Thank you! Your booking request has been received. Kostas & Maria will contact you shortly to confirm availability and direct rates.")
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
    st.write("🔗 **Airbnb:** [View selected units on Airbnb](https://www.airbnb.gr/rooms/559151340688341474)")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer-title">SEA VIEW HOTEL & APARTMENTS</div>
    <div class="footer-text">
        Ammoudara · Heraklion · Crete (23 Units)<br>
        50 metres from the beach<br><br>
        Hosted by Kostas & Maria<br><br>
        © 2026 Sea View Apartments. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)