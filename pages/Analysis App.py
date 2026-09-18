import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('data_viz1.csv')
feature_text = pickle.load(open('feature_text.pkl','rb'))


group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

st.header('Features Wordcloud')


# Create sector options
sector_choose = sorted(new_df['sector'].unique().tolist())
sector_choose.insert(1, 'gwal pahari')
selected_sector = st.selectbox('Select sector', sector_choose)

# Filter by sector
if selected_sector == 'overall':
    features_list = sum(feature_text['features'], [])  # Flatten all feature lists
else:
    filtered_df =  new_df[new_df['sector'] == selected_sector]
    if 'features' in filtered_df.columns and not filtered_df.empty:
        features_list = sum(filtered_df['features'], [])
        # Convert feature list to string
        feature_text = ' '.join(features_list)


wordcloud = WordCloud(width = 800, height = 800,
                  background_color ='black',
                  stopwords = set(['s']),
                  min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

Selected_sector = st.selectbox('Select Sector', sector_options)

if Selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == Selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)










