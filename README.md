# Solar Energy Prediction

A solar energy prediction model that uses real-time METAR and forecased TAF-weather data from Charlotetown Airport to estimate the hourly solar power output for Slemon Park, Summerside, PE. It integrates weather station data from Environment Canada and advanced machine learning model to provide 4-Hr solar power prediction.


## Key Features:
- **Real-time Weather Data**: Fetches METAR and TAF data to incorporate dynamic environmental conditions.
- **Machine Learning Predictions**: Uses an optimized XGBoost model for accurate solar power forecasts.
- **Cloud Coverage Integration**: Accounts for low, mid, and high-level clouds affecting solar radiation.
- **Solar Position Calculations**: Computes solar elevation and azimuth angles for better prediction accuracy.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Hangman25/Energy.git
   cd Energy
   ```
2. **Set Up a Virtual Environment using Conda**:
   ```bash
   conda create --name my_env python=3.9
   conda activate my_env
   ```
3. **Install Dependencies**:
   ```bash
   conda install pip
   pip install -r requirements.txt
   ```

## Usage

1. **Trained Model**:
   - `model.pkl` is the trained xg-boost model.
   - Fintune it on new data to increase its accuracy. 
2. **CSV**:
   - `residuals.csv` contains the current results of the trained model.
   - `solar_2025.csv` contains the solar parameters, calculated for Slemon Park. 

   
## Project Structure

```
SolarEnergy_Prediction/
│── csv/                # Processed datasets
│   ├── residuals.csv/  # Results data file
│   ├── solar_2025.csv/ # Solar parameters 
│── scripts/            # Python scripts for prediction & email
│   ├── app.py          # Main application 
│   ├── about.py        # About page
│   ├── cloud.py        # NOAA Cloud script
│   ├── csv_email.py    # Email script
│   ├── metar.py        # METAR script
│   ├── model.py        # Model script
│   ├── prediction.py   # Prediction script
│   ├──solar.py         # Solar script
│   ├── taf.py          # TAR script
│   ├── weather.py      # Weather script
│── docs/                # Documentation files
│   ├── README.md        # Documentation for the project
│   ├── API_guide.md     # API documentation (if applicable)
│── requirements.txt     # Dependencies
│── .gitignore           # Files to be ignored by Git
```

## Libraries
```
streamlit==1.42.0
plotly==6.0.0
joblib==1.4.2
xgboost==2.1.4
requests==2.32.3
pandas==2.2.2
numpy==1.26.4
python-dateutil==2.9.0  
pytz==2024.1 
python-dotenv==1.0.1
```

## Contributing

This work is for 3rd-Year Design project. 

## License

This project is licensed under the MIT License.

## Contact

For questions or collaboration opportunities, please reach out via the repository's issue tracker.



