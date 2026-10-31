


import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="ECFC Houston Outreach Ministry App",
    page_icon="Screenshot_20261026_112519_ChatGPT.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Login protection
if not st.session_state.get("logged_in", False):
    st.image("Screenshot_20261026_112519_ChatGPT.jpg", width=220)
    st.title("🔐 ECFC Houston Outreach Ministry")
    password = st.text_input("የመግቢያ የይለፍ ቃል", type="password")

    if st.button("ግባ / Login"):
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("የይለፍ ቃሉ ትክክል አይደለም።")

    st.stop()

# Custom CSS for Styling with ECFC Houston Colors
st.markdown("""
<style>
   div[style*="background-color: white"],
div[style*="background-color: #fff"],
div[style*="background-color: #f8f9fa"] {
    color: #111111 !important;
} 
.main-title {
        color: #102B52;
        font-size: 2.2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #D4AF37;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 600;
    }
    .card {
        background-color: #f8f9fa;
        color: #111111 !important;
        border-radius: 10px;
        padding: 18px;
        border-left: 5px solid #102B52;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .gold-card {
        background-color: #fffdf5;
        border-radius: 10px;
        padding: 18px;
        border-left: 5px solid #D4AF37;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #102B52;
    }
    .metric-label {
        color: #555;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='main-title'>✝️ ECFC Houston Outreach Ministry</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>የአውትሪች አገልግሎት መከታተያ እና ማስተባበሪያ መተግበሪያ (App)</div>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("ECFC Houston Outreach Ministry")
st.sidebar.markdown("**የአገልግሎት ክፍሎችና ሞጁሎች**")

menu = st.sidebar.radio(
    "መኑ (Navigation):",
    [
        "📊 ዋና ዳሽቦርድ (Overview)",
        "🏛️ የአምስቱ ክፍሎች መዋቅር (5 Departments)",
        "🔄 የወንጌል ስርጭት ሂደት (4-Step Workflow)",
        "👥 የክትትልና የአዲሶች መዝገብ (Follow-Up Register)",
        "📝 የጸሎት ጥያቄዎች (Prayer Requests)",
        "📑 ሪፖርትና ግምገማ (Reports & Leadership)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("📌 **ECFC Houston Texas**\n\nየአውትሪች አገልግሎት አስተባባሪ አፕሊኬሽን")

# Initialize Session State Data if not present
if 'visitors' not in st.session_state:
    st.session_state.visitors = pd.DataFrame([
        {"መታወቂያ": "V-101", "ሙሉ ስም": "ዮሐንስ ተስፋዬ", "ስልክ": "832-555-0142", "የተመሰከረበት ቀን": "2026-10-20", "የመጣበት ቦታ": "Houston Downtown", "የተመደበ የክትትል አገልጋይ": "ዳንኤል ከበደ", "ደረጃ (Status)": "በስልክ ተደውሏል"},
        {"መታወቂያ": "V-102", "ሙሉ ስም": "ማርታ አለሙ", "ስልክ": "713-555-0188", "የተመሰከረበት ቀን": "2026-10-25", "የመጣበት ቦታ": "Galleria Area", "የተመደበ የክትትል አገልጋይ": "ሳራ መኮንን", "ደረጃ (Status)": "አዲስ መረጃ ተቀብሏል"},
        {"መታወቂያ": "V-103", "ሙሉ ስም": "ሳሙኤል በቀለ", "ስልክ": "281-555-0199", "የተመሰከረበት ቀን": "2026-10-27", "የመጣበት ቦታ": "Sugar Land", "የተመደበ የክትትል አገልጋይ": "ዮሴፍ ታደሰ", "ደረጃ (Status)": "ከትምህርት ጋር ተያይዟል"}
    ])

if 'prayers' not in st.session_state:
    st.session_state.prayers = pd.DataFrame([
        {"ቀን": "2026-10-22", "የተጠየቀው አካል/ርዕስ": "ስለ አዲስ አማኞች ጽናት", "የጸሎት አይነት": "የመውጣት በፊት ጸሎት", "ሁኔታ": "በጸሎት ላይ"},
        {"ቀን": "2026-10-25", "የተጠየቀው አካል/ርዕስ": "ለማርታ አለሙ የጤና ጸሎት", "የጸሎት አይነት": "የክትትል ጸሎት", "ሁኔታ": "ምስክርነት ተገኝቷል"}
    ])

# MODULE 1: OVERVIEW DASHBOARD
if menu == "📊 ዋና ዳሽቦርድ (Overview)":
    st.header("📊 የኪነ-አገልግሎት ዋና ዳሽቦርድ")
    st.caption("በ ECFC Houston Outreach Ministry መዋቅር መሰረት የተዘጋጀ")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='card'><div class='metric-value'>5</div><div class='metric-label'>የተደራጁ ክፍሎች</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><div class='metric-value'>3</div><div class='metric-label'>በክትትል ላይ ያሉ አዲሶች</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><div class='metric-value'>2</div><div class='metric-label'>የጸሎት ጥያቄዎች</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='card'><div class='metric-value'>100%</div><div class='metric-label'>የክፍላት ቅንጅት</div></div>", unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("🎯 የ 5ቱ አገልግሎት ክፍሎች ፈጣን ሁኔታ")
        dept_status = pd.DataFrame([
            {"ክፍል": "1. የጸሎት ቡድን (Prayer)", "የመሪ ስም": "የጸሎት ቡድን መሪ", "ዋና ተግባር": "የጸሎት ጥያቄዎችን መሰብሰብና መጸለይ", "ሁኔታ": "🟢 ዝግጁ"},
            {"ክፍል": "2. የወንጌል ስርጭት (Evangelism)", "የመሪ ስም": "የወንጌል ስርጭት መሪ", "ዋና ተግባር": "መውጣት፣ ወንጌል ማካፈልና መጋበዝ", "ሁኔታ": "🟢 ንቁ"},
            {"ክፍል": "3. የክትትል ቡድን (Follow-Up)", "የመሪ ስም": "የክትትል ቡድን መሪ", "ዋና ተግባር": "መደወል፣ መጎብኘትና ከትምህርት ጋር ማገናኘት", "ሁኔታ": "🟢 በስራ ላይ"},
            {"ክፍል": "4. እንግዳ ተቀባይነትና መጓጓዣ", "የመሪ ስም": "የኢንቨንተሪ/ትራንስፖርት መሪ", "ዋና ተግባር": "ቦታ፣ ትራንስፖርትና ቁሳቁስ ማዘጋጀት", "ሁኔታ": "🟢 ዝግጁ"},
            {"ክፍል": "5. ሚዲያና ግንኙነት (Media)", "የመሪ ስም": "የሚዲያ መሪ", "ዋና ተግባር": "ማስታወቂያ፣ ፎቶ/ምስክርነትና ውጤት ማሳየት", "ሁኔታ": "🟢 ዝግጁ"}
        ])
        st.table(dept_status)

    with col_right:
        st.subheader("👑 የአመራር ተዋረድ (Leadership Hierarchy)")
        st.markdown("""
        <div class='gold-card'>
        <b>1. የቤተክርስቲያን አመራር</b><br>
        └─ <b>2. ዋና አስተናጋጅ (Coordinator)</b><br>
        &nbsp;&nbsp;&nbsp;&nbsp;├─ <b>ምክትል አስተናጋጅ (Assistant)</b><br>
        &nbsp;&nbsp;&nbsp;&nbsp;├─ <b>ጸሐፊ / መዝገብ ያዥ (Secretary)</b><br>
        &nbsp;&nbsp;&nbsp;&nbsp;└─ <b>የ 5ቱ ቡድን መሪዎች</b> (የየክፍሉ አገልጋዮች)
        </div>
        """, unsafe_allow_html=True)

# MODULE 2: 5 DEPARTMENTS
elif menu == "🏛️ የአምስቱ ክፍሎች መዋቅር (5 Departments)":
    st.header("🏛️ የአምስቱ አገልግሎት ክፍሎች ዝርዝር መዋቅርና ተግባራት")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. ጸሎት (Prayer)", 
        "2. ወንጌል ስርጭት (Evangelism)", 
        "3. ክትትል (Follow-Up)", 
        "4. እንግዳና መጓጓዣ (Hospitality)", 
        "5. ሚዲያ (Media)"
    ])

    with tab1:
        st.subheader("🙏 1. የጸሎት ቡድን (Prayer Team)")
        st.markdown("""
        * **ዋና ተግባራት:**
          1. የጸሎት ጥያቄዎችን መሰብሰብ
          2. ከወጣቱ/ቡድኑ ጋር ከመውጣት በፊት በጋራ መጸለይ
          3. ለተገኙ ሰዎችና ለክትትል ቡድኑ አባላት መጸለይ
          4. የጸሎት ምስክርነቶችን መመዝገብ
        * **ከሌሎች ጋር የሚያணைበው መስመር:** ከመውጣት በፊት ከወንጌል ስርጭት ጋር፤ በጸሎት ጥያቄዎች ከክትትል ጋር።
        """)

    with tab2:
        st.subheader("📢 2. የወንጌል ስርጭት ቡድን (Evangelism Team)")
        st.markdown("""
        * **ዋና ተግባራት:**
          1. የመውጫ ቦታና ዓላማ መወሰን
          2. ወንጌልን ማካፈልና ሰዎችን መጋበዝ
          3. የክትትል ፈቃደኝነት መገናኛ (ስም/ስልክ) መመዝገብ
          4. መረጃውን ለክትትል ቡድን ማስተላለፍ
        * **ከሌሎች ጋር የሚያணைበው መስመር:** ከጸሎት ቡድን ጋር በዝግጅት፤ ከትራንስፖርት ጋር በትራንስፖርት፤ ከክትትል ጋር በመረጃ።
        """)

    with tab3:
        st.subheader("🤝 3. የክትትል ቡድን (Follow-Up Team)")
        st.markdown("""
        * **ዋና ተግባራት:**
          1. የተላከውን መረጃ መቀበል
          2. በተስማሙበት ጊዜ መደወልና መጎብኘት
          3. ማበረታታትና ለጸሎት ማገናኘት
          4. ከቤተክርስቲያን ትምህርት/ህብረት ጋር ማገናኘት
        * **ከሌሎች ጋር የሚያணைበው መስመር:** ከወንጌል ስርጭት መረጃ ይቀበላል፤ ለጸሐፊውና ለአስተናጋጁ ውጤት ያሳውቃል።
        """)

    with tab4:
        st.subheader("🚗 4. እንግዳ ተቀባይነትና መጓጓዣ (Hospitality & Logistics)")
        st.markdown("""
        * **ዋና ተግባራት:**
          1. ቦታና የተቀባይ አካል ግንኙነት ማረጋገጥ
          2. መጓጓዣና የመመለሻ ሰዓት ማዘጋጀት
          3. እቃዎችና የእርዳታ ዝግጅት ማሟላት
          4. ወጪና ደረሰኝ መመዝገብና ማቅረብ
        * **ከሌሎች ጋር የሚያணைበው መስመር:** ከወንጌል ስርጭት እና ሚዲያ ጋር በቦታና በቁሳቁስ ዝግጅት።
        """)

    with tab5:
        st.subheader("📸 5. ሚዲያ እና ግንኙነት (Media & Communications)")
        st.markdown("""
        * **ዋና ተግባራት:**
          1. ማስታወቂያና ጥሪ መልእክት ማዘጋጀት
          2. ቀን፣ ሰዓትና ቦታን ማረጋገጥ
          3. ፎቶና ምስክርነት በፈቃድ መቅረጽ
          4. የአገልግሎቱን ውጤት ለማሳየት ማዘጋጀት
        * **ከሌሎች ጋር የሚያணைበው መስመር:** ከሁሉም ክፍሎች መረጃ በመቀበል ማስታወቂያና ምስክርነት ያዘጋጃል።
        """)

# MODULE 3: 4-STEP WORKFLOW
elif menu == "🔄 የወንጌል ስርጭት ሂደት (4-Step Workflow)":
    st.header("🔄 የአንድ የወንጌል ስርጭት ተግባር 4 ደረጃዎች")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h4>ደረጃ 1: እቅድና ዝግጅት</h4>
        <p><b>ተሳታፊ:</b> አስተናጋጅ + ቡድን መሪዎች</p>
        <p>ቀን፣ ቦታ፣ ትራንስፖርትና የጸሎት ጊዜ መወሰን።</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
        <h4>ደረጃ 2: መውጣትና መጋበዝ</h4>
        <p><b>ተሳታፊ:</b> የወንጌል ስርጭት ቡድን</p>
        <p>ወንጌል ማካፈል፣ መገናኛ መመዝገብና ሰዎችን መጋበዝ።</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card'>
        <h4>ደረጃ 3: የሰዎች ክትትል</h4>
        <p><b>ተሳታፊ:</b> የክትትል ቡድን</p>
        <p>መደወል፣ መጎብኘት፣ መጸለይና ወደ ትምህርት ማምጣት።</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class='card'>
        <h4>ደረጃ 4: ሪፖርትና ግምገማ</h4>
        <p><b>ተሳታፊ:</b> ጸሐፊ + አስተናጋጅ</p>
        <p>ውጤትን መገምገም፣ ሪፖርት ማጠናቀርና ማቅረብ።</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📋 የቀጥታ ስርጭት / የኢቨንት ሂደት መከታተያ")
    event_name = st.text_input("የኢቨንቱ/የወንጌል ስርጭቱ ስም:", "የኦክቶበር ወር የከተማ ውስጥ አውትሪች")
    status_step = st.select_slider(
        "የአሁኑ የኢቨንት ደረጃ:",
        options=["1. እቅድና ዝግጅት", "2. መውጣትና መጋበዝ", "3. የሰዎች ክትትል", "4. ሪፖርትና ግምገማ"]
    )
    st.success(f"**{event_name}** በአሁኑ ወቅት በ **{status_step}** ላይ ይገኛል።")

# MODULE 4: FOLLOW-UP REGISTER
elif menu == "👥 የክትትልና የአዲሶች መዝገብ (Follow-Up Register)":
    st.header("👥 የአዲስ አማኞች እና የተመሰከረላቸው ሰዎች መዝገብ")
    
    st.dataframe(st.session_state.visitors, use_container_width=True)

    st.markdown("---")
    st.subheader("➕ አዲስ ሰው መመዝገቢያ ቅጽ")
    
    with st.form("add_visitor_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            name = st.text_input("ሙሉ ስም:")
            phone = st.text_input("ስልክ ቁጥር:")
            location = st.text_input("የመጣበት / የተገናኘበት ቦታ:")
        with col_b:
            date_found = st.date_input("የተመሰከረበት ቀን:", datetime.now())
            assigned_to = st.text_input("የተመደበ የክትትል አገልጋይ:")
            status = st.selectbox("ደረጃ (Status):", ["አዲስ መረጃ ተቀብሏል", "በስልክ ተደውሏል", "ተጎብኝቷል", "ከትምህርት ጋር ተያይዟል"])
            
        submitted = st.form_submit_button("💾 መዝግብ")
        if submitted and name:
            new_id = f"V-10{len(st.session_state.visitors) + 1}"
            new_row = {
                "መታወቂያ": new_id,
                "ሙሉ ስም": name,
                "ስልክ": phone,
                "የተመሰከረበት ቀን": str(date_found),
                "የመጣበት ቦታ": location,
                "የተመደበ የክትትል አገልጋይ": assigned_to,
                "ደረጃ (Status)": status
            }
            st.session_state.visitors = pd.concat([st.session_state.visitors, pd.DataFrame([new_row])], ignore_index=True)
            st.success(f"አዲስ ሰው {name} በስኬት ተመዝግቧል!")
            st.rerun()

# MODULE 5: PRAYER REQUESTS
elif menu == "📝 የጸሎት ጥያቄዎች (Prayer Requests)":
    st.header("📝 የጸሎት ጥያቄዎች መከታተያ")
    
    st.table(st.session_state.prayers)
    
    st.markdown("---")
    st.subheader("➕ አዲስ የጸሎት ጥያቄ አስገባ")
    with st.form("prayer_form"):
        p_title = st.text_input("የተጠየቀው አካል / የጸሎት ርዕስ:")
        p_type = st.selectbox("የጸሎት አይነት:", ["የመውጣት በፊት ጸሎት", "የክትትል ጸሎት", "የአገልጋዮች ጸሎት", "የህሙማን ጸሎት"])
        p_submit = st.form_submit_button("🙏 የጸሎት ጥያቄ መዝግብ")
        if p_submit and p_title:
            new_p = {
                "ቀን": str(datetime.now().strftime("%Y-%m-%d")),
                "የተጠየቀው አካል/ርዕስ": p_title,
                "የጸሎት አይነት": p_type,
                "ሁኔታ": "በጸሎት ላይ"
            }
            st.session_state.prayers = pd.concat([st.session_state.prayers, pd.DataFrame([new_p])], ignore_index=True)
            st.success("የጸሎት ጥያቄው ተመዝግቧል!")
            st.rerun()

# MODULE 6: REPORTS & LEADERSHIP
elif menu == "📑 ሪፖርትና ግምገማ (Reports & Leadership)":
    st.header("📑 የአገልግሎት ሪፖርት ማጠናቀሪያና ማቅረቢያ")
    st.caption("በመመሪያው ገጽ 10 በነበረው የሪፖርትና ውሳኔ መዋቅር መሰረት")

    st.markdown("""
    <div class='card'>
    <b>የሪፖርት ፍሰት አቅጣጫ:</b><br>
    ምክትሎችና አገልጋዮች ➔ የአምስቱ ቡድን መሪዎች ➔ ዋና አስተናጋጅ (Coordinator) ➔ የቤተክርስቲያን አመራር
    </div>
    """, unsafe_allow_html=True)

    st.subheader("✍️ ሳምንታዊ/ወርሃዊ የቡድን ሪፖርት ማቅረቢያ")
    
    with st.form("report_submission"):
        rep_dept = st.selectbox("ሪፖርት የሚያቀርበው ክፍል:", [
            "1. የጸሎት ቡድን", 
            "2. የወንጌል ስርጭት ቡድን", 
            "3. የክትትል ቡድን", 
            "4. እንግዳ ተቀባይነትና መጓጓዣ", 
            "5. ሚዲያና ግንኙነት"
        ])
        q1 = st.text_area("1. ምን ተሰራ? (የተከናወኑ ተግባራት):")
        q2 = st.text_area("2. ምን ውጤት አለ? (የተገኙ ውጤቶች/ቁጥሮች):")
        q3 = st.text_area("3. ምን ድጋፍ ያስፈልጋል? (የሚያስፈልግ እገዛ):")
        q4 = st.text_input("4. ቀጣይ ኃላፊና ቀን (ማን/መቼ):")
        
        rep_submit = st.form_submit_button("📤 ሪፖርት አስተላልፍ")
        if rep_submit:
            st.success(f"ለ {rep_dept} የቀረበው ሪፖርት ለዋና አስተናጋጁ እና ለቤተክርስቲያን አመራር ተልኳል!")

st.markdown("---")
st.caption("© 2026 ECFC Houston Outreach Ministry Application | Houston, Texas")





