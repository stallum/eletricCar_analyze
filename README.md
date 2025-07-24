# Electric Vehicles Dashboard

This project features an interactive dashboard built with Streamlit to analyze electric vehicle (EV) specifications and market interest based on 2025 data.

## 📝 Project Overview

This dashboard aims to provide clear and actionable insights into the electric vehicle market, assisting in the strategic development of new products and understanding current trends.

## 📊 Analyses and Visualizations

The dashboard is structured into sections to facilitate navigation and understanding of the information. The following analyses are presented:

* **Market Overview by Brand:** Bar chart showing the number of electric vehicle models per manufacturer, highlighting market share.
* **Battery Performance and Efficiency:**
    * Scatter plot relating battery capacity (kWh) to range (km), colored by brand.
    * Histogram of the distribution of vehicle efficiency (Wh/km).
* **Speed and Acceleration:**
    * Scatter plot showing the relationship between 0-100 km/h acceleration and top speed, colored by brand.
* **Physical Vehicle Characteristics:**
    * Box plot of the distribution of the number of seats by car body type.
    * Bar chart showing the distribution and popularity of different car body types (SUV, Sedan, Hatchback, etc.).
* **Charging Details:**
    * Histogram of the distribution of DC fast charging power (kW).
    * Pie chart showing the distribution of fast charge port types.

## 🚀 How to Run the Project

To run this dashboard on your local machine, follow the steps below:

### Prerequisites

Ensure you have Python installed (version 3.8+ recommended).

### Installation

1.  Clone this repository to your local environment:
    ```bash
    git clone https://github.com/stallum/eletricCar_analyze.git
    cd eletricCar_analyze
    ```

2.  Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    * **Lembrete:** Para gerar o `requirements.txt` após instalar as bibliotecas (pandas, streamlit, plotly), execute no terminal: `pip freeze > requirements.txt`

### Execution

1.  **Data File Location:** Create a folder named `data` in the root directory of the project (ao lado do arquivo `dash.py`). Place the `electric_vehicles_spec_2025.csv` file inside this `data` folder.
    * **Importante:** No seu código Python, certifique-se de que a linha de leitura do CSV esteja ajustada para um caminho relativo, por exemplo:
        ```python
        df = pd.read_csv('./data/electric_vehicles_spec_2025.csv', index_col=False)
        ```

2.  Run the Streamlit application:
    ```bash
    streamlit run dash.py
    ```

## 💾 Data Source

The data used in this project is publicly available and was obtained from:

* **Dataset:** [Electric Vehicle Specifications Dataset 2025](https://www.kaggle.com/datasets/urvishahir/electric-vehicle-specifications-dataset-2025)


## 🤝 Contributions

This project was entirely created by me (User). Suggestions and improvements are welcome!

## 📜 License

This project is licensed under the MIT License.
