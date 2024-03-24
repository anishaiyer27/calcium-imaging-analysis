"""
    Well class to enable modular framework for Ca2+ imaging analysis. One Well object represents the data contained in one file of data
    for one well imaged on one day (within a folder for all wells imaged that day)

    Upper: File / Load class if modularized (load.py)
    Middle: Well
    Lower: Cell
"""

class Well():
    def __init__(filename, n_perfs):
        self.filename = filename
        self.n_perfs = n_perfs
        self.perfusions = {}
        self.cells = []

    def add_perfusion(compound, cycle_num):
        if str.lower(compound) not in self.perfusions.keys():
            self.perfusions[compound] = cycle_num
        self.perfusions[compound].extend(cycle_num)

class Cell():
    def __init__(ID, loc, size, A, well):
        self.ID = ID
        self.location = loc
        self.size = size
        self.area = A
        self.well = well
        self.F = []
    
    def set_fluoros():
        pass
