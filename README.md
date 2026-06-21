


#  Rule-Based Customer Segmentation and Revenue Prediction

##  Project Overview

This project focuses on building a rule-based customer segmentation system** for a gaming company using demographic and behavioral data. The main goal is to define customer personas and estimate the average revenue potential of new customers** based on these personas.

No machine learning models were used; the approach is entirely based on data analysis and business rules.

---

##  Dataset Description

The dataset contains sales records from a global gaming company and includes the following features:

* **PRICE**: Purchase amount
* **SOURCE**: Device type (Android / iOS)
* **SEX**: Gender of the customer
* **COUNTRY**: Country of the customer
* **AGE**: Age of the customer

Each row represents a transaction, meaning a customer may appear multiple times.

---

##  Project Steps

The following steps were performed in this project:

* Exploratory data analysis (EDA)
* Aggregation of sales data by demographic groups
* Creation of level-based customer personas
* Conversion of numerical age into categorical segments
* Calculation of average revenue per persona
* Segmentation of customers using quantiles (A–D groups)
* Building a prediction function for new customers

---

## Methodology

* Grouped data using `pivot_table` to calculate mean revenue per segment
* Converted age into categorical intervals:

  * `0_18`, `19_23`, `24_30`, `31_40`, `41_70`
* Created a combined feature:

```
COUNTRY + SOURCE + SEX + AGE_GROUP
```

* Segments were created using quartile-based binning (qcut):

  * **A**: Highest revenue potential
  * **D**: Lowest revenue potential

---

##  Example Output

Example customer:

```
33-year-old female Android user from Turkey
```

Predicted:

* Segment: B / C (depending on data distribution)
* Expected average revenue: ~X

---

##  Prediction Function

A function was created to estimate the segment and expected revenue for new customers:

```python
predict(age, source, country, sex, agg_df)
```

Example:

```python
predict(35, "ios", "fra", "female", agg_df)
```

---

##  Results

This project demonstrates:

* How to build customer personas using data
* How to segment customers using rule-based logic
* How to extract business insights from raw transaction data
* How to estimate potential revenue for new customers

---

##  Technologies Used

* Python
* Pandas
* NumPy

---

##  Notes

This project is for educational purposes and demonstrates a rule-based segmentation approach, not a machine learning model.

---

##  Workflow

```
Raw Data → Grouping → Persona Creation → Segmentation → Revenue Prediction
```


