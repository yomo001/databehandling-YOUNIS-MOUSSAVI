# Dash skriver på Flask och React
# Flask är ett webbramverk för att bygga webbapplikationer med Python
# React är ett JavaScript-bibliotek för att bygga användargränssnitt
# Dash är ett Python-ramverk för att bygga analytiska webbapplikationer

# Dash ger oss möjlighet att bygga webbapplikationer med Python och HTML
# Kan köras i jupyter notebook också och renderas där direkt så att man inte behöver se via webläsare

from dash import Dash, html, dcc, callback, Output, Input


app = Dash("__name__") # skapar en instans av Dash
# __name__ är namnet på filen som körs.



my_H1 = app.layout = html.H1(children= "My dash application.")  # skapar en layout för webbapplikationen
my_H2 = html.H2(children = "More info ...")  # Behöver ej skriva ut children, men bara för tydlighetsskull
my_dropdown = dcc.Dropdown(options = ["Äpple", "Päron", "Apelsin"], value="Päron")
app.layout = html.Div(children = [my_H1, my_H2, my_dropdown]) # layout del: Hur komponenteran ligger i förhållande till varandra


@callback(
        Output(my_H2, component_property="children"),     # Property children vill vi ändra på
        Input(my_dropdown, component_property="value")
)
def update_heading2(fruit):
    return fruit.upper()


# Tre delar man egentligen vill göra
# hmtl komponenter, dash har egna också
# layout
# Funktionalitet som gör att ngt händer när man klickar någonstans: callbacks

# Detta genererar egentligen (kan antingen skrivas såhär i html fil eller via dash html komponenter):
# <div>
#   <h1>My dash application.</h1>
#   <h2>More info ...</h2>
# </div>
# Man skriver med dessa komponenter för att kunna köra med pythonkod.
# https://dash.plotly.com/dash-html-components

# Children: Berättar vilka taggar som finns inom H1. Flesta komponenter har den, berättar vad som ingår i komponenten.
# H1 är en tagg som finns i html
# Det man säger här är att man ska skriva h1 taggen med texten "My dash app.": <h1>My dash app.</h1>
# Då den loopar löpande när den körs uppdaterar den det man ändrar här live.

app.run(debug=True) 
# Den startar servern på med flask och renderar webbapplikationen
# Flask är applikationen som startar servern och renderar det på en webbläsare
# startar servern och renderar webbapplikationen, är igång nu med loop. 
# Debug Lägger till knappen nere till höger i 
# webbläsarsidan. Litet debug verktyg man har. Laddar även om automatiskt så fort man uppdaterar den.

# För att stänga av servern tryck ctrl + c i terminalen

# host=0.0.0.0, så kan man gå in i en lokal server på en annan dator. 
# kommando ipconfig i powershell, terminal. IPv4 adress wirelsess tittar man på då : porten
# Gör man det själv behöver man öppna porten.
# Tillåter varning.
# Man kan göra så och köra igång på dator, sedan ansluta med mobil eller liknande hemma.







