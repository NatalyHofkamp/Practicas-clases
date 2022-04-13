#%%
def net_gain (volume,initial_price,final_price):
    """

    Parameters
    ----------
    volume : TYPE (int)
        la cantidad de items que compramos en un principio.
    initial_price : TYPE(int)
        El precio por el cual compramos cada Item en un principio.
    final_price : TYPE(int)
        El valor actual de cada Item.

    Returns
    -------
    TYPE(int)
        La función devolverá el valor de la ganancia neta
        una vez vendidos todos los items.
    """
    i= volume * initial_price
    f= volume * final_price    
    return (f-i)

print(net_gain(12095.2, 0.86, 1.28))

#%%


def item_to_sell (volume, initial_price, final_price, book_price):
    """
    

    Parameters
    ----------
    volume : TYPE (int)
        la cantidad de items que compramos en un principio.
    initial_price : TYPE(int)
        El precio por el cual compramos cada Item en un principio.
    final_price : TYPE(int)
        El valor actual de cada Item.
    book_price : TYPE(int)
        El valor en GRO del libro que queremos comprar.

    Returns
    -------
    dev_total : TYPE(int)
       La función devolverá la cantidad de items que debemos vender
       para poder comprar el libro y devolver el dinero prestado.

    """
    prest_gro= volume*initial_price
    dev_item= prest_gro / final_price
    book_item= book_price / final_price
    dev_total=dev_item + book_item 

    return  dev_total 
print((item_to_sell(12095.2, 0.86, 1.28,2831.97)))