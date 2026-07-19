fruchtmenge=750

def marmeladenRechner(fruchtmenge):
    suessungsmittel=300/1000*fruchtmenge
    geliermittel=22/1000*fruchtmenge+22/600*suessungsmittel
    return print('Für', fruchtmenge, 'g Früchte:\n',round(geliermittel,1),'g Geliermittel\n',round(suessungsmittel),'g Süßungsmittel')


marmeladenRechner(fruchtmenge)