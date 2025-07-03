Weather Forecast Prediction App

A Streamlit web application that predicts weather forecasts using the OpenWeatherMap API. Created by Tortrong Yang, this app provides a user-friendly interface to view real-time weather forecasts in 3-hour intervals up to 6 days, along with visual data for U.S. climate trends.

Features
⛅ Weather Forecast
- Enter any city to view forecast data for every 3 hours up to 6 days
- Weather description, temperature, feels-like, humidity, and wind speed included
- Auto-displays relevant images based on weather conditions (e.g., rain, clear sky)

🌎 United States Annual Weather
- Shows average monthly temperature and rainfall data
- Visualized with bar and line charts using matplotlib
- Interactive U.S. map displays the hottest and coldest cities with coordinates

🎯 Knowledge Quiz Section
- Users can test knowledge on the app’s U.S. climate data
- Includes color picker and user preference poll for interactivity

Technologies Used
- Streamlit: Web UI
- Python: Core programming language
- Pandas / NumPy: Data management
- Matplotlib: Data visualization
- OpenWeatherMap API: Real-time weather forecast data

Setup Instructions
1. Clone this repo
2. Ensure Python and pip are installed
3. Run pip install -r requirements.txt
4. Add your API key to the api_key variable in the code
5. Place relevant image files inside the /media directory
6. Run using: streamlit run app.py

Media Files Used
Ensure the following images are placed in the /media folder:
banner.png, clearSky.jpg, rainCity.jpg, snowCity.jpg, etc.

Author
Tortrong YangLinkedIn: linkedin.com/in/tortrong-yang-41b56227aGitHub: github.com/tyang

License
This project is for educational and demonstration purposes.
