import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title('5-Day Weather Forecast')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
type  = st.selectbox('Select data to view', ('Temperature',
                                             'Sky conditions'))

if days < 2:
    plural = ''
else:
    plural = 's'

st.subheader(f'{type} for the next {days} day{plural} in {place}')

# Get the temperature/sky data

if place: # <-- Indicates to only retrieve data if place string exists

    try:
        filtered_data = get_data(place, days)

    # VISUALIZE DATA

    # Plot graph only if the type 'Temperature' is requested
        if type == 'Temperature':
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

    # Show images only if the type 'Sky conditions' is  requested
        if type == 'Sky conditions':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

    # Handle error when user enters an invalid place name
    except KeyError:
        st.write('Please enter a valid place name.')


