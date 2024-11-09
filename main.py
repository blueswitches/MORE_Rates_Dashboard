# Necessary Imports
import mysql.connector
import pandas as pd
import streamlit as st

# Set up the Streamlit page configuration with a wide layout and custom page title
st.set_page_config(layout="wide", page_title='Rates Database')

# Inject CSS to hide header, footer, and menu
hide_st_style = """
           <style>
           header {visibility: hidden;}
           footer {visibility: hidden;}
           .css-18ni7ap.e8zbici2 {visibility: hidden;}
           </style>
           """
st.markdown(hide_st_style, unsafe_allow_html=True)

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

#SQL query to retrieve the residential_rate value from Mar_23 where Short_Name is 'MORE Power'
query_21 = "SELECT Mar_23 FROM residential_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_21)
# Fetch the result
result_21 = cursor.fetchone()

#SQL query to retrieve the residential_rate value from Mar_23 where Short_Name is 'CENECO'
query_22 = "SELECT Mar_23 FROM residential_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_22)
# Fetch the result
result_22 = cursor.fetchone()

#SQL query to retrieve the residential_rate value from Mar_23 where Short_Name is 'BLCI'
query_23 = "SELECT Mar_23 FROM residential_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_23)
# Fetch the result
result_23 = cursor.fetchone()

#SQL query to retrieve the generation rate value from Mar_23 where Short_Name is 'MORE Power'
query_24 = "SELECT Mar_23 FROM generation_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_24)
# Fetch the result
result_24 = cursor.fetchone()

#SQL query to retrieve the generation rate value from Mar_23 where Short_Name is 'CENECO'
query_25 = "SELECT Mar_23 FROM generation_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_25)
# Fetch the result
result_25 = cursor.fetchone()

#SQL query to retrieve the generation rate value from Mar_23 where Short_Name is 'BLCI'
query_26 = "SELECT Mar_23 FROM generation_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_26)
# Fetch the result
result_26 = cursor.fetchone()

query_27 = """
SELECT Short_Name, Mar_23
FROM residential_rate
WHERE Mar_23_Ranking BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking ASC;
"""
cursor.execute(query_27)
result_27 = cursor.fetchall()

query_28 = """
SELECT Short_Name, Mar_23
FROM residential_rate
WHERE Mar_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking_Vis ASC;
"""
cursor.execute(query_28)
result_28 = cursor.fetchall()

query_29 = """
SELECT Short_Name, Mar_23
FROM generation_rate
WHERE Mar_23_Ranking BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking ASC;
"""
cursor.execute(query_29)
result_29 = cursor.fetchall()

query_30 = """
SELECT Short_Name, Mar_23
FROM generation_rate
WHERE Mar_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking_Vis ASC;
"""
cursor.execute(query_30)
result_30 = cursor.fetchall()

query_31 = "SELECT Apr_23 FROM residential_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_31)
# Fetch the result
result_31 = cursor.fetchone()

query_32 = "SELECT Apr_23 FROM residential_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_32)
# Fetch the result
result_32 = cursor.fetchone()

query_33 = "SELECT Apr_23 FROM residential_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_33)
# Fetch the result
result_33 = cursor.fetchone()

query_34 = "SELECT Apr_23 FROM generation_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_34)
# Fetch the result
result_34 = cursor.fetchone()

query_35 = "SELECT Apr_23 FROM generation_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_35)
# Fetch the result
result_35 = cursor.fetchone()

query_36 = "SELECT Apr_23 FROM generation_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_36)
# Fetch the result
result_36 = cursor.fetchone()

query_37 = """
SELECT Short_Name, Apr_23
FROM residential_rate
WHERE Apr_23_Ranking BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking ASC;
"""
cursor.execute(query_37)
result_37 = cursor.fetchall()

query_38 = """
SELECT Short_Name, Apr_23
FROM residential_rate
WHERE Apr_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking_Vis ASC;
"""
cursor.execute(query_38)
result_38 = cursor.fetchall()

query_39 = """
SELECT Short_Name, Apr_23
FROM generation_rate
WHERE Apr_23_Ranking BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking ASC;
"""
cursor.execute(query_39)
result_39 = cursor.fetchall()

query_40 = """
SELECT Short_Name, Apr_23
FROM generation_rate
WHERE Apr_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking_Vis ASC;
"""
cursor.execute(query_40)
result_40 = cursor.fetchall()

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
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_11[0], result_12[0], result_13[0]], 
        "Generation Rate": [result_14[0], result_15[0], result_16[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

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

elif month_selected == 'March 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_21[0], result_22[0], result_23[0]],
        "Generation Rate": [result_24[0], result_25[0], result_26[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_27], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_27] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_28], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_28] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_29], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_29] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_30], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_30] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'April 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_31[0], result_32[0], result_33[0]],
        "Generation Rate": [result_34[0], result_35[0], result_36[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_37], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_37] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_38], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_38] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_39], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_39] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_40], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_40] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)