import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()


header=dbc.Container(
    [
      dbc.Row(
           [
            dbc.Col(
                  [
                     html.H1("dcnsakthi.co"),
                     html.P(
                         """This is skeleton for Python Plotly-Dash Web sites and Web applications using Bootstrap, Core and HTML Components.""",
                         className="lead",
                           ),
                           dbc.Button("Learn more »", color="secondary", className="btn btn-primary btn-large"),
                   ],
               ),
           ],
            no_gutters=True,
            className="jumbotron",
            align="center",
                
        ),
      ]
    )
body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Dash"),
                     html.P(
                         """Dash is Python framework for building web applications. It built on top of Flask, Plotly.js, React and React Js. It enables you to build dashboards using pure Python. Dash is open source, and its apps run on the web browser. In this tutorial, we introduce the reader to Dash fundamentals and assume that they have prior experience with Plotly."""
                            ),
                           dbc.Button("Learn more »", color="secondary"),
                   ],
                  md=4,
               ),
               dbc.Col(
                  [
                     html.H2("PyPI"),
                     html.P(
                         """Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications."""
                            ),
                           dbc.Button("Learn more »", color="secondary"),
                   ],
                  md=4,
               ),
               dbc.Col(
                  [
                     html.H2("Python"),
                     html.P(
                         """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."""
                            ),
                           dbc.Button("Learn more »", color="secondary"),
                   ],
                  md=4,
               ),
                ]
            )
       ],
className="mt-4",
)

footer=dbc.Container(
    [
      dbc.Row(
           [
            dbc.Col(
                  [
                     html.Br(),
                     html.Hr(),
                     html.P(
                         """© 2020 - dcnsakthi.co"""
                           ),
                   ],
               ),
           ],
            no_gutters=True,
            className="ml-auto flex-nowrap mt-3 mt-md-0",
            align="center",
        ),
      ])
def Homepage():
    layout = html.Div([
    nav,
    header,
    body,
    footer
    ])
    return layout

external_stylesheets = ['/static/content/site.css', '/static/content/bootstrap.min.css', '/static/content/bootstrap.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED, external_stylesheets, dbc.themes.BOOTSTRAP])
app.title = 'Home Page - dcnsakthi.co'
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()