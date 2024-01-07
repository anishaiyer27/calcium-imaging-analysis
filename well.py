"""
    Well class to enable modular framework for Ca2+ imaging analysis. One Well object represents the data contained in one file of data
    for one well imaged on one day (within a folder for all wells imaged that day)

    Parents: File / Load class if modularized (load.py)
    Children: Cell (cell.py)
"""

class Well():
    def __init__(filename, n_perfs):
        filename = filename
        n_perfs = n_perfs
        perfusions = {}
    
    def add_perfusion(compound, cycle):
        perfusions[compound] = cycle
    
    