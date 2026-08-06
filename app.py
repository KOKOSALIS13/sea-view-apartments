
import streamlit as st
from pathlib import Path
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Sea View Apartments | Ammoudara, Crete",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


# =========================================================
# IMAGE LOADER
# =========================================================

def get_image(filename):
    path = IMAGE_DIR / filename

    if path.exists():
        try:
            return Image.open(path)
        except Exception:
            return None

    return None


# =========================================================
# LOAD IMAGES
# =========================================================

hotel = get_image("hotel.jpg")

# SEA / CRETE
sea = get_image("sea.jpg")
sea1 = get_image("sea1.jpg")
seaview = get_image("seaview.jpg")
seabynight = get_image("seabynight.jpg")

# APARTMENT
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
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #faf9f6;
        color: #222222;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 25px;
        padding-bottom: 60px;
        padding-left: 5%;
        padding-right: 5%;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif !important;
        color: #173b43 !important;
        font-weight: 400 !important;
    }

    h1 {
        font-size: 3.3rem !important;
    }

    h2 {
        font-size: 2.3rem !important;
    }

    h3 {
        font-size: 1.5rem !important;
    }

    p {
        color: #555555;
        line-height: 1.8;
    }

    hr {
        border: none;
        border-top: 1px solid #e5e0d8;
        margin-top: 40px;
        margin-bottom: 40px;
    }

    .stButton > button {
        background: #173b43;
        color: white;
        border: none;
        border-radius: 3px;
        padding: 0.7rem 1.4rem;
        font-size: 13px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #285b64;
        color: white;
    }

    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 4px;
        padding: 18px;
    }

    [data-testid="stMetricLabel"] {
        color: #777777 !important;
    }

    [data-testid="stMetricValue"] {
        color: #173b43 !important;
        font-family: Georgia, "Times New Roman", serif;
    }

    .section-label {
        color: #a0784c;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        margin-bottom: 8px;
    }

    .feature-box {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 4px;
        padding: 28px;
        min-height: 190px;
    }

    .feature-icon {
        font-size: 27px;
        margin-bottom: 12px;
    }

    .feature-title {
        color: #173b43;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 22px;
        margin-bottom: 10px;
    }

    .feature-text {
        color: #666666;
        line-height: 1.7;
        font-size: 14px;
    }

    .host-box {
        background: #173b43;
        border-radius: 4px;
        padding: 32px;
        color: white;
    }

    .host-title {
        color: white;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 27px;
        margin-bottom: 15px;
    }

    .host-text {
        color: #e5eeee;
        line-height: 1.8;
        font-size: 15px;
    }

    .review-box {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 4px;
        padding: 30px;
        min-height: 220px;
    }

    .review-stars {
        color: #a0784c;
        font-size: 18px;
        letter-spacing: 2px;
    }

    .review-quote {
        color: #444444;
        font-size: 15px;
        line-height: 1.8;
        font-style: italic;
        margin-top: 15px;
    }

    .review-author {
        color: #777777;
        font-size: 13px;
        margin-top: 20px;
    }

    .gallery-title {
        font-family: Georgia, "Times New Roman", serif;
        color: #173b43;
        font-size: 21px;
        margin-top: 12px;
        margin-bottom: 3px;
    }

    .gallery-counter {
        color: #888888;
        font-size: 12px;
        letter-spacing: 0.05em;
        margin-bottom: 12px;
    }

    .footer-title {
        font-family: Georgia, "Times New Roman", serif;
        color: #173b43;
        font-size: 25px;
    }

    .footer-text {
        color: #777777;
        line-height: 1.8;
    }

    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 5%;
            padding-right: 5%;
            padding-top: 15px;
        }

        h1 {
            font-size: 2.4rem !important;
            line-height: 1.15 !important;
        }

        h2 {
            font-size: 1.9rem !important;
            line-height: 1.2 !important;
        }

        h3 {
            font-size: 1.4rem !important;
        }

        p {
            font-size: 15px;
            line-height: 1.7;
        }

        [data-testid="stHorizontalBlock"] {
            gap: 1rem !important;
        }

        [data-testid="stMetric"] {
            padding: 12px;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.4rem !important;
        }

        .feature-box {
            min-height: auto;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# NAVBAR
# =========================================================

nav_left, nav_center, nav_right = st.columns(
    [2.2, 2.2, 1],
    gap="medium"
)

with nav_left:

    st.markdown("### SEA VIEW")
    st.caption("AMMOUDARA · CRETE")

with nav_center:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding-top:15px;
            color:#666666;
            font-size:13px;
            letter-spacing:0.04em;
        ">
            STAY · EXPERIENCE · LOCATION
        </div>
        """,
        unsafe_allow_html=True,
    )

with nav_right:

    if st.button(
        "BOOK",
        key="top_booking",
        width="stretch"
    ):

        st.markdown(
            """
            [BOOK YOUR STAY](https://www.airbnb.gr/rooms/559151340688341474)
            """
        )

st.divider()


# =========================================================
# HERO
# =========================================================

hero_left, hero_right = st.columns(
    [0.9, 1.4],
    gap="large"
)

with hero_left:

    st.markdown(
        '<div class="section-label">AMMOUDARA · HERAKLION · CRETE</div>',
        unsafe_allow_html=True,
    )

    st.title("Wake up by the sea.")

    st.write(
        """
        Comfortable private apartments just steps from the beach,
        with beautiful sea views, spacious balconies and everything
        you need for a relaxing stay in Crete.
        """
    )

    if st.button("CHECK AVAILABILITY", key="hero_booking"):

        st.markdown(
            "[Open our Airbnb listing](https://www.airbnb.gr/rooms/559151340688341474)"
        )

with hero_right:

    if hotel:

        st.image(
            hotel,
            width="stretch"
        )


# =========================================================
# QUICK STATS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Beach", "50 m")

with c2:
    st.metric("Guest Rating", "4.68 / 5")

with c3:
    st.metric("Reviews", "93")

with c4:
    st.metric("Host Experience", "5 years")


# =========================================================
# EXPERIENCE
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">THE EXPERIENCE</div>',
    unsafe_allow_html=True,
)

st.header("A quiet place beside the Cretan sea.")

experience_left, experience_right = st.columns(
    [1.1, 1],
    gap="large"
)

with experience_left:

    st.write(
        """
        Located in Ammoudara, just outside Heraklion,
        our apartments combine the simplicity of a private
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

        st.image(
            balcony,
            caption="Sea view from the balcony",
            width="stretch"
        )

# =========================================================
# WHY STAY
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">WHY STAY WITH US</div>',
    unsafe_allow_html=True,
)

st.header("Everything you need for a relaxing stay.")

f1, f2, f3 = st.columns(3)

with f1:

    st.markdown(
        """
        <div class="feature-box">

            <div class="feature-icon">
                🌊
            </div>

            <div class="feature-title">
                By the sea
            </div>

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

            <div class="feature-icon">
                🌅
            </div>

            <div class="feature-title">
                Beautiful views
            </div>

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

            <div class="feature-icon">
                🚗
            </div>

            <div class="feature-title">
                Free parking
            </div>

            <div class="feature-text">
                Convenient free parking makes arriving by
                car and exploring Crete easier.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )




# =========================================================
# APARTMENT
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">THE APARTMENT</div>',
    unsafe_allow_html=True,
)

st.header("Simple. Comfortable. Authentic.")


# =========================================================
# APARTMENT SLIDESHOW
# =========================================================

apartment_images = [
    ("Living room", livingroom),
    ("Living room", livingroom1),
    ("Living room", livingroom2),
    ("Bedroom", bedroom),
    ("Bedroom", bedroom1),
    ("Bedroom", bedroom2),
    ("Kitchen", kitchen),
    ("Bathroom", bathroom),
    ("Bathroom", bathroom1),
    ("Balcony", balcony),
]

# Remove missing images
apartment_images = [
    (name, image)
    for name, image in apartment_images
    if image is not None
]


if apartment_images:

    if "apartment_slide" not in st.session_state:
        st.session_state.apartment_slide = 0

    current_apartment = st.session_state.apartment_slide

    apartment_name, apartment_image = apartment_images[
        current_apartment
    ]

    gallery_left, gallery_right = st.columns(
        [1.35, 0.85],
        gap="large"
    )

    with gallery_left:

        st.image(
            apartment_image,
            width="stretch"
        )

        st.markdown(
            f"""
            <div class="gallery-title">
                {apartment_name}
            </div>

            <div class="gallery-counter">
                {current_apartment + 1} / {len(apartment_images)}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with gallery_right:

        st.subheader("A comfortable home in Ammoudara")

        st.write(
            """
            The apartment offers a comfortable bedroom,
            living area, fully equipped kitchen and private
            balcony with sea views.
            """
        )

        st.markdown(
            """
            **The apartment includes:**

            • 1 bedroom with double bed  
            • Living room  
            • Fully equipped kitchen  
            • Private balcony  
            • Bathroom with shower  
            • Air conditioning  
            • Wi-Fi  
            • Washing machine  
            • Free parking  
            • Sea and mountain views
            """
        )


    apartment_prev, apartment_spacer, apartment_next = st.columns(
        [1, 4, 1]
    )

    with apartment_prev:

        if st.button(
            "← Previous",
            key="apartment_previous",
            width="stretch"
        ):

            st.session_state.apartment_slide = (
                current_apartment - 1
            ) % len(apartment_images)

            st.rerun()

    with apartment_next:

        if st.button(
            "Next →",
            key="apartment_next",
            width="stretch"
        ):

            st.session_state.apartment_slide = (
                current_apartment + 1
            ) % len(apartment_images)

            st.rerun()


# =========================================================
# CRETE / SEA
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">CRETE</div>',
    unsafe_allow_html=True,
)

st.header("The sea is part of the stay.")


# Only location / sea images here.
# Apartment photos are NOT repeated.

sea_images = [
    ("Ammoudara beach", sea),
    ("The Cretan coastline", sea1),
    ("Sea view", seaview),
    ("Ammoudara by night", seabynight),
]

# Remove missing images
sea_images = [
    (name, image)
    for name, image in sea_images
    if image is not None
]


if sea_images:

    if "sea_slide" not in st.session_state:
        st.session_state.sea_slide = 0

    current_sea = st.session_state.sea_slide

    sea_name, sea_image = sea_images[current_sea]

    sea_gallery_left, sea_gallery_right = st.columns(
        [1.35, 0.85],
        gap="large"
    )

    with sea_gallery_left:

        st.image(
            sea_image,
            width="stretch"
        )

        st.markdown(
            f"""
            <div class="gallery-title">
                {sea_name}
            </div>

            <div class="gallery-counter">
                {current_sea + 1} / {len(sea_images)}
            </div>
            """,
            unsafe_allow_html=True,
        )

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


    sea_prev, sea_spacer, sea_next = st.columns(
        [1, 4, 1]
    )

    with sea_prev:

        if st.button(
            "← Previous",
            key="sea_previous",
            width="stretch"
        ):

            st.session_state.sea_slide = (
                current_sea - 1
            ) % len(sea_images)

            st.rerun()

    with sea_next:

        if st.button(
            "Next →",
            key="sea_next",
            width="stretch"
        ):

            st.session_state.sea_slide = (
                current_sea + 1
            ) % len(sea_images)

            st.rerun()


# =========================================================
# HOSTS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">YOUR HOSTS</div>',
    unsafe_allow_html=True,
)

st.header("A warm welcome from Kostas & Maria.")

host_left, host_right = st.columns(
    [1.1, 1],
    gap="large"
)

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

            <div class="host-title">
                Feel at home in Crete.
            </div>

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

st.markdown(
    '<div class="section-label">GUEST REVIEWS</div>',
    unsafe_allow_html=True,
)

st.header("What our guests say.")

r1, r2 = st.columns(2, gap="large")

with r1:

    st.markdown(
        """
        <div class="review-box">

            <div class="review-stars">
                ★★★★★
            </div>

            <div class="review-quote">
                “The location was unbeatable. Waking up with
                a sea view made the whole trip feel special.
                The apartment was clean, comfortable and
                exactly as described.”
            </div>

            <div class="review-author">
                — Obada · Guest
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with r2:

    st.markdown(
        """
        <div class="review-box">

            <div class="review-stars">
                ★★★★★
            </div>

            <div class="review-quote">
                “Very clean, quiet, with a large balcony and
                beautiful sea view. The beach and restaurants
                are just a short walk away.”
            </div>

            <div class="review-author">
                — Véronique · Guest
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )




# =========================================================
# LOCATION
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">LOCATION</div>',
    unsafe_allow_html=True,
)

st.header("The sea is close. Heraklion is closer than you think.")

location_left, location_right = st.columns(
    [1, 1.15],
    gap="large"
)

with location_left:

    st.write(
        """
        Located in Ammoudara, just outside Heraklion,
        our apartments offer a relaxed seaside atmosphere
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

    if st.button(
        "OPEN LOCATION IN GOOGLE MAPS",
        key="maps_button"
    ):

        st.markdown(
            """
            [Open Sea View Apartments in Google Maps](https://www.google.com/maps/search/Ammoudara+Heraklion+Crete)
            """
        )


with location_right:

    st.subheader("Find us in Ammoudara")

    st.write(
        """
        Ammoudara · Heraklion · Crete
        """
    )

    map_data = {
        "lat": [35.3400],
        "lon": [25.0800],
    }

    st.map(
        map_data,
        latitude="lat",
        longitude="lon",
        zoom=14
    )


# =========================================================
# LOCATION HIGHLIGHTS
# =========================================================

st.write("")

l1, l2, l3, l4 = st.columns(4)

with l1:

    st.metric(
        "Beach",
        "50 m",
        "Walking distance"
    )

with l2:

    st.metric(
        "Area",
        "Ammoudara",
        "Heraklion"
    )

with l3:

    st.metric(
        "Nearby",
        "Restaurants",
        "Cafés & shops"
    )

with l4:

    st.metric(
        "Parking",
        "FREE",
        "Available"
    )


# =========================================================
# FINAL BOOKING CTA
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">READY FOR CRETE?</div>',
    unsafe_allow_html=True,
)

st.header("Your stay by the sea starts here.")

st.write(
    """
    Wake up to the Cretan sea, enjoy the beach just steps away
    and explore Heraklion from a comfortable private apartment
    in Ammoudara.
    """
)

booking_left, booking_right = st.columns(
    [1.4, 1],
    gap="large"
)

with booking_left:

    st.subheader("Stay with Kostas & Maria")

    st.write(
        """
        We would be happy to welcome you to Ammoudara and
        help make your stay in Crete comfortable, relaxing
        and memorable.
        """
    )

    st.write(
        """
        **Beach · Sea views · Private apartment · Free parking**
        """
    )

with booking_right:

    if st.button(
        "CHECK AVAILABILITY ON AIRBNB",
        key="final_booking",
        width="stretch"
    ):

        st.markdown(
            """
            [VIEW AVAILABILITY & BOOK ON AIRBNB](https://www.airbnb.gr/rooms/559151340688341474)
            """
        )

    st.caption(
        "You will be redirected to our Airbnb listing."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer-title">
        SEA VIEW APARTMENTS
    </div>

    <div class="footer-text">
        Ammoudara · Heraklion · Crete
        <br>
        50 metres from the beach
        <br><br>
        Hosted by Kostas & Maria
        <br><br>
        © 2026 Sea View Apartments
    </div>
    """,
    unsafe_allow_html=True,
)

