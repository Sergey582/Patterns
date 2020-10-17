import copy


class Ribosome:

    def __init__(self, consist):
        self.consist = consist


class Bacterium:

    def __init__(self, cytoskeleton: str, ribosomes: Ribosome, specialized_intracellular_structures: list):
        self.cytoskeleton = cytoskeleton
        self.ribosomes = ribosomes
        self.specialized_intracellular_structures = specialized_intracellular_structures

    def __copy__(self):
        new_specialized_intracellular_structures = copy.copy(self.specialized_intracellular_structures)
        new_ribosomes = copy.copy(self.ribosomes)
        new_obj = self.__class__(self.cytoskeleton, new_ribosomes, new_specialized_intracellular_structures)
        return new_obj

    def __deepcopy__(self, memodict={}):
        new_specialized_intracellular_structures = copy.deepcopy(self.specialized_intracellular_structures, memodict)
        new_ribosomes = copy.deepcopy(self.ribosomes, memodict)
        new_obj = self.__class__(self.cytoskeleton, new_ribosomes, new_specialized_intracellular_structures)
        new_obj.__dict__ = copy.deepcopy(self.__dict__, memodict)
        return new_obj
