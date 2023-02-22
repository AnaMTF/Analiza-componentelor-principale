import pandas as pd
import functii as f
import acp.ACP as acp
import grafice as g


tabel = pd.read_csv('./dataIN/Crimes_All_Years.csv', index_col=0)
print(tabel)

etichete_linii = tabel.index.values.tolist()
print(etichete_linii)
etichete_coloane = tabel.columns.values[:].tolist()
print(etichete_coloane)
X = tabel[etichete_coloane].values
print(X); print(type(X)); print(X.shape)

# standardizare matrice de variabile observate
Xstd = f.standardizare(X)
Xstd_df = pd.DataFrame(data=Xstd, columns=etichete_coloane,
                       index=etichete_linii)
Xstd_df.to_csv('./dataOUT/Xstd.csv')

# instatiere obiect ACP
acp_obj = acp.ACP(Xstd)

# salvare vectori proprii in fisier CSV
a_df = pd.DataFrame(data=acp_obj.getVectoriProprii())
a_df.to_csv('./dataOUT/MatriceVectoriProprii.csv')

# realizare grafic valori proprii
g.componentePrincipale(valoriProprii=acp_obj.getValoriProprii())
# g.afisare()

# salvare componente principale in fisier CSV
componente = ['C'+str(j+1) for j in range(len(etichete_coloane))]
C = acp_obj.getComponente()
C_df = pd.DataFrame(data=C,
        columns=componente,
        index=etichete_linii)
C_df.to_csv('./dataOUT/ComponentePrincipale.csv')

# realizarea corelogramei factorilor de corelatie
Rxc = acp_obj.getRxc()
Rxc_df = pd.DataFrame(data=Rxc,
    columns=componente,
    index=etichete_coloane)
Rxc_df.to_csv('./dataOUT/FactoriCorelatie.csv')
g.corelograma(matrice=Rxc_df, titlu='Corelograma factorilor de corelatie')
# g.afisare()

# corelogram scorurilor
scoruri = acp_obj.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri,
                          columns=componente,
                          index=etichete_linii)
# salvare scoruri in fisier CSV
scoruri_df.to_csv('./dataOUT/Scoruri.csv')

g.corelograma(matrice=scoruri_df, titlu='Corelorgrama scorurilor')
# g.afisare()

# corelograma calitatiii observatiilor pe axele componentelor principale
calObs = acp_obj.getCalObs()
calObs_df = pd.DataFrame(data=calObs,
                         columns=componente,
                         index=etichete_linii)
# salvare calitateatea observatiilor in fisier CSV
calObs_df.to_csv('./dataOUT/CalitateaObs.csv')

g.corelograma(matrice=calObs_df,
    titlu='Corelograma calitatiii observatiilor pe axele componentelor principale')
# g.afisare()

# cercul corelatiilor cu variabilele observate
g.cerculCorelatiilor(matrice=Rxc_df,
        titlu='Variabilele initiale in spatiul componentelor principale C1 si C2')
# g.afisare()


# cercul corelatiilor cu scoruri
scoruri = acp_obj.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, columns=componente,
                          index=etichete_linii)

g.cerculCorelatiilor(matrice=scoruri_df, titlu='Cercul corelatiilor al scorurilor calitative')


# corelograma comunalitatilor
comun = acp_obj.getComun()
comun_df = pd.DataFrame(data=comun,
                        columns=componente,
                        index=etichete_coloane)
# salvare comunalitati in fisier CSV
comun_df.to_csv('./dataOUT/Comunalitati.csv')

g.corelograma(matrice=comun_df, titlu='Corelograma comunalitatilor')
g.afisare()

