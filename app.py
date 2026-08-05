
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
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GENERAL
       ===================================================== */

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

    header {
        background: transparent !important;
    }


    /* =====================================================
       TYPOGRAPHY
       ===================================================== */

    h1,
    h2,
    h3 {
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

    p {
        color: #555555;
        line-height: 1.8;
    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {
        border: none;
        border-top: 1px solid #e5e0d8;
        margin-top: 40px;
        margin-bottom: 40px;
    }


    /* =====================================================
       BUTTONS
       ===================================================== */

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


    /* =====================================================
       METRICS
       ===================================================== */

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


    /* =====================================================
       SECTION LABEL
       ===================================================== */

    .section-label {
        color: #a0784c;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        margin-bottom: 8px;
    }


    /* =====================================================
       WHY STAY FEATURE BOXES
       ===================================================== */

    .feature-box {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 6px;
        padding: 30px;
        min-height: 230px;
        box-shadow: 0 6px 20px rgba(23, 59, 67, 0.04);
    }

    .feature-icon {
        font-size: 28px;
        margin-bottom: 18px;
    }

    .feature-title {
        font-family: Georgia, "Times New Roman", serif;
        color: #173b43;
        font-size: 24px;
        margin-bottom: 12px;
    }

    .feature-text {
        color: #5f625f;
        font-size: 15px;
        line-height: 1.8;
    }


    /* =====================================================
       HOST
       ===================================================== */

    .host-box {
        background: #173b43;
        border-radius: 6px;
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


    /* =====================================================
       REVIEWS
       ===================================================== */

    .review-box {
        background: white;
        border: 1px solid #ebe7df;
        border-radius: 6px;
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


    /* =====================================================
       FOOTER
       ===================================================== */

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
            padding: 25px;
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
        """
        <div class="section-label">
            AMMOUDARA · HERAKLION · CRETE
        </div>
        """,
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

    if st.button(
        "CHECK AVAILABILITY",
        key="hero_booking"
    ):

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
    """
    <div class="section-label">
        THE EXPERIENCE
    </div>
    """,
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
        """)


with experience_right:

    if balcony:

        st.image(
            balcony,
            caption="Sea view from the balcony",
            width="stretch"
        )


# =========================================================
# SEA IMAGE
# =========================================================

if seaview:

    st.image(
        seaview,
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

f1, f2, f3 = st.columns(3, gap="large")


with f1:

    st.html("""
        <div class="feature-box">
            <div class="feature-icon">🌊</div>

            <div class="feature-title">
                By the sea
            </div>

            <div class="feature-text">
                Approximately 50 metres from the beach,
                perfect for morning walks, swimming and
                relaxing beside the Cretan coast.
            </div>
        </div>
    """)


with f2:

    st.html("""
        <div class="feature-box">
            <div class="feature-icon">🌅</div>

            <div class="feature-title">
                Beautiful views
            </div>

            <div class="feature-text">
                Enjoy views of the sea and surrounding
                landscape from the apartment and balcony.
            </div>
        </div>
    """)


with f3:

    st.html("""
        <div class="feature-box">
            <div class="feature-icon">🚗</div>

            <div class="feature-title">
                Free parking
            </div>

            <div class="feature-text">
                Convenient free parking makes arriving by
                car and exploring Crete easier.
            </div>
        </div>
    """)




# =========================================================
# APARTMENT
# =========================================================

st.divider()

st.markdown(
    """
    <div class="section-label">
        THE APARTMENT
    </div>
    """,
    unsafe_allow_html=True,
)

st.header("Simple. Comfortable. Authentic.")

apt_left, apt_right = st.columns(
    [1.1, 1],
    gap="large"
)

with apt_left:

    if livingroom:

        st.image(
            livingroom,
            caption="Living room",
            width="stretch"
        )


with apt_right:

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



# =========================================================
# CRETE & SEA SLIDESHOW
# =========================================================

st.divider()

st.markdown("**CRETE**")

st.header("The sea is part of the stay.")

sea_images = [
    ("Ammoudara beach", sea),
    ("The Cretan coastline", sea1),
    ("Sea view", seaview),
    ("Ammoudara by night", seabynight),
    ("Balcony", balcony),
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

    # Main slideshow image
    st.image(
        sea_image,
        caption=sea_name,
        width="stretch"
    )

    # Counter
    st.caption(
        f"{current_sea + 1} / {len(sea_images)}"
    )

    # Simple slideshow indicators
    indicator_text = ""

    for i in range(len(sea_images)):

        if i == current_sea:
            indicator_text += "━ "
        else:
            indicator_text += "• "

    st.write(indicator_text)

    # Navigation
    sea_prev, sea_space, sea_next = st.columns(
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
    """
    <div class="section-label">
        YOUR HOSTS
    </div>
    """,
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


r1, r2 = st.columns(2, gap="large")

with r1:

    st.markdown("★★★★★")

    st.write(
        """
        “The location was unbeatable. Waking up with
        a sea view made the whole trip feel special.
        The apartment was clean, comfortable and
        exactly as described.”
        """
    )

    st.caption("— Obada · Guest")


with r2:

    st.markdown("★★★★★")

    st.write(
        """
        “Very clean, quiet, with a large balcony and
        beautiful sea view. The beach and restaurants
        are just a short walk away.”
        """
    )

    st.caption("— Véronique · Guest")


# =========================================================
# GUEST REVIEWS
# =========================================================

st.divider()

st.markdown("**GUEST REVIEWS**")

st.header("What our guests say.")

r1, r2 = st.columns(2, gap="large")

with r1:

    st.markdown("★★★★★")

    st.write(
        """
        “The location was unbeatable. Waking up with
        a sea view made the whole trip feel special.
        The apartment was clean, comfortable and
        exactly as described.”
        """
    )

    st.caption("— Obada · Guest")


with r2:

    st.markdown("★★★★★")

    st.write(
        """
        “Very clean, quiet, with a large balcony and
        beautiful sea view. The beach and restaurants
        are just a short walk away.”
        """
    )

    st.caption("— Véronique · Guest")



# =========================================================
# LOCATION
# =========================================================

st.divider()

st.markdown(
    """
    <div class="section-label">
        LOCATION
    </div>
    """,
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
    """
    <div class="section-label">
        READY FOR CRETE?
    </div>
    """,
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

