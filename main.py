# IMPORTS
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

# Inject CSS to color the selectbox
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        background-color: #2E8B57;  /* Background color of the dropdown */
        color: white;                 /* Text color inside the dropdown */
    }
    div[data-baseweb="select"] > div:hover {
        background-color: #3CB371; /* Hover color of the dropdown */
    }
    </style>
    """, unsafe_allow_html=True)

# Create a selectbox widget for the user to choose a month and year for data filtering
month_selected = st.selectbox(label='For the month of', options=['January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023', 'January 2024', 'February 2024', 'March 2024', 'April 2024', 'May 2024', 'June 2024', 'July 2024', 'August 2024', 'September 2024', 'October 2024', 'November 2024'])

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

# QUERIES

# January 2023
query_1 = "SELECT Jan_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_1)
# Fetch the result
result_1 = cursor.fetchone()

# SQL query to retrieve the residential_rate value from Jan_23 where Short_Name is 'CENECO'
query_2 = "SELECT Jan_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_2)
# Fetch the result
result_2 = cursor.fetchone()

# SQL query to retrieve the residential_rate value from Jan_23 where Short_Name is 'BLCI'
query_3 = "SELECT Jan_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_3)
# Fetch the result
result_3 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'MORE Power'
query_4 = "SELECT Jan_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_4)
# Fetch the result
result_4 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'CENECO'
query_5 = "SELECT Jan_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_5)
# Fetch the result
result_5 = cursor.fetchone()

# SQL query to retrieve the generation_rate value from Jan_23 where Short_Name is 'BLCI'
query_6 = "SELECT Jan_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_6)
# Fetch the result
result_6 = cursor.fetchone()

# SQL query to retrieve Short_Name for Jan_23_Ranking values 1 to 5
query_7 = """
SELECT Short_Name, Jan_23
FROM res_rate
WHERE Jan_23_Ranking BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking ASC;
"""
cursor.execute(query_7)
result_7 = cursor.fetchall()

query_8 = """
SELECT Short_Name, Jan_23
FROM res_rate
WHERE Jan_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking_Vis ASC;
"""

cursor.execute(query_8)
result_8 = cursor.fetchall()

query_9 = """
SELECT Short_Name, Jan_23
FROM gen_rate
WHERE Jan_23_Ranking BETWEEN 1 AND 5
ORDER BY Jan_23_Ranking ASC;
"""

cursor.execute(query_9)
result_9 = cursor.fetchall()

query_10 = """
SELECT Short_Name, Jan_23
FROM gen_rate
WHERE Jan_23_Ranking_Vis BETWEEN 1 and 5
ORDER BY Jan_23_Ranking_Vis ASC;
"""

cursor.execute(query_10)
result_10 = cursor.fetchall()

# February 2023
query_11 = "SELECT Feb_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_11)
# Fetch the result
result_11 = cursor.fetchone()

query_12 = "SELECT Feb_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_12)
# Fetch the result
result_12 = cursor.fetchone()

query_13 = "SELECT Feb_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_13)
# Fetch the result
result_13 = cursor.fetchone()

query_14 = "SELECT Feb_23 FROM gen_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_14)
# Fetch the result
result_14 = cursor.fetchone()

query_15 = "SELECT Feb_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_15)
# Fetch the result
result_15 = cursor.fetchone()

query_16 = "SELECT Feb_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_16)
# Fetch the result
result_16 = cursor.fetchone()

query_17 = """
SELECT Short_Name, Feb_23
FROM res_rate
WHERE Feb_23_Ranking BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking ASC;
"""
cursor.execute(query_17)
result_17 = cursor.fetchall()

query_18 = """
SELECT Short_Name, Feb_23
FROM res_rate
WHERE Feb_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking_Vis ASC;
"""
cursor.execute(query_18)
result_18 = cursor.fetchall()

query_19 = """
SELECT Short_Name, Feb_23
FROM gen_rate
WHERE Feb_23_Ranking BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking ASC;
"""
cursor.execute(query_19)
result_19 = cursor.fetchall()

query_20 = """
SELECT Short_Name, Feb_23
FROM gen_rate
WHERE Feb_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_23_Ranking_Vis ASC;
"""
cursor.execute(query_20)
result_20 = cursor.fetchall()

# March 2023
query_21 = "SELECT Mar_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_21)
# Fetch the result
result_21 = cursor.fetchone()

query_22 = "SELECT Mar_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_22)
# Fetch the result
result_22 = cursor.fetchone()

query_23 = "SELECT Mar_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_23)
# Fetch the result
result_23 = cursor.fetchone()

query_24 = "SELECT Mar_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_24)
# Fetch the result
result_24 = cursor.fetchone()

query_25 = "SELECT Mar_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_25)
# Fetch the result
result_25 = cursor.fetchone()

query_26 = "SELECT Mar_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_26)
# Fetch the result
result_26 = cursor.fetchone()

query_27 = """
SELECT Short_Name, Mar_23
FROM res_rate
WHERE Mar_23_Ranking BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking ASC;
"""
cursor.execute(query_27)
result_27 = cursor.fetchall()

query_28 = """
SELECT Short_Name, Mar_23
FROM res_rate
WHERE Mar_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking_Vis ASC;
"""
cursor.execute(query_28)
result_28 = cursor.fetchall()

query_29 = """
SELECT Short_Name, Mar_23
FROM gen_rate
WHERE Mar_23_Ranking BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking ASC;
"""
cursor.execute(query_29)
result_29 = cursor.fetchall()

query_30 = """
SELECT Short_Name, Mar_23
FROM gen_rate
WHERE Mar_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_23_Ranking_Vis ASC;
"""
cursor.execute(query_30)
result_30 = cursor.fetchall()

# April 2023
query_31 = "SELECT Apr_23 FROM res_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_31)
# Fetch the result
result_31 = cursor.fetchone()

query_32 = "SELECT Apr_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_32)
# Fetch the result
result_32 = cursor.fetchone()

query_33 = "SELECT Apr_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_33)
# Fetch the result
result_33 = cursor.fetchone()

query_34 = "SELECT Apr_23 FROM gen_rate WHERE Short_Name = 'MORE POWER'"
# Execute the query
cursor.execute(query_34)
# Fetch the result
result_34 = cursor.fetchone()

query_35 = "SELECT Apr_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_35)
# Fetch the result
result_35 = cursor.fetchone()

query_36 = "SELECT Apr_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_36)
# Fetch the result
result_36 = cursor.fetchone()

query_37 = """
SELECT Short_Name, Apr_23
FROM res_rate
WHERE Apr_23_Ranking BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking ASC;
"""
cursor.execute(query_37)
result_37 = cursor.fetchall()

query_38 = """
SELECT Short_Name, Apr_23
FROM res_rate
WHERE Apr_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking_Vis ASC;
"""
cursor.execute(query_38)
result_38 = cursor.fetchall()

query_39 = """
SELECT Short_Name, Apr_23
FROM gen_rate
WHERE Apr_23_Ranking BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking ASC;
"""
cursor.execute(query_39)
result_39 = cursor.fetchall()

query_40 = """
SELECT Short_Name, Apr_23
FROM gen_rate
WHERE Apr_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_23_Ranking_Vis ASC;
"""
cursor.execute(query_40)
result_40 = cursor.fetchall()

# May 2023
query_41 = "SELECT May_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_41)
# Fetch the result
result_41 = cursor.fetchone()

query_42 = "SELECT May_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_42)
# Fetch the result
result_42 = cursor.fetchone()

query_43 = "SELECT May_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_43)
# Fetch the result
result_43 = cursor.fetchone()

query_44 = "SELECT May_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_44)
# Fetch the result
result_44 = cursor.fetchone()

query_45 = "SELECT May_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_45)
# Fetch the result
result_45 = cursor.fetchone()

query_46 = "SELECT May_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_46)
# Fetch the result
result_46 = cursor.fetchone()

query_47 = """
SELECT Short_Name, May_23
FROM res_rate
WHERE May_23_Ranking BETWEEN 1 AND 5
ORDER BY May_23_Ranking ASC;
"""
cursor.execute(query_47)
result_47 = cursor.fetchall()

query_48 = """
SELECT Short_Name, May_23
FROM res_rate
WHERE May_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY May_23_Ranking_Vis ASC;
"""
cursor.execute(query_48)
result_48 = cursor.fetchall()

query_49 = """
SELECT Short_Name, May_23
FROM gen_rate
WHERE May_23_Ranking BETWEEN 1 AND 5
ORDER BY May_23_Ranking ASC;
"""
cursor.execute(query_49)
result_49 = cursor.fetchall()

query_50 = """
SELECT Short_Name, May_23
FROM gen_rate
WHERE May_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY May_23_Ranking_Vis ASC;
"""
cursor.execute(query_50)
result_50 = cursor.fetchall()

# June 2023
query_51 = "SELECT Jun_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_51)
# Fetch the result
result_51 = cursor.fetchone()

query_52 = "SELECT Jun_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_52)
# Fetch the result
result_52 = cursor.fetchone()

query_53 = "SELECT Jun_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_53)
# Fetch the result
result_53 = cursor.fetchone()

query_54 = "SELECT Jun_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_54)
# Fetch the result
result_54 = cursor.fetchone()

query_55 = "SELECT Jun_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_55)
# Fetch the result
result_55 = cursor.fetchone()

query_56 = "SELECT Jun_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_56)
# Fetch the result
result_56 = cursor.fetchone()

query_57 = """
SELECT Short_Name, Jun_23
FROM res_rate
WHERE Jun_23_Ranking BETWEEN 1 AND 5
ORDER BY Jun_23_Ranking ASC;
"""
cursor.execute(query_57)
result_57 = cursor.fetchall()

query_58 = """
SELECT Short_Name, Jun_23
FROM res_rate
WHERE Jun_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jun_23_Ranking_Vis ASC;
"""
cursor.execute(query_58)
result_58 = cursor.fetchall()

query_59 = """
SELECT Short_Name, Jun_23
FROM gen_rate
WHERE Jun_23_Ranking BETWEEN 1 AND 5
ORDER BY Jun_23_Ranking ASC;
"""
cursor.execute(query_59)
result_59 = cursor.fetchall()

query_60 = """
SELECT Short_Name, Jun_23
FROM gen_rate
WHERE Jun_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jun_23_Ranking_Vis ASC;
"""
cursor.execute(query_60)
result_60 = cursor.fetchall()

# July 2023
query_61 = "SELECT Jul_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_61)
# Fetch the result
result_61 = cursor.fetchone()

query_62 = "SELECT Jul_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_62)
# Fetch the result
result_62 = cursor.fetchone()

query_63 = "SELECT Jul_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_63)
# Fetch the result
result_63 = cursor.fetchone()

query_64 = "SELECT Jul_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_64)
# Fetch the result
result_64 = cursor.fetchone()

query_65 = "SELECT Jul_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_65)
# Fetch the result
result_65 = cursor.fetchone()

query_66 = "SELECT Jul_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_66)
# Fetch the result
result_66 = cursor.fetchone()

query_67 = """
SELECT Short_Name, Jul_23
FROM res_rate
WHERE Jul_23_Ranking BETWEEN 1 AND 5
ORDER BY Jul_23_Ranking ASC;
"""
cursor.execute(query_67)
result_67 = cursor.fetchall()

query_68 = """
SELECT Short_Name, Jul_23
FROM res_rate
WHERE Jul_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jul_23_Ranking_Vis ASC;
"""
cursor.execute(query_68)
result_68 = cursor.fetchall()

query_69 = """
SELECT Short_Name, Jul_23
FROM gen_rate
WHERE Jul_23_Ranking BETWEEN 1 AND 5
ORDER BY Jul_23_Ranking ASC;
"""
cursor.execute(query_69)
result_69 = cursor.fetchall()

query_70 = """
SELECT Short_Name, Jul_23
FROM gen_rate
WHERE Jul_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jul_23_Ranking_Vis ASC;
"""
cursor.execute(query_70)
result_70 = cursor.fetchall()

# August 2023
query_71 = "SELECT Aug_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_71)
# Fetch the result
result_71 = cursor.fetchone()

query_72 = "SELECT Aug_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_72)
# Fetch the result
result_72 = cursor.fetchone()

query_73 = "SELECT Aug_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_73)
# Fetch the result
result_73 = cursor.fetchone()

query_74 = "SELECT Aug_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_74)
# Fetch the result
result_74 = cursor.fetchone()

query_75 = "SELECT Aug_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_75)
# Fetch the result
result_75 = cursor.fetchone()

query_76 = "SELECT Aug_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_76)
# Fetch the result
result_76 = cursor.fetchone()

query_77 = """
SELECT Short_Name, Aug_23
FROM res_rate
WHERE Aug_23_Ranking BETWEEN 1 AND 5
ORDER BY Aug_23_Ranking ASC;
"""
cursor.execute(query_77)
result_77 = cursor.fetchall()

query_78 = """
SELECT Short_Name, Aug_23
FROM res_rate
WHERE Aug_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Aug_23_Ranking_Vis ASC;
"""
cursor.execute(query_78)
result_78 = cursor.fetchall()

query_79 = """
SELECT Short_Name, Aug_23
FROM gen_rate
WHERE Aug_23_Ranking BETWEEN 1 AND 5
ORDER BY Aug_23_Ranking ASC;
"""
cursor.execute(query_79)
result_79 = cursor.fetchall()

query_80 = """
SELECT Short_Name, Aug_23
FROM gen_rate
WHERE Aug_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Aug_23_Ranking_Vis ASC;
"""
cursor.execute(query_80)
result_80 = cursor.fetchall()

# September 2023
query_81 = "SELECT Sep_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_81)
# Fetch the result
result_81 = cursor.fetchone()

query_82 = "SELECT Sep_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_82)
# Fetch the result
result_82 = cursor.fetchone()

query_83 = "SELECT Sep_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_83)
# Fetch the result
result_83 = cursor.fetchone()

query_84 = "SELECT Sep_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_84)
# Fetch the result
result_84 = cursor.fetchone()

query_85 = "SELECT Sep_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_85)
# Fetch the result
result_85 = cursor.fetchone()

query_86 = "SELECT Sep_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_86)
# Fetch the result
result_86 = cursor.fetchone()

query_87 = """
SELECT Short_Name, Sep_23
FROM res_rate
WHERE Sep_23_Ranking BETWEEN 1 AND 5
ORDER BY Sep_23_Ranking ASC;
"""
cursor.execute(query_87)
result_87 = cursor.fetchall()

query_88 = """
SELECT Short_Name, Sep_23
FROM res_rate
WHERE Sep_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Sep_23_Ranking_Vis ASC;
"""
cursor.execute(query_88)
result_88 = cursor.fetchall()

query_89 = """
SELECT Short_Name, Sep_23
FROM gen_rate
WHERE Sep_23_Ranking BETWEEN 1 AND 5
ORDER BY Sep_23_Ranking ASC;
"""
cursor.execute(query_89)
result_89 = cursor.fetchall()

query_90 = """
SELECT Short_Name, Sep_23
FROM gen_rate
WHERE Sep_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Sep_23_Ranking_Vis ASC;
"""
cursor.execute(query_90)
result_90 = cursor.fetchall()

# October 2023
query_91 = "SELECT Oct_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_91)
# Fetch the result
result_91 = cursor.fetchone()

query_92 = "SELECT Oct_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_92)
# Fetch the result
result_92 = cursor.fetchone()

query_93 = "SELECT Oct_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_93)
# Fetch the result
result_93 = cursor.fetchone()

query_94 = "SELECT Oct_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_94)
# Fetch the result
result_94 = cursor.fetchone()

query_95 = "SELECT Oct_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_95)
# Fetch the result
result_95 = cursor.fetchone()

query_96 = "SELECT Oct_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_96)
# Fetch the result
result_96 = cursor.fetchone()

query_97 = """
SELECT Short_Name, Oct_23
FROM res_rate
WHERE Oct_23_Ranking BETWEEN 1 AND 5
ORDER BY Oct_23_Ranking ASC;
"""
cursor.execute(query_97)
result_97 = cursor.fetchall()

query_98 = """
SELECT Short_Name, Oct_23
FROM res_rate
WHERE Oct_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Oct_23_Ranking_Vis ASC;
"""
cursor.execute(query_98)
result_98 = cursor.fetchall()

query_99 = """
SELECT Short_Name, Oct_23
FROM gen_rate
WHERE Oct_23_Ranking BETWEEN 1 AND 5
ORDER BY Oct_23_Ranking ASC;
"""
cursor.execute(query_99)
result_99 = cursor.fetchall()

query_100 = """
SELECT Short_Name, Oct_23
FROM gen_rate
WHERE Oct_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Oct_23_Ranking_Vis ASC;
"""
cursor.execute(query_100)
result_100 = cursor.fetchall()

# November 2023
query_101 = "SELECT Nov_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_101)
# Fetch the result
result_101 = cursor.fetchone()

query_102 = "SELECT Nov_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_102)
# Fetch the result
result_102 = cursor.fetchone()

query_103 = "SELECT Nov_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_103)
# Fetch the result
result_103 = cursor.fetchone()

query_104 = "SELECT Nov_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_104)
# Fetch the result
result_104 = cursor.fetchone()

query_105 = "SELECT Nov_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_105)
# Fetch the result
result_105 = cursor.fetchone()

query_106 = "SELECT Nov_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_106)
# Fetch the result
result_106 = cursor.fetchone()

query_107 = """
SELECT Short_Name, Nov_23
FROM res_rate
WHERE Nov_23_Ranking BETWEEN 1 AND 5
ORDER BY Nov_23_Ranking ASC;
"""
cursor.execute(query_107)
result_107 = cursor.fetchall()

query_108 = """
SELECT Short_Name, Nov_23
FROM res_rate
WHERE Nov_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Nov_23_Ranking_Vis ASC;
"""
cursor.execute(query_108)
result_108 = cursor.fetchall()

query_109 = """
SELECT Short_Name, Nov_23
FROM gen_rate
WHERE Nov_23_Ranking BETWEEN 1 AND 5
ORDER BY Nov_23_Ranking ASC;
"""
cursor.execute(query_109)
result_109 = cursor.fetchall()

query_110 = """
SELECT Short_Name, Nov_23
FROM gen_rate
WHERE Nov_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Nov_23_Ranking_Vis ASC;
"""
cursor.execute(query_110)
result_110 = cursor.fetchall()

# December 2023
query_111 = "SELECT Dec_23 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_111)
# Fetch the result
result_111 = cursor.fetchone()

query_112 = "SELECT Dec_23 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_112)
# Fetch the result
result_112 = cursor.fetchone()

query_113 = "SELECT Dec_23 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_113)
# Fetch the result
result_113 = cursor.fetchone()

query_114 = "SELECT Dec_23 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_114)
# Fetch the result
result_114 = cursor.fetchone()

query_115 = "SELECT Dec_23 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_115)
# Fetch the result
result_115 = cursor.fetchone()

query_116 = "SELECT Dec_23 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_116)
# Fetch the result
result_116 = cursor.fetchone()

query_117 = """
SELECT Short_Name, Dec_23
FROM res_rate
WHERE Dec_23_Ranking BETWEEN 1 AND 5
ORDER BY Dec_23_Ranking ASC;
"""
cursor.execute(query_117)
result_117 = cursor.fetchall()

query_118 = """
SELECT Short_Name, Dec_23
FROM res_rate
WHERE Dec_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Dec_23_Ranking_Vis ASC;
"""
cursor.execute(query_118)
result_118 = cursor.fetchall()

query_119 = """
SELECT Short_Name, Dec_23
FROM gen_rate
WHERE Dec_23_Ranking BETWEEN 1 AND 5
ORDER BY Dec_23_Ranking ASC;
"""
cursor.execute(query_119)
result_119 = cursor.fetchall()

query_120 = """
SELECT Short_Name, Dec_23
FROM gen_rate
WHERE Dec_23_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Dec_23_Ranking_Vis ASC;
"""
cursor.execute(query_120)
result_120 = cursor.fetchall()

# January 2024
query_121 = "SELECT Jan_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_121)
# Fetch the result
result_121 = cursor.fetchone()

query_122 = "SELECT Jan_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_122)
# Fetch the result
result_122 = cursor.fetchone()

query_123 = "SELECT Jan_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_123)
# Fetch the result
result_123 = cursor.fetchone()

query_124 = "SELECT Jan_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_124)
# Fetch the result
result_124 = cursor.fetchone()

query_125 = "SELECT Jan_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_125)
# Fetch the result
result_125 = cursor.fetchone()

query_126 = "SELECT Jan_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_126)
# Fetch the result
result_126 = cursor.fetchone()

query_127 = """
SELECT Short_Name, Jan_24
FROM res_rate
WHERE Jan_24_Ranking BETWEEN 1 AND 5
ORDER BY Jan_24_Ranking ASC;
"""
cursor.execute(query_127)
result_127 = cursor.fetchall()

query_128 = """
SELECT Short_Name, Jan_24
FROM res_rate
WHERE Jan_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jan_24_Ranking_Vis ASC;
"""
cursor.execute(query_128)
result_128 = cursor.fetchall()

query_129 = """
SELECT Short_Name, Jan_24
FROM gen_rate
WHERE Jan_24_Ranking BETWEEN 1 AND 5
ORDER BY Jan_24_Ranking ASC;
"""
cursor.execute(query_129)
result_129 = cursor.fetchall()

query_130 = """
SELECT Short_Name, Jan_24
FROM gen_rate
WHERE Jan_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jan_24_Ranking_Vis ASC;
"""
cursor.execute(query_130)
result_130 = cursor.fetchall()

# February 2024
query_131 = "SELECT Feb_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_131)
# Fetch the result
result_131 = cursor.fetchone()

query_132 = "SELECT Feb_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_132)
# Fetch the result
result_132 = cursor.fetchone()

query_133 = "SELECT Feb_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_133)
# Fetch the result
result_133 = cursor.fetchone()

query_134 = "SELECT Feb_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_134)
# Fetch the result
result_134 = cursor.fetchone()

query_135 = "SELECT Feb_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_135)
# Fetch the result
result_135 = cursor.fetchone()

query_136 = "SELECT Feb_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_136)
# Fetch the result
result_136 = cursor.fetchone()

query_137 = """
SELECT Short_Name, Feb_24
FROM res_rate
WHERE Feb_24_Ranking BETWEEN 1 AND 5
ORDER BY Feb_24_Ranking ASC;
"""
cursor.execute(query_137)
result_137 = cursor.fetchall()

query_138 = """
SELECT Short_Name, Feb_24
FROM res_rate
WHERE Feb_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_24_Ranking_Vis ASC;
"""
cursor.execute(query_138)
result_138 = cursor.fetchall()

query_139 = """
SELECT Short_Name, Feb_24
FROM gen_rate
WHERE Feb_24_Ranking BETWEEN 1 AND 5
ORDER BY Feb_24_Ranking ASC;
"""
cursor.execute(query_139)
result_139 = cursor.fetchall()

query_140 = """
SELECT Short_Name, Feb_24
FROM gen_rate
WHERE Feb_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Feb_24_Ranking_Vis ASC;
"""
cursor.execute(query_140)
result_140 = cursor.fetchall()

# March 2024
query_141 = "SELECT Mar_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_141)
# Fetch the result
result_141 = cursor.fetchone()

query_142 = "SELECT Mar_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_142)
# Fetch the result
result_142 = cursor.fetchone()

query_143 = "SELECT Mar_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_143)
# Fetch the result
result_143 = cursor.fetchone()

query_144 = "SELECT Mar_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_144)
# Fetch the result
result_144 = cursor.fetchone()

query_145 = "SELECT Mar_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_145)
# Fetch the result
result_145 = cursor.fetchone()

query_146 = "SELECT Mar_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_146)
# Fetch the result
result_146 = cursor.fetchone()

query_147 = """
SELECT Short_Name, Mar_24
FROM res_rate
WHERE Mar_24_Ranking BETWEEN 1 AND 5
ORDER BY Mar_24_Ranking ASC;
"""
cursor.execute(query_147)
result_147 = cursor.fetchall()

query_148 = """
SELECT Short_Name, Mar_24
FROM res_rate
WHERE Mar_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_24_Ranking_Vis ASC;
"""
cursor.execute(query_148)
result_148 = cursor.fetchall()

query_149 = """
SELECT Short_Name, Mar_24
FROM gen_rate
WHERE Mar_24_Ranking BETWEEN 1 AND 5
ORDER BY Mar_24_Ranking ASC;
"""
cursor.execute(query_149)
result_149 = cursor.fetchall()

query_150 = """
SELECT Short_Name, Mar_24
FROM gen_rate
WHERE Mar_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Mar_24_Ranking_Vis ASC;
"""
cursor.execute(query_150)
result_150 = cursor.fetchall()

# April 2024
query_151 = "SELECT Apr_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_151)
# Fetch the result
result_151 = cursor.fetchone()

query_152 = "SELECT Apr_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_152)
# Fetch the result
result_152 = cursor.fetchone()

query_153 = "SELECT Apr_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_153)
# Fetch the result
result_153 = cursor.fetchone()

query_154 = "SELECT Apr_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_154)
# Fetch the result
result_154 = cursor.fetchone()

query_155 = "SELECT Apr_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_155)
# Fetch the result
result_155 = cursor.fetchone()

query_156 = "SELECT Apr_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_156)
# Fetch the result
result_156 = cursor.fetchone()

query_157 = """
SELECT Short_Name, Apr_24
FROM res_rate
WHERE Apr_24_Ranking BETWEEN 1 AND 5
ORDER BY Apr_24_Ranking ASC;
"""
cursor.execute(query_157)
result_157 = cursor.fetchall()

query_158 = """
SELECT Short_Name, Apr_24
FROM res_rate
WHERE Apr_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_24_Ranking_Vis ASC;
"""
cursor.execute(query_158)
result_158 = cursor.fetchall()

query_159 = """
SELECT Short_Name, Apr_24
FROM gen_rate
WHERE Apr_24_Ranking BETWEEN 1 AND 5
ORDER BY Apr_24_Ranking ASC;
"""
cursor.execute(query_159)
result_159 = cursor.fetchall()

query_160 = """
SELECT Short_Name, Apr_24
FROM gen_rate
WHERE Apr_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Apr_24_Ranking_Vis ASC;
"""
cursor.execute(query_160)
result_160 = cursor.fetchall()

# May 2024
query_161 = "SELECT May_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_161)
# Fetch the result
result_161 = cursor.fetchone()

query_162 = "SELECT May_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_162)
# Fetch the result
result_162 = cursor.fetchone()

query_163 = "SELECT May_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_163)
# Fetch the result
result_163 = cursor.fetchone()

query_164 = "SELECT May_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_164)
# Fetch the result
result_164 = cursor.fetchone()

query_165 = "SELECT May_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_165)
# Fetch the result
result_165 = cursor.fetchone()

query_166 = "SELECT May_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_166)
# Fetch the result
result_166 = cursor.fetchone()

query_167 = """
SELECT Short_Name, May_24
FROM res_rate
WHERE May_24_Ranking BETWEEN 1 AND 5
ORDER BY May_24_Ranking ASC;
"""
cursor.execute(query_167)
result_167 = cursor.fetchall()

query_168 = """
SELECT Short_Name, May_24
FROM res_rate
WHERE May_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY May_24_Ranking_Vis ASC;
"""
cursor.execute(query_168)
result_168 = cursor.fetchall()

query_169 = """
SELECT Short_Name, May_24
FROM gen_rate
WHERE May_24_Ranking BETWEEN 1 AND 5
ORDER BY May_24_Ranking ASC;
"""
cursor.execute(query_169)
result_169 = cursor.fetchall()

query_170 = """
SELECT Short_Name, May_24
FROM gen_rate
WHERE May_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY May_24_Ranking_Vis ASC;
"""
cursor.execute(query_170)
result_170 = cursor.fetchall()

# June 2024
query_171 = "SELECT Jun_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_171)
# Fetch the result
result_171 = cursor.fetchone()

query_172 = "SELECT Jun_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_172)
# Fetch the result
result_172 = cursor.fetchone()

query_173 = "SELECT Jun_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_173)
# Fetch the result
result_173 = cursor.fetchone()

query_174 = "SELECT Jun_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_174)
# Fetch the result
result_174 = cursor.fetchone()

query_175 = "SELECT Jun_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_175)
# Fetch the result
result_175 = cursor.fetchone()

query_176 = "SELECT Jun_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_176)
# Fetch the result
result_176 = cursor.fetchone()

query_177 = """
SELECT Short_Name, Jun_24
FROM res_rate
WHERE Jun_24_Ranking BETWEEN 1 AND 5
ORDER BY Jun_24_Ranking ASC;
"""
cursor.execute(query_177)
result_177 = cursor.fetchall()

query_178 = """
SELECT Short_Name, Jun_24
FROM res_rate
WHERE Jun_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jun_24_Ranking_Vis ASC;
"""
cursor.execute(query_178)
result_178 = cursor.fetchall()

query_179 = """
SELECT Short_Name, Jun_24
FROM gen_rate
WHERE Jun_24_Ranking BETWEEN 1 AND 5
ORDER BY Jun_24_Ranking ASC;
"""
cursor.execute(query_179)
result_179 = cursor.fetchall()

query_180 = """
SELECT Short_Name, Jun_24
FROM gen_rate
WHERE Jun_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jun_24_Ranking_Vis ASC;
"""
cursor.execute(query_180)
result_180 = cursor.fetchall()

# July 2024
query_181 = "SELECT Jul_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_181)
# Fetch the result
result_181 = cursor.fetchone()

query_182 = "SELECT Jul_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_182)
# Fetch the result
result_182 = cursor.fetchone()

query_183 = "SELECT Jul_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_183)
# Fetch the result
result_183 = cursor.fetchone()

query_184 = "SELECT Jul_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_184)
# Fetch the result
result_184 = cursor.fetchone()

query_185 = "SELECT Jul_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_185)
# Fetch the result
result_185 = cursor.fetchone()

query_186 = "SELECT Jul_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_186)
# Fetch the result
result_186 = cursor.fetchone()

query_187 = """
SELECT Short_Name, Jul_24
FROM res_rate
WHERE Jul_24_Ranking BETWEEN 1 AND 5
ORDER BY Jul_24_Ranking ASC;
"""
cursor.execute(query_187)
result_187 = cursor.fetchall()

query_188 = """
SELECT Short_Name, Jul_24
FROM res_rate
WHERE Jul_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jul_24_Ranking_Vis ASC;
"""
cursor.execute(query_188)
result_188 = cursor.fetchall()

query_189 = """
SELECT Short_Name, Jul_24
FROM gen_rate
WHERE Jul_24_Ranking BETWEEN 1 AND 5
ORDER BY Jul_24_Ranking ASC;
"""
cursor.execute(query_189)
result_189 = cursor.fetchall()

query_190 = """
SELECT Short_Name, Jul_24
FROM gen_rate
WHERE Jul_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Jul_24_Ranking_Vis ASC;
"""
cursor.execute(query_190)
result_190 = cursor.fetchall()

# August 2024
query_191 = "SELECT Aug_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_191)
# Fetch the result
result_191 = cursor.fetchone()

query_192 = "SELECT Aug_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_192)
# Fetch the result
result_192 = cursor.fetchone()

query_193 = "SELECT Aug_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_193)
# Fetch the result
result_193 = cursor.fetchone()

query_194 = "SELECT Aug_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_194)
# Fetch the result
result_194 = cursor.fetchone()

query_195 = "SELECT Aug_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_195)
# Fetch the result
result_195 = cursor.fetchone()

query_196 = "SELECT Aug_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_196)
# Fetch the result
result_196 = cursor.fetchone()

query_197 = """
SELECT Short_Name, Aug_24
FROM res_rate
WHERE Aug_24_Ranking BETWEEN 1 AND 5
ORDER BY Aug_24_Ranking ASC;
"""
cursor.execute(query_197)
result_197 = cursor.fetchall()

query_198 = """
SELECT Short_Name, Aug_24
FROM res_rate
WHERE Aug_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Aug_24_Ranking_Vis ASC;
"""
cursor.execute(query_198)
result_198 = cursor.fetchall()

query_199 = """
SELECT Short_Name, Aug_24
FROM gen_rate
WHERE Aug_24_Ranking BETWEEN 1 AND 5
ORDER BY Aug_24_Ranking ASC;
"""
cursor.execute(query_199)
result_199 = cursor.fetchall()

query_200 = """
SELECT Short_Name, Aug_24
FROM gen_rate
WHERE Aug_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Aug_24_Ranking_Vis ASC;
"""
cursor.execute(query_200)
result_200 = cursor.fetchall()

# September 2024
query_201 = "SELECT Sep_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_201)
# Fetch the result
result_201 = cursor.fetchone()

query_202 = "SELECT Sep_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_202)
# Fetch the result
result_202 = cursor.fetchone()

query_203 = "SELECT Sep_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_203)
# Fetch the result
result_203 = cursor.fetchone()

query_204 = "SELECT Sep_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_204)
# Fetch the result
result_204 = cursor.fetchone()

query_205 = "SELECT Sep_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_205)
# Fetch the result
result_205 = cursor.fetchone()

query_206 = "SELECT Sep_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_206)
# Fetch the result
result_206 = cursor.fetchone()

query_207 = """
SELECT Short_Name, Sep_24
FROM res_rate
WHERE Sep_24_Ranking BETWEEN 1 AND 5
ORDER BY Sep_24_Ranking ASC;
"""
cursor.execute(query_207)
result_207 = cursor.fetchall()

query_208 = """
SELECT Short_Name, Sep_24
FROM res_rate
WHERE Sep_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Sep_24_Ranking_Vis ASC;
"""
cursor.execute(query_208)
result_208 = cursor.fetchall()

query_209 = """
SELECT Short_Name, Sep_24
FROM gen_rate
WHERE Sep_24_Ranking BETWEEN 1 AND 5
ORDER BY Sep_24_Ranking ASC;
"""
cursor.execute(query_209)
result_209 = cursor.fetchall()

query_210 = """
SELECT Short_Name, Sep_24
FROM gen_rate
WHERE Sep_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Sep_24_Ranking_Vis ASC;
"""
cursor.execute(query_210)
result_210 = cursor.fetchall()

# October 2024
query_211 = "SELECT Oct_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_211)
# Fetch the result
result_211 = cursor.fetchone()

query_212 = "SELECT Oct_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_212)
# Fetch the result
result_212 = cursor.fetchone()

query_213 = "SELECT Oct_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_213)
# Fetch the result
result_213 = cursor.fetchone()

query_214 = "SELECT Oct_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_214)
# Fetch the result
result_214 = cursor.fetchone()

query_215 = "SELECT Oct_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_215)
# Fetch the result
result_215 = cursor.fetchone()

query_216 = "SELECT Oct_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_216)
# Fetch the result
result_216 = cursor.fetchone()

query_217 = """
SELECT Short_Name, Oct_24
FROM res_rate
WHERE Oct_24_Ranking BETWEEN 1 AND 5
ORDER BY Oct_24_Ranking ASC;
"""
cursor.execute(query_217)
result_217 = cursor.fetchall()

query_218 = """
SELECT Short_Name, Oct_24
FROM res_rate
WHERE Oct_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Oct_24_Ranking_Vis ASC;
"""
cursor.execute(query_218)
result_218 = cursor.fetchall()

query_219 = """
SELECT Short_Name, Oct_24
FROM gen_rate
WHERE Oct_24_Ranking BETWEEN 1 AND 5
ORDER BY Oct_24_Ranking ASC;
"""
cursor.execute(query_219)
result_219 = cursor.fetchall()

query_220 = """
SELECT Short_Name, Oct_24
FROM gen_rate
WHERE Oct_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Oct_24_Ranking_Vis ASC;
"""
cursor.execute(query_220)
result_220 = cursor.fetchall()

# November 2024
query_221 = "SELECT Nov_24 FROM res_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_221)
# Fetch the result
result_221 = cursor.fetchone()

query_222 = "SELECT Nov_24 FROM res_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_222)
# Fetch the result
result_222 = cursor.fetchone()

query_223 = "SELECT Nov_24 FROM res_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_223)
# Fetch the result
result_223 = cursor.fetchone()

query_224 = "SELECT Nov_24 FROM gen_rate WHERE Short_Name = 'MORE Power'"
# Execute the query
cursor.execute(query_224)
# Fetch the result
result_224 = cursor.fetchone()

query_225 = "SELECT Nov_24 FROM gen_rate WHERE Short_Name = 'CENECO'"
# Execute the query
cursor.execute(query_225)
# Fetch the result
result_225 = cursor.fetchone()

query_226 = "SELECT Nov_24 FROM gen_rate WHERE Short_Name = 'BLCI'"
# Execute the query
cursor.execute(query_226)
# Fetch the result
result_226 = cursor.fetchone()

query_227 = """
SELECT Short_Name, Nov_24
FROM res_rate
WHERE Nov_24_Ranking BETWEEN 1 AND 5
ORDER BY Nov_24_Ranking ASC;
"""
cursor.execute(query_227)
result_227 = cursor.fetchall()

query_228 = """
SELECT Short_Name, Nov_24
FROM res_rate
WHERE Nov_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Nov_24_Ranking_Vis ASC;
"""
cursor.execute(query_228)
result_228 = cursor.fetchall()

query_229 = """
SELECT Short_Name, Nov_24
FROM gen_rate
WHERE Nov_24_Ranking BETWEEN 1 AND 5
ORDER BY Nov_24_Ranking ASC;
"""
cursor.execute(query_229)
result_229 = cursor.fetchall()

query_230 = """
SELECT Short_Name, Nov_24
FROM gen_rate
WHERE Nov_24_Ranking_Vis BETWEEN 1 AND 5
ORDER BY Nov_24_Ranking_Vis ASC;
"""
cursor.execute(query_230)
result_230 = cursor.fetchall()

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
            "Generation Rate": [row[1] for row in result_9] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_10], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_10] # Extract Residential Rate
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
            "Generation Rate": [row[1] for row in result_19] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_20], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_20] # Extract Residential Rate
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
            "Generation Rate": [row[1] for row in result_29] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_30], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_30] # Extract Residential Rate
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
            "Generation Rate": [row[1] for row in result_39] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_40], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_40] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'May 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_41[0], result_42[0], result_43[0]],
        "Generation Rate": [result_44[0], result_45[0], result_46[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_47], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_47] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_48], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_48] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_49], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_49] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_50], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_50] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'June 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_51[0], result_52[0], result_53[0]],
        "Generation Rate": [result_54[0], result_55[0], result_56[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_57], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_57] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_58], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_58] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_59], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_59] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_60], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_60] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'July 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_61[0], result_62[0], result_63[0]],
        "Generation Rate": [result_64[0], result_65[0], result_66[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_67], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_67] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_68], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_68] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_69], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_69] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_70], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_70] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'August 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_71[0], result_72[0], result_73[0]],
        "Generation Rate": [result_74[0], result_75[0], result_76[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_77], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_77] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_78], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_78] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_79], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_79] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_80], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_80] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'September 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_81[0], result_82[0], result_83[0]],
        "Generation Rate": [result_84[0], result_85[0], result_86[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_87], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_87] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_88], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_88] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_89], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_89] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_90], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_90] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'October 2023':
        # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_91[0], result_92[0], result_93[0]],
        "Generation Rate": [result_94[0], result_95[0], result_96[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_97], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_97] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_98], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_98] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_99], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_99] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_100], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_100] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'November 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_101[0], result_102[0], result_103[0]],
        "Generation Rate": [result_104[0], result_105[0], result_106[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_107], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_107] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_108], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_108] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_109], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_109] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_110], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_110] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'December 2023':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_111[0], result_112[0], result_113[0]],
        "Generation Rate": [result_114[0], result_115[0], result_116[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_117], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_117] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_118], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_118] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_119], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_119] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_120], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_120] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'January 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_121[0], result_122[0], result_123[0]],
        "Generation Rate": [result_124[0], result_125[0], result_126[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_127], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_127] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_128], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_128] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_129], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_129] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_130], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_130] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'February 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_131[0], result_132[0], result_133[0]],
        "Generation Rate": [result_134[0], result_135[0], result_136[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_137], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_137] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_138], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_138] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_139], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_139] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_140], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_140] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'March 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_141[0], result_142[0], result_143[0]],
        "Generation Rate": [result_144[0], result_145[0], result_146[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_147], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_147] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_148], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_148] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_149], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_149] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_150], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_150] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'April 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_151[0], result_152[0], result_153[0]],
        "Generation Rate": [result_154[0], result_155[0], result_156[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_157], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_157] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_158], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_158] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_159], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_159] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_160], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_160] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'May 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_161[0], result_162[0], result_163[0]],
        "Generation Rate": [result_164[0], result_165[0], result_166[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_167], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_167] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_168], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_168] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_169], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_169] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_170], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_170] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'June 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_171[0], result_172[0], result_173[0]],
        "Generation Rate": [result_174[0], result_175[0], result_176[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_177], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_177] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_178], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_178] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_179], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_179] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_180], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_180] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'July 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_181[0], result_182[0], result_183[0]],
        "Generation Rate": [result_184[0], result_185[0], result_186[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_187], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_187] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_188], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_188] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_189], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_189] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_190], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_190] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'August 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_191[0], result_192[0], result_193[0]],
        "Generation Rate": [result_194[0], result_195[0], result_196[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_197], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_197] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_198], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_198] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_199], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_199] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_200], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_200] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'September 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_201[0], result_202[0], result_203[0]],
        "Generation Rate": [result_204[0], result_205[0], result_206[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_207], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_207] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_208], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_208] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_209], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_209] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_210], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_210] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

elif month_selected == 'October 2024':
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [result_211[0], result_212[0], result_213[0]],
        "Generation Rate": [result_214[0], result_215[0], result_216[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_217], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_217] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_218], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_218] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_219], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_219] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_220], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_220] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)

else:
    # 1st Table
    st.markdown("Residential Rate and Generation Rate of MORE Power, NEPC, and BLCI")
    table_1 = {
        "": ["MORE", "NEPC", "BLCI"],
        "Residential Rate": [11.8092, result_222[0], result_223[0]],
        "Generation Rate": [result_224[0], result_225[0], result_226[0]]
    }

    df = pd.DataFrame(table_1)
    st.dataframe(df, hide_index=True)

    # Table 2 and Table 3 side-by-side
    col1, col2 = st.columns(2)

    # 2nd Table
    with col1:
        st.markdown("Top 5 Lowest Residential Rate in the Philippines")
        table_2 = {
            "DU": [row[0] for row in result_227], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_227] # Extract Residential Rate
        }

        df_2 = pd.DataFrame(table_2)
        st.dataframe(df_2, hide_index=True)

    # 3rd Table
    with col2:
        st.markdown("Top 5 Lowest Residential Rate in the Visayas")
        table_3 = {
            "DU": [row[0] for row in result_228], # Extract Short_Name
            "Residential Rate": [row[1] for row in result_228] # Extract Residential Rate
        }

        df_3 = pd.DataFrame(table_3)
        st.dataframe(df_3, hide_index=True)

    # Table 4 and Table 5 side-by-side
    col3, col4 = st.columns(2)

    # 4th Table
    with col3:
        st.markdown("Top 5 Lowest Generation Rate in the Philippines")
        table_4 = {
            "DU": [row[0] for row in result_229], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_229] # Extract Residential Rate
        }

        df_4 = pd.DataFrame(table_4)
        st.dataframe(df_4, hide_index=True)

    # 5th Table
    with col4:
        st.markdown("Top 5 Lowest Generation Rate in the Visayas")
        table_5 = {
            "DU": [row[0] for row in result_230], # Extract Short_Name
            "Generation Rate": [row[1] for row in result_230] # Extract Residential Rate
        }

        df_5 = pd.DataFrame(table_5)
        st.dataframe(df_5, hide_index=True)