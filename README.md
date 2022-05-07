# Xi correlation coefficient

Implementation of the Xi correlation coefficient described by Sourav Chatterjee in https://arxiv.org/abs/1909.10140. There exists other implementation, but none of them suits me well. I prefered to rebuild it, and decided to use functionnal programming to look like the *pearsonr* or *spearmanr* function from scipy.stats.


## Visual comparison between Pearson and Xi correlation coefficient

https://user-images.githubusercontent.com/63822750/167273825-cd75fa7f-7ef7-4f5c-b86c-af1039cfe3eb.mp4


## Additionnal scripts:
* *Manim_correlation.py* : script generating the above animation
* *Correlation_matrix.py* : script that both compute and show a correlation matrix for any given correlation function as long as it returns a tuple (coefficient, pvalue)


## Example of use
```python
import numpy as np
import pandas as pd
import Xi_Correlation
import Correlation_matrix



size = 500
x = np.linspace(start=-15, stop=15, num=size)
y = x / 2 + np.sin(x) + 0.8 * np.random.normal(size=size)
z = (x ** 2) / 5 + 0.8 * np.random.normal(size=size)
random = np.random.normal(size=size)
df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'random': random})



print(xi_correlation(x, y))
show_correlation_matrix(df, xi_correlation)
```
One can check the vision with the function *pairplot* from seaborn.
