import os
from dash import Dash
from topic_extraction.dashboard_finalresults.layout import layout
from topic_extraction.dashboard_finalresults.callbacks import register_callbacks

app = Dash(__name__)
app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # Render sets PORT
    app.run(host="0.0.0.0", port=port, debug=False)
    # app.run(debug=True, port=8080)
