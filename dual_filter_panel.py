
import streamlit as st

def render_dual_filter_panel(filtered_df):
    st.header("📊 Flowline Shaker Cost Summary")

    cols = st.columns(3)
    with cols[0]:
        st.metric("Haul OFF", f"{filtered_df['Haul_OFF'].sum():,.0f}")
    with cols[1]:
        st.metric("Total Dilution", f"{filtered_df['Total_Dil'].sum():,.0f}")
    with cols[2]:
        st.metric("IntLength", f"{filtered_df['IntLength'].sum():,.0f} ft")

    st.markdown("### 💰 Cost Breakdown")
    dilution_rate = st.slider("Dilution Cost Rate ($/unit)", 100, 500, 100, 50)
    haul_rate = st.slider("Haul-Off Cost Rate ($/unit)", 20, 50, 20, 10)
    equip_cost = st.number_input("Total Equipment Cost ($)", value=100000)
    shakers_installed = st.slider("Number of Shakers Installed", 1, 10, 3)
    life_years = st.slider("Shaker Life (Years)", 1, 10, 7)
    screen_cost = st.number_input("Screen Cost ($)", value=1500)
    other_cost = st.number_input("Other Daily Cost ($)", value=500)

    total_dil = filtered_df['Total_Dil'].sum()
    total_haul = filtered_df['Haul_OFF'].sum()
    int_length = filtered_df['IntLength'].sum()

    cost_dil = dilution_rate * total_dil
    cost_haul = haul_rate * total_haul
    cost_equip = (equip_cost * shakers_installed) / life_years
    cost_total = cost_dil + cost_haul + cost_equip + screen_cost + other_cost
    cost_per_ft = cost_total / int_length if int_length else 0

    st.markdown(f"""
    - 💧 **Dilution Cost**: ${cost_dil:,.0f}  
    - 🛢️ **Haul-Off Cost**: ${cost_haul:,.0f}  
    - 🛠️ **Equipment Cost**: ${cost_equip:,.0f}  
    - 🧪 **Screen Cost**: ${screen_cost:,.0f}  
    - 📦 **Other Cost**: ${other_cost:,.0f}  
    - ---
    - 🧮 **Cumulative Cost**: ${cost_total:,.0f}  
    - 📏 **Cost per Foot**: ${cost_per_ft:,.2f} / ft
    """)
