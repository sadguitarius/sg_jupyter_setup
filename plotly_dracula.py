import plotly.graph_objects as go
import plotly.io as pio

pio.templates["dracula"] = go.layout.Template(
    layout = {
        'colorway': ['#8be9fd', '#50fa7b', '#ffb86c', '#ff79c6', '#bd93f9', '#ff5555', '#f1fa8c'],
        'font': {'color': '#f8f8f2'},
        'paper_bgcolor': '#282a36',
        'plot_bgcolor': '#282a36',
        'xaxis': {'gridcolor': '#6272a4',
                          'linecolor': '#6272a4',
                          'zerolinecolor': '#6272a4',
        },
        'yaxis': {'gridcolor': '#6272a4',
                          'linecolor': '#282a36',
                          'zerolinecolor': '#282a36',
        }
    }
)
