from dash import Dash
from topic_extraction.dashboard_finalresults.topic_extraction.dashboard_finalresults.layout import layout
from topic_extraction.dashboard_finalresults.topic_extraction.dashboard_finalresults.callbacks import register_callbacks

app = Dash(__name__)
app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
