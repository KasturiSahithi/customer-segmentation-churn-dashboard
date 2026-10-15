from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    try:
        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans
    except ImportError as e:
        root=tk.Tk(); root.withdraw()
        messagebox.showerror("Install packages", f"{e}\nRun in Command Prompt:\npython -m pip install pandas numpy scikit-learn openpyxl")
        return
    root=tk.Tk(); root.withdraw()
    file_path=filedialog.askopenfilename(title="Select Customer Segmentation dataset", filetypes=[("Excel workbook","*.xlsx")])
    if not file_path: return
    try:
        orders=pd.read_excel(file_path, sheet_name="Orders")
        customers=pd.read_excel(file_path, sheet_name="Customers")
        orders["OrderDate"]=pd.to_datetime(orders["OrderDate"], errors="coerce")
        completed=orders[orders["OrderStatus"].astype(str).str.strip().str.lower().eq("completed")].dropna(subset=["OrderDate","CustomerID","OrderID"]).copy()
        as_of=pd.Timestamp("2026-01-01")
        agg=completed.groupby("CustomerID").agg(LastOrderDate=("OrderDate","max"), Frequency=("OrderID","nunique"), Monetary=("NetSales","sum")).reset_index()
        rfm=customers[["CustomerID","Region","AcquisitionChannel","CustomerType","Industry","SignupDate"]].merge(agg,on="CustomerID",how="left")
        rfm["Frequency"]=rfm["Frequency"].fillna(0).astype(int)
        rfm["Monetary"]=rfm["Monetary"].fillna(0).round(2)
        rfm["Recency"]=(as_of-pd.to_datetime(rfm["LastOrderDate"])).dt.days
        signup_recency=(as_of-pd.to_datetime(rfm["SignupDate"])).dt.days
        rfm["Recency"]=rfm["Recency"].fillna(signup_recency).clip(lower=0).astype(int)
        rfm["LastOrderDate"]=pd.to_datetime(rfm["LastOrderDate"],errors="coerce")
        def quintile(s):
            return pd.qcut(s.rank(method="first"),5,labels=[1,2,3,4,5]).astype(int)
        rfm["R_Score"]=6-quintile(rfm["Recency"])
        rfm["F_Score"]=quintile(rfm["Frequency"])
        rfm["M_Score"]=quintile(rfm["Monetary"])
        rfm["RFM_Score"]=rfm["R_Score"].astype(str)+rfm["F_Score"].astype(str)+rfm["M_Score"].astype(str)
        features=np.log1p(rfm[["Recency","Frequency","Monetary"]].astype(float))
        scaled=StandardScaler().fit_transform(features)
        rfm["Cluster"]=KMeans(n_clusters=4,random_state=42,n_init=10).fit_predict(scaled)+1
        rfm["InactivityRisk"]=np.select([rfm["Recency"]>=180,rfm["Recency"]>=90],["At-Risk (180+ days)","Watchlist (90-179 days)"],default="Recently Active (<90 days)")
        rfm["AnalysisAsOfDate"]=as_of
        profiles=rfm.groupby("Cluster").agg(Customers=("CustomerID","nunique"),AvgRecencyDays=("Recency","mean"),AvgFrequency=("Frequency","mean"),AvgMonetary=("Monetary","mean"),TotalMonetary=("Monetary","sum")).reset_index()
        profiles["RevenueSharePct"]=100*profiles["TotalMonetary"]/profiles["TotalMonetary"].sum()
        profiles[["AvgRecencyDays","AvgFrequency","AvgMonetary","TotalMonetary","RevenueSharePct"]]=profiles[["AvgRecencyDays","AvgFrequency","AvgMonetary","TotalMonetary","RevenueSharePct"]].round(2)
        out=Path(file_path).with_name("RFM_Analysis_Output.xlsx")
        with pd.ExcelWriter(out,engine="openpyxl") as w:
            rfm.to_excel(w,sheet_name="RFM_Customers",index=False)
            profiles.to_excel(w,sheet_name="Cluster_Summary",index=False)
        messagebox.showinfo("Completed",f"Created {out}\nCustomers: {len(rfm):,}\nCompleted orders used: {len(completed):,}")
    except Exception as e:
        messagebox.showerror("Error",f"{type(e).__name__}: {e}")
if __name__=="__main__": main()
