import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import plotly.express as px

    return pd, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Armani Cabey - A1204 Portfolio Dashboard
    ##Stock Price analysis of 2023
    The dashboard below illustrates 5 different companies throught 2023. Use the interactive slider to explore the companies from month 1 to 12.
    - Line chart: Select a comapany to see its price over the 12 months📈
    - Bar chart: Use the slider to compare the companies by month📊
    """)
    return


@app.cell
def _(pd):
    # Stock price data for five global companies
    data = {
        "Date": pd.date_range(start="2023-01-01", periods=12, freq="MS"),
        "Apple": [130, 145, 157, 165, 177, 189, 192, 178, 171, 182, 191, 197],
        "Tesla": [123, 189, 207, 165, 178, 256, 274, 231, 244, 198, 212, 248],
        "Amazon": [84, 96, 103, 115, 124, 131, 133, 128, 127, 133, 146, 153],
        "Nike": [112, 118, 124, 119, 107, 113, 98, 95, 92, 101, 108, 112],
        "Microsoft": [239, 256, 271, 285, 308, 331, 337, 316, 319, 340, 368, 374]
    }

    df = pd.DataFrame(data)
    df
    return (df,)


@app.cell
def _(mo):
    # Dropdown to select a company
    company = mo.ui.dropdown(
        options=["Apple", "Tesla", "Amazon", "Nike", "Microsoft"],
        value="Apple",
        label="Select a company"
    )
    company
    return (company,)


@app.cell
def _(company, df, mo, px):
    # Chart that updates based on dropdown selection
    fig = px.line(
        df, 
        x="Date", 
        y=company.value,
        title=f"{company.value} Stock Price 2023 (USD per share)",
        labels={"y": "Price (USD)", "Date": "Month"}
    )
    mo.ui.plotly(fig)
    return


@app.cell
def _(mo):
    # Bar chart comparing all companies for a selected month
    month = mo.ui.slider(
        start=1, 
        stop=12, 
        value=1,
        label="Select Month (1=Jan, 12=Dec)"
    )
    month
    return (month,)


@app.cell
def _(df, mo, month, px):
    # Bar chart for selected month
    month_data = df.iloc[month.value - 1]
    companies = ["Apple", "Tesla", "Amazon", "Nike", "Microsoft"]
    prices = [month_data[c] for c in companies]

    fig2 = px.bar(
        x=companies,
        y=prices,
        title=f"Stock Price Comparison - Month {month.value} of 2023",
        labels={"x": "Company", "y": "Price (USD)"},
        color=companies
    )
    mo.ui.plotly(fig2)
    return


if __name__ == "__main__":
    app.run()
