import streamlit as st
import plotly.express as px
from backend import get_data

st.title('5-Day Weather Forecast')

place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
type  = st.selectbox('Select data to view', ('Temperature', 'Sky conditions'))

st.subheader(f'{option} for the next {days} days in {place}')

d, t = get_data(place, days, type)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)


