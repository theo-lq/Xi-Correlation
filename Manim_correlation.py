from manim import *
from scipy.stats import pearsonr
from xi_correlation import *

class Correlation(Scene):
    
    def sinus(self, size):
        x = np.linspace(-5, 5, size)
        y = x + np.sin(2*x) + 0.5 * np.random.normal(size=size)
        return x, y
    
    
    def squared(self, size):
        x = np.linspace(-5, 5, size)
        y = 0.5 * x**2 + 0.5 *np.random.normal(size=size)
        return x, y
    
    
    def inverse_squared(self, size):
        y, x  = self.squared(size)
        return x, y
    
    
    def blurred(self, size):
        x = np.linspace(-5, 5, size)
        y = 5 * np.random.normal(size=size)
        return x, y
    
    
    
    def create_axis(self, x, y, alpha=0.1):
        x_range = [np.min(x) * (1 - np.sign(np.min(x)) * alpha), np.max(x) * (1 + alpha), 1]
        y_range = [np.min(y) * (1 - np.sign(np.min(y)) * alpha), np.max(y) * (1 + alpha), 1]
        axes = Axes(x_range, y_range, tips=False)
        return axes
    
    
    def create_plot(self, function, **kwargs):
        x, y = function(**kwargs)
        text = "Pearson: %0.2f (p=%0.2f)" % pearsonr(x, y)
        text = text + " | Xi: %0.2f (p=%0.2f)" % xi_correlation(x, y)
        
        axes = self.create_axis(x, y)
        points = axes.plot_line_graph(x, y)
        title = Title(text)
        plot = VGroup(axes, points["vertex_dots"], title)
        return plot
        
    
    
    
    def construct(self):
        size = 300
        plot_1 = self.create_plot(self.sinus, size=size)
        plot_2 = self.create_plot(self.squared, size=size)
        plot_3 = self.create_plot(self.inverse_squared, size=size)
        plot_4 = self.create_plot(self.blurred, size=size)
        self.add(plot_1)
        self.wait(3)
        self.play(Transform(plot_1, plot_2))
        self.wait(3)
        self.play(Transform(plot_1, plot_3))
        self.wait(3)
        self.play(Transform(plot_1, plot_4))
        self.wait(3)