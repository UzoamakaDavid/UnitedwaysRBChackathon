import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset (replace with the actual path to your CSV file)
df = pd.read_csv("new_phases.csv")

# Set page title
st.set_page_config(page_title="Housing Construction Dashboard", layout="wide")

# Dashboard title
st.write("--------------------------------------------------------------------------------")
st.title("Housing Dashboard - August")
st.write("--------------------------------------------------------------------------------")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_province = st.sidebar.multiselect("Select Province", options=df['Province'].unique(), default=df['Province'].unique())
selected_city = st.sidebar.multiselect("Select City", options=df['City'].unique(), default=df['City'].unique())

# Filter data based on sidebar inputs
filtered_df = df[(df['Province'].isin(selected_province)) & (df['City'].isin(selected_city))]

# Main page layout
st.header("Homelessness Breakdown  By Province")
st.markdown("")
st.markdown("")
st.markdown("")
# Columns for the cards
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("PRINCE EDWARDS ISLAND")
    st.markdown("#### Individuals experiencing homelessness")
    st.markdown("##### 147")

with col2:
    st.subheader("NOVA SCOTIA")
    st.markdown("#### Individuals experiencing homelessness")
    st.markdown("##### 907")

with col3:
    st.subheader("NEW BRUNSWICK")
    st.markdown("#### Individuals experiencing homelessness")
    st.markdown("##### 644")

st.write("--------------------------------------------------------------------------------")
st.markdown("")
st.markdown("")
st.markdown("")

# Main page layout
st.header("Overview of Housing Construction Phases")

# Display total starts, completions, and under construction in cards
st.subheader("Total Housing Data Breakdown (By Type)")

# Columns for the cards
col1, col2, col3 = st.columns(3)

# Convert relevant columns to numeric to avoid errors
cols_to_convert = [
    'Starts/Single', 'Starts/Semi', 'Starts/Row', 'Starts/Apt', 'Starts/Total',
    'Completions/Single', 'Completions/Semi', 'Completions/Row', 'Completions/Apt', 'Completions/Total',
    'Under Construction/Single', 'Under Construction/Semi', 'Under Construction/Row', 'Under Construction/Apt', 'Under Construction/Total'
]

# Ensure that columns are numeric (converts any non-numeric values to NaN)
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Card 1: Total Starts
with col1:
    st.markdown("### Total Starts")
    total_starts_single = pd.to_numeric(filtered_df['Starts/Single'].sum(), errors='coerce')
    total_starts_semi = pd.to_numeric(filtered_df['Starts/Semi'].sum(), errors='coerce')
    total_starts_row = pd.to_numeric(filtered_df['Starts/Row'].sum(), errors='coerce')
    total_starts_apt = pd.to_numeric(filtered_df['Starts/Apt'].sum(), errors='coerce')
    total_starts_total = pd.to_numeric(filtered_df['Starts/Total'].sum(), errors='coerce')

    st.write(f"Single: {total_starts_single:,.0f}" if pd.notnull(total_starts_single) else "Single: N/A")
    st.write(f"Semi: {total_starts_semi:,.0f}" if pd.notnull(total_starts_semi) else "Semi: N/A")
    st.write(f"Row: {total_starts_row:,.0f}" if pd.notnull(total_starts_row) else "Row: N/A")
    st.write(f"Apt: {total_starts_apt:,.0f}" if pd.notnull(total_starts_apt) else "Apt: N/A")
    st.write(f"**Total: {total_starts_total:,.0f}**" if pd.notnull(total_starts_total) else "**Total: N/A**")

# Card 2: Total Completions
with col2:
    st.markdown("### Total Completions")
    total_completions_single = pd.to_numeric(filtered_df['Completions/Single'].sum(), errors='coerce')
    total_completions_semi = pd.to_numeric(filtered_df['Completions/Semi'].sum(), errors='coerce')
    total_completions_row = pd.to_numeric(filtered_df['Completions/Row'].sum(), errors='coerce')
    total_completions_apt = pd.to_numeric(filtered_df['Completions/Apt'].sum(), errors='coerce')
    total_completions_total = pd.to_numeric(filtered_df['Completions/Total'].sum(), errors='coerce')

    st.write(f"Single: {total_completions_single:,.0f}" if pd.notnull(total_completions_single) else "Single: N/A")
    st.write(f"Semi: {total_completions_semi:,.0f}" if pd.notnull(total_completions_semi) else "Semi: N/A")
    st.write(f"Row: {total_completions_row:,.0f}" if pd.notnull(total_completions_row) else "Row: N/A")
    st.write(f"Apt: {total_completions_apt:,.0f}" if pd.notnull(total_completions_apt) else "Apt: N/A")
    st.write(f"**Total: {total_completions_total:,.0f}**" if pd.notnull(total_completions_total) else "**Total: N/A**")

# Card 3: Total Under Construction
with col3:
    st.markdown("### Under Construction")
    total_under_construction_single = pd.to_numeric(filtered_df['Under Construction/Single'].sum(), errors='coerce')
    total_under_construction_semi = pd.to_numeric(filtered_df['Under Construction/Semi'].sum(), errors='coerce')
    total_under_construction_row = pd.to_numeric(filtered_df['Under Construction/Row'].sum(), errors='coerce')
    total_under_construction_apt = pd.to_numeric(filtered_df['Under Construction/Apt'].sum(), errors='coerce')
    total_under_construction_total = pd.to_numeric(filtered_df['Under Construction/Total'].sum(), errors='coerce')

    st.write(f"Single: {total_under_construction_single:,.0f}" if pd.notnull(total_under_construction_single) else "Single: N/A")
    st.write(f"Semi: {total_under_construction_semi:,.0f}" if pd.notnull(total_under_construction_semi) else "Semi: N/A")
    st.write(f"Row: {total_under_construction_row:,.0f}" if pd.notnull(total_under_construction_row) else "Row: N/A")
    st.write(f"Apt: {total_under_construction_apt:,.0f}" if pd.notnull(total_under_construction_apt) else "Apt: N/A")
    st.write(f"**Total: {total_under_construction_total:,.0f}**" if pd.notnull(total_under_construction_total) else "**Total: N/A**")

st.write("--------------------------------------------------------------------------------")
st.markdown("")
st.markdown("")
st.markdown("")

# Columns for starts, completions, and under construction charts
st.header("Visual Analysis by City and Province")

# Get unique provinces
provinces = df['Province'].unique()

# Dropdown filter for the user to select 'Starts', 'Completions', or 'Under Construction'
chart_type = st.selectbox(
    "Select Data to Display on Chart",
    ["Starts", "Completions", "Under Construction"]
)

# Function to plot housing data by province based on the selected chart type
def plot_housing_data_by_province(province_data, province_name, chart_type):
    # Create a figure
    fig = go.Figure()

    if chart_type == "Starts":
        # Starts data
        data = province_data[['Starts/Single', 'Starts/Semi', 'Starts/Row', 'Starts/Apt']].sum()
        title = f"Starts in {province_name}"
    elif chart_type == "Completions":
        # Completions data
        data = province_data[['Completions/Single', 'Completions/Semi', 'Completions/Row', 'Completions/Apt']].sum()
        title = f"Completions in {province_name}"
    elif chart_type == "Under Construction":
        # Under Construction data
        data = province_data[['Under Construction/Single', 'Under Construction/Semi', 'Under Construction/Row', 'Under Construction/Apt']].sum()
        title = f"Under Construction in {province_name}"

    # Add bar trace with gradient from dark to light blue
    fig.add_trace(go.Bar(
        x=data.index,
        y=data.values,
        text=data.values,  # Show values on top of the bars
        textposition='auto',  # Automatically position the text on top
        marker_color=['#003f5c', '#2f4b7c', '#665191', '#a05195'],  # Blue gradient colors
        textfont=dict(size=20),  # Set the font size for the numbers
        name=chart_type
    ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title='Housing Type',
        yaxis_title='Number of Houses',
        showlegend=False
    )

    return fig

# Get unique provinces
provinces = df['Province'].unique()

# Loop over each province and create a chart for the selected chart type
for province in provinces:
    # Filter the dataframe for the current province
    province_data = df[df['Province'] == province]
    
    # Create a section for each province
    st.markdown(f"## Housing Data for {province}")
    
    # Display the chart based on the dropdown selection
    st.plotly_chart(plot_housing_data_by_province(province_data, province, chart_type), use_container_width=True)

# Detailed breakdown
st.header("Detailed Breakdown by Housing Type")
st.dataframe(filtered_df)