# ⚡ Electricity Prices and Weather Conditions in Finland

## 📌 Overview

This project analyzes the relationship between weather conditions and electricity prices in Finland. The study incorporates historical electricity prices, weather data (temperature, wind speed), and electricity consumption data to explore correlations and develop predictive models.

## 📊 Data Sources

| Source | Description |
|--------|-------------|
| [Nord Pool](https://data.nordpoolgroup.com/) | Historical day-ahead electricity prices for Finland. |
| [Finnish Meteorological Institute](https://www.ilmatieteenlaitos.fi/havaintojen-lataus) | Historical weather data (temperature, wind speed, precipitation). |
| [Statistics Finland](https://stat.fi/til/ehk/index_en.html) | Historical electricity consumption data. |


## 📁 Project Structure


- `app.py` : Streamlit application for interactive analysis.
- `README.md` : Documentation file.


## 🔧 Installation
### Requirements
**Ensure you have Python 3.x installed along with the following dependencies:**
$ pip install pandas numpy matplotlib seaborn statsmodels streamlit
$ streamlit run app.py

## 📈 Key Findings

- 📉 **Weak negative correlation** between wind speed and electricity prices.
  - Higher wind speeds → More wind energy → Lower electricity prices.
- 🌡️ **Weak positive correlation** between temperature and electricity prices.
  - Possible seasonal effects: **colder months increase demand**.
- ⚡ **Electricity consumption is a stronger predictor of price fluctuations**.

## 📜 License

**This project is open-source and available for further development and improvement.**
