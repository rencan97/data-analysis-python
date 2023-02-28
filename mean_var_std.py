import numpy as np

def get_dictionaryItems():
    items = {"mean", "variance", "standard deviation", "max", "min", "sum"}
    return dict.fromkeys(items, int(0))

def set_mean(numpyArray, dictionary):
    dictionary['mean'] = [np.ndarray.tolist(np.mean(numpyArray, axis = 0)) , np.ndarray.tolist(np.mean(numpyArray, axis=1)), np.mean(numpyArray)]

def set_variance(array, dictionary):
    dictionary['variance'] = [np.ndarray.tolist(np.var(array, axis = 0 )), np.ndarray.tolist(np.var(array, axis = 1)), np.var(array)]

def set_std(array, dictionary):
    dictionary['standard deviation'] = [np.ndarray.tolist(np.std(array, axis=0)), np.ndarray.tolist(np.std(array, axis=1)), np.std(array)]

def set_max(array, dictionary):
    dictionary['max'] = [np.ndarray.tolist(np.max(array, axis=0)), np.ndarray.tolist(np.max(array, axis= 1)), np.max(array)]

def set_min(array, dictionary):
    dictionary['min'] = [np.ndarray.tolist(np.min(array, axis=0)), np.ndarray.tolist(np.min(array, axis= 1)), np.min(array)]

def set_sum(array, dictionary):
    dictionary['sum'] = [np.ndarray.tolist(np.sum(array, axis=0)), np.ndarray.tolist(np.sum(array, axis = 1)), np.sum(array)]

def calculate(list):
    dictionary = get_dictionaryItems()
    try:
        numpyArray = np.array(list).reshape(3, 3)
    except: 
        raise ValueError("List must contain nine numbers.")
    set_mean(numpyArray, dictionary)
    set_variance(numpyArray, dictionary)
    set_std(numpyArray, dictionary)
    set_max(numpyArray, dictionary)
    set_min(numpyArray, dictionary)
    set_sum(numpyArray, dictionary)

    return dictionary

print(calculate([2,6,2,8,4,0,1,5,7]))