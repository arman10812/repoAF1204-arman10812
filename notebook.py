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


if __name__ == "__main__":
    app.run()
