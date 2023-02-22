'''
Clasa care incapsuleaza implementarea modelului de ACP
'''
import numpy as np

class ACP:
    def __init__(self, X):
        self.X = X

        self.Cov = np.cov(self.X, rowvar=False)  # avem variabilele pe coloane

        self.valori_prop, self.vectori_prop = np.linalg.eigh(self.Cov)
        # print('Valori proprii:', self.valori_prop)
        # print('Vectori proprii:', self.vectori_prop.shape)

        # sortam descrescator valorile proprii si pe baza indicilor lor si vectorii proprii
        k_des = [k for k in reversed(np.argsort(self.valori_prop))]
        # print(k_des)
        self.alpha = self.valori_prop[k_des]
        # print(self.alpha)
        self.a = self.vectori_prop[:, k_des]
        # print(self.a)

        # regularizarea vectorilor proprii
        for j in range(self.X.shape[1]):
            minCol = np.min(self.a[:, j])
            maxCol = np.max(self.a[:, j])
            if np.abs(minCol) > np.abs(maxCol):
                self.a[:, j] = -self.a[:, j]

        # calcul componente principale
        self.C = self.X @ self.a  # inmultire matrici dreptunghiulare
        # self.C = np.matmul(x1=self.X, x2=self.a)

        # calcul factori de corelatie (corelatia dintre variabilele observate
        # si cimponentele principale) - factor loading
        self.Rxc = self.a * np.sqrt(self.alpha)


    def getValoriProprii(self):
        return self.alpha

    def getVectoriProprii(self):
        return self.a

    def getComponente(self):
        return self.C

    def getRxc(self):
        return self.Rxc

    def getScoruri(self):
        return self.C / np.sqrt(self.alpha)

    def getCalObs(self):
        C2 = self.C * self.C
        return C2 / np.sum(C2, axis=0)  # sume pe coloane

    def getComun(self):
        Rxc2 = self.Rxc * self.Rxc
        return np.cumsum(a=Rxc2, axis=1)  # sume cumulative pe linii


