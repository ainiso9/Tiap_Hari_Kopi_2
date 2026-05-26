import streamlit as st
import pandas as pd
import plotly.express as px
import PIL
import base64
import os

# --------------------------------------------------
# 1. SET PAGE CONFIG & TIAP HARI KOPI THEME CSS
# --------------------------------------------------
st.set_page_config(page_title="Tiap Hari Kopi", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Montserrat', sans-serif;
    background-color: #0b131f !important;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 5rem !important;
    max-width: 1200px !important;
}

/* NAVBAR STYLE */
.nk-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    border-bottom: 1px solid #1a2636;
    margin-bottom: 40px;
}
.nk-logo {
    color: #ffffff;
    font-weight: 800;
    font-size: 26px;
    letter-spacing: 2px;
}
.nk-logo span {
    color: #004481; /* Branded Logo Blue */
}
.nk-nav {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.5px;
    color: #92a4b8;
}

/* HERO BANNER TEXT */
.nk-hero-title {
    color: #ffffff;
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 10px;
    letter-spacing: -1px;
}
.nk-hero-subtitle {
    color: #004481; /* Branded Logo Blue */
    font-size: 18px;
    font-weight: 600;
    text-transform: uppercase;
    text-align: center;
    letter-spacing: 3px;
    margin-bottom: 50px;
}

/* CARDS */
.nk-card {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    height: 100%;
}

/* MENU COMPONENT STYLING */
.nk-menu-title {
    font-size: 18px;
    font-weight: 700;
    color: #111111;
    margin-top: 15px;
}
.nk-menu-cat {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    color: #888888;
    letter-spacing: 1px;
    margin-bottom: 10px;
}
.nk-menu-price {
    font-size: 18px;
    font-weight: 700;
    color: #ffffff; 
    background-color: #004481; /* Branded Logo Blue */
    display: inline-block;
    padding: 2px 12px;
    border-radius: 4px;
}

/* TAB ADJUSTMENTS */
.stTabs [data-baseweb="tab-list"] {
    background-color: #121e2e;
    padding: 8px;
    border-radius: 8px;
}
.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    color: #ffffff !important; 
    background-color: #004481; /* Branded Logo Blue */
    border-radius: 4px;
}

div.stButton > button {
    background-color: #004481 !important; /* Branded Logo Blue */
    color: #ffffff !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 28px !important;
    font-weight: 700 !important;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #003361 !important;
}

/* GOOGLE REVIEWS INTERFACE STYLING */
.google-review-card {
    background-color: #121e2e;
    border: 1px solid #1a2636;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    font-family: Roboto, Helvetica, Arial, sans-serif;
    color: #e8eaed;
    text-align: left;
}
.gr-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}
.gr-profile {
    display: flex;
    align-items: center;
    gap: 12px;
}
.gr-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
}
.gr-user-info {
    display: flex;
    flex-direction: column;
}
.gr-name {
    font-weight: 500;
    font-size: 14px;
    color: #e8eaed;
}
.gr-meta {
    font-size: 12px;
    color: #9aa0a6;
}
.gr-more-btn {
    color: #9aa0a6;
    font-size: 18px;
}
.gr-stars-row {
    display: flex;
    align-items: center;
    gap: 4px;
    margin-bottom: 8px;
}
.gr-stars {
    color: #fbbc05; 
    font-size: 14px;
}
.gr-time {
    font-size: 12px;
    color: #9aa0a6;
    margin-left: 4px;
}
.gr-badge {
    background-color: #1a2636;
    color: #e8eaed;
    font-size: 10px;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 4px;
    margin-left: 8px;
}
.gr-text {
    font-size: 14px;
    line-height: 1.46;
    color: #bdc1c6;
    margin-bottom: 12px;
}
.gr-images-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    margin-top: 12px;
    margin-bottom: 12px;
}
.gr-img {
    width: 100%;
    height: 70px;
    object-fit: cover;
    border-radius: 6px;
}
.gr-aspects {
    background-color: #0b131f;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 12px;
    color: #bdc1c6;
    margin-top: 8px;
    border: 1px solid #1a2636;
}
.gr-footer {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 12px;
    padding-top: 8px;
    border-top: 1px solid #1a2636;
    color: #9aa0a6;
    font-size: 13px;
}
.local-review-card {
    background-color: #162a45;
    border: 1px solid #1d3b61;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    color: #8ab4f8;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTION: BASE64 ENCODING ---
def get_b64_image(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            ext = img_path.split(".")[-1]
            return f"data:image/{ext};base64,{encoded}"
    return "https://via.placeholder.com/600x450"

# --- INITIALIZE STATE ARRAYS ---
if "total_reviews" not in st.session_state:
    st.session_state.total_reviews = 1259

if "customer_metrics" not in st.session_state:
    st.session_state.customer_metrics = {
        "First-Time Customer": 655,
        "Repeat Customer": 604
    }

# --- BRAND NAVIGATION HEADER ---
st.markdown("""
<div class="nk-header">
    <div class="nk-logo">TIAP HARI <span>KOPI</span></div>
    <div class="nk-nav">
        HOME &nbsp;&nbsp;&bull;&nbsp;&nbsp; 
        MENU &nbsp;&nbsp;&bull;&nbsp;&nbsp; 
        RESERVATIONS &nbsp;&nbsp;&bull;&nbsp;&nbsp; 
        FEEDBACK &nbsp;&nbsp;&bull;&nbsp;&nbsp; 
        ABOUT US &nbsp;&nbsp;&bull;&nbsp;&nbsp; 
        LOG IN
    </div>
</div>
""", unsafe_allow_html=True)

page_options = ["HOME + MENU", "RESERVATIONS", "FEEDBACK", "ABOUT US", "LOG IN"]
selected_route = st.radio(label="Active View", options=page_options, horizontal=True, label_visibility="collapsed")

# ==================================================
# CONDITIONAL RENDERING FRAMEWORK
# ==================================================

if selected_route == "HOME + MENU":
    st.markdown('<div class="nk-hero-title">Local Coffee, Premium Vibes.</div>', unsafe_allow_html=True)
    st.markdown('<div class="nk-hero-subtitle">Every Single Day Perfection</div>', unsafe_allow_html=True)

    # 1. Fetch targeted sliding graphics for Home hero banner
    home_images = [
        "images/tiapharibefore.jpg",
        "images/tiapharifront.jpg",
        "images/tiapharigrab.jpg",
        "images/tiapharibestdrinks.jpg"
    ]
    h_b64 = [get_b64_image(p) for p in home_images]

    # 2. Infinite Loop pure CSS Slider (Transitions every 1.5s, total timeline 6s)
    home_slider_html = f"""
    <style>
        .home-slider-wrapper {{
            width: 100%;
            max-width: 850px;
            margin: 0 auto 40px auto;
            overflow: hidden;
            border-radius: 16px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            background-color: #121e2e;
        }}
        .home-slider-track {{
            display: flex;
            width: 400%;
            animation: homeSlideLoop 6s cubic-bezier(0.85, 0, 0.15, 1) infinite;
        }}
        .home-slider-track img {{
            width: 25%;
            height: 480px;
            object-fit: cover;
        }}
        @keyframes homeSlideLoop {{
            0%, 20%   {{ transform: translateX(0); }}
            25%, 45%  {{ transform: translateX(-25%); }}
            50%, 70%  {{ transform: translateX(-50%); }}
            75%, 95%  {{ transform: translateX(-75%); }}
            100%      {{ transform: translateX(0); }}
        }}
    </style>
    <div class="home-slider-wrapper">
        <div class="home-slider-track">
            <img src="{h_b64[0]}">
            <img src="{h_b64[1]}">
            <img src="{h_b64[2]}">
            <img src="{h_b64[3]}">
        </div>
    </div>
    """
    st.components.v1.html(home_slider_html, height=500)

    st.markdown("<hr style='border-color: #1a2636; margin: 60px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#ffffff; font-weight:800; text-align:center;'>Explore Our Signature Menu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#92a4b8; margin-bottom:30px;'>Crafted to give you the perfect boost</p>", unsafe_allow_html=True)

    menu_items = [
        {"name": "Matcha Latte", "category": "Beverage", "price": 9, "image": "images/tiapharimatchalatte.jpg"},
        {"name": "Passion Soda", "category": "Beverage", "price": 8, "image": "images/tiapharipassionsoda.jpg"},
        {"name": "Iced Latte", "category": "Beverage", "price": 9, "image": "images/tiaphariicedlatte.jpg"},
        {"name": "Lotus Biscoff Cheese Tart", "category": "Dessert", "price": 12, "image": "images/biscoffcheesetart.jpg"},
        {"name": "Chocolate Cheese Tart", "category": "Dessert", "price": 12, "image": "images/choccheesetart.jpg"},
        {"name": "Chocolate Moise Belanda", "category": "Dessert", "price": 14, "image": "images/chocmoistbelanda.jpg"},
        {"name": "Mini Pavlova", "category": "Dessert", "price": 12, "image": "images/minipavlova.jpg"},
        {"name": "Strawberry Cheese Tart", "category": "Dessert", "price": 12, "image": "images/strawberrycheesetart.jpg"},
        {"name": "Fettucine Bolognese Meatballs", "category": "Western Food", "price": 15, "image": "images/fettucinebolognesemeatballs.jpg"},
        {"name": "Garlic Butter Fettucine", "category": "Western Food", "price": 15, "image": "images/garlicbutterseafoodfettucine.jpg"},
        {"name": "Crispy Veggie Cucur", "category": "Local Food", "price": 9, "image": "images/crispyveggiecucur.jpg"},
        {"name": "Veggie Spring Rolls", "category": "Local Food", "price": 9, "image": "images/veggiespringrolls.jpg"},
    ]

    filter_col1, filter_col2, filter_col3 = st.columns([1, 1.5, 1])
    with filter_col2:
        selected_category = st.selectbox("✨ Select Category to Explore:", options=["All Items", "Beverage", "Dessert", "Western Food", "Local Food"], index=0)

    filtered_items = menu_items if selected_category == "All Items" else [item for item in menu_items if item["category"] == selected_category]

    m_cols = st.columns(3, gap="large")
    for idx, item in enumerate(filtered_items):
        with m_cols[idx % 3]:
            try:
                st.image(item["image"], width=320)
            except Exception:
                st.image("https://via.placeholder.com/300x220", width=320)
                
            st.markdown(f"""
            <div class="nk-card" style="margin-top: -10px; border-top-left-radius: 0px; border-top-right-radius: 0px; margin-bottom: 30px;">
                <div class="nk-menu-cat">{item['category']}</div>
                <div class="nk-menu-title" style="margin-top: 5px; font-size:16px; color:#111111;">{item['name']}</div>
                <div style="margin-top: 15px;">
                    <div class="nk-menu-price">RM {item['price']:.2f}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif selected_route == "RESERVATIONS":
    st.markdown("<h3 style='color:#ffffff; font-weight:700; margin-bottom:20px;'>Secure Orders & Bookings</h3>", unsafe_allow_html=True)
    b_col1, b_col2 = st.columns(2, gap="large")
    with b_col1:
        st.markdown("""
        <div class="nk-card">
            <h4 style="color:#111111; font-weight:700;">📲 Reserve via WhatsApp</h4>
            <p style="color:#555555; font-size:14px;">Skip the queue! Book your table session seamlessly with our baristas online.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Book Table via WhatsApp", "https://wa.me/60123456789")
    with b_col2:
        st.markdown("""
        <div class="nk-card">
            <h4 style="color:#111111; font-weight:700;">🛵 Instant Grab Delivery</h4>
            <p style="color:#555555; font-size:14px;">Craving our local snacks or main courses? Hit the button below to buy on GrabFood.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Find Us On GrabFood", "https://r.grab.com/")

elif selected_route == "FEEDBACK":
    st.markdown("<h2 style='color: white; margin-bottom: 20px; text-align:center;'>Customer Feedback Hub</h2>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1.1, 0.9], gap="large")

    with col_left:
        st.markdown('<h3 style="color: white; margin-bottom: 20px;">What they say about us (Google Reviews)</h3>', unsafe_allow_html=True)
        
        # --- REVIEW 1: NurZetty Sofia ---
        st.markdown("""
        <div class="google-review-card">
            <div class="gr-header">
                <div class="gr-profile">
                    <img class="gr-avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100" alt="Avatar">
                    <div class="gr-user-info">
                        <span class="gr-name">NurZetty Sofia</span>
                        <span class="gr-meta">6 ulasan • 6 foto</span>
                    </div>
                </div>
                <div class="gr-more-btn">⋮</div>
            </div>
            <div class="gr-stars-row">
                <span class="gr-stars">★★★★★</span>
                <span class="gr-time">3 minggu yang lalu</span>
                <span class="gr-badge" style="background-color:#1a2636; color:#e8eaed; font-size:9px; padding:2px 5px; border-radius:3px;">BAHARU</span>
            </div>
            <div class="gr-text">
                Saya kenal TiapHari ni semenjak 2022. Speciality mmg Nisse Latte dan Kacang Phool. Walaupun KB ni byk kedai kopi, tp tak boleh lagi lawan Nisse latte TiapHari (ice/hot dua2 sedap) dan takde tempat lain nak cari kacang phool. Bukan tak ... <span style="color:#8ab4f8; cursor:pointer;">Lagi</span>
            </div>
            <div class="gr-images-grid">
                <img class="gr-img" src="images/tiapharibestdrinks.jpg" onerror="this.src='https://images.unsplash.com/photo-1541167760496-1628856ab772?w=150'">
                <img class="gr-img" src="images/tiaparipasta.jpg" onerror="this.src='https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=150'">
                <img class="gr-img" src="images/tiapharisnack.jpg" onerror="this.src='https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=150'">
                <img class="gr-img" src="images/tiapharikacangphool.jpg" onerror="this.src='https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=150'">
            </div>
            <div class="gr-footer">
                <div style="display:flex; align-items:center; gap:4px;">❤️ <span>1</span></div>
                <div>🔗</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # --- REVIEW 2 ---
        st.markdown("""
        <div class="local-review-card">
            <div style="display: flex; gap: 4px; margin-bottom: 4px; color: #fbbc05;">★★★★★</div>
            <span style="font-weight: bold; color: #8ab4f8;">Farhana</span> 
            <span style="color: #bdc1c6;">— Super friendly service. Perfect environment to chill out or focus on remote work. (Verified Website Feedback)</span>
        </div>
        """, unsafe_allow_html=True)

        # --- REVIEW 3: Isabella Anne ---
        st.markdown("""
        <div class="google-review-card">
            <div class="gr-header">
                <div class="gr-profile">
                    <img class="gr-avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100" alt="Avatar">
                    <div class="gr-user-info">
                        <span class="gr-name">Isabella Anne</span>
                        <span class="gr-meta">Jurupandu Tempatan • 36 ulasan • 23 foto</span>
                    </div>
                </div>
                <div class="gr-more-btn">⋮</div>
            </div>
            <div class="gr-stars-row">
                <span class="gr-stars">★★★★★</span>
                <span class="gr-time">4 bulan yang lalu</span>
            </div>
            <div class="gr-text">
                Good food , just parking abit hard
                <div class="gr-aspects">
                    <b>Makanan:</b> 5/5  |  <b>Perkhidmatan:</b> 5/5  |  <b>Suasana:</b> 5/5
                </div>
                <span style="font-size:12px; color:#8ab4f8; cursor:pointer; margin-top:5px; display:inline-block;">Lihat terjemahan (Melayu)</span>
            </div>
            <div class="gr-footer">
                <div style="display:flex; align-items:center; gap:4px;">❤️ <span>1</span></div>
                <div>🔗</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown('<h3 style="color: white; margin-bottom: 20px;">Share your feedback</h3>', unsafe_allow_html=True)
        cust_name = st.text_input("Customer Name", placeholder="Enter name")
        cust_type = st.radio("✨ Is this your first time visiting Tiap Hari Kopi?", options=["First-Time Customer", "Repeat Customer"], horizontal=True)
        st.write("⭐ Rate your experience:")
        cust_stars = st.feedback("stars", key="feedback_stars")
        cust_text = st.text_area("Your Review", placeholder="Write something...", height=120)
        
        if st.button("Post Live Feedback"):
            if cust_name and cust_text:
                st.session_state.total_reviews += 1
                st.success("✨ Thank you for your feedback! It helps us grow.")
            else:
                st.error("Please fill in both your name and review text before submitting.")

elif selected_route == "ABOUT US":
    st.markdown("<h3 style='color:#ffffff; font-weight:700; margin-bottom:20px;'>About Us</h3>", unsafe_allow_html=True)
    st.info("Every single cup carries raw passion, home comfort, and a little bit of daily happiness.")

    st.markdown("<hr style='border-color: #1a2636; margin: 40px 0;'>", unsafe_allow_html=True)
    st.header("📸 Gallery and Our Story")

    slider_images = [
        "images/tiapharibefore.jpg",
        "images/tiapharifront.jpg",
        "images/tiapharigrab.jpg",
        "images/tiapharibestdrinks.jpg",
        "images/tiapharipasta.jpg",
        "images/tiapharisnack.jpg",
        "images/tiapharikacangphool.jpg",
        "images/veggiespringrolls.jpg",      
        "images/crispyveggiecucur.jpg"       
    ]

    b64_srcs = [get_b64_image(p) for p in slider_images]

    slider_html = f"""
    <style>
        .slider-container {{
            width: 100%;
            overflow: hidden;
            border-radius: 12px;
            background-color: #0b131f;
            padding: 15px 0;
        }}
        .slider-track {{
            display: flex;
            width: 300%; 
            gap: 16px;
            padding-left: 8px;
            padding-right: 8px;
            box-sizing: border-box;
            animation: slide-9-images 6s ease-in-out infinite; 
        }}
        .slider-track:hover {{
            animation-play-state: paused;
        }}
        .slider-track img {{
            width: calc(33.333vw - 22px); 
            height: 280px;
            object-fit: cover;
            border-radius: 8px;
            flex-shrink: 0;
        }}
        @keyframes slide-9-images {{
            0%, 25% {{ transform: translateX(0); }}
            33%, 58% {{ transform: translateX(calc(-100vw + 8px)); }}
            66%, 91% {{ transform: translateX(calc(-200vw + 16px)); }}
            100% {{ transform: translateX(0); }}
        }}
    </style>
    <div class="slider-container">
        <div class="slider-track">
            <img src="{b64_srcs[0]}">
            <img src="{b64_srcs[1]}">
            <img src="{b64_srcs[2]}">
            
            <img src="{b64_srcs[3]}">
            <img src="{b64_srcs[4]}">
            <img src="{b64_srcs[5]}">
            
            <img src="{b64_srcs[6]}">
            <img src="{b64_srcs[7]}">
            <img src="{b64_srcs[8]}">
        </div>
    </div>
    """
    st.components.v1.html(slider_html, height=315)

    st.markdown("""
    <div style='background-color:#004481; color:#ffffff; padding:20px; border-radius:15px; margin-top:25px; text-align:center; font-size:16px; font-weight:600;'>
        ✨ Our journey started from a small idea and grew into a cozy café loved by many. <br>
        Every cup of coffee we serve carries passion, comfort, and a little bit of happiness ☕💛
    </div>
    """, unsafe_allow_html=True)
    
elif selected_route == "LOG IN":
    st.markdown("<h2 style='color:#ffffff; font-weight:800; text-align:center;'>🔒 Internal Portal & Analytics</h2>", unsafe_allow_html=True)
    
    tab_metrics, tab_login = st.tabs(["📊 Business Metrics & Sentiment", "🔑 Staff Login Portal"])
    
    with tab_metrics:
        d_col1, d_col2 = st.columns([1, 1.2], gap="large")
        with d_col1:
            st.metric("Total Shared Reviews", f"{st.session_state.total_reviews:,}")
            total_counted = sum(st.session_state.customer_metrics.values())
            repeat_pct = (st.session_state.customer_metrics["Repeat Customer"] / total_counted) * 100
            st.metric("Returning Visitors Rate", f"{repeat_pct:.1f}%")
            st.metric("Average Rating", "4.9 / 5.0")
            
        with d_col2:
            chart_df = pd.DataFrame({
                "Customer Type": list(st.session_state.customer_metrics.keys()),
                "Count": list(st.session_state.customer_metrics.values())
            })
            fig = px.pie(chart_df, values="Count", names="Customer Type", title="Customer Demographics Breakdown", color_discrete_sequence=["#004481", "#ffffff"])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#ffffff', height=280, margin=dict(t=50, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
            
    with tab_login:
        st.warning("Secure Portal Access - Cloud verification active.")
        st.text_input("Staff Email ID", placeholder="barista@tiapharikopi.com")
        st.text_input("Access Password", type="password", placeholder="••••••••")
        st.button("Authenticate & Log In")

# ==================================================
# FOOTER SECTION
# ==================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---") 

f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.markdown("### TIAP HARI KOPI")
    st.caption("Every single cup carries raw passion, home comfort, and a little bit of daily happiness. ☕💛")

with f_col2:
    st.markdown("📍 **Visit Our Hub**")
    st.caption("Lot 2046, Kampung Gok Bata,\nJalan Raja Perempuan Zainab II,\n16150 Kota Bharu, Kelantan.")

with f_col3:
    st.markdown("🔗 **Connect With Us**")
    st.markdown("[🌐 Facebook](https://facebook.com)")
    st.markdown("[📸 Instagram](https://instagram.com)")

st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.3); font-size: 0.8rem; margin-top: 40px;'>© 2026 Tiap Hari Kopi Enterprise. All Rights Reserved. | Inspired by Nasken Modern Template</p>", unsafe_allow_html=True)