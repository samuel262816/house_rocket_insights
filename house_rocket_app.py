from functools import cache
from turtle import width
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config( page_title='House Rocket App', page_icon=':bar_chart:', layout= 'wide')

# Escondendo estilo streamlit
hide_st_style = '''
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
'''
st.markdown( hide_st_style, unsafe_allow_html= True)

# ------------------------------------------------------------------------------------------

#Carregando datasets
df_buy = pd.read_csv('dataset/data_address.csv')
df_sell = pd.read_csv('dataset/sales_report.csv')
aux = df_buy[['id', 'grade', 'view']]
df_sell = pd.merge( df_sell, aux, how= 'left', on= 'id')

#gráficos dos insights
df = pd.read_csv('dataset/df_eda.csv')

# ------------------------------------------------------------------------------------------
# FUNÇÕES
# ------------------------------------------------------------------------------------------

def houses_grade_graph( df ):
    below_10 = df[ df['grade'] <= 10 ]['price'].mean()
    above_10 = df[ df['grade'] > 10 ]['price'].mean()
    aux4 = pd.DataFrame( {'grades': ['below_10', 'above_10'], 'price': [below_10, above_10] } )

    fig_design = px.bar(aux4, x='grades', y='price', template= 'plotly_white', color_discrete_sequence=['#229BE2'] )
    fig_design.update_layout( plot_bgcolor= 'rgba(0,0,0,0)', yaxis= (dict( showgrid = False)) )
    return fig_design


def view_houses_graph( df ):
    aux3= df[['view', 'price']].groupby('view').mean().reset_index()

    fig = px.bar(aux3, x='view', y='price', template= 'plotly_white', color_discrete_sequence=['#229BE2'] )
    fig.update_layout( plot_bgcolor= 'rgba(0,0,0,0)', yaxis= (dict( showgrid = False)) )
    return fig


def new_houses_graph( df ):
    renovated = df[ df['yr_renovated'] > 0 ] ['price'].mean()
    new = df[ df['yr_renovated'] == 0 ] ['price'].mean()
    aux2 = pd.DataFrame( {'attributes':['renovated', 'new'] , 'price': [renovated, new] } )

    fig = px.bar(aux2, x='attributes', y='price', template= 'plotly_white', color_discrete_sequence=['#229BE2'] )
    fig.update_layout( plot_bgcolor= 'rgba(0,0,0,0)' , yaxis= (dict( showgrid = False)))
    return fig


def water_front_graph( df ):
    aux1 = df[['waterfront', 'price']].groupby('waterfront').mean().reset_index()
    fig = px.bar(aux1, x='waterfront', y='price', template= 'plotly_white', color_discrete_sequence=['#229BE2'] )
    fig.update_layout( plot_bgcolor= 'rgba(0,0,0,0)', yaxis= (dict( showgrid = False)) )
    return fig


def show_map( df_buy ):
    houses = df_buy[ (df_buy['price'] < price_filter) & (df_buy['grade'] >= grade_filter) ] [['id', 'price', 'lat', 'long']]
    fig = px.scatter_mapbox(houses,
                            lat = 'lat', lon = 'long', size = 'price', size_max = 15, zoom = 10)

    fig.update_layout( mapbox_style = 'open-street-map')
    fig.update_layout( height = 500, width= 1000, margin = {'r':0, 'l':0, 't':0, 'b':0} )
    return fig


# ------------------------------------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------------------------------------

image = Image.open( 'logo.png' )
st.sidebar.image( image, width= 200)

#criando filtros
st.sidebar.markdown('# Commercial Options')

#filtro escolha do relatório
report_filter = st.sidebar.radio( "Choose the report", ('Purchase Report', 'Sales Report') )

st.sidebar.markdown( '''___''')

#filtro preço maximo - compra
price_filter = st.sidebar.slider(
    'Maximum Price', min_value= 100000, max_value= 2000000, value= 500000 )

#filtro grade minima
grade_filter = st.sidebar.slider(
    'Minimun Grade', min_value= 0, max_value= 10, value= 5 )
    
# ------------------------------------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------------------------------------

#Titulos
st.markdown( '# House Rocket Company')
st.markdown('##### Welcome to House Rocket Data Analysis')
st.markdown( """___""")
   
#Tabelas de compra ou venda
if report_filter == 'Purchase Report':
    st.header(':chart_with_upwards_trend: Purchase Report')
    df_buy_filtered = df_buy[ (df_buy['price'] < price_filter) & (df_buy['grade'] >= grade_filter) ] [['id', 'zipcode', 'grade', 'view', 'median_price', 'price', ]]
    st.dataframe( df_buy_filtered, width=800 )

else:
    st.header(':chart_with_upwards_trend: Sales Report')
    df_sell_filtered = df_sell[ (df_sell['price'] < price_filter) & (df_sell['grade'] >= grade_filter) ] [['id', 'zipcode', 'season', 'median_price', 'price', 'sell_price', 'profit']]
    st.dataframe( df_sell_filtered, width=800 )

st.markdown( """___""")
    
# ------------------------------------------------------------------------------------------

# Mapa
st.markdown('# House Rocket Map')
st.markdown('##### Check below to see the map')

is_map = st.checkbox( 'Display Map' )

if is_map:
    fig = show_map( df_buy )
    st.plotly_chart(fig)

st.markdown( """___""")

# ------------------------------------------------------------------------------------------

st.header(':bar_chart: House Rocket Insights')
c1, c2 = st.columns( (1, 1) )

#gráfico waterfront
c1.subheader('Waterfront houses')
c1.markdown('Waterfront houses are on average 221% more expensive')
fig = water_front_graph( df )
c1.plotly_chart( fig )

#gráfico New Houses
c2.subheader('New houses')
c2.markdown('New houses are around 30% cheaper than the renovated ones')
fig = new_houses_graph( df )
c2.plotly_chart( fig )

# ------------------------------------------------------------------------------------------

c3, c4 = st.columns( (1,1) )

#gráfico View Houses
c3.subheader('View houses')
c3.markdown(' Houses with excellent views (grade 4) are around 51% more expensive')
fig = view_houses_graph( df )
c3.plotly_chart( fig )


#gráfico Houses grade design
c4.subheader('Houses grade design')
c4.markdown(' Houses with grade above 10 are on average 227% more expensive')
fig_design = houses_grade_graph( df )
c4.plotly_chart( fig_design )


