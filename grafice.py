import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def corelograma(matrice=None, dec=1, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice, dec), cmap='Spectral', vmin=valMin, vmax=valMax, annot=True)


def cerculCorelatiilor(matrice=None, X1=0, X2=1, raza=1, dec=2, titlu='Cercul corelatiilor',
                       valMin=-1, valMax=1, etichetaX=None, etichetaY=None):
    plt.figure(titlu, figsize=(8, 8))
    plt.title(titlu, fontsize=14, color='indigo', verticalalignment='bottom')
    # construirea coordonatelor punctelor pe cerc
    T = [t for t in np.arange(0, np.pi*2, 0.01)]
    X = [np.cos(t)*raza for t in T]
    Y = [np.sin(t)*raza for t in T]
    plt.plot(X, Y)
    plt.axhline(y=0, color='deepskyblue')
    plt.axvline(x=0, color='deepskyblue')
    if etichetaX==None or etichetaY==None:
        if isinstance(matrice, pd.DataFrame):
            plt.xlabel(xlabel=matrice.columns[X1], fontsize=14, color='crimson', verticalalignment='top')
            plt.ylabel(ylabel=matrice.columns[X2], fontsize=14, color='crimson', verticalalignment='bottom')
        else:
            plt.xlabel(xlabel='Var ' + str(X1 + 1), fontsize=14, color='crimson', verticalalignment='top')
            plt.ylabel(ylabel='Var ' + str(X2 + 1), fontsize=14, color='crimson', verticalalignment='bottom')
    else:
        plt.xlabel(xlabel=etichetaX, fontsize=14, color='blueviolet', verticalalignment='top')
        plt.ylabel(ylabel=etichetaY, fontsize=14, color='blueviolet', verticalalignment='bottom')

    if isinstance(matrice, np.ndarray):
        plt.scatter(x=matrice[:, X1], y=matrice[:, X2], color='orange', vmin=valMin, vmax=valMax)
        for i in range(matrice.shape[0]):
            # plt.text(x=0.25, y=0.25, s='un text')
            # plt.text(x=matrice[i, X1], y=matrice[i, X2], s='eticheta')
            plt.text(x=matrice[i, X1], y=matrice[i, X2], s='(' +
                    str(np.round(matrice[i, X1], dec)) + ', ' +
                    str(np.round(matrice[i, X2], dec)) + ')')

    if isinstance(matrice, pd.DataFrame):
        # plt.text(x=0.25, y=0.25, s='avem un pandas.DataFrame')
        plt.scatter(x=matrice.iloc[:, X1], y=matrice.iloc[:, X2], color ='orangered', vmin=valMin, vmax=valMax)
        # for i in range(matrice.index.shape[0]):
        # for i in range(len(matrice.index)):
        for i in range(matrice.values.shape[0]):
            # plt.text(x=matrice.iloc[i, X1], y=matrice.iloc[i, X2], s='(' +
            #            str(np.round(matrice.iloc[i, X1], dec)) + ', ' +
            #            str(np.round(matrice.iloc[i, X2], dec)) + ')')
            plt.text(x=matrice.iloc[i, X1], y=matrice.iloc[i, X2], s=matrice.index[i])


def componentePrincipale(valoriProprii=None, titlu='Varianta explicata de componentele pricipale',
                         etichetaX='Componente principale', etichetaY='Valori proprii'):
    plt.figure(titlu, figsize=(11, 8))
    plt.title(titlu, fontsize=14, color='indigo', verticalalignment='bottom')
    plt.xlabel(xlabel=etichetaX, fontsize=14, color='blueviolet', verticalalignment='top')
    plt.ylabel(ylabel=etichetaY, fontsize=14, color='blueviolet', verticalalignment='bottom')
    componente = ['C'+str(i+1) for i in range(len(valoriProprii))]
    plt.axhline(y=1, color='orangered')
    plt.plot(componente, valoriProprii, 'bo-')


def norPuncte(matrice=None, titlu='Grafic nor de puncte', etichetaX='Variabile',
              etichetaY='Observatii'):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    plt.xlabel(xlabel=etichetaX, fontsize=14, color='k', verticalalignment='top')
    plt.ylabel(ylabel=etichetaY, fontsize=14, color='k', verticalalignment='bottom')

    plt.scatter(x=matrice.iloc[:, 0].values, y=matrice.index[:])


def afisare():
    plt.show()