# Customer Segmentation & Churn Dashboard

## 1. Project Overview

This project analyzes customer purchasing behavior using **RFM (Recency, Frequency, Monetary) analysis**, Python-based K-Means clustering, and Power BI dashboards.

The goal is to understand customer segments, identify customers who may be at risk of inactivity, analyze customer retention patterns, and explore potential revenue improvement scenarios.

The project uses a synthetic dataset to demonstrate an end-to-end customer analytics workflow.

## 2. Dashboard Screenshots

### 2.1 Executive Overview

Provides a high-level view of revenue, orders, customer metrics, and potential revenue improvement scenarios.

![Executive Overview](Executiveoverview.png)

### 2.2 Customer Segmentation

Explores RFM-based customer clusters, customer distribution, and revenue contribution across clusters.

![Customer Segmentation](customer-segmentation.png)

### 2.3 Churn & Retention

Displays customer inactivity risk categories, purchase status, and cohort retention analysis.

![Churn and Retention](churn-retention.png)

## 3. Project Objectives

1. Analyze customer purchasing behavior using RFM metrics.
2. Segment customers using the K-Means clustering algorithm.
3. Identify customers based on inactivity risk categories.
4. Analyze customer retention using cohort analysis.
5. Build interactive dashboards in Power BI.
6. Estimate historical revenue per purchasing customer.
7. Explore hypothetical revenue improvement scenarios.

## 4. Tools and Technologies

- **Power BI Desktop** – Dashboard development and visualization
- **Python** – Data processing and customer segmentation
- **Pandas and NumPy** – Data manipulation and analysis
- **Scikit-learn** – K-Means clustering
- **DAX** – Measures and calculations
- **Power Query** – Data transformation
- **Excel** – Dataset storage and analysis
- **GitHub** – Project documentation and version control

## 5. Dataset

The project uses a **synthetic e-commerce dataset** containing:

- 50,000 customer profiles
- 180,000 order records
- 350 products

The dataset supports customer segmentation, purchasing behavior analysis, inactivity classification, and retention analysis.

**Note:** The dataset is synthetic and is used for learning and portfolio demonstration purposes.

## 6. Methodology

### 6.1 Data Preparation

1. Imported customer, order, and product data.
2. Prepared the data for analysis.
3. Used completed orders for relevant purchase and revenue calculations.
4. Connected tables in Power BI using relationships.

### 6.2 RFM Analysis

RFM analysis evaluates customers using three metrics:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How often a customer purchased.
- **Monetary:** The total monetary value of a customer's purchases.

RFM scores were calculated to support customer behavior analysis.

### 6.3 Customer Segmentation

The Python script `run_rfm_clustering.py` processes the customer data and applies K-Means clustering to group customers into four clusters.

The resulting customer-level metrics and cluster information are exported to `RFM_Analysis_Output.xlsx` for use in Power BI.

### 6.4 Inactivity Risk Analysis

Customers are categorized using the time since their last recorded purchase:

- **Recently Active:** Less than 90 days
- **Watchlist:** 90–179 days
- **At-Risk:** 180 days or more

These categories use inactivity as a proxy for churn risk. They do not confirm that a customer has permanently churned.

### 6.5 Cohort Retention Analysis

Cohort analysis groups customers by their first completed purchase month and examines subsequent purchasing activity over time.

### 6.6 Revenue Improvement Scenario

A Power BI what-if parameter allows users to explore hypothetical revenue uplift percentages.

This scenario illustrates potential revenue improvement under an assumed uplift rate; it is not a forecast of actual future revenue.

## 7. Dashboard Features

### 7.1 Executive Overview

- Revenue and order KPIs
- Customer metrics
- Revenue analysis
- Customer summary
- Historical revenue per purchasing customer
- Interactive revenue improvement scenario

### 7.2 Customer Segmentation

- Customer distribution across four clusters
- Revenue contribution by cluster
- RFM-based customer behavior analysis
- Cluster-level comparisons

### 7.3 Churn & Retention

- At-risk customer count
- Watchlist customer count
- Recently active customer count
- Purchase status analysis
- Cohort retention matrix

## 8. Key Analytical Concepts

1. RFM analysis
2. K-Means clustering
3. Customer segmentation
4. Inactivity-based churn risk
5. Cohort retention analysis
6. DAX measures and calculated columns
7. Interactive Power BI dashboards
8. What-if analysis
9. Historical customer revenue analysis

## 9. Results and Interpretation

The project demonstrates how customer transaction data can be transformed into customer segments and interactive business dashboards.

The analysis supports exploration of:

- Differences in purchasing behavior across clusters
- Customer inactivity patterns
- Revenue contribution across customer groups
- Changes in purchasing activity across cohorts
- Hypothetical revenue uplift scenarios

The insights should be interpreted in the context of the synthetic dataset and the assumptions used in the analysis.

## 10. Limitations

- The dataset is synthetic and may not represent real-world customer behavior.
- Inactivity is used as a proxy for churn risk.
- Historical revenue per purchasing customer is not a predictive customer lifetime value model.
- Revenue improvement scenarios are hypothetical, not guaranteed outcomes.
- Cluster labels are numerical and require further behavioral validation before assigning business-specific names.
- Cohort retention calculations should be validated before using the results for business decisions.

## 11. Future Improvements

- Apply the analysis to a real-world e-commerce dataset.
- Improve customer segment interpretation using cluster profiles.
- Develop a more robust churn prediction model.
- Validate cohort retention calculations against customer-level purchase histories.
- Build predictive customer lifetime value models.
- Add automated data refresh and reporting.

## 12. Skills Demonstrated

- Data cleaning and preparation
- Python data analysis
- Customer segmentation
- Machine learning fundamentals
- SQL and analytical thinking
- Power BI dashboard development
- DAX calculations
- Data visualization
- Business insight generation

## 13. Project Files

- `run_rfm_clustering.py` – Python script for RFM analysis and clustering
- `RFM_Analysis_Output.xlsx` – Processed output for Power BI
- `.pbix` file – Power BI dashboard and data model
- `executive-overview.png` – Executive dashboard screenshot
- `customer-segmentation.png` – Segmentation dashboard screenshot
- `churn-retention.png` – Churn and retention dashboard screenshot

## 14. Author

**Sahithi Kasturi**

Electrical and Electronics Engineering | Data Science Minor

GitHub: [KasturiSahithi](https://github.com/KasturiSahithi)
