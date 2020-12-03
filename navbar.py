import dash_bootstrap_components as dbc

def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Home", href="/home")),
              dbc.NavItem(dbc.NavLink("About", href="/about")),
              dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
              #dbc.NavItem(dbc.NavLink("Admin", href="/admin")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Admin",
                 children=[
                    dbc.DropdownMenuItem("Preference"),
                    dbc.DropdownMenuItem("Administration"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Logout"),
                          ],
                      ),
                    ],
          brand="dcnsakthi.co",
          brand_href="#",
          sticky="top",
          color="black",
          dark=True,
        )

     return navbar