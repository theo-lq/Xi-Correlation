import numpy as np
from scipy.stats import rankdata, norm




def xi_correlation(x, y, continuous=False):
    """Compute the correlation coefficient between x and y according to the xi coefficient defined by Chatterjee.

    Usage::
        >>> size = 250
        >>> x = np.linspace(start=-5, stop=5, num=size)
        >>> y = x / 2 + np.sin(x) + 0.2 * np.random.normal(size)
        >>> xi_correlation(

    :param x: A list.
    :param y: A list.
    :rtype: A tuple of real.
    """
    
    
    
    def rank_order(vector):
        random_index = np.random.choice(np.arange(length), length, replace=False)
        randomized_vector = vector[random_index]
        ranked_vector = rankdata(randomized_vector, method="ordinal")
        answer = [ranked_vector[j] for _, j in sorted(zip(random_index, range(length)))]
        return answer
    
    
    
    
    def compute_d_sequence(y):
        l = rankdata([-i for i in y], method="max")
        return np.sum(l * (length - l)) / (length ** 3)
    
    
    
    
    def compute_xi_coefficient(vector):
        mean_absolute = np.sum(np.abs([a - b for a, b in zip(vector[:- 1], vector[1:])]))
        return 1 - mean_absolute / (2 * (length**2) * d_sequence)
    
    
    
    
    def compute_p_value(continuous=continuous):
        
        if continuous:
            sigma = 2 / 5
        
        else:
            sorted_x_ordered = sorted(x_ordered_max_rank)
            
            index = [i for i in range(1, length+1)]
            doubled_index = [2 * length - 2 * i + 1 for i in index]
            cumulative_sum = np.cumsum(sorted_x_ordered)
            
            a = np.sum([i * (u**2) for i, u in zip(doubled_index, sorted_x_ordered)]) / (length ** 4)
            b = np.sum([v + (length - i) * u for i, u, v in zip(index, sorted_x_ordered, cumulative_sum)]) / (length ** 5)
            c = np.sum([i * u for i, u in zip(doubled_index, sorted_x_ordered)]) / (length ** 3)
            
            tau_squared = (a - 2 * b + np.square(c)) / (np.square(d_sequence))
            
            sigma = np.sqrt(tau_squared)
        
        
        
        p_value = 1 - norm.cdf(np.sqrt(length) * correlation / np.sqrt(sigma))
        
        return p_value
    
    
    
    
    
    
    
    x, y = np.array(x), np.array(y)
    length = len(x)
    
    x_ordered = np.argsort(rank_order(x))
    y_rank_max = rankdata(y, method="max")
    x_ordered_max_rank = y_rank_max[x_ordered]
    d_sequence = compute_d_sequence(y)
    
    correlation = compute_xi_coefficient(x_ordered_max_rank)
    p_value = compute_p_value(continuous=continuous)
    
    return correlation, p_value