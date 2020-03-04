import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

from prepare_data import read_from_file


def colors (labels):
    return ['green' if label == 'P' else 'red' for label in labels]

chips = 'data/chips.csv'
geyser = 'data/geyser.csv'

X, y = read_from_file(geyser)

clf = svm.SVC(kernel='linear', C=10.0)
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=colors(y), cmap=plt.cm.Paired)


ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()


xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)


ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')

plt.show()
