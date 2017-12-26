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
        self.x = np.arange(0, self.x_range, self.minimum_update)
        self.y = np.zeros_like(self.x)
        self.z = np.zeros_like(self.x)

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, sharex=False, sharey=False)
        self.lines1, = self.ax1.plot(self.x, self.y)
        self.lines2, = self.ax2.plot(self.x, self.z)

    def updateFig(self, datay, dataz):
        print((datay, dataz))
        self.x += self.interval
        # 先頭を削り新しいデータをケツに挿入
        self.y = np.hstack((self.y[len(datay):], datay))
        self.lines1.set_data(self.x, self.y)
        self.z = np.hstack((self.z[len(dataz):], dataz))
        self.lines2.set_data(self.x, self.z)

        # 描画範囲を更新
        self.ax1.set_xlim((self.x.min(), self.x.max()))
        self.ax1.set_ylim((self.y.min(), self.y.max()))
        self.ax2.set_xlim((self.x.min(), self.x.max()))
        self.ax2.set_ylim((self.z.min(), self.z.max()))
        plt.pause(.01)
