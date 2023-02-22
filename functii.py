import numpy as np


def standardizare(X):
    if isinstance(X, np.ndarray):
        medii = np.mean(a=X, axis=0)  # medii pe coloane
        abateriStd = np.std(a=X, axis=0)  # abateri standard pe coloane
        Xstd = (X - medii) / abateriStd
        return Xstd
