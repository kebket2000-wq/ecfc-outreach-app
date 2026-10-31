import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='ECFC Houston Outreach Ministry',page_icon='✝️',layout='wide')
st.markdown('''<style>.stApp{background:#0c1423;color:#f6f8fc}h1,h2,h3{color:#f6f8fc!important}.stMetric{background:#fff;color:#152945;border-radius:12px;padding:14px}div[data-testid="stMetricValue"],div[data-testid="stMetricLabel"]{color:#152945!important}section[data-testid="stSidebar"]{background:#222936} .stButton button{background:#d8ac45;color:#14233b;border:0}</style>''',unsafe_allow_html=True)

# Individual Supabase Auth accounts; access is enforced by database RLS.
from supabase import create_client
try:
    url=st.secrets["SUPABASE_URL"].rstrip("/")
    key=st.secrets["SUPABASE_KEY"]
    if not url.startswith("https://") or "/rest/v1" in url:
        raise ValueError("SUPABASE_URL must be the project URL, without /rest/v1")
except (KeyError, ValueError) as exc:
    st.error(f"Supabase configuration needed: {exc}")
    st.stop()
client=create_client(url,key)
if "ecfc_session" not in st.session_state:
    st.session_state.ecfc_session=None
if st.session_state.ecfc_session is None:
    st.title("✝️ ECFC Houston Outreach Ministry")
    st.caption("የግል መለያ / Individual account login")
    with st.form("login"):
        login_email=st.text_input("Email")
        login_password=st.text_input("Password",type="password")
        do_login=st.form_submit_button("ግባ / Log in")
    if do_login:
        try:
            result=client.auth.sign_in_with_password({"email":login_email,"password":login_password})
            st.session_state.ecfc_session={"access_token":result.session.access_token,"refresh_token":result.session.refresh_token}
            st.rerun()
        except Exception:
            st.error("Login failed. Check your email and password.")
    st.stop()
try:
    tokens=st.session_state.ecfc_session
    client.auth.set_session(tokens["access_token"],tokens["refresh_token"])
    session=client.auth.get_session()
    st.session_state.ecfc_session={"access_token":session.access_token,"refresh_token":session.refresh_token}
    user=client.auth.get_user().user
    profiles=client.table("ecfc_profiles").select("role,team,display_name").eq("user_id",user.id).execute().data
    if not profiles:
        st.warning("Your account needs an assigned ministry role. Contact the admin.")
        if st.button("Log out"):
            st.session_state.ecfc_session=None
            st.rerun()
        st.stop()
    profile=profiles[0]
    role=profile["role"]
    my_team=profile.get("team")
except Exception as exc:
    st.session_state.ecfc_session=None
    st.error("Could not connect to Supabase. Please log in again or check database setup.")
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
    st.caption(f'Account: {profile.get("display_name") or user.email} | {role}')
    page=st.radio('መርጫ',PAGES)
    if st.button('ውጣ / Log out'):
        st.session_state.ecfc_session=None
        st.rerun()

st.title('✝️ ECFC Houston Outreach Ministry')
st.caption('የአገልግሎት እቅድ • የቡድኖች መዋቅር • ክትትል')
if page==PAGES[0]:
    st.header('የአገልግሎቱ አጠቃላይ እይታ')
    a,b,c=st.columns(3)
    a.metric('የአገልግሎት ቡድኖች',len(TEAMS));b.metric('በሮስተር የተመደቡ ቦታዎች',sum(TEAMS.values()));c.metric('የወራት የሥራ እቅድ',5)
    st.info('ይህ አፕ በተላከው Roster መሠረት 6 ቡድኖችን ያሳያል። ስሞች ባዶ ናቸው፤ አልተፈጠሩም።')
    st.subheader('የቡድኖች አቀራረብ')
    for team,n in TEAMS.items(): st.write(f'**{team}** — {n} የአገልጋዮች ቦታዎች')
elif page==PAGES[1]:
    st.header('ራዕይና የሥራ እቅድ')
    st.success('“አዲስ ነገር ለመፍጠር አይደለም፤ እግዚአብሔር ቀድሞ በECFC Houston ያስቀመጠውን ተልዕኮ እንደገና ለማንቃት ነው።”')
    st.write('**የትኩረት አቅጣጫ:** ጸሎት፣ ወንጌል ስርጭት፣ ክትትል፣ የማህበረሰብ አገልግሎት፣ ግንኙነትና ሪፖርት።')
    st.subheader('የሳምንት የሥራ ሂደት')
    st.dataframe(pd.DataFrame([['ሰኞ–ማክሰኞ','ጸሎትና የሰዎች ዝርዝር','Prayer'],['ረቡዕ','የቡድን መሪዎች ማስተባበር','Coordinator + Leaders'],['ሐሙስ–ዓርብ','ጥሪ፣ ግብዣና ክትትል','Follow-Up'],['ቅዳሜ','የወንጌል አገልግሎት','All Teams'],['እሁድ','የቤተክርስቲያን ግንኙነትና ሪፖርት','Secretary + Leaders']],columns=['ቀን','ተግባር','ተጠሪ']),hide_index=True,width="stretch")
elif page==PAGES[2]:
    st.header('የአመራርና የቡድኖች መዋቅር')
    st.write('**Church Leadership → Coordinator → Assistant Coordinator / Team Leaders / Secretary**')
    st.info('Leadership assignments are not yet entered. Team roster changes are saved in Supabase.')
    st.subheader('የቡድኖች መዋቅር / Team roster')
    labels={'Prayer':'ጸሎት','Restoration':'እንደገና ማቋቋም','Evangelism':'ወንጌል ስርጭት',
            'Follow-Up':'ክትትል','Hospitality':'እንግዳ አቀባበልና ሎጂስቲክስ','Media':'ሚዲያና ግንኙነት'}
    try:
        roster=client.table('ecfc_roster').select('id,team,slot,full_name,phone,email,position').order('slot').execute().data
    except Exception:
        st.error('Roster table is not available. Run the database SQL setup first.')
        st.stop()
    for team_name,slots in [('Prayer',6),('Restoration',3),('Evangelism',4),('Follow-Up',3),('Hospitality',3),('Media',3)]:
        rows=[r for r in roster if r['team']==team_name]
        can_edit=role=='admin' or (role=='leader' and my_team==team_name)
        with st.expander(f'{labels[team_name]} | {team_name} — {slots} ቦታዎች'):
            st.dataframe(pd.DataFrame([{'ቁጥር':r['slot'],'ስም':r['full_name'],'ስልክ':r['phone'],
                  'ኢሜይል':r['email'],'ኃላፊነት':r['position']} for r in rows]),hide_index=True,width='stretch')
            if can_edit:
                slot_options={f"{r['slot']}. {r['full_name'] or '—'}":r for r in rows}
                chosen=st.selectbox('የሚሻሻለው ቦታ / Select slot',list(slot_options),key=f'select_{team_name}')
                selected=slot_options[chosen]
                with st.form(f'edit_{team_name}_{selected["id"]}'):
                    name=st.text_input('የአገልጋይ ስም',value=selected['full_name'])
                    phone=st.text_input('ስልክ',value=selected['phone'])
                    email=st.text_input('ኢሜይል',value=selected['email'])
                    position=st.text_input('ኃላፊነት / Role',value=selected['position'])
                    save=st.form_submit_button('💾 አስቀምጥ / Save')
                if save:
                    try:
                        client.table('ecfc_roster').update({'full_name':name.strip(),'phone':phone.strip(),
                          'email':email.strip(),'position':position.strip()}).eq('id',selected['id']).execute()
                        st.success('ተቀምጧል / Saved')
                        st.rerun()
                    except Exception:
                        st.error('Save denied or failed. Check your team permissions and Supabase RLS.')
            else:
                st.caption('View only / ለማየት ብቻ')
elif page==PAGES[3]:
    st.header('የአምስት ወር የአገልግሎት እቅድ')
    rows=[['1','የማህበረሰብ ወንጌል ስርጭት','Evangelism & Prayer'],['2','ቤት አልባ ሰዎችን / ማህበረሰብን መርዳት','Hospitality & Outreach'],['3','ታካሚዎችንና አረጋውያንን ማበረታታት','Follow-Up & Hospitality'],['4','የሰፈር ወንጌል ስርጭት','Evangelism & Media'],['5','የቤተሰብ / ማህበረሰብ ዝግጅት','All Teams']]
    st.dataframe(pd.DataFrame(rows,columns=['ወር','ዋና ተግባር','ተጠሪ ቡድኖች']),hide_index=True,width="stretch")
elif page==PAGES[4]:
    st.header('የክትትል ሰባት ደረጃዎች / Follow-Up')
    stages=['ሰው ማግኘት','ስምና የመገናኛ መረጃ መቀበል','ስልክ መደወል','መጎብኘት','መጋበዝ','ማስተማር / ማስተዋወቅ','ደቀ መዝሙር ማድረግ']
    for i,step in enumerate(stages,1): st.write(f'**{i}. {step}**')
    try:
        followups=client.table('ecfc_followups').select('id,team,contact_code,stage,notes,next_date,created_at').order('created_at',desc=True).limit(200).execute().data
        st.dataframe(pd.DataFrame(followups),hide_index=True,width='stretch')
    except Exception: st.warning('Follow-up database table is not configured yet.')
    allowed=['Prayer','Restoration','Evangelism','Follow-Up','Hospitality','Media'] if role=='admin' else ([my_team] if role=='leader' and my_team else [])
    if allowed:
        with st.form('followup_new'):
            team=st.selectbox('ቡድን / Team',allowed)
            code=st.text_input('የግንኙነት መለያ / Contact code (no private information)')
            stage=st.selectbox('ደረጃ / Stage',range(1,8),format_func=lambda n:f'{n}. {stages[n-1]}')
            notes=st.text_area('ማስታወሻ / Notes (no private information)')
            next_date=st.date_input('የሚቀጥለው ቀን / Next date',date.today())
            save=st.form_submit_button('💾 አስቀምጥ / Save')
        if save:
            try:
                if not code.strip(): st.error('Contact code is required.')
                else:
                    client.table('ecfc_followups').insert({'team':team,'contact_code':code.strip(),'stage':stage,'notes':notes.strip(),'next_date':next_date.isoformat(),'created_by':user.id}).execute()
                    st.success('ተቀምጧል / Saved'); st.rerun()
            except Exception as exc: st.error('Could not save follow-up. Check database setup and permissions.')
elif page==PAGES[5]:
    st.header('የሥራ መመዝገቢያ ቅጽ / Activity Form')
    allowed=['Prayer','Restoration','Evangelism','Follow-Up','Hospitality','Media'] if role=='admin' else ([my_team] if role=='leader' and my_team else [])
    if allowed:
        with st.form('activity'):
            team=st.selectbox('ቡድን / Team',allowed)
            day=st.date_input('ቀን / Date',date.today())
            activity=st.text_area('የተከናወነ ሥራ / Activity (no private information)')
            submitted=st.form_submit_button('💾 አስቀምጥ / Save')
        if submitted:
            try:
                if not activity.strip(): st.error('Activity is required.')
                else:
                    client.table('ecfc_activities').insert({'team':team,'activity_date':day.isoformat(),'description':activity.strip(),'created_by':user.id}).execute()
                    st.success('ተቀምጧል / Saved'); st.rerun()
            except Exception: st.error('Could not save. Check database setup and permissions.')
    else: st.info('View only / ለማየት ብቻ')
    try:
        activities=client.table('ecfc_activities').select('team,activity_date,description,created_at').order('activity_date',desc=True).limit(200).execute().data
        st.dataframe(pd.DataFrame(activities),hide_index=True,width='stretch')
    except Exception: st.warning('Activity database table is not configured yet.')
elif page==PAGES[6]:
    st.header('ሪፖርት / Reports')
    try:
        activities=client.table('ecfc_activities').select('team,activity_date,description').execute().data
        followups=client.table('ecfc_followups').select('team,stage').execute().data
        a,b=st.columns(2)
        a.metric('የተመዘገቡ ሥራዎች / Activities',len(activities))
        b.metric('የክትትል መዝገቦች / Follow-ups',len(followups))
        summary=[]
        for label in ['Prayer','Restoration','Evangelism','Follow-Up','Hospitality','Media']:
            summary.append({'ቡድን / Team':label,'Activities':sum(x['team']==label for x in activities),'Follow-ups':sum(x['team']==label for x in followups)})
        st.dataframe(pd.DataFrame(summary),hide_index=True,width='stretch')
        st.download_button('⬇️ Download summary CSV',pd.DataFrame(summary).to_csv(index=False).encode('utf-8-sig'),'ecfc_summary.csv','text/csv')
    except Exception: st.warning('Reports require the database setup to be completed.')
