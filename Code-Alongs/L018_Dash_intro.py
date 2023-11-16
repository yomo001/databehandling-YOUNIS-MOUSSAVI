# Dash skriver på Flask och React
# Flask är ett webbramverk för att bygga webbapplikationer med Python
# React är ett JavaScript-bibliotek för att bygga användargränssnitt
# Dash är ett Python-ramverk för att bygga analytiska webbapplikationer

# Dash ger oss möjlighet att bygga webbapplikationer med Python och HTML
# Kan köras i jupyter notebook också och renderas där direkt så att man inte behöver se via webläsare

from dash import Dash, html, dcc, callback, Output, Input

# Tre delar man egentligen vill göra

# hmtl komponenter, dash har egna också
# layout
# Funktionalitet som gör att ngt händer när man klickar någonstans: callbacks




app = Dash("__name__") # skapar en instans av Dash klassen
# __name__ är namnet på filen som körs.



# Skapar komponenter
my_H1 = html.H1(children= "My dash application.")  # Skapar en rubrik komponent, Behöver ej skriva ut children, men bara för tydlighetsskull
my_H2 = html.H2(children = "More info ...")  # Skapar underrubrik komponent
my_dropdown = dcc.Dropdown(options = ["Äpple", "Päron", "Apelsin"], value="Päron") # Skapar en dropdown komponent, options är en lista med alternativ, value är default värde

# Detta genererar egentligen (kan antingen skrivas såhär i html fil eller via dash html komponenter):
# <div>
#   <h1>My dash application.</h1>
#   <h2>More info ...</h2>
# </div>
# och sedan liknande HTML kod med olika css styling för att skapa buttom
# Man skriver med dessa komponenter för att kunna köra med pythonkod.
# https://dash.plotly.com/dash-html-components
# Children: Berättar vilka taggar som finns inom H1. Flesta komponenter har den, berättar vad som ingår i komponenten.
# H1 är en tagg som finns i html


# Lägger till komponenter i layouten
app.layout = html.Div(children = [my_H1, my_H2, my_dropdown]) # layout del: Hur komponenteran ligger i förhållande till varandra


# Funktionalitet
@callback(   # callback är en property som finns i Dash, den tar in en lista med inputs och outputs
        Output(my_H2, component_property="children"),    # Output är en property som finns i Dash, den tar in en komponent och en property 
        Input(my_dropdown, component_property="value")   # Input är en property som finns i Dash, den tar in en komponent och en property
)                                                        
def update_heading2(fruit):                              # Funktion som tar in en frukt och returnerar den med stora bokstäver
    return fruit.upper()                                 



app.run(debug=True) 
# Den startar servern på med flask och renderar webbapplikationen
    # Då den loopar löpande när den körs uppdaterar den det man ändrar här live.    
# Debug Lägger till knappen nere till höger i webbläsarsidan. Litet debug verktyg man har. Laddar även om automatiskt så fort man uppdaterar den.

# För att stänga av servern tryck ctrl + c i terminalen

# Gå in i en lokal server på annan dator
    # host=0.0.0.0, så kan man gå in i en lokal server på en annan dator. 
    # kommando ipconfig i powershell, terminal. IPv4 adress wirelsess tittar man på då : porten
    # Gör man det själv behöver man öppna porten.
    # Tillåter varning.
    # Man kan göra så och köra igång på dator, sedan ansluta med mobil eller liknande hemma.

#Mer om detta:

# Diverse anteckningar:
    # Bli värd så andra kan gå in i ens server:
        # host=0.0.0.0, jupyter external så kan man gå in i en lokal server på en annan dator. 
        # kommando ipconfig i powershell, terminal. IPv4 adress wirelsess tittar man på då : porten
        # Gör man det själv behöver man öppna porten.
        # Tillåter varning.
        # Man kan göra så och köra igång på dator, sedan ansluta med mobil eller liknande hemma.


    #IP adress is built on:
        # 1. The network adress
        # 2. The subnet mask
        # 3. The host adress
        # 4. The port number

    # I vårt fall där vi kör lokalt på datorn:
        # IP Nummer pekar på adress till datorn, och porten pekar på adress till tjänsten på datorn
        # Kör man redan något på 8050, så väljer man annan port.
        # Kör på port 8050, komplierad diskussion tyckte han om hur man ska veta portnummer






