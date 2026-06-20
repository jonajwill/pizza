marinara=0
margherita=2
funghi=1
salame=1
funghiesalame=0
caprese=1
cacioepepe=0
verdura=0
quattrostagioni=0
rossa=2
parmigiana=1
caprino=1
stracciatella=1
cipolle=0


def zutaten(marinara, margherita, funghi, salame, funghiesalame, caprese, cacioepepe, verdura, quattrostagioni, rossa, parmigiana, caprino, stracciatella, cipolle):
    tomaten=100*(marinara+margherita+funghi+salame+funghiesalame+caprese+verdura+quattrostagioni+parmigiana+caprino+stracciatella)
    fiordilatte=90*(margherita+funghi+salame+funghiesalame+caprese+verdura+quattrostagioni+parmigiana+caprino)
    basilikum=5*(marinara+margherita+parmigiana+stracciatella)
    olivenöl=marinara+margherita+funghi+funghiesalame+salame+caprese+verdura+quattrostagioni+parmigiana+caprino+stracciatella
    parmigiano=10*(margherita+funghi+salame+funghiesalame+verdura+parmigiana+stracciatella)
    champignons=2*(funghi+funghiesalame)+verdura+quattrostagioni
    knoblauch=marinara+quattrostagioni
    oregano=marinara+quattrostagioni
    salami=6*(salame+funghiesalame)
    kirschtomaten=7*(caprese+caprino)
    basilikumpesto=caprese+caprino
    balsamico=caprese
    pecorino=30*cacioepepe
    pfeffer=5*(cacioepepe)
    zucchini=4*(verdura+quattrostagioni)
    paprika=verdura
    getrockneteTomaten=7*rossa+3*quattrostagioni
    pestoRosso=100*rossa
    burrata=rossa
    pinienkerne=rossa+cipolle
    aubergine=7*parmigiana
    ziegenkäse=7*caprino+15*cipolle
    stracciatellaDiBurrata=stracciatella
    ricotta=2*cipolle
    zwiebeln=cipolle
    zutatenliste=[tomaten, "g San Marzano Tomaten\n",fiordilatte, "g Fior di latte\n", basilikum, "Blätter Basilikum\n", parmigiano, "g Parmigiano Reggiano\n", champignons, "Champignons\n", knoblauch, "Knoblauchzehen\n", oregano, "Prisen Oregano\n", salami, "Scheiben vegetarische Salami\n", kirschtomaten, "Kirschtomaten\n", basilikumpesto, "EL Basilikumpesto\n", balsamico, "Schuss Aceto di balsamico\n", pecorino, "g Pecorino Romano\n", pfeffer, "schwarze Pfefferkörner\n", zucchini, "Zucchinischeiben\n", paprika, "rote Paprika\n", pestoRosso, "g Pesto Rosso\n", getrockneteTomaten, "getrocknete Tomaten\n", burrata, "Burrata\n", pinienkerne, "EL Pinienkerne\n", aubergine, "Scheiben Aubergine\n", ziegenkäse, "Scheiben Ziegenkäse\n", stracciatellaDiBurrata, "Portionen Stracciatella di burrata\n",ricotta, "EL Ricotta\n", zwiebeln, "Portionen karamellisierte Zwiebeln", olivenöl, "Schuss Olivenöl\n"]
    ausgabe="Zutaten:\n"
    for i in range(int(len(zutatenliste)/2)):
        if zutatenliste[2*i]!=0:
            ausgabe+=str(zutatenliste[2*i])+' '+str(zutatenliste[2*i+1])
    return print(ausgabe)

# zutaten(2,1,0,0,0,0,0,0,0,0,0,0,0,0)
zutaten(marinara, margherita, funghi, salame, funghiesalame, caprese, cacioepepe, verdura, quattrostagioni, rossa, parmigiana, caprino, stracciatella, cipolle)