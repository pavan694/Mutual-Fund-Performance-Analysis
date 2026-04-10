# Mutual Fund Performance Analysis & Investment Insights Dashboard

## 👋 Hi, Welcome!
I’m **Pavan Jinugu**, and this project showcases my ability to analyze financial data and build data-driven solutions using Python and Power BI.

This project focuses on evaluating mutual fund performance and helping investors make informed decisions through data analytics and visualization.

---

## 📌 Overview
This project presents a comprehensive analysis of 500+ mutual funds by integrating Python-based data processing with an interactive Power BI dashboard.  

The goal is to create a data-driven framework for evaluating mutual funds by balancing returns, expense ratio, and risk-adjusted performance metrics.

---

## ⚙️ Project Workflow

### 🔹 Data Analysis using Python

#### Data Exploration
- Imported mutual fund dataset using Pandas  
- Performed exploratory analysis using `.head()`, `.describe()`, `.unique()`  
- Analyzed distribution of financial metrics and fund categories  

#### Data Cleaning & Preprocessing
- Identified missing values using `.isnull().sum()`  
- Applied mean imputation for missing values (3Y & 5Y returns)  
- Replaced invalid entries and converted data into numeric format  

#### Feature Engineering & Normalization
- Selected key financial metrics:
  - Expense Ratio  
  - Returns (1Y, 3Y, 5Y)  
  - Sharpe Ratio  
  - Sortino Ratio  
  - Alpha & Beta  

- Normalized values using MinMaxScaler  
- Adjusted metrics where lower values are better (expense ratio, beta)  

#### Composite Scoring Model
- Built a weighted scoring system prioritizing:
  - Returns  
  - Cost efficiency  
  - Risk-adjusted performance  

- Calculated a composite score for each fund  

#### Ranking & Output
- Ranked funds based on composite score  
- Identified Top 30 performing funds  
- Exported results into Excel for reporting  

---

### 🔹 Power BI Dashboard

#### Data Integration
- Imported processed dataset into Power BI  
- Established relationships between fund categories and metrics  

#### Data Transformation
- Used Power Query for:
  - Data cleaning  
  - Column formatting  
  - Handling missing values  

#### DAX Measures
Created key metrics such as:
- Composite Score  
- Fund Ranking  
- Average Returns  
- Expense Ratio  
- Risk Ratios  

#### Dashboard Design
Developed an interactive dashboard including:
- KPI cards (returns, expense ratio, performance metrics)  
- Bar charts for fund ranking  
- Scatter plots for risk vs return analysis  
- Tables with conditional formatting for Top 30 funds  

#### Interactivity
- Added slicers for:
  - Fund category  
  - Asset type  
  - Time horizon (1Y, 3Y, 5Y)  

- Enabled cross-filtering for better exploration  
- Used tooltips and color coding for insights  

---

## 📊 Key Insights

| Insight Category        | Summary                                      |
|------------------------|----------------------------------------------|
| Investment Trends      | Equity funds dominate overall market share   |
| Fund Performance       | Top funds consistently outperform peers      |
| Cost Efficiency        | Index funds have lower expense ratios        |
| Risk vs Return         | Higher returns are often linked with risk    |
| Investment Strategy    | SIP enables steady long-term investment      |
| Long-Term Growth       | Equity funds outperform over 3–5 years       |

---

## 📈 Dashboard Preview

![Dashboard](https://github.com/user-attachments/assets/633894da-ba1f-4bcf-8ce5-ce2ef72abfad)

---

## 🧠 Business Insights & Conclusion

This project highlights how data analytics can improve financial decision-making.

Key takeaways:
- Data-driven analysis helps identify high-performing funds  
- Balancing risk and return is critical for investors  
- Expense ratio significantly impacts long-term returns  
- Visualization simplifies complex financial insights  

By combining Python for analysis and Power BI for visualization, this project demonstrates an end-to-end data analytics workflow for investment evaluation.

---

## 🛠️ Tools & Technologies

| Tool        | Purpose                                      |
|------------|----------------------------------------------|
| Python      | Data cleaning, analysis, and scoring model   |
| Excel       | Data validation and preprocessing            |
| Power BI    | Dashboard development and visualization      |

---

## 👨‍💻 About Me

**Pavan Jinugu**

🔗 LinkedIn: https://www.linkedin.com/in/pavan-jinugu-81571822a  
💻 GitHub: https://github.com/pavan694  

Aspiring Data Analyst focused on solving real-world business problems using data analytics, SQL, Python, and Power BI.

---

## ⭐ Feedback

Thank you for exploring this project!  
Feedback, suggestions, and improvements are always welcome.
