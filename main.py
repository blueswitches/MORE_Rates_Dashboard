# Necessary Imports
import mysql.connector
import pandas as pd
import streamlit as st

# Set up the Streamlit page configuration with a wide layout and custom page title
st.set_page_config(layout="wide", page_title='Rates Database')

# Create a selectbox widget for the user to choose a month and year for data filtering
month_selected = st.selectbox(label='For the month of', options=['January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023', 'January 2024', 'February 2024', 'March 2024', 'April 2024', 'May 2024', 'June 2024', 'July 2024', 'August 2024', 'September 2024'])

# MySQL connection
conn = mysql.connector.connect(
    host='cesra-db.cxkuksua06qz.ap-southeast-1.rds.amazonaws.com', 
    port=3309,       
    database='du_rates_comparison',         
    user='cesra_dbm',             
    password='ibIDN0NcnGYo71qDZuHw'      
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

#SQL query to retrieve the residential_rate value from Jan_23 where Short_Name is 'MORE Power'
query_1 = "SELECT Jan_23 FROM residential_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_1)
# Fetch the result
result_1 = cursor.fetchone()

# SQL query to retrieve the residential_rate value from Jan_23 where Short_Name is 'CENECO'
query_2 = "SELECT Jan_23 FROM residential_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_2)
# Fetch the result
result_2 = cursor.fetchone()


# SQL query to retrieve the residential_rate value from Jan_23 where Short_Name is 'BLCI'
query_3 = "SELECT Jan_23 FROM residential_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_3)
# Fetch the result
result_3 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'MORE Power'
query_4 = "SELECT Jan_23 FROM generation_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_4)
# Fetch the result
result_4 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'CENECO'
query_5 = "SELECT Jan_23 FROM generation_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_5)
# Fetch the result
result_5 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'BLCI'
query_6 = "SELECT Jan_23 FROM generation_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_6)
# Fetch the result
result_6 = cursor.fetchone()

# SQL query to retrieve Short_Name for Jan_23_Ranking values 1 to 5
query_7 = """
SELECT Short_Name, Jan_23
FROM residential_rate
WHERE Jan_23_Ranking BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking ASC;
"""
cursor.execute(query_7)
result_7 = cursor.fetchall()

query_8 = """
SELECT Short_Name, Jan_23
FROM residential_rate
WHERE Jan_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking_Vis ASC;
"""

cursor.execute(query_8)
result_8 = cursor.fetchall()

query_9 = """
SELECT Short_Name, Jan_23
FROM generation_rate
WHERE Jan_23_Ranking BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking ASC;
"""

cursor.execute(query_9)
result_9 = cursor.fetchall()

query_10 = """
SELECT Short_Name, Jan_23
FROM generation_rate
WHERE Jan_23_Ranking_Vis BETWEEN 1 and 5
ORDER BY Jan_23_Ranking_Vis ASC;
"""

cursor.execute(query_10)
result_10 = cursor.fetchall()

#SQL query to retrieve the residential_rate value from Feb_23 where Short_Name is 'MORE Power'
query_11 = "SELECT Feb_23 FROM residential_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_11)
# Fetch the result
result_11 = cursor.fetchone()

#SQL query to retrieve the residential_rate value from Feb_23 where Short_Name is 'CENECO'
query_12 = "SELECT Feb_23 FROM residential_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_12)
# Fetch the result
result_12 = cursor.fetchone()

#SQL query to retrieve the residential_rate value from Feb_23 where Short_Name is 'BLCI'
query_13 = "SELECT Feb_23 FROM residential_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_13)
# Fetch the result
result_13 = cursor.fetchone()

#SQL query to retrieve the generation_rate value from Feb_23 where Short_Name is 'MORE POWER'
query_14 = "SELECT Feb_23 FROM generation_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_14)
# Fetch the result
result_14 = cursor.fetchone()

#SQL query to retrieve the generation_rate value from Feb_23 where Short_Name is 'CENECO'
query_15 = "SELECT Feb_23 FROM generation_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_15)
# Fetch the result
result_15 = cursor.fetchone()

#SQL query to retrieve the generation_rate value from Feb_23 where Short_Name is 'BLCI'
query_16 = "SELECT Feb_23 FROM generation_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_16)
# Fetch the result
result_16 = cursor.fetchone()

# SQL query to retrieve Short_Name for Feb_23_Ranking values 1 to 5
query_17 = """
SELECT Short_Name, Feb_23
FROM residential_rate
WHERE Feb_23_Ranking BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking ASC;
"""
cursor.execute(query_17)
result_17 = cursor.fetchall()

# SQL query to retrieve Short_Name for Feb_23_Ranking_Vis values 1 to 5
query_18 = """
SELECT Short_Name, Feb_23
FROM residential_rate
WHERE Feb_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking_Vis ASC;
"""
cursor.execute(query_18)
result_18 = cursor.fetchall()

query_19 = """
SELECT Short_Name, Feb_23
FROM generation_rate
WHERE Feb_23_Ranking BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking ASC;
"""
cursor.execute(query_19)
result_19 = cursor.fetchall()

query_20 = """
SELECT Short_Name, Feb_23
FROM generation_rate
WHERE Feb_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking_Vis ASC;
"""
cursor.execute(query_20)
result_20 = cursor.fetchall()

# SQL 
if month_selected == 'January 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_1[0], result_2[0], result_3[0]], 
        "Generation Rate": [result_4[0], result_5[0], result_6[0]]
    }

    df_1 = pd.DataFrame(table_1)
    st.dataframe(df_1, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_7], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_7] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_8], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_8] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_9], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_9] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_10], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_10] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'February 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_6 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_11[0], result_12[0], result_13[0]], 
        "Generation Rate": [result_14[0], result_15[0], result_16[0]]
    }

    df_6 = pd.DataFrame(table_6)
    st.dataframe(df_6, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_17], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_17] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_18], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_18] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)
    
    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_19], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_19] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_20], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_20] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)