import numpy as np
import matplotlib.pyplot as plt


class RealtimePlot(object):
    # interval:データの更新頻度(sec)
    # x_range:描画範囲(sec)
    def __init__(self, interval, x_range):
        self.minimum_update = 0.01
        self.interval = interval
        self.x_range = x_range

    def initializeFig(self):
        self.fig, self.ax = plt.subplots(1, 1)
        self.x = np.arange(0, self.x_range, self.minimum_update)
        self.y = np.zeros_like(self.x)
        self.lines, = self.ax.plot(self.x, self.y)

    def updateFig(self, data):
        self.x += self.interval
        # 先頭を削り新しいデータをケツに挿入
        dataarray = np.array(data, dtype=int)
        self.y = np.hstack((self.y[len(data):], dataarray))
        self.lines.set_data(self.x, self.y)
        # 描画範囲を更新
        self.ax.set_xlim((self.x.min(), self.x.max()))
        self.ax.set_ylim((self.y.min(), self.y.max()))
        plt.pause(.01)
