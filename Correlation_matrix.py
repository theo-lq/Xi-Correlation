import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





def correlation_matrix(dataframe, correlation_function, **kwargs):
    """Compute the correlation coefficient for each variable in the dataframe according to the correlation function choosed.

    Usage::
        >>> from Xi_correlation import xi_correlation
        >>> size = 250
        >>> x = np.linspace(start=-5, stop=5, num=size)
        >>> y = x / 2 + np.sin(x) + 0.2 * np.random.normal(size)
        >>> z = (x ** 2) / 5 + 0.2 * np.random.normal(size)
        >>> X = pd.DataFrame({'x': x, 'y': y, 'z': z})
        >>> matrix = correlation_matrix(X, xi_correlation)

    :param dataframe: A pandas DataFrame.
    :param correlation_function: A function, returning tuple (coefficient, pvalue).
    :rtype: A pandas DataFrame.
    """
    
    
    n_columns = dataframe.shape[1]
    matrix = np.zeros((n_columns, n_columns))
    
    
    x_index = 0
    for x_column in dataframe.columns:
        
        y_index = 0
        for y_column in dataframe.columns:
            correlation, _ = correlation_function(dataframe[x_column], dataframe[y_column], **kwargs)
            matrix[x_index, y_index] = correlation
            
            y_index += 1
        
        x_index += 1
    
    matrix = pd.DataFrame(matrix, columns=dataframe.columns, index=dataframe.columns)
    return matrix







def show_correlation_matrix(dataframe, correlation_function, **kwargs):
    """Show the correlation matrix for a given dataframe according to the correlation function given.

    Usage::
        >>> from Xi_correlation import xi_correlation
        >>> size = 250
        >>> x = np.linspace(start=-5, stop=5, num=size)
        >>> y = x / 2 + np.sin(x) + 0.2 * np.random.normal(size)
        >>> z = (x ** 2) / 5 + 0.2 * np.random.normal(size)
        >>> X = pd.DataFrame({'x': x, 'y': y, 'z': z})
        >>> show_correlation_matrix(X, xi_correlation)

    :param dataframe: A pandas DataFrame.
    :param correlation_function: A function, returning tuple (coefficient, pvalue).
    :rtype: A matplotlib type plot
    """
    
    
    matrix = correlation_matrix(dataframe, correlation_function, **kwargs)
    sns.heatmap(matrix, annot=True, fmt='f', linewidths=0.5, cmap='Reds')
    plt.show()



show_correlation_matrix(X, xi_correlation)