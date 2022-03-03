import streamlit as st
import pandas as pd
import plotly.express as px


'''
# Club and Nationality App

This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''
df = st.cache(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
work_rate = st.sidebar.multiselect('Show Player with work rate?', df['Work Rate'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities)) & (df['Work Rate'].isin(work_rate))]
new_df.reset_index(drop = True, inplace = True)
st.write(new_df)

# Create distplot with custom bin_size
try:
    fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')
    # fig2 = px.scatter_polar(new_df, r='SprintSpeed', theta='Acceleration', color = 'Name', template='plotly_dark')
    # px.treemap(new_df, )
    # px.scatter_ternary(new_df, )
    fig2 = px.scatter_polar(new_df, r = 'SprintSpeed', theta='Acceleration', template='plotly_dark', color='Name')
    '''
    ### Here is a simple chart between player age and overall
    '''
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
except KeyError as e:
    print("\nNothing to show on the graph right now!\n")