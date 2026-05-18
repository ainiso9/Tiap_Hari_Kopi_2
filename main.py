import streamlit as st
import pandas as pd
import plotly.express as px
import PIL

# --------------------------------------------------
# 1. SET PAGE CONFIG & TIAP HARI KOPI THEME CSS
# --------------------------------------------------
st.set_page_config(page_title="Tiap Hari Kopi", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Montserrat', sans-serif;
    background-color: #121212 !important;
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
    border-bottom: 1px solid #222222;
    margin-bottom: 40px;
}
.nk-logo {
    color: #ffffff;
    font-weight: 800;
    font-size: 26px;
    letter-spacing: 2px;
}
.nk-logo span {
    color: #ffc107; 
}
.nk-nav {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1.5px;
    color: #b3b3b3;
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
    color: #ffc107;
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
    color: #ffc107;
    background-color: #111111;
    display: inline-block;
    padding: 2px 12px;
    border-radius: 4px;
}

/* OVERRIDE STREAMLIT SELECTION WORKFLOW */
.stTabs [data-baseweb="tab-list"] {
    background-color: #1a1a1a;
    padding: 8px;
    border-radius: 8px;
}
.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    color: #ffc107 !important;
    background-color: #262626;
    border-radius: 4px;
}

div.stButton > button {
    background-color: #ffc107 !important;
    color: #111111 !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 28px !important;
    font-weight: 700 !important;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #e0a800 !important;
}

.map-container {
    border: 2px solid #222222;
    border-radius: 12px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INITIALIZE STATE-BASED REACTION ARRAYS
# --------------------------------------------------
if "total_reviews" not in st.session_state:
    st.session_state.total_reviews = 1259

if "customer_metrics" not in st.session_state:
    st.session_state.customer_metrics = {
        "First-Time Customer": 655,
        "Repeat Customer": 604
    }

# --------------------------------------------------
# 2. BRAND NAVIGATION HEADER
# --------------------------------------------------
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

# --------------------------------------------------
# 3. CONTROLLER ROUTER
# --------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "HOME + MENU"

page_options = ["HOME + MENU", "RESERVATIONS", "FEEDBACK", "ABOUT US", "LOG IN"]

selected_route = st.radio(
    label="Active View", 
    options=page_options, 
    horizontal=True, 
    label_visibility="collapsed"
)
st.session_state.current_page = selected_route

# ==================================================
# CONDITIONAL RENDERING FRAMEWORK
# ==================================================

# --- PAGE VALUE: HOME + MENU ---
if st.session_state.current_page == "HOME + MENU":
    st.markdown('<div class="nk-hero-title">Local Coffee, Premium Vibes.</div>', unsafe_allow_html=True)
    st.markdown('<div class="nk-hero-subtitle">Every Single Day Perfection</div>', unsafe_allow_html=True)

    col_img1, col_img2 = st.columns([1, 1], gap="large")
    SQUARE_SIZE = 400 

    with col_img1:
        try:
            img1 = PIL.Image.open("images/tiapharifront.jpg")
            w, h = img1.size
            min_dim = min(w, h)
            img1_cropped = img1.crop(((w - min_dim) / 2, (h - min_dim) / 2, (w + min_dim) / 2, (h + min_dim) / 2))
            st.image(img1_cropped.resize((SQUARE_SIZE, SQUARE_SIZE), PIL.Image.Resampling.LANCZOS), caption="Every Single Day Perfection", width="stretch")
        except Exception:
            st.image("https://via.placeholder.com/400", caption="Every Single Day Perfection", width="stretch")

    with col_img2:
        try:
            img2 = PIL.Image.open("images/tiapharibestdrinks.jpg")
            w, h = img2.size
            min_dim = min(w, h)
            img2_cropped = img2.crop(((w - min_dim) / 2, (h - min_dim) / 2, (w + min_dim) / 2, (h + min_dim) / 2))
            st.image(img2_cropped.resize((SQUARE_SIZE, SQUARE_SIZE), PIL.Image.Resampling.LANCZOS), caption="Your Cozy Space", width="stretch")
        except Exception:
            st.image("https://via.placeholder.com/400", caption="Your Cozy Space", width="stretch")

    st.markdown("<hr style='border-color: #222; margin: 60px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#ffffff; font-weight:800; text-align:center;'>Explore Our Signature Menu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888888; margin-bottom:30px;'>Crafted to give you the perfect boost</p>", unsafe_allow_html=True)

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
                st.image(item["image"], width="stretch")
            except Exception:
                st.image("https://via.placeholder.com/300x220", width="stretch")
                
            st.markdown(f"""
            <div class="nk-card" style="margin-top: -10px; border-top-left-radius: 0px; border-top-right-radius: 0px; margin-bottom: 30px;">
                <div class="nk-menu-cat">{item['category']}</div>
                <div class="nk-menu-title" style="margin-top: 5px; font-size:16px; color:#111111;">{item['name']}</div>
                <div style="margin-top: 15px;">
                    <div class="nk-menu-price">RM {item['price']:.2f}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 🌟 FIXED: MOVED NEWS & PROMOTIONS SLIDER HERE SO IT ONLY RUNS INSIDE HOME + MENU
    st.markdown("<hr style='border-color: #222; margin: 60px 0;'>", unsafe_allow_html=True)
    st.header("📢 News and Promotions")

    slider_images = [
        "images/tiapharibestdrinks.jpg",
        "images/tiapharipasta.jpg",
        "images/tiapharisnack.jpg",
        "images/tiapharikacangphool.jpg"
    ]

    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    nav1, nav2, nav3 = st.columns([1, 6, 1])
    with nav1:
        if st.button("⬅️"):
            st.session_state.img_index -= 1
            if st.session_state.img_index < 0:
                st.session_state.img_index = 0
    with nav3:
        if st.button("➡️"):
            st.session_state.img_index += 1
            if st.session_state.img_index > len(slider_images) - 3:
                st.session_state.img_index = len(slider_images) - 3

    start = st.session_state.img_index
    end = start + 3
    slider_cols = st.columns(3)

    for i, img_path in enumerate(slider_images[start:end]):
        with slider_cols[i]:
            try:
                st.image(img_path, width="stretch")
            except:
                st.image("https://via.placeholder.com/300x200", width="stretch")

    st.markdown(f"""
    <div style='
        background-color:#0047AB;
        color:white;
        padding:20px;
        border-radius:15px;
        margin-top:15px;
        text-align:center;
        font-size:16px;
    '>
        ✨ Come and grab a cup of coffee to start your day. Fresh brew with every order. <br>
        Every cup of coffee we serve carries passion, comfort, and a little bit of happiness ☕💙
    </div>
    """, unsafe_allow_html=True)

# --- STANDALONE PAGE: RESERVATIONS ---
elif st.session_state.current_page == "RESERVATIONS":
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

# --- STANDALONE PAGE: FEEDBACK ---
elif st.session_state.current_page == "FEEDBACK":
    st.markdown("<h3 style='color:#ffffff; font-weight:700; margin-bottom: 25px;'>Customer Feedback Hub</h3>", unsafe_allow_html=True)
    f_col1, f_col2 = st.columns(2, gap="large")
    
    with f_col1:
        st.markdown("<h4 style='color:white;'>What they say about us</h4>", unsafe_allow_html=True)
        st.info("⭐⭐⭐⭐⭐ Ariff — Perfect atmosphere to study and grab local tarts. (Repeat Customer)")
        st.info("⭐⭐⭐⭐⭐ Jane — Strong espresso blends. Highly recommended! (First-Time Customer)")
        st.info("⭐⭐⭐⭐⭐ Hafizuddin — Always hang out here with my friends, the staff is so friendly! (Repeat Customer)")
        st.info("⭐⭐⭐⭐ Mark Adam — Very affordable price but the parking space is too small. (First-Time Customer)")

    with f_col2:
        st.markdown("<h4 style='color:white;'>Share your feedback</h4>", unsafe_allow_html=True)
        cust_name = st.text_input("Customer Name", placeholder="Enter name")
        
        cust_type = st.radio(
            "✨ Is this your first time visiting Tiap Hari Kopi?",
            options=["First-Time Customer", "Repeat Customer"],
            horizontal=True
        )
        
        st.write("⭐ Rate your experience:")
        cust_stars = st.feedback("stars", key=f"stars_rating_{st.session_state.total_reviews}")
        cust_text = st.text_area("Your Review", placeholder="Write something...")
        
        if st.button("Post Live Feedback"):
            if cust_name and cust_text:
                st.session_state.total_reviews += 1
                st.session_state.customer_metrics[cust_type] += 1
                star_score = (cust_stars + 1) if cust_stars is not None else 5
                st.success(f"Thank you {cust_name}! Your {star_score}-star feedback was successfully recorded.")
                st.rerun()
            else:
                st.error("Please fill up both your name and review text before posting!")

# --- STANDALONE PAGE: ABOUT US ---
elif st.session_state.current_page == "ABOUT US":
    st.markdown("<h3 style='color:#ffffff; font-weight:700; margin-bottom:20px;'>About Us</h3>", unsafe_allow_html=True)
    st.info("Insert your 'About Us' content details here.")

    # ==================================================
    # GALLERY SLIDER (RESTORED EXACTLY AS IT WAS)
    # ==================================================
    st.markdown("<hr style='border-color: #222; margin: 60px 0;'>", unsafe_allow_html=True)
    st.header(" Gallery and Our Story ")

    images = [
        "images/tiapharibefore.jpg",
        "images/tiaphariopen.jpg",
        "images/tiapharibestdrinks.jpg",
        "images/tiapharipasta.jpg",
        "images/tiapharisnack.jpg",
        "images/tiapharikacangphool.jpg"
    ]

    # Initialize slider index
    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    # Buttons
    nav1, nav2, nav3 = st.columns([1,6,1])

    with nav1:
        if st.button("⬅️"):
            st.session_state.img_index -= 1
            if st.session_state.img_index < 0:
                st.session_state.img_index = 0

    with nav3:
        if st.button("➡️"):
            st.session_state.img_index += 1
            if st.session_state.img_index > len(images) - 3:
                st.session_state.img_index = len(images) - 3

    # Show 3 images
    start = st.session_state.img_index
    end = start + 3

    cols = st.columns(3)

    for i, img_path in enumerate(images[start:end]):
        with cols[i]:
            try:
                st.image(img_path, width="stretch")
            except:
                st.image("https://via.placeholder.com/300x200", width="stretch")

    st.markdown(f"""
    <div style='
        background-color:#0047AB;
        color:white;
        padding:20px;
        border-radius:15px;
        margin-top:15px;
        text-align:center;
        font-size:16px;
    '>
        ✨ Our journey started from a small idea and grew into a cozy café loved by many. <br>
        Every cup of coffee we serve carries passion, comfort, and a little bit of happiness ☕💙
    </div>
    """, unsafe_allow_html=True)

# --- STANDALONE PAGE: LOG IN ---
elif st.session_state.current_page == "LOG IN":
    st.markdown("<h2 style='color:#ffffff; font-weight:800; text-align:center;'>🔒 Internal Portal & Analytics</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888888; margin-bottom:40px;'>Administrative tools & live restaurant insights.</p>", unsafe_allow_html=True)
    
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
            fig = px.pie(chart_df, values="Count", names="Customer Type", title="Customer Demographics Breakdown", color_discrete_sequence=["#ffc107", "#ffffff"])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#ffffff', height=280, margin=dict(t=50, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
            
    with tab_login:
        st.warning("Secure Portal Access - Cloud verification active.")
        st.text_input("Staff Email ID", placeholder="barista@tiapharikopi.com")
        st.text_input("Access Password", type="password", placeholder="••••••••")
        st.button("Authenticate & Log In")


# ==================================================
# CLEAN FOOTER SECTION (RUNS ON ALL PAGES SAFELY)
# ==================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")  # Elegant layout divider line

# 3-column layout built out of core Streamlit modules (unbreakable)
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

# Clean, simple center aligned metadata alignment string
st.markdown(
    "<p style='text-align: center; color: rgba(255,255,255,0.3); font-size: 0.8rem; margin-top: 40px;'>"
    "© 2026 Tiap Hari Kopi Enterprise. All Rights Reserved. | Inspired by Nasken Modern Template"
    "</p>", 
    unsafe_allow_html=True
)