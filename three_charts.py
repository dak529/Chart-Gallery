# three_charts.py

#
# CHART 1 (PIE)
#

#pie_data = [
 #   {"company": "Company X", "market_share": 0.55},
  #  {"company": "Company Y", "market_share": 0.30},
   # {"company": "Company Z", "market_share": 0.15}
#]

#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) # TODO: create a pie chart based on the pie_data


import plotly
import plotly.graph_objs as go
colors = ['gold', 'mediumturquoise', 'darkorange']
fig = go.Figure(data=[go.Pie(
            labels=['Company X','Company Y','Company Z'],
            values=[0.55,0.30,0.15])])
            #layout=(title="Pie Chart"))])
#layout(title="Pie Chart")
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.show()


#
# CHART 2 (LINE)
#

#line_data = [
   # {"date": "2019-01-01", "stock_price_usd": 100.00},
   # {"date": "2019-01-02", "stock_price_usd": 101.01},
   # {"date": "2019-01-03", "stock_price_usd": 120.20},
   # {"date": "2019-01-04", "stock_price_usd": 107.07},
   # {"date": "2019-01-05", "stock_price_usd": 142.42},
   # {"date": "2019-01-06", "stock_price_usd": 135.35},
   # {"date": "2019-01-07", "stock_price_usd": 160.60},
   # {"date": "2019-01-08", "stock_price_usd": 162.62},
#]

#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

import plotly.graph_objects as go

# Hard Coded (Trial 1)
#fig = go.Figure(go.Bar(
           # x=[123456, 234567, 987654, 876543, 283105, 544099, 121212],
            #y=['Thriller', 'Mystery', 'Sci-Fi', 'Fantasy', 'Documentary','Action', 'Romantic Comedy'],
            #orientation='h'))

#fig.show()

#Dynamic List pull Trial

x = []
y = []

for d in bar_data:
    x.append(d["viewers"])
    y.append(d["genre"])

fig = go.Figure([go.Bar(x=x, y=y, orientation='h')])
fig.show()

#Hard Coded (Example Online)

#fig = go.Figure(go.Bar(
           #x=[20, 14, 23],
           #y=['giraffes', 'orangutans', 'monkeys'],
           #orientation='h'))

#fig.show()
