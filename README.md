# Indian Startup Funding Analysis Project

This project explores and analyzes a dataset of Indian startup funding to uncover key patterns and insights about investment trends across the country.

---

## 🚀 Project Overview

The core objective is to understand the landscape of startup investments in India through a systematic data science workflow.

### Workflow

1.  **Data Cleaning and Preprocessing**
2.  **Exploratory Data Analysis (EDA)**
3.  **Interactive Streamlit Dashboard** for visualization and insights presentation.

---

## 🛠️ Data Cleaning and Preprocessing

A significant effort was made to clean and prepare the raw data for accurate analysis.

* **Missing Values:** Handled **31%** missing values in the investment amount column.
* **False Entries:** Identified and corrected false entries (e.g., correcting an entry like `₹34,500 Cr` to an estimated `₹488.4 Cr`).
* **Standardization:** Standardized city names, date formats, and vertical categories.
* **Duplicates & Inconsistencies:** Removed duplicate entries and formatted inconsistent text entries.
* **Derived Columns:** Created new columns for richer analysis, such as **total investment per company** and **investment counts**.

---

## 📊 Exploratory Data Analysis (EDA) - Key Insights

The EDA phase revealed critical statistical and structural patterns within the dataset.

### Statistical Observations

| Metric | Value | Observation |
| :--- | :--- | :--- |
| **Median Investment** | **₹18 Cr** | Typical funding amount. |
| **Median Investment per Vertical** | **₹115 Cr** | Median total funding received by a business category. |
| **Skewness** | Highly **right-skewed** | Dominated by extreme outliers (large investments). |
| **Mean vs. Median** | Large difference | Indicates significant **inequality** in investment distribution. |

### Structural Insights

* **Funding Concentration:** **90%** of startups received less than **₹150 Cr** in funding.
* **Outliers:** Approximately **400 investments** are considered outliers (>$120 Cr).
* **Startups Funded:** Around **2,300 startups** received funding, with **80%** receiving only a single round.

### Top Performers and Trends

| Category | Top Entities |
| :--- | :--- |
| **Top Funded Startups** | **Flipkart**, **Paytm**, **Udaan**, **Ola**, and **Snapdeal**. |
| **Most Common Sectors** | **Consumer Internet**, **Technology**, and **E-commerce**. |
| **Top Startup Cities** | **Bengaluru**, **Mumbai**, **Delhi**, **Gurugram**, and **Noida**. |
| **Top Investors (by Count)** | **Sequoia**, **Accel Partners**, **IAN**, **Tiger Global**, and **Kalaari Capital**. |
| **Top Investors (by Total Investment)** | **SoftBank**, **WestBridge**, **Sequoia**, **Microsoft**, and **Tiger Global**. |

---

## 🖥️ Streamlit Dashboard Features

The Streamlit app provides an interactive and visual presentation of the findings.

* **Dashboards:**
    * Top Investors Dashboard (by count and total investment).
    * Top Startups Dashboard.
    * City and Sector-wise Insights.
* **Visualizations:** Interactive charts for investment distribution and trends.
* **User Exploration:** Filters and dropdowns enable user-driven data exploration.

### Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

---

## ✅ Results Summary

* **Geographic Dominance:** Startups in **Bangalore**, **Mumbai**, and **Delhi NCR** dominate both the number of deals and the total capital invested.
* **Sector Focus:** **E-commerce, Fintech, and Consumer Internet** are the top funded sectors.
* **Uneven Funding:** Funding is highly concentrated and **uneven**—a small number of startups and investors account for the majority of the total capital.
* **Conclusion:** The project effectively highlights key investment patterns and the concentration of funding in specific hubs and sectors.

---

## ➡️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone [https://github.com/your-username/startup-funding-analysis.git](https://github.com/your-username/startup-funding-analysis.git)
cd startup-funding-analysis
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit App
```bash
streamlit run app.py
```

## 📂 Folder Structure
```
startup-funding-analysis/
│
├── .ipynb_checkpoints/     # Jupyter Notebook checkpoints
├── myenv/                  # Python virtual environment folder
│
├── app.py                  # Streamlit dashboard application
├── Data_cleaning.ipynb     # Data cleaning and preprocessing notebook
├── EDA.ipynb               # Exploratory Data Analysis notebook
│
├── startup_cleaned.csv     # Cleaned dataset (used by app.py)
├── startup_funding.csv     # Raw dataset
│
└── temp.py                
```

## 📈 Future Improvements

* Add **time-series analysis** to study investment trends year-over-year.
* Include **predictive modeling** for funding estimation.
* Enhance dashboard interactivity and user experience.












