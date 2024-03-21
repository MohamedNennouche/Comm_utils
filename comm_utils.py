import numpy as np

def random_bin_generator(nBits:int) -> np.array : 
    """Generateur binaire pseudo aléatoire

    Args:
        nBits (int): Nombre de bits aléatoire (0 ou 1) qu'on veut avoir

    Returns:
        np.array: vecteur numpy de ces bits aléatoires
    """
    seed = np.random.randint(0, 10000)
    np.random.seed(seed)
    out = np.random.randint(0,2,nBits)

    return out

def ook(bits:np.array, high:str, ext:str) -> np.array : 
    """modulateur OOK

    Args:
        bits (np.array): Entrée binaire sous forme de vecteur NumPy
        high (str): Niveau haut de la modulation OOK
        ext (str): Taux d'extinction (ratio entre niveau haut et niveau bas)

    Returns:
        np.array: Vecteur avec les valeurs correspondantes des niveaux hauts et bas
    """
    output_bits = bits.astype(np.float32)
    output_bits[bits == 1] = high
    output_bits[bits == 0] = high*ext 
    return output_bits

def mod_4PPM(binary_array:np.array, high:float=1., ext:float=0.) -> np.array:
    """Modulateur 4PPM

    Args:
        binary_array (np.array): Flux binaire d'entrée sous forme de vecteur NumPy
        high (float, optional): Niveau haut voulu. Defaults to 1..
        ext (float, optional): Taux d'extinction entre le niveau haut et le niveau bas. Defaults to 0..

    Raises:
        ValueError: Dans le cas où l'entrée binaire n'est pas de taille paire

    Returns:
        np.array: Vecteur NumPy modulé
    """
    if len(binary_array) % 2 != 0:
        raise ValueError("Le nombre d'éléments dans le tableau binaire doit être pair.")
    
    modulated_array = np.zeros(len(binary_array) // 2 * 4)  # Initialiser le tableau modulé avec des zéros
    
    # Parcourir le tableau binaire et appliquer la modulation 4PPM
    for i in range(0, len(binary_array), 2):
        symbol = binary_array[i] * 2 + binary_array[i+1]  # Convertir les deux bits en un symbole (0, 1, 2 ou 3)
        low = high * ext
        if symbol == 0:
            modulated_array[i*2:i*2+4] = [high, low, low, low]
        elif symbol == 1:
            modulated_array[i*2:i*2+4] = [low, high, low, low]
        elif symbol == 2:
            modulated_array[i*2:i*2+4] = [low, low, high, low]
        elif symbol == 3:
            modulated_array[i*2:i*2+4] = [low, low, low, high]
    
    return modulated_array