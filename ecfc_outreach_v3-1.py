import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='ECFC Houston Outreach Ministry',page_icon='✝️',layout='wide')
st.markdown('''<style>.stApp{background:#0c1423;color:#f6f8fc}h1,h2,h3{color:#f6f8fc!important}.stMetric{background:#fff;color:#152945;border-radius:12px;padding:14px}div[data-testid="stMetricValue"],div[data-testid="stMetricLabel"]{color:#152945!important}section[data-testid="stSidebar"]{background:#222936} .stButton button{background:#d8ac45;color:#14233b;border:0}</style>''',unsafe_allow_html=True)

if 'APP_PASSWORD' in st.secrets:
    if not st.session_state.get('authenticated',False):
        st.title('✝️ ECFC Houston Outreach Ministry')
        password=st.text_input('የመግቢያ የይለፍ ቃል',type='password')
        if st.button('ግባ / Log in'):
            if password==st.secrets['APP_PASSWORD']:
                st.session_state.authenticated=True
                st.rerun()
            else: st.error('የይለፍ ቃሉ ትክክል አይደለም።')
        st.stop()
else:
    st.error('APP_PASSWORD በStreamlit Secrets ውስጥ አልተዘጋጀም።')
    st.stop()

TEAMS={
 'ጸሎት | Prayer':6,
 'እንደገና ማቋቋም | Restoration':3,
 'ወንጌል ስርጭት | Evangelism':4,
 'ክትትል | Follow-Up':3,
 'እንግዳ አቀባበልና ሎጂስቲክስ | Hospitality':3,
 'ሚዲያና ግንኙነት | Media':3,
}
PAGES=['🏠 ዋና ገጽ','🧭 ራዕይና የሥራ እቅድ','👥 የአመራርና የቡድኖች መዋቅር','📅 የአምስት ወር እቅድ','🔁 የሰባት ደረጃ ክትትል','📝 መመዝገቢያ ቅጾች','📊 ሪፖርት']
with st.sidebar:
    st.header('✝️ ECFC Houston')
    st.caption('Outreach Ministry • የወንጌል አገልግሎት')
    page=st.radio('መርጫ',PAGES)
    if st.button('ውጣ / Log out'):
        st.session_state.authenticated=False
        st.rerun()

st.title('✝️ ECFC Houston Outreach Ministry')
st.caption('የአገልግሎት እቅድ • የቡድኖች መዋቅር • ክትትል')
if page==PAGES[0]:
    st.header('የአገልግሎቱ አጠቃላይ እይታ')
    a,b,c=st.columns(3)
    a.metric('የአገልግሎት ቡድኖች',len(TEAMS));b.metric('በሮስተር የተመደቡ ቦታዎች',sum(TEAMS.values()));c.metric('የወራት የሥራ እቅድ',5)
    st.info('ይህ አዲስ ስሪት በተላከው Roster መሠረት 6 ቡድኖችን ያሳያል። ስሞች ባዶ ናቸው፤ አልተፈጠሩም።')
    st.subheader('የቡድኖች አቀራረብ')
    for team,n in TEAMS.items(): st.write(f'**{team}** — {n} የአገልጋዮች ቦታዎች')
elif page==PAGES[1]:
    st.header('ራዕይና የሥራ እቅድ')
    st.success('“አዲስ ነገር ለመፍጠር አይደለም፤ እግዚአብሔር ቀድሞ በECFC Houston ያስቀመጠውን ተልዕኮ እንደገና ለማንቃት ነው።”')
    st.write('**የትኩረት አቅጣጫ:** ጸሎት፣ ወንጌል ስርጭት፣ ክትትል፣ የማህበረሰብ አገልግሎት፣ ግንኙነትና ሪፖርት።')
    st.subheader('የሳምንት የሥራ ሂደት')
    st.dataframe(pd.DataFrame([['ሰኞ–ማክሰኞ','ጸሎትና የሰዎች ዝርዝር','Prayer'],['ረቡዕ','የቡድን መሪዎች ማስተባበር','Coordinator + Leaders'],['ሐሙስ–ዓርብ','ጥሪ፣ ግብዣና ክትትል','Follow-Up'],['ቅዳሜ','የወንጌል አገልግሎት','All Teams'],['እሁድ','የቤተክርስቲያን ግንኙነትና ሪፖርት','Secretary + Leaders']],columns=['ቀን','ተግባር','ተጠሪ']),hide_index=True,use_container_width=True)
elif page==PAGES[2]:
    st.header('የአመራር መዋቅር')
    st.write('**Church Leadership → Coordinator → Assistant Coordinator / Team Leaders / Secretary**')
    st.dataframe(pd.DataFrame({'ኃላፊነት':['ዋና አስተባባሪ','ምክትል አስተባባሪ','የቡድን መሪዎች','ጸሐፊ / መዝገብ ያዥ'],'ስም':['—']*4}),hide_index=True,use_container_width=True)
    st.subheader('የቡድኖች መዋቅር')
    for name,slots in TEAMS.items():
        with st.expander(f'{name} — {slots} ቦታዎች'):
            st.dataframe(pd.DataFrame({'ቁጥር':range(1,slots+1),'የአገልጋይ ስም':['']*slots,'ስልክ / ኢሜይል':['']*slots}),hide_index=True,use_container_width=True)
elif page==PAGES[3]:
    st.header('የአምስት ወር የአገልግሎት እቅድ')
    rows=[['1','የማህበረሰብ ወንጌል ስርጭት','Evangelism & Prayer'],['2','ቤት አልባ ሰዎችን / ማህበረሰብን መርዳት','Hospitality & Outreach'],['3','ታካሚዎችንና አረጋውያንን ማበረታታት','Follow-Up & Hospitality'],['4','የሰፈር ወንጌል ስርጭት','Evangelism & Media'],['5','የቤተሰብ / ማህበረሰብ ዝግጅት','All Teams']]
    st.dataframe(pd.DataFrame(rows,columns=['ወር','ዋና ተግባር','ተጠሪ ቡድኖች']),hide_index=True,use_container_width=True)
elif page==PAGES[4]:
    st.header('የክትትል ሰባት ደረጃዎች')
    for i,step in enumerate(['ሰው ማግኘት','ስምና የመገናኛ መረጃ መቀበል','ስልክ መደወል','መጎብኘት','መጋበዝ','ማስተማር / ማስተዋወቅ','ደቀ መዝሙር ማድረግ'],1): st.write(f'**{i}. {step}**')
    st.warning('የሰዎች የግል መረጃ በዚህ የሙከራ ስሪት አታስገቡ። ደህንነቱ የተረጋገጠ የመረጃ ማከማቻ ገና አልተገናኘም።')
elif page==PAGES[5]:
    st.header('የሥራ መመዝገቢያ ቅጽ — የሙከራ ማሳያ')
    with st.form('activity'):
        team=st.selectbox('ቡድን',list(TEAMS));day=st.date_input('ቀን',date.today());activity=st.text_area('የተከናወነ ሥራ (የግል መረጃ አይጻፉ)');submitted=st.form_submit_button('ቅጹን አሳይ')
    if submitted: st.info(f'የሙከራ ቅጽ: {team} | {day} | {activity}\n\nይህ ቅጽ በዳታቤዝ ውስጥ አይቀመጥም።')
elif page==PAGES[6]:
    st.header('ሪፖርትና አመራር')
    st.info('ይህ ስሪት የመዋቅርና የእቅድ ማሳያ ነው። የቡድን መለያዎች፣ ቋሚ የመረጃ ማከማቻና የሪፖርት ስርዓት በቀጣይ ደረጃ ይጨመራሉ።')
    st.dataframe(pd.DataFrame({'ቡድን':list(TEAMS),'በሮስተር ያሉ ቦታዎች':list(TEAMS.values())}),hide_index=True,use_container_width=True)
