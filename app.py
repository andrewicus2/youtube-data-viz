import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image_yt = Image.open('youtube-logo-small.png')
st.image(image_yt, width = 80)


st.title("YouTube Data")

# Clean up the data
df = pd.read_csv("Global YouTube Statistics.csv", encoding='unicode_escape')
df = df.dropna()
df.drop(101, axis = 0, inplace = True)

# Sort by top subbed
df_top_subbed = df.head(10)
df_top_subbed_sort = df_top_subbed.sort_values(by="subscribers", ascending=False)

st.dataframe(df.head(5))

st.subheader("Overview")
m1, m2 = st.columns((1,1))
m1.metric(label ='Number of Channels', value = df.shape[0])
m2.metric(label ='Avg Subs', value = df["subscribers"].mean())

top_channels, by_year, by_location = st.tabs(["Top Channels", "Year", "Location"])



top_channels.subheader("Top Channels")
top_channels.bar_chart(data=df_top_subbed_sort, x="Youtuber", y="subscribers", color="#FF0000", use_container_width=True)

group_by_year = df.groupby(['created_year']).size()

by_year.subheader("Channels by Create Year")
by_year.line_chart(group_by_year)

by_location.subheader("Channels by Location")
by_location.map(data=df, latitude="Latitude", longitude="Longitude", color="#FF0000")

list_variables = df.columns
user_selection = st.multiselect("Select two variables",list_variables,["Youtuber", "subscribers"])

tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.title("Line Chart")
tab1.line_chart(data = df, x = user_selection[0], y = user_selection[1])

tab2.title("Bar Chart")
tab2.bar_chart(data = df, x = user_selection[0], y = user_selection[1])


subs_min, subs_max = st.sidebar.slider('Select Subscriber Range', min_value=int(df['subscribers'].min()), max_value=int(df['subscribers'].max()), value=(int(df['subscribers'].min()), int(df['subscribers'].max())))


filtered_df = df[(df['subscribers'] >= subs_min) & (df['subscribers'] <= subs_max)]


st.bar_chart(data = filtered_df, x = "Youtuber", y = "subscribers")
