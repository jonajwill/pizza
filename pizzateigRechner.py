teigart = 'biga'
teiglinganzahl = 6
teiglinggewicht = 285
hydration = 0.7
poolishanteil = 0.3
bigaanteil = 1
rezeptmodus = 'an'


def pizza(teigart,teiglinganzahl,teiglinggewicht,hydration,poolishanteil,bigaanteil,rezeptmodus):
    g = teiglinganzahl*teiglinggewicht
    h = hydration
    p = poolishanteil
    b = bigaanteil
    if teigart == 'poolish':
        mehl_ges = g/(1+h+4/155+3/60*p*h)
        wasser_ges = h*mehl_ges
        wasser_poolish = p*wasser_ges
        mehl_poolish = p*wasser_ges
        if wasser_poolish>=2000:
            hefe_poolish = 2000/30
            honig_poolish=2000/60
        else:
            hefe_poolish = wasser_poolish/30
            honig_poolish = wasser_poolish/60
        salz = mehl_ges*4/155
        mehl_hauptteig = mehl_ges - mehl_poolish
        wasser_hauptteig = wasser_ges - wasser_poolish
        if rezeptmodus == 'aus':
            ausgabe = print(teiglinganzahl, 'Teiglinge á',round(teiglinggewicht),'g mit',hydration*100,'%\nHydration und',round(poolishanteil*100),'% Poolish','\n\nPoolish:', '\n    Mehl:', round(mehl_poolish),'g',
          '\n    Wasser:', round(wasser_poolish),'g',
          '\n    Hefe:', round(hefe_poolish,2),'g',
          '\n    Honig:', round(honig_poolish,2),'g'
          '\n\n Hauptteig:', '\n    Mehl:', round(mehl_hauptteig),'g',
          '\n    Wasser:', round(wasser_hauptteig),'g',
          '\n    Salz:', round(salz,2),'g')
        elif rezeptmodus == 'an':
            ausgabe = print(teiglinganzahl, 'Teiglinge á',round(teiglinggewicht),'g mit',hydration*100,'%\nHydration und',round(poolishanteil*100),'% Poolish','\n\nPoolish:', '\n    Mehl:', round(mehl_poolish),'g',
              '\n    Wasser:', round(wasser_poolish),'g',
              '\n    Hefe:', round(hefe_poolish,2),'g',
              '\n    Honig:', round(honig_poolish,2),'g','\nHefe und Honig im Wasser verrühren. \nNach 2-3 min das Mehl unterrühren. \nDas Poolish nun 1 h bei Raumtemperatur\nund anschließend 16-24 h im Kühl-\nschrank ruhen lassen.'
              '\n\n Hauptteig:', '\n    Mehl:', round(mehl_hauptteig),'g',
              '\n    Wasser:', round(wasser_hauptteig),'g',
              '\n    Salz:', round(salz,2),'g','\nPoolish im Wasser auflösen. Nun die \nHälfte des Mehls einarbeiten.\nAnschließend das Salz und etwas später\ndas restliche Mehl zugeben und\nverkneten. Nach 15 min abgedeckter\nRuhe den Teig dehnen und falten.\n30 min in geölter abgedeckter Schüssel\nruhen lassen. Teiglinge formen und\n1-3 h ruhen lassen.')
    elif teigart == 'direkter Teig':
          mehl = g/(1 + h + 0.001 + 0.03)
          wasser = h*mehl
          salz = 0.03*mehl
          hefe = 0.001*mehl
          if rezeptmodus == 'an':
              ausgabe = print(teiglinganzahl,'Teiglinge á',teiglinggewicht,'g mit',hydration*100,'%\nHydration','\n\nTeig:','\n    Mehl:', round(mehl),'g','\n    Wasser:',round(wasser),'g','\n    Salz:',round(salz,2),'g','\n    Hefe',round(hefe,2),'g','\nSalz im Wasser auflösen. Mehl und Hefe\nhinzugeben und 20 min kneten. Teig\nluftdicht verschlossen für 24 h bei\nRaumtemperatur oder bis zu 72 h im\nKühlschrank ruhen lassen. Teiglinge\nformen und 8-12 h bei Raumtemperatur\nruhen lassen.')
          if rezeptmodus == 'aus':
              ausgabe = print(teiglinganzahl,'Teiglinge á',teiglinggewicht,'g mit',hydration*100,'%\nHydration','\n\nTeig:','\n    Mehl:', round(mehl),'g','\n    Wasser:',round(wasser),'g','\n    Salz:',round(salz,2),'g','\n    Hefe',round(hefe,2),'g')
    elif teigart == 'biga':
          mehl_ges = g/(1+h+0.02+0.01+b*0.01)
          wasser_ges = h*mehl_ges
          salz = 0.02*mehl_ges
          öl = 0.01*mehl_ges
          mehl_biga = b*mehl_ges
          wasser_biga = 0.5*mehl_biga
          hefe_biga = 0.01*mehl_biga
          mehl_haupt = mehl_ges - mehl_biga
          wasser_haupt = wasser_ges - wasser_biga
          hefe_haupt = 1/1200*mehl_ges
          ausgabe = print(teiglinganzahl, 'Teiglinge á',round(teiglinggewicht),'g mit',hydration*100,'%\nHydration und',round(bigaanteil*100),'% Biga','\n\nBiga:', '\n    Mehl:', round(mehl_biga),'g',
          '\n    Wasser:', round(wasser_biga),'g',
          '\n    Hefe:', round(hefe_biga,2),'g (', round(hefe_biga/3,2),'g Trockenhefe)\n\n Hauptteig:', '\n    Mehl:', round(mehl_haupt),'g',
          '\n    Wasser:', round(wasser_haupt),'g',
          '\n    Hefe:', round(hefe_haupt,2),'g (', round(hefe_haupt/3,2),'g Trockenhefe)\n    Salz:', round(salz,2),'g',
          '\n    Öl:', round(öl,2),'g (optional)\n\nGesamtgewicht:',round(teiglinganzahl*teiglinggewicht),'g')
    elif teigart == 'biga capvin':
          mehl_ges = g/(1+h+0.03+b*0.02)
          wasser_ges = h*mehl_ges
          salz = 0.03*mehl_ges
          mehl_biga = b*mehl_ges
          wasser_biga = 0.45*mehl_biga
          hefe_biga = 0.01*mehl_biga
          mehl_haupt = mehl_ges - mehl_biga
          wasser_haupt = wasser_ges - wasser_biga
          hefe_haupt = hefe_biga
          if rezeptmodus == 'aus':
            ausgabe = print(teiglinganzahl, 'Teiglinge á',round(teiglinggewicht),'g mit',hydration*100,'%\nHydration und',round(bigaanteil*100),'% Biga\nnach Vincenzo Capuano','\n\nBiga:', '\n    Mehl:', round(mehl_biga),'g',
          '\n    Wasser:', round(wasser_biga),'g',
          '\n    Hefe:', round(hefe_biga,2),'g (', round(hefe_haupt/3,2),'g Trockenhefe)',
          '\n\nHauptteig:', '\n    Mehl:', round(mehl_haupt),'g',
          '\n    Wasser:', round(wasser_haupt),'g',
          '\n    Salz:', round(salz,2),'g',
	  '\n    Hefe:', round(hefe_haupt,2),'g (', round(hefe_haupt/3,2),'g Trockenhefe)','\n\nGesamtteiggewicht:',round(teiglinganzahl*teiglinggewicht),'g')
          elif rezeptmodus == 'an':
	          ausgabe = print(teiglinganzahl, 'Teiglinge á',round(teiglinggewicht),'g mit',hydration*100,'%\nHydration und',round(bigaanteil*100),'% Biga\nnach Vincenzo Capuano','\n\nBiga:', '\n    Mehl:', round(mehl_biga),'g',
          '\n    Wasser:', round(wasser_biga),'g',
          '\n    Hefe:', round(hefe_biga,2),'g (', round(hefe_haupt/3,2),'g Trockenhefe)', '\n\nHefe im Mehl auflösen. Wasser und Mehl\nsolange vermengen, ohne zu kneten, bis\nalles Mehl vollständig gebunden ist. \n18 Stunden bei 18 ° C ruhen lassen. \n\nHauptteig:', '\n    Mehl:', round(mehl_haupt),'g',
          '\n    Wasser:', round(wasser_haupt),'g',
          '\n    Salz:', round(salz,2),'g',
	  '\n    Hefe:', round(hefe_haupt,2),'g (', round(hefe_haupt/3,2),'g Trockenhefe)', '\n\nGesamtteiggewicht:',round(teiglinganzahl*teiglinggewicht),'g\n\nBiga klein schneiden, mit dem Mehl und\nder Hefe vermengen und Stück für Stück', round(mehl_ges*0.6-wasser_biga),'g Wasser verkneten, bis alles gut\nvermischt ist.\nTeig 15 Minuten ruhen lassen.\nSalz hinzugeben, etwas einarbeiten\nund Stück für Stück die Hälfte des\nverbleibenden Wassers einarbeiten.\nTeig erneut 15 Minuten ruhen lassen.\nStück für Stück das verbleibende\nWasser einarbeiten.\nTeig 1 Stunde bei ruhen lassen.\nTeiglinge formen und 4 bis 6 Stunden\nruhen lassen.')
    elif teigart == 'notfall':
        if rezeptmodus == 'an':
            ausgabe 
        ausgabe = print(888)
    return ausgabe
    
         
         
pizza(teigart,teiglinganzahl,teiglinggewicht,hydration,poolishanteil,bigaanteil,rezeptmodus)
