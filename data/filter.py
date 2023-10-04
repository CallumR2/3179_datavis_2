import pandas as pd
import geopandas as gpd

# Load CSV data
df_csv = pd.read_csv('data/Global Electricity Statistics.csv')

# Load the TopoJSON file using geopandas
topojson_data = gpd.read_file('js/ne_110m.topojson')

# Access and work with the topojson_data as needed
print(topojson_data.ne_110m_admin_0_countries.geometries[0])