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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##
    """)
    return


@app.cell
def _(mo, pd, px):
    about_me = mo.md("""
    ## About me 
    ## Armani Cabey
    ### Accounting & Finance Undergraduate | Aspiring Financial Accountant or related financial roles.

    **Summary:**
    An Accounting and Finance Undergraduate currently learning data visualisation, python, and web development as a part of my 1204 module.

    **Education:**
    - BSc Accounting & Finance, City University (Sept 2025 - Present)
    - Relevant Modules: Introduction to Data Science and AI Tools, Financial Accounting
    """)

    skills = mo.md("""
    ## Skills 

    **Hard Skills:**
    - Python (pandas, plotly, marimo)
    - Data visualisation
    - GitHub & version control
    - Interactive dashboard development

    **Soft Skills:**
    - Communication
    - Problem Solving
    - Quick Learner
    - Teamwork
    - Numerical/Data Analysis
    """)

    interests = mo.md("""
    ## Personal Interests
    - Finance and stock markets
    - Technology and Media
    - Mathematics
    - Films and Music
    - Gymn goer
    """)

    travel_data = {
        "Country": ["France", "Jamaica", "Scotland", "Spain", "Portugal", "Greece", "Turkey", "USA", "Netherlands", "Trinidad"],
        "Status": ["Visited", "Visited", "Visited", "Visited", "Want to Visit", "Want to Visit", "Want to Visit", "Want to Visit", "Want to Visit", "Want to Visit"],
        "Lat": [46.2276, 18.1096, 56.4907, 40.4637, 39.3999, 39.0742, 38.9637, 37.0902, 52.1326, 10.6918],
        "Lon": [2.2137, -77.2975, -4.2026, -3.7492, -8.2245, 21.8243, 35.2433, -95.7129, 5.2913, -61.2225]
    }

    travel_df = pd.DataFrame(travel_data)

    fig3 = px.scatter_geo(
        travel_df,
        lat="Lat",
        lon="Lon",
        color="Status",
        hover_name="Country",
        text="Country",
        title="My Travel Map",
        color_discrete_map={"Visited": "green", "Want to Visit": "blue"}
    )

    fig3.update_layout(geo=dict(showland=True, showcountries=True, projection_type="orthographic", center=dict(lat=30, lon=-20)))
    fig3.update_traces(marker=dict(size=8))

    interests_tab = mo.vstack([interests, mo.ui.plotly(fig3)])


    mo.ui.tabs({
        "👤 About Me": about_me,
        "🛠️ Skills": skills,
        "⭐ Personal Interests": interests_tab
    })
    return


if __name__ == "__main__":
    app.run()
