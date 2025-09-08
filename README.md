# Full-Cycle Inventory & Vendor Analysis

## Overview
This project delivers a comprehensive analysis of inventory movement, purchasing behavior, vendor performance, and sales trends for the HARDERSFIELD store. It integrates six datasets and applies SQL-based extraction with Python-powered analytics and visualization.

## Objectives
- Track inventory changes across the year
- Analyze product-level profitability and turnover
- Evaluate vendor reliability, freight impact, and payment cycles
- Identify top-selling products and margin drivers
- Build a foundation for strategic decision-making and reporting

## Datasets Used
1. `begin_inventory.csv` – Starting inventory snapshot
2. `end_inventory.csv` – Year-end inventory snapshot
3. `purchase_prices.csv` – Product cost and vendor info
4. `vendor_invoice.csv` – Delivered quantities and invoice details
5. `sales_data.csv` – Daily sales transactions
6. `vendor_payments.csv` – Payment, freight, and approval records

## Tools & Technologies
- **Database**: MySQL
- **Data Analysis**: Pandas
- **Visualization**: Matplotlib, Seaborn
- **Environment**: Jupyter Notebook

## Key Metrics Calculated
- Inventory movement and valuation change
- Gross margin and markup percentage
- Product turnover rate
- Vendor freight ratio and spend analysis
- Payment lag and approval tracking
- Sales revenue and excise tax impact

## Visualizations
- This scatter plot visualizes the relationship between total sales and profit margin across different brands, helping you identify which products may need promotional or pricing adjustments.
- This Pareto chart adds a strategic layer to your vendor analysis by showing not just who contributes most to purchases, but how quickly those contributions accumulate.
- This pie chart explains the purchase contribution relationships among top vendors, showing how much each supplier accounts for in total procurement.
- Top-selling products by revenue
- The heatmap reveals the strength and direction of relationships between key variables across inventory, purchasing, vendor, and sales data

## Reporting Structure
1. **Executive Summary**
2. **Inventory Analysis**
3. **Pricing & Profitability**
4. **Vendor Performance**
5. **Sales Trends**
6. **Payment & Freight Insights**
7. **Strategic Recommendations**

## Strategic Questions for Stakeholders
These questions guide deeper analysis and support data-driven decisions:

1. Which products had the highest and lowest inventory turnover rates?
2. What is the gross margin and markup percentage for each product?
3. Are there statistically significant differences in freight cost ratios across vendors?
4. Which vendors contribute most to revenue and margin performance?
5. Are there discrepancies between invoice quantities and inventory received?
6. Which products show pricing inconsistencies over time?
7. What is the average time from PO to payment across vendors?
8. Which SKUs have high value but low sales velocity?
9. How does excise tax impact profitability across product categories?
10. What are the top 10 SKUs by contribution to total revenue and profit?

# These questions help stakeholders identify opportunities for cost reduction, inventory optimization, vendor negotiation, and strategic growth.

## How to Run
1. Import datasets into MySQL
2. Connect using SQLAlchemy 
3. Run analysis scripts in Jupyter Notebook
4. Generate visual reports using Matplotlib and Seaborn

## Conclusion
This project successfully delivers a full-cycle analysis of inventory, purchasing, vendor performance, and sales operations for the HARDERSFIELD store. By integrating six datasets and applying SQL-powered extraction with Python-based analytics, it uncovers actionable insights into stock movement, profitability, vendor efficiency, and sales trends. The findings support smarter inventory decisions, optimized vendor relationships, and more strategic financial planning—laying the groundwork for scalable, data-driven operations.



