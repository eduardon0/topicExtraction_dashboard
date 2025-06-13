from dash import dcc, html
import dash_mantine_components as dmc

# from topic_extraction.setUp.setUp_objs import (
#     var_names
# )

var_names = ["V241170", "V241174"]
varNames_data = [
    ["V241170", "Democratic", "blue"],
    ["V241174", "Republican", "red"]
]


layout = dmc.MantineProvider(
    theme={
        "colorScheme": "light",
        "primaryColor": "violet",
        # "fontFamily": "Inter, sans-serif",
        "defaultRadius": "md",
        # "headings": {"fontWeight": 600},
    },

    children=[
        dmc.Container(
            fluid=True,
            style={"height": "100vh"},
            children=[
                # dmc.Title("Topic Extraction GridSearch", order=2),
                dmc.Center([
                    dmc.Group([
                        # dmc.Title("Liked Traits of American Parties", order=1),
                        dmc.Title(
                            dmc.Text(
                                "Liked Traits of American Parties: Topic Modeling of Open-Ended Survey Responses",
                                variant="gradient",
                                gradient={"from": "blue", "to": "red", "deg": 45},
                                inherit=True
                            ),
                            order=1
                        )
                    ])
                ]),
                dmc.Space(h=30),

                dmc.Grid(
                    style={"height": "100vh"},  # stretch grid
                    children=[

                        dmc.GridCol(
                            span=2,
                            # span="auto",
                            style={
                                # "height": "90vh",
                                # "border": "1px solid #e0e0e0",  # light neutral grey
                                # "textAlign": "center",
                                # "padding": "10px",
                                # "borderRadius": "20px"
                            },
                            children=[
                                dmc.Flex(
                                    direction="column",
                                    justify="space-between",
                                    # style={"height": "100%"},
                                    children=[

                                        dmc.Box(
                                            style={
                                                # "height": "100%",
                                                "border": "1px solid #e0e0e0",  # light neutral grey
                                                "textAlign": "center",
                                                "padding": "20px 10px 20px 10px",
                                                "borderRadius": "20px"
                                            },
                                            children=[
                                                dmc.Tabs(
                                                    value="tab-varSelector",
                                                    children=[
                                                        dmc.TabsList([
                                                            dmc.TabsTab("🏛️ Party", value="tab-varSelector")
                                                        ], grow = False),
                                                        dmc.TabsPanel(
                                                            value="tab-varSelector",
                                                            children=[
                                                                dmc.Space(h=10),
                                                                dmc.RadioGroup(
                                                                    # label="⚙️Variable",
                                                                    # children=[dmc.Radio(i, value=i) for i in var_names],
                                                                    children=[dmc.Radio(l, value=k, color=c) for k, l, c in varNames_data],
                                                                    id="varName-radio",
                                                                    value=var_names[0],
                                                                    size="sm"
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.Space(h=50),
                                                # dmc.Box(
                                                #     style={
                                                #         # "height": "100%",
                                                #         "border": "1px solid #e0e0e0",  # light neutral grey
                                                #         "textAlign": "center",
                                                #         "padding": "10px",
                                                #         # "padding-bottom": "40px",
                                                #         "borderRadius": "20px"
                                                #     },
                                                #     children=[
                                                #         dmc.Space(h=5),
                                                dmc.List(
                                                    id="varInfo-list",
                                                    size="sm",
                                                    spacing="sm",
                                                    style={"textAlign": "left"}
                                                )
                                                #     ]
                                                # ),
                                            ]
                                        ),
                                        dmc.Space(h=30),
                                        dmc.Box(
                                            style={
                                                # "height": "70%",
                                                "border": "1px solid #e0e0e0",  # light neutral grey
                                                "textAlign": "center",
                                                "padding": "10px",
                                                "borderRadius": "20px"
                                            },
                                            children=[
                                                dmc.Flex(
                                                    justify="center",
                                                    align="center",
                                                    direction="column",
                                                    # style={"height": "100%"},  # or full parent height
                                                    children=[
                                                        dmc.Button(
                                                            children="ℹ️ Model Info",
                                                            id="info_model-drawer-button",
                                                            variant="light",
                                                            fullWidth=True
                                                        ),
                                                        dmc.Space(h=10),
                                                        dmc.Button(
                                                            children="ℹ️ Dashboard Info",
                                                            id="info_dashboard-drawer-button",
                                                            variant="light",
                                                            fullWidth=True
                                                        ),
                                                    ]
                                                ),
                                                dmc.Drawer(
                                                    title="Model information",
                                                    id="info_model-drawer",
                                                    position="right",
                                                    padding="md",
                                                    opened=False,
                                                    children=[
                                                        dmc.Stack(
                                                            style={"gap": "0.5rem"},
                                                            children=[
                                                                # Section: Topic Modeling
                                                                dmc.Title("Topic Modeling", order=4),
                                                                dmc.Text(
                                                                    "Topic modeling is a text analysis technique that uncovers recurring themes or topics across a collection of documents. "
                                                                    "In the context of this dashboard, it is used to summarize and categorize open-ended survey responses by identifying the main ideas expressed.",
                                                                    size="sm"
                                                                ),

                                                                # Section: BERTopic
                                                                dmc.Title("BERTopic", order=4),
                                                                dmc.Text(
                                                                    "BERTopic is a topic modeling framework that leverages state-of-the-art language models like BERT to generate document embeddings, "
                                                                    "which are then clustered using dimensionality reduction and density-based algorithms. This approach produces interpretable topics "
                                                                    "that are particularly effective for short texts such as survey answers.",
                                                                    size="sm"
                                                                ),

                                                                # Section: Data Processing
                                                                dmc.Title("Data Processing", order=4),
                                                                dmc.Text(
                                                                    "The survey data was processed entirely in Python. Preprocessing included programmatically simplifying or replacing terms that introduced noise, "
                                                                    "such as overly specific phrases, spelling variants, or redundant expressions. This helped standardize responses and improve topic coherence. "
                                                                    "After preprocessing, each response was transformed into vector embeddings using a BERT model.",
                                                                    size="sm"
                                                                ),
                                                                dmc.Text(
                                                                    "Although the original ANES survey questions allowed multiple open-ended responses per respondent, "
                                                                    "only the first response was used for topic modeling to ensure consistency and to reduce noise in the analysis.",
                                                                    size="sm"
                                                                ),

                                                                dmc.Title("Limitations", order=4),
                                                                dmc.Text(
                                                                    "It’s important to note that topic labeling is not perfect. Although the model identifies dominant patterns in the data, "
                                                                    "some responses may be misclassified or grouped into a generic 'outlier' category if they don't clearly align with any specific theme. "
                                                                    "Labels are automatically generated and then manually refined, but edge cases and ambiguous responses may still lead to imperfect classification.",
                                                                    size="sm"
                                                                ),

                                                                dmc.Space(h=10),
                                                                dmc.Button("Close", id="close-info_model-drawer-button", variant="subtle",
                                                                           size="xs"
                                                                           )
                                                            ]
                                                        )
                                                    ]

                                                ),
                                                dmc.Drawer(
                                                    title="Dashboard information",
                                                    id="info_dashboard-drawer",
                                                    position="right",
                                                    padding="md",
                                                    opened=True,
                                                    children=[
                                                        dmc.Stack(
                                                            style={"gap": "0.5rem"},
                                                            children=[
                                                                dmc.Title("What is this dashboard?", order=4),
                                                                dmc.Text(
                                                                    "This dashboard displays topic modeling results from open-ended survey responses in the ANES 2024 study. Each question asks respondents what they like about one of the two main political parties in the United States: the Democratic Party and the Republican Party.",
                                                                    size="sm"
                                                                ),

                                                                dmc.Title("How to use it", order=4),
                                                                dmc.List(
                                                                    size="sm",
                                                                    spacing="xs",
                                                                    icon=html.Span("•"),
                                                                    children=[
                                                                        dmc.ListItem(
                                                                            "Select a party from the left panel to explore topics."),
                                                                        dmc.ListItem(
                                                                            "Use the 'Topic Distribution' tab to view topic distributions."),
                                                                        dmc.ListItem(
                                                                            "Browse representative answers in the 'Representative Docs' tab."),
                                                                        dmc.ListItem(
                                                                            "Explore all processed data in the 'Full results' tab."),
                                                                    ]
                                                                ),

                                                                dmc.Title("Tabs explained", order=4),
                                                                dmc.Text("🌎 Topic Distribution",
                                                                         style={"fontWeight": 500},
                                                                         size="sm", mt=5
                                                                ),
                                                                dmc.Text(
                                                                    "Bar chart showing the proportion of responses in each topic.",
                                                                    size="sm"),

                                                                dmc.Text("📄 Representative Docs",
                                                                         style={"fontWeight": 500},
                                                                         size="sm", mt=5
                                                                ),
                                                                dmc.Text(
                                                                    "Select a topic to see top responses most associated with it.",
                                                                    size="sm"),

                                                                dmc.Text("🗃️ Full results",
                                                                         style={"fontWeight": 500},
                                                                         size="sm", mt=5
                                                                ),
                                                                dmc.Text(
                                                                    "Browse and download the full dataset including document-topic assignments.",
                                                                    size="sm"),

                                                                dmc.Title("Data Source", order=4, mt=5),
                                                                dmc.Text(
                                                                    "Based on the 2024 American National Election Studies open-ended responses.",
                                                                    size="sm"),

                                                                dmc.Space(h=10),
                                                                dmc.Button("Close", id="close-info_dashboard-drawer-button", variant="subtle",
                                                                           size="xs")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        #     ]
                        # ),
                        dmc.GridCol(
                            # span=11.2,
                            # span="content",
                            span="auto",
                            style={
                                "height": "100%",
                                "border": "1px solid #e0e0e0",  # light neutral grey
                                # "textAlign": "center",
                                "padding": "10px",
                                "margin": "20px 4px 0 4px",
                                "borderRadius": "20px"
                            },
                            children=[
                                dmc.Tabs(
                                    variant="pills",
                                    value="tab-fig",
                                    children=[
                                        dmc.TabsList([
                                            dmc.TabsTab("🌎 Topic Distribution", value="tab-fig"),
                                            dmc.TabsTab("📄 Representative Docs", value="tab-reprDocs"),
                                            dmc.TabsTab("🗃️ Full results", value="tab-df"),
                                            ],
                                        grow = True,
                                        justify="space-around",
                                        style={"padding": "12px 16px"}  # affects all children

                                        ),
                                        dmc.TabsPanel(
                                            value="tab-fig",
                                            children=[
                                                # dcc.Store(id="freqs-graph"),
                                                dmc.Space(h=10),
                                                dcc.Graph(id="freqs-graph", style={"height": "80vh"})
                                            ]
                                        ),
                                        dmc.TabsPanel(
                                            value="tab-reprDocs",
                                            children=[
                                                dcc.Store(id="reprDocs-dict"),
                                                dmc.Space(h=10),
                                                dmc.Select(
                                                    id="topic-selector",
                                                    # description="topic",
                                                    placeholder="Select a topic",
                                                    # label="Topic",
                                                    clearable=False,
                                                    searchable=False,
	                                                variant="filled",
	                                                radius="xl",
                                                ),
                                                dmc.Space(h=20),
                                                dmc.List(id="docs-list",
                                                         spacing="sm",
                                                         size="sm",
                                                         icon=html.Span(
                                                             "•")
                                                         )

                                            ]
                                        ),
                                        dmc.TabsPanel(
                                            value="tab-df",
                                            children=[
                                                dcc.Store(id="df-dfDict"),
                                                dmc.Space(h=10),
                                                # dash_table.DataTable(
                                                #     id="df-dfDict",
                                                #     data=[],
                                                #     page_size=20,
                                                #     sort_action="native",
                                                #     style_table={
                                                #         "overflowX": "auto"},
                                                #     style_cell={
                                                #         "textAlign": "left",
                                                #         "whiteSpace": "normal"
                                                #     },
                                                # ),
                                                dmc.Group(
                                                    justify="flex-end",
                                                    children=[
                                                        dmc.Button("⬇️ Download CSV", id="download-df-button",
                                                                   variant="outline"),
                                                        dcc.Download(id="download-df")
                                                    ]
                                                ),
                                                dmc.Space(h=10),
                                                dmc.TableScrollContainer(
                                                    dmc.Table(
                                                        id="df-table",
                                                        highlightOnHover=False
                                                    ),
                                                    maxHeight=600,
                                                    minWidth=100,
                                                    type="scrollarea",
                                                )

                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)