import requests
import pandas as pd

data = {"drilldowns": "Nation", "measures": "Population"}
response = requests.get("https://datausa.io/api/data", params=data)
jresponse = response.json()
if response.status_code == 200:
    print(jresponse)
    dataInfo = jresponse["data"]
    sourceInfo = jresponse["source"][0]["annotations"]["source_name"]

    df = pd.DataFrame(dataInfo,
                      columns=['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation', 'YoY Growth%'])

    # Calculating Year-on-Year growth of population
    df_sortvalue = df.sort_values('ID Year', ascending=True)
    df_sortvalue['YoY Growth%'] = (df_sortvalue.select_dtypes(include=['int', 'float']).pct_change()['Population'])

    # Peak growth percentage year and calculating the time duration
    peakGrowthPercent = df_sortvalue.loc[df_sortvalue['YoY Growth%'].idxmax()]
    start_year = df_sortvalue['ID Year'].min()
    end_year = df_sortvalue['ID Year'].max()
    years = end_year - start_year

    # Lowest growth percentage year
    lowestGrowthPercent = df_sortvalue.loc[df_sortvalue['YoY Growth%'].idxmin()]
    print("According to", sourceInfo + ", in " + str(years) + " years from " + str(start_year) + " to " + str(
        end_year) + ", peak population growth was {:.2%}".format(peakGrowthPercent['YoY Growth%']),
          "in " + peakGrowthPercent['Year'],
          "and the lowest population increase was {:.2%}".format(lowestGrowthPercent['YoY Growth%']), "in",
          lowestGrowthPercent['Year'])
