import pandas as pd
import plotly.express as px
import os
import numpy as np

import plotly.io as pio
pio.renderers.default = "browser"

import plotly.graph_objects as go

def find_fit(x, y):
    # Make fit;
    try:
        z = np.polyfit(x, y, 4)

        p = np.poly1d(z)

        return p

    except TypeError:

        return None

data_dir = '/Users/rplesha/Desktop/random_scripts/ScienceSaturday/data'

df_order = pd.read_csv(os.path.join(data_dir, 'SS2_beerOrder.csv'))
df_ratings = pd.read_csv(os.path.join(data_dir, 'SS2_beerScores.csv'))

ratings_only = df_ratings.drop(columns='Beer_Letter')

fig = px.scatter(df_ratings, y=df_ratings.mean(axis=1), size=df_ratings.std(axis=1), error_y=df_ratings.std(axis=1))#, #color=ratings_only.mean(axis=1))

#fig = px.scatter(ratings_only, y=ratings_only.mean(axis=1), size=ratings_only.std(axis=1), error_y=ratings_only.std(axis=1))#, #color=ratings_only.mean(axis=1))
fig.show()

# beer_order = []
# beer = []
# beer_ratings = []
# people = []
# for beer_letter in df_order['Beer_Letter']:
#     for person in ratings_only.keys():
#         try:
#             wh_beer = np.where(np.array(df_order[person]) == beer_letter)[0][0]
#         except IndexError:
#             continue
#         beer_ratings.append(ratings_only[person][wh_beer])
#         beer_order.append(wh_beer)
#         #print(beer_letter, wh_beer, df_order['Beer'][df_order['Beer_Letter'] == beer_letter].iloc[0])
#         beer.append(df_order['Beer'][df_order['Beer_Letter'] == beer_letter].iloc[0])
#         people.append(person)
# df = pd.DataFrame({'beer' : beer, 'order' : beer_order, 'rating' : beer_ratings, 'person' : people})
#
# #fig = px.scatter(df, x='order', y='rating', color='beer')
#
# df = df.sort_values(by=['order'])
#
# fig = go.Figure()
# for beer in np.unique(df['beer']):
#     mask = df['beer'] == beer
#     fig.add_trace(go.Scatter(x=df['order'][mask],
#                              y=df['rating'][mask],
#                              mode='markers',
#                              marker=dict(size=12,
#                                          color=['red']),
#                              name = beer
#                                     ))
#
#     p = find_fit(df['order'][mask], df['rating'][mask])
#
#     if p != None:
#         fig.add_trace(go.Scatter(x=df['order'][mask],
#                                  y=p(df['order'][mask]),
#                                  mode='lines',
#                                  name=f'{beer} Fit',
#                                  line = dict(width=4,
#                                              dash='dash')
#                                 ))
#
# fig.show()

# fig = go.Figure()
# for person in ratings_only.keys():
#     print(person)
#     temp_data = df_order[person]
#     temp_data['number_order'] = [temp_data[temp_data == l.strip()].index[0] for l in df_order['Beer_Letter']]
#
#     temp_data['ranking'] = [df_ratings[person][df_ratings['Beer_Letter'] == l] for l in df_order['Beer_Letter']]
#
#     #print(temp_data)
#     fig.add_trace(go.Scatter(x=temp_data['number_order'], y=temp_data['ranking'], mode='markers'))
#     break
# fig.show()
