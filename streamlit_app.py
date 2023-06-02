import streamlit
import snowflake.connector
import pandas as pd

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# import color_or_style column in a df
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
df = pd.DataFrame(my_catalog)
streamlit.write(df)

color_list = df[0].values.tolist()
streamlit.write(color_list)

# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
