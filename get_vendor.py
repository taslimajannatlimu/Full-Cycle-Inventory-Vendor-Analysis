import pandas as pd
import numpy as np
import os
import logging
from Ingestion import ingest_db
import time

os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/get_vendor_summery.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)    
def create_vendor_summery(conn):
    vendor_sales_summery= pd.read_sql_query("""with freight_summery as (Select VendorNumber, 
    Sum(Freight) as freightCost 
    from vendor_invoice 
    Group By VendorNumber),

    purchase_summery as(select p.Brand, 
    p.VendorNumber, 
    p.VendorName,
    p.PurchasePrice, 
    pp.Volume,
    pp.Price as ActualPrice, 
    sum(p.Quantity) as TotalPurchaseQuantity,
    sum (p.Dollars) as TotalpurchaseDollars 
    from purchases p join purchase_prices pp 
    On p.Brand = pp.Brand 
    where p.PurchasePrice>0
    group by p.VendorNumber,p.VendorName,p.Brand, p.Description, p.PurchasePrice, pp.Price,pp.Volume),

    sales_summery as (select Brand,
    VendorNo,
    Description,
    sum(SalesQuantity) as TotalSalesQuantity,
    sum(SalesDollars)as TotalSalesDollars,
    Sum(SalesPrice) as TotalSalesPrice,
    sum(ExciseTax) as TotalExciseTax 
    from sales
    Group By Brand,VendorNo,Description)

    select 
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Volume,
    ps.ActualPrice,
    ps.PurchasePrice,
    ps.TotalPurchaseQuantity,
    ps.TotalpurchaseDollars,
    ss.Description,
    ss.TotalSalesQuantity,
    ss.TotalSalesDollars,
    ss.TotalSalesPrice,
    ss.TotalExciseTax, 
    fs.freightCost 
    from 
    purchase_summery ps left join sales_summery ss on ps.VendorNumber=ss.VendorNo and ps.Brand=ss.Brand
    left join freight_summery fs on ps.VendorNumber=fs.VendorNumber 
    order by ps.TotalpurchaseDollars """, conn)
    return vendor_sales_summery
def clean_data(df):
    df["Volume"]=df['Volume'].astype("float64")
    df.fillna(0, inplace=True)
    df["VendorName"]=df["VendorName"].str.strip() 
    vendor_sales_summery["GrossProfit"]=vendor_sales_summery["TotalSalesDollars"]-vendor_sales_summery["TotalpurchaseDollars"]
    vendor_sales_summery["ProfitMargin"]=(vendor_sales_summery["GrossProfit"]/vendor_sales_summery["TotalSalesDollars"])*100
    vendor_sales_summery["StockTurnOver"]= vendor_sales_summery["TotalSalesQuantity"]/vendor_sales_summery["TotalPurchaseQuantity"]
    vendor_sales_summery["SalestoPurchaseRation"]=vendor_sales_summery["TotalSalesDollars"]/vendor_sales_summery["TotalpurchaseDollars"]
    return df
if __name__ == "__main__":
    conn=sqlite3.connect("inventory.db")
    logging.info("Creating vendor Summery table...")
    summery_df= create_vendor_summery(conn)
    logging.info(summery_df.head())

    logging.info("Cleaning data...")
    clean_df= clean_data(summery_df)
    logging.info(clean_df.head())  
     
    logging.info("Ingesting data...")
    ingest_db= (clean_df,"vendor_sales_summery",conn)
    logging.info("completed")
     
