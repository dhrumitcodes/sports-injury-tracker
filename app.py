import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import database as db

db.init_db()

st.set_page_config(page_title="Advanced Rehab Ecosystem", page_icon="💪", layout="wide")
st.title("🛡️ Advanced Injury Rehab & Safe-Dosage Ecosystem")

MED_RULES = {
    "Ibuprofen (Advil)": {"clearance_hrs": 6, "max_daily_mg": 1200, "default_dose": 200, "class": "NSAID"},
    "Naproxen (Aleve)": {"clearance_hrs": 12, "max_daily_mg": 660, "default_dose": 220, "class": "NSAID"},
    "Acetaminophen (Tylenol)": {"clearance_hrs": 6, "max_daily_mg": 3000, "default_dose": 500, "class": "Analgesic"}
}

INJURY_PRESETS = {
    "Custom (Manual Input)": {"med": "Ibuprofen (Advil)", "dose": 200, "pain": 5},
    " Lumbar Disc Back Pain": {"med": "Naproxen (Aleve)", "dose": 220, "pain": 7},
    "🦶 Acute Ankle Sprain": {"med": "Ibuprofen (Advil)", "dose": 400, "pain": 6},
    "🧠 Severe Migraine": {"med": "Acetaminophen (Tylenol)", "dose": 500, "pain": 8}
}

df_logs = db.load_logs_df()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🚀 One-Click Injury Presets & Intake")
    

    preset_choice = st.selectbox("Load Condition Profile Preset:", list(INJURY_PRESETS.keys()))
    active_preset = INJURY_PRESETS[preset_choice]
    
    with st.form("intake_form"):
        med_selected = st.selectbox("Medication Choice:", list(MED_RULES.keys()), 
                                    index=list(MED_RULES.keys()).index(active_preset["med"]))
        
        dosage_input = st.number_input("Dosage Amount (mg):", min_value=50, max_value=1000, 
                                       value=int(active_preset["dose"]), step=50)
        
        pain_rating = st.slider("Current Pain Level (1-10):", 1, 10, int(active_preset["pain"]))
        

        trigger_selected = st.selectbox("Possible Pain Trigger:", 
                                        ["None/Routine", "Long Sitting", "Driving", "Poor Sleep", "Stress", "Cold Weather"])
        
    
        side_effect = st.selectbox("Experienced Side Effects:", ["None", "Drowsiness", "Stomach Ache", "Nausea"])
        
        submit_btn = st.form_submit_button("Log Entry to Local Database")
        
        if submit_btn:
            rules = MED_RULES[med_selected]
            today_str = datetime.now().strftime("%Y-%m-%d")
            
        
            current_daily_total = 0
            if not df_logs.empty:
                todays_rows = df_logs[df_logs['timestamp'].dt.strftime('%Y-%m-%d') == today_str]
                current_daily_total = todays_rows[todays_rows['medication'] == med_selected]['mg'].sum()
                
        
            if (current_daily_total + dosage_input) > rules["max_daily_mg"]:
                st.error(f"⚠️ **Maximum Daily Dose Reached!** Adding this would put your 24hr intake at "
                         f"{current_daily_total + dosage_input}mg. Limit is {rules['max_daily_mg']}mg. Entry Denied.")
            else:
                db.save_log(med_selected, dosage_input, pain_rating, trigger_selected, side_effect)
                st.success(f"Successfully recorded data into local secure repository!")
                st.rerun()

with col2:
    st.subheader("🛡️ Active Medical Warning Controls")
    
    if df_logs.empty:
        st.info("Your database is clean. Enter clinical records on the left to start processing safety tracking loops.")
    else:
        
        time_now = datetime.now()
        active_nsaids = []
        
        for med, rule in MED_RULES.items():
            med_rows = df_logs[df_logs['medication'] == med]
            if not med_rows.empty:
                latest_record = med_rows.iloc[0] # Sorted descending, so index 0 is newest
                log_time = latest_record['timestamp']
                expiry_time = log_time + timedelta(hours=rule['clearance_hrs'])
                
                if time_now < expiry_time:
            
                    time_remaining = expiry_time - time_now
                    mins_remaining = int(time_remaining.total_seconds() / 60)
                    
                    st.metric(label=f"⏳ Active {med}", value=f"{mins_remaining} mins left", 
                              delta=f"Taken {latest_record['time_display'] if 'time_display' in latest_record else log_time.strftime('%I:%M %p')}", 
                              delta_color="inverse")
                    
                    if rule["class"] == "NSAID":
                        active_nsaids.append(med)
                        
        if len(active_nsaids) > 1:
            st.error(f"🚨 **NSAID Overlap Warning:** You currently have multiple active NSAID components "
                     f"({', '.join(active_nsaids)}) processing concurrently in your bloodstream. "
                     f"This increases risk of gastric irritation. Consult your physical health practitioner.")

if not df_logs.empty:
    st.markdown("---")
    st.subheader("📊 Long-Term Pain Reduction & Behavioral Analytics")
    
    analytics_col1, analytics_col2 = st.columns([2, 1])
    
    with analytics_col1:
        
        fig_pain = px.line(df_logs, x='timestamp', y='pain_before', title='Pain Progression Matrix Over Time',
                           labels={'timestamp': 'Timeline Checkpoint', 'pain_before': 'Pain Score (1-10)'},
                           markers=True, color_discrete_sequence=["#FF4B4B"])
        st.plotly_chart(fig_pain, use_container_width=True)
        
    with analytics_col2:
        st.markdown("**🎯 Top Pain Triggers Identified:**")
        # Count values of environmental or physical triggers recorded
        trigger_counts = df_logs[df_logs['trigger'] != "None/Routine"]['trigger'].value_counts()
        if not trigger_counts.empty:
            st.bar_chart(trigger_counts)
        else:
            st.caption("No custom external physical triggers logged yet.")
            
        st.markdown("**🛡️ Side Effect Tracker Distribution:**")
        se_counts = df_logs[df_logs['side_effect'] != "None"]['side_effect'].value_counts()
        if not se_counts.empty:
            st.dataframe(se_counts, use_container_width=True)
        else:
            st.caption("Zero medication side-effects reported across history logs.")