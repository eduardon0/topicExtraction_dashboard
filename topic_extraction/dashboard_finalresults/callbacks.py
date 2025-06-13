from dash import Output, Input, State, dcc
import dash_mantine_components as dmc
import pandas as pd
from pathlib import Path
import pickle
import plotly.io as pio

# from topic_extraction.setUp.setUp_objs import (
#     path_manager
# )

# root_path = path_manager.paths["final_results"]
root_path = Path(__file__).parent / "data"

var_name_chosen = "V241170"



def register_callbacks(app):

    # info - model
    @app.callback(
        Output("info_dashboard-drawer", "opened"),
        Input("info_dashboard-drawer-button", "n_clicks"),
        Input("close-info_dashboard-drawer-button", "n_clicks"),
        State("info_dashboard-drawer", "opened"),
        prevent_initial_call=True
        )
    def toggle_drawer(open_click, close_click, is_open):
        return not is_open

    # info - dashboard
    @app.callback(
        Output("info_model-drawer", "opened"),
        Input("info_model-drawer-button", "n_clicks"),
        Input("close-info_model-drawer-button", "n_clicks"),
        State("info_model-drawer", "opened"),
        prevent_initial_call=True
        )
    def toggle_drawer(open_click, close_click, is_open):
        return not is_open


    # @app.callback(
    #     Output("info_dashboard-drawer", "opened"),
    #     Input("info_dashboard-drawer-button", "n_clicks"),
    #     Input("close-info_dashboard-drawer-button", "n_clicks"),
    #     State("info_dashboard-drawer", "opened"),
    #     prevent_initial_call=True
    #     )
    # def toggle_drawer(open_click, close_click, is_open):
    #     return not is_open

    # update from varName
    @app.callback(
        Output(component_id='freqs-graph', component_property='figure'),
        Output(component_id='reprDocs-dict', component_property='data'),
        # Output(component_id='reprDocs-list', component_property='children'),
        Output(component_id='df-dfDict', component_property='data'),
        Output("varInfo-list", "children"),
        # Output("df-table", "rows"),
        # Output("df-table", "head"),
        Output("df-table", "children"),
        Input(component_id='varName-radio', component_property='value')
    )
    def update_content_fromVarName(var_name_chosen):
        path_fig = root_path / var_name_chosen / "topic_frequencies.json"
        path_dataframe = root_path / var_name_chosen / "data_frame.parquet"
        path_representativedocs = root_path / var_name_chosen / "representative_docs.pkl"


        with open(path_fig, "r", encoding="utf-8") as f:
            fig = pio.from_json(f.read())

        with open(path_representativedocs, "rb") as f:
            reprDocs = pickle.load(f)

        with open(path_dataframe, "rb") as f:
            df = pd.read_parquet(f)
        df["probability"] = df["probability"].map(lambda x: round(x, 2))
        df = df.reset_index(drop=False, inplace=False)


        questions_byVar = {
            "V241170": "What does respondent \n like about Democratic party?",
            "V241174": "What does respondent \n like about Republican party?",
        }
        question = questions_byVar[var_name_chosen]
        n_responses = len(df)

        question_f = f"❓Question: {question}"
        nResponses_f = f"👥Responses: {n_responses}"




        index_col_style = {
            "width": "50px",
            "whiteSpace": "normal",
            "overflow": "hidden",
            "textOverflow": "ellipsis"
        }
        doc_col_style = {
            "maxWidth": "300px",
            "minWidth": "200px",
            "whiteSpace": "normal",
            "overflow": "hidden",
            "textOverflow": "ellipsis"
        }
        topic_col_style = {
            "maxWidth": "100px",
            "minWidth": "100px",
            "whiteSpace": "normal",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "textAlign": "left"
        }
        # Table header
        df_table_head = dmc.TableThead(
            dmc.TableTr([
                dmc.TableTh(x,
                            style=topic_col_style if x.lower() == "topic" else
                            doc_col_style if x.lower() == "document" else
                            index_col_style if x.lower() == "index" else {})
                for x in df.columns
            ])
        )

        # Table body
        df_table_rows = [
            dmc.TableTr([
                dmc.TableTd(
                    element[x],
                    style=topic_col_style if x.lower() == "topic" else
                    doc_col_style if x.lower() == "document" else
                    index_col_style if x.lower() == "index" else  {}
                ) for x in df.columns
            ])
            for element in df.to_dict("records")
        ]

        # df_table_elements =  df.to_dict("records")
        # df_table_rows = [
        #     dmc.TableTr(
        #         [dmc.TableTd(element[x]) for x in df_table_elements[0].keys()]
        #     )
        #     for element in df_table_elements
        # ]
        df_table_body = dmc.TableTbody(df_table_rows)

        # df_table_head = dmc.TableThead(
        #     dmc.TableTr(
        #         [dmc.TableTh(x) for x in df.columns]
        #     )
        # )

        df_table_data = [df_table_head, df_table_body]

        return (
            fig,
            reprDocs,
            df.to_dict("records"),
            [dmc.ListItem(x) for x in [question_f, nResponses_f]],
            # df_table_rows, df_table_head,
            df_table_data
        )


    # representative docs

    @app.callback(
        Output("topic-selector", "data"),
        # Output("topic-selector", "value"),
        Input("reprDocs-dict", "data")
    )
    def popoulate_representativeDocs_topic_selector(xdict):
        # sorted_keys = sorted(map(int, xdict.keys()))
        # str_keys = [str(k) for k in sorted_keys]

        sorted_keys = list(xdict.keys())
        str_keys = [str(k) for k in sorted_keys]

        xdata = [{"label": k, "value": k} for k in str_keys]
        xdefault = str_keys[0] if str_keys else None
        return xdata

    @app.callback(
        Output("docs-list", "children"),
        Input("reprDocs-dict", "data"),
        Input("topic-selector", "value"),
    )
    def update_topic_docs(topics_dict, topic_key):
        docs = topics_dict.get(topic_key, [])

        # output = [dmc.ListItem(doc) for doc in docs]

        output = dmc.Stack(
            gap="md",  # or "md", or a number like 10
            children=[
                dmc.Paper(
                    shadow="sm",
                    p="md",
                    withBorder=False,
                    radius="md",
                    children=dmc.Text(doc_text, size="sm")
                )
                for doc_text in docs
            ]
        )

        return output

    # download sd
    @app.callback(
        Output("download-df", "data"),
        Input("download-df-button", "n_clicks"),
        State("df-dfDict", "data"),
        State(component_id='varName-radio', component_property='value'),
        prevent_initial_call=True
    )
    def download_dataframe(n_clicks1, df_dict, varName):

        # recreate df from dict records
        # df_dict = df.to_dict("records")
        df = pd.DataFrame(df_dict)
        # df = pd.read_parquet("path/to/your/data_frame.parquet")

        fileName_byVar = {
            "V241170": "democrats.csv",
            "V241174": "republicans.csv"
        }
        filename = fileName_byVar[varName]

        return dcc.send_data_frame(df.to_csv, filename=filename, index=False)
