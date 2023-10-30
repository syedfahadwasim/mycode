import numpy as np
import pandas as pd
import seaborn as sns
import csv
from tabulate import tabulate
import plotly.express as px
import statsmodels.api as sm
import kaleido
import os

def main():

    df = pd.read_csv('usdata.csv')
    df = df.drop(columns=['DATE'])

    print("Select your dependent and independent variables from the table below by typing their symbols:")

    table = [
    ["10YYIELD", "Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity"],
    ["MORTGAGE30US", "30-Year Fixed Rate Mortgage Average in the United States"],
    ["USHPI", "All-Transactions House Price Index for the United States"],
    ["SHILLER", "S&P/Case-Shiller U.S. National Home Price Index"],
    ["MEDIANSALEPRICE", "Median Sales Price of Houses Sold for the United States (Percentage Change)"],
    ["FEDFUNDS", "Federal Funds Effective Rate"]]

    print(tabulate(table, headers=["Variable Symbol","Variable Name"],tablefmt="heavy_grid"))

    #Prompt the user to select two variables
    indep_var = input("Choose your independent variable: ")
    dep_var = input("Choose your dependent variable: ")

    #Prompt the user to choose between regression or correlation
    validity = is_valid(df, indep_var, dep_var)
    if validity is not None:
        route = input("Choose your route -- Regression or Correlation: ")
        if route == "Regression":
            reg = regression(validity, indep_var, dep_var)

        elif route == "Correlation":
            cor = correlation(validity)

        else:
            print("Choose a valid route")


def is_valid(df, indep_var,dep_var):

    if indep_var == dep_var:
        print("Two variables can't be the same")
        return None

    if indep_var in df.columns and dep_var in df.columns:
        data_subset = df[[indep_var, dep_var]]
        return data_subset

    else:
        print("Invalid variable name")
        return None

def regression(data_subset, indep_var, dep_var):

    fig = px.scatter(
        data_subset, x=indep_var, y=dep_var, opacity=0.65,
        trendline='ols', trendline_color_override='darkblue'
    )

    fig.update_layout(title_text='<b>Regression Analysis<b>', font_size=12)

    return fig.write_image('regression_plot.png')


def correlation(data_subset):
    ds_correlation = data_subset.corr().round(3)
    fig = px.imshow(ds_correlation, text_auto=True, color_continuous_scale='curl')
    fig.update_layout(title_text='<b>Correlation Plot<b>')

    return fig.write_image('correlation_plot.png')

if __name__ == "__main__":
    main()
