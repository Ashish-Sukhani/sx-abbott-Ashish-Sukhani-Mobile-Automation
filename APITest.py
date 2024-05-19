import requests
import pandas as pd

# Fetch the data from the API
data = {"drilldowns": "Nation", "measures": "Population"}
response = requests.get("https://datausa.io/api/data", params=data)
jresponse = response.json()

if response.status_code == 200:
    dataInfo = jresponse["data"]
    sourceInfo = jresponse["source"][0]["annotations"]["source_name"]
    df = pd.DataFrame(dataInfo, columns=['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation'])
    # Sort the DataFrame by 'ID Year'
    sortvalue = df.sort_values('ID Year', ascending=True).reset_index(drop=True)

    # Manually calculate Year-on-Year growth percentage as pct_change is deprecated
    sortvalue['YoY Growth%'] = (sortvalue['Population'] - sortvalue['Population'].shift(1)) / sortvalue['Population'].shift(1) * 100

    # Find the peak growth percentage year and the time duration
    peakGrowthPercent = sortvalue.loc[sortvalue['YoY Growth%'].idxmax()]
    start_year = sortvalue['ID Year'].min()
    end_year = sortvalue['ID Year'].max()
    years = end_year - start_year

    # Find the lowest growth percentage year
    lowestGrowthPercent = sortvalue.loc[sortvalue['YoY Growth%'].idxmin()]
    print(f"According to {sourceInfo}, in {years} years from {start_year} to {end_year}, peak population growth was {peakGrowthPercent['YoY Growth%']:.2f}% in {peakGrowthPercent['Year']} and the lowest population increase was {lowestGrowthPercent['YoY Growth%']:.2f}% in {lowestGrowthPercent['Year']}.")
