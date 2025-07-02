import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import date
import matplotlib.pyplot as plt

st.set_page_config(
    layout="wide",
    page_title = "Weather Forecast Prediction",
    menu_items = {
    'about' : "Welcome to Weather Forecast by Tortrong Yang"
    }
)

api_key = "fb55caf2f53d7d57fd62c4ee236598f8"
api_key1 = "0990b94305mshfdce560ea8ec110p11e22djsn40b35c1c835e"

#st.title("Weather Forecast Prediction")
#st.subheader("Forecast for Every Three Hours in 6 Days")
#st.subheader("Look up any city's latest weather condition around the world")
st.image('media/banner.png')
sidebar = st.sidebar.selectbox(
    "Options",
    ["Weather Forecast ", "United States Annual Weather", "Test Time"]
)
if sidebar == "Weather Forecast ":
    city1 = st.header("Enter a city 🏙")
    city = st.text_input("Type here")
    if st.button("Predict forecast"):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=fb55caf2f53d7d57fd62c4ee236598f8"
            response = requests.get(url).json()
            data = requests.get(url).json()
            # st.write(data)

            today = date.today()
            if data["cod"] == "200":
                st.header(
                    "Weather Forecast Prediction generates the latest weather condition of a city for every 3 hours up to 6 days.")
                d2 = today.strftime(" %B %d, %Y")
                st.header("Today is...")
                st.header(d2)
                five_days_forecast = data["list"]
                col1, col2 = st.columns(2)
                for weather_forecast in five_days_forecast:
                    st.success("The city's information is found!", icon="✅")

                    date = weather_forecast["dt_txt"]
                    weather_description = weather_forecast["weather"][0]["description"]
                    temperature = weather_forecast["main"]["temp"] * (9 / 5) - 459.67
                    feels_like = weather_forecast["main"]["feels_like"] * (9 / 5) - 459.67
                    humidity = weather_forecast["main"]["humidity"]
                    wind_speed = weather_forecast["wind"]["speed"]

                    if "few clouds" in weather_description:
                        st.image('media/fewClouds.jpg')
                    if "clear sky" in weather_description:
                        st.image('media/clearSky.jpg')
                    if "broken clouds" in weather_description:
                        st.image('media/brokenClouds.jpg')
                    if "scattered clouds" in weather_description:
                        st.image('media/scatteredClouds.jpg')
                    if "overcast clouds" in weather_description:
                        st.image('media/overcastClouds (2).jpg')
                    if "thunderstorm" in weather_description:
                        st.image('media/thunderstorm.jpg')
                    if "drizzle" in weather_description:
                        st.image('media/drizzleClouds.jpg')
                    if "rain" in weather_description:
                        st.image('media/rainCity.jpg')
                    if "snow" in weather_description:
                        st.image('media/snowCity.jpg')
                    st.header(f"The weather in {city} is {weather_description}.")
                    st.write("\n")
                    st.subheader(f"Current Day/Military Time: {date}")
                    st.write("\n")
                    st.subheader(f"Temperature🌡️{temperature: .2f}°F")
                    st.write("\n")
                    st.subheader(f"Feels like🔥❄️ {feels_like: .2f} °F")
                    st.write("\n")
                    st.subheader(f"Humidity🧊 {humidity}%")
                    st.write("\n")
                    st.subheader(f"Wind Speed💨 {wind_speed} m/s")
            else:
                st.error("Please enter a valid city.", icon="🚨")
        else:
            st.warning("No city was entered. Try again")
if sidebar == "Weather Forecast ":
    col1, col2= st.columns(2)
    with col2:
        st.image('media/globe.jpg')
    with col1:
        st.subheader("List of Cities on The Globe")
        cities = pd.read_json('media/city.list.json')
        st.dataframe(cities)
        st.caption(" ")
        st.write("\n")

elif sidebar == "United States Annual Weather":
    col1, col2 = st.columns(2)
    st.write("\n")
    st.title("What is the Average Temperatures in Each Month for the US?")
    st.image('media/avgTemp1.png')
    st.subheader(
        "The average temperatures for the United States falls between 41°F to 79°F or 5°C to 26°C annually.")
    st.image('media/myplot.png')
    st.caption("Line Chart of The Highest and Lowest Temperature Monthly")
    st.subheader("Although the temperature varies each year,"
        " the months of July and August are the warmest at 79.9°F or 26°C while December and January is the lowest at 40°F or 4°C.")

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [40.2, 41.8, 47.4, 56.3, 65, 71.3, 78.5, 79.5, 73.6, 64.3, 54.2, 44.4]
    plt.plot(x, y, marker='*')
    plt.bar(x, y, width=0.5, color='red')
    plt.title('Average Temperature Per Month in the US')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°F)')
    plt.grid(True)
    plt.show()

    st.title("Average Precipitation per Month")
    st.subheader("The month with the least amount of precipitation exhibiting only an "
             "average of 58 mm or 2.3 inch of rainfall is December.")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [2, 2, 4, 4, 5, 11, 8, 6, 7, 5, 2, 2]
    plt.plot(x, y, color='green')
    plt.bar(x, y)
    plt.xlabel('Month')
    plt.ylabel('Precipitation/ Rainfall (inches)')
    plt.title("Average Precipitation/Rainfall in the US per Month")
    plt.show()
    st.image('media/barPlot.png')
    st.caption("Bar chart of the average rainfall in the US with June being the peak month of the highest precipitation.")
    st.subheader("The warmest months of June and July tend to have the highest rainfall levels due to warmer climate.")
    if map:
        df = pd.DataFrame(
            np.array([
                [33.4484, -112.0740],
                [21.3099, -157.8581],
                [36.1716, -115.1391],
                [25.7617, -80.1918],
                [27.9517, -82.4588],
                [32.2540, -110.9742],
                [30.2672, -97.7431],
                [29.4252, -98.4946],
                [29.9509, -90.0758],
                [32.7767, -96.7970],

                [64.8353, -147.7767],
                [61.2174, -149.8631],
                [47.9252, -97.0328],
                [46.0038, -112.5348],
                [46.5476, -87.3956],
                [46.7867, -92.1004],
                [48.1469, -103.6179],
                [46.8958, -102.7896],
                [58.3058, -134.4333],
                [46.8737, -96.7678],
            ]),
            columns=["lat", "lon"],
        )

        st.title("Where are the coldest and warmest places on the US map?")
        st.subheader("The coldest cities are located in the north from Alaska to Michigan while"
                     " the warmest cities are in the south from Hawaii to Florida.")
        st.map(df, size=10, color="#00f900")
        st.caption("Map of where the hottest and coldest cities in the United States")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Top 10 Coldest and Warmest US Citites")
            hot_cold_cities = pd.DataFrame(
                {
                    "City": ["Anchorage","Fairbanks", "Juneau","Butte","Williston", "Dickinson","Grand Forks", "Moorhead", "Duluth",
                                        "Marquette", "Honolulu", "Las Vegas", "Phoenix", "Tucson", "San Antonio", "Austin", "Dallas",
                                           "New Orleans", "Tampa", "Miami"],
                    "State": ["Alaska", "Alaska", "Alaska", "Montana", "North Dakota",  "North Dakota", "North Dakota", "Minnesota", "Minnesota", "Michigan",
                              "Hawaii", "Nevada", "Arizona", "Arizona", "Texas", "Texas", "Texas", "Louisiana","Florida", "Florida"
                              ],
                    "Temperature °F": [37.6, 28.3, 42.1, 40.1,41.7, 42.0, 39.8, 42.2, 40.6, 40.4, 85, 81, 87, 84, 80, 81, 78, 79, 83, 84 ]
                }
            )
            st.dataframe(hot_cold_cities)
        with col2:
            st.image('media/cold_weather.jpg')
            st.caption("Downtown of Milwaukee, Wisconsin in freezing blizzard, Jan. 18, 2024. Photo by Isaac Rowlett")
            st.image('media/hot_weather.jpg')
            st.caption("Waikiki Beach, Oahu, Hawaii in March, 2024. ")
elif sidebar == "Test Time":
        st.write("\n")
        st.title("Test your knowledge!")

        answer1 = ["A) 41°F-79°F", "B) 69°F-55°F", "C) 70°F-78°F", "D) 49°F-70°F"]
        page = st.radio('1) In the section "United States Annual Weather," what degrees °F does the average temperature fall between?', answer1)
        if page == "A) 41°F-79°F":
            nested_btn = st.button("Are you sure?")
            if nested_btn:
                st.subheader("CORRECT ✅")
        else:
            nested_btn = st.button('Are you sure?')
            if nested_btn:
                st.subheader("INCORRECT")

        answer2 = ["A) September", "B) January", "C) December", "D) October"]
        page1 = st.radio(
            '2) In the section "United States Annual Weather," what month has the least amount of precipitation?',
            answer2)
        if page1 == "C) December":
            nested_btn2 = st.button('Are you sure')
            if nested_btn2:
                st.subheader("CORRECT ✅")
        else:
            nested_btn2 = st.button("Are you sure")
            if nested_btn2:
                st.subheader("INCORRECT")
        st.subheader("Take a Questionare!")
        st.write(" What is your favorite color?")
        color = st.color_picker("Pick a color", "#00f900")
        st.write("This color is", color)

        page_names = ["yes", "No"]
        page = st.radio('Do you like weather forecasting?', page_names)
        if page == "yes":
            nested_btn = st.button("I do like weather forecasting")
            if nested_btn:
                st.subheader("Thank you for using this app!",":smile:"*20)
        else:
            nested_btn = st.button("I dislike weather forecasting")
            if nested_btn:
                txt = st.text_area(
                    "Please explain why you dislike weather forecasting. After you are done, press ctrl + enter."
                )
                st.write(f"You wrote {len(txt)} characters.")
                if nested_btn == txt:
                    st.subheader("Hope you have a wonderful day.", ":cry:"*20)