# gm_matrix_equation_class.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMMatrixEq: solving matrix equation ***')
print('    *** with known/unknown condition ***')
# ---------------------------------------------------------
print('### --- section_module: (GMMatrixEq) importing items from module --- ###')
from numpy import (
    ndarray, array, dot, full, ix_, linalg, logical_not as loginot)
import copy

# =========================================================
print('### --- section_class: (GMMatrixEq) describing class --- ###')
class GMMatrixEq():
    ## --- section_ca: (GMMatrixEq) initializing class instance --- ##
    def __init__(self,
            aa: tuple = ((1, 1, 1, 1), (1, 2, 1, 1), (1, 1, 3, 1), (1, 1, 1, 4)),
            xx: tuple = None, bb: tuple = None,
            cndxx: tuple = None, cndbb: tuple = None ) -> None:
        ''' matrix equation; [A] * (X) = (B) '''
        self._aa = None  # matrix [A]: ndarray
        self._xx = None  # left vector (X): ndarray
        self._bb = None  # right vector (B): ndarray
        self._cndxx = None  # known/unknown condition for vector (X): tuple
        self._cndbb = None  # known/unknown condition for vector (B): tuple
        self.set_matrix_eq(aa=aa, xx=xx, bb=bb, cndxx=cndxx, cndbb=cndbb)
    ## --- section_cb: (GMMatrixEq) setting and getting functions --- ##
    ## setting functions
    def set_matrix_eq(self,
            aa: tuple = None, xx: tuple = None, bb: tuple = None,
            cndxx: tuple = None, cndbb: tuple = None) -> None:
        if aa is not None:
            self._aa = array(aa, dtype='float64')
            self._bb = full(len(self._aa), None, dtype='float64')  # preparing default problem
            self._bb = array([sum(aai) for aai in aa], dtype='float64')
            self._cndxx = tuple([False] * len(self._aa))
            self._cndbb = tuple([True] * len(self._aa))
        if xx is not None: self._xx = array(xx, dtype='float64')
        if bb is not None: self._bb = array(bb, dtype='float64')
        if cndxx is not None: self._cndxx = tuple(cndxx)
        if cndbb is not None: self._cndbb = tuple(cndbb)
    ## getting functions
    def aa(self) -> ndarray: return self._aa
    def xx(self) -> ndarray: return self._xx
    def bb(self) -> ndarray: return self._bb
    def cndxx(self) -> tuple: return self._cndxx
    def cndbb(self) -> tuple: return self._cndbb
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: (GMMatrixEq) string function for print() --- ##
    def __str__(self) -> str:
        return (
            f'    aa = \n{self._aa}  \n    xx = {self._xx}  \n    bb = {self._bb}\n'
            f'    cndxx = {self._cndxx}\n    cndbb = {self._cndbb}' )
    ## --- section_cd: (GMMatrixEq) solving matrix equation --- ##
    def solve(self) -> None:
        if all(self._cndxx):  ## Type-A; xx is known; finding bb; calculate inner product
            self._bb = dot(self._aa, self._xx)
        elif all(self._cndbb):  ## Type-B; bb is known; finding aa; solving whole matrix equation xx
            self._xx = linalg.solve(self._aa, self._bb)
        else:  ## Type-C; forming and solving partial matrix equation
            aa_wk = self._aa[ix_(self._cndbb, loginot(self._cndxx))]  # forming partial matrix aa
            bb_wk = self._bb[ix_(self._cndbb)]  # forming partial vector bb
            bb_wk -= dot(
                self._aa[ix_(self._cndbb, self._cndxx)],
                self._xx[ix_(self._cndxx)] )
            xx_wk = linalg.solve(aa_wk, bb_wk)  # solving partial matrix equation
            self._xx[loginot(self._cndxx)] = xx_wk
            self._bb[loginot(self._cndbb)] = dot(
                self._aa[ix_(loginot(self._cndbb))], self._xx)

# =========================================================
if __name__ == '__main__':
    print('### --- section_main: (GMMatrixEq) main process --- ###')
    ## --- section_ma: (GMMatrixEq) setting matrix equation --- ##
    aa, xx, bb = None, None, None
    cndxx, cndbb = None, None
    rank = ('4x4', '6x6')[1]
    type = ('type-1', 'type-2')[1]
    knwc = ('xx', 'bb', 'fix')[2]
    if rank == '4x4':
        if type == 'type-1':
            aa = ( (1, 1, 1, 1), (1, 2, 1, 1),
                   (1, 1, 3, 1), (1, 1, 1, 4))
            if knwc == 'xx':
                xx, bb = (1, 2, 3, 4), (0, 0, 0, 0)
                cndxx, cndbb = (True, True, True, True), (False, False, False, False)
            elif knwc == 'bb':
                xx, bb = (0, 0, 0, 0), (10, 12, 16, 22)
                cndxx, cndbb = (False, False, False, False), (True, True, True, True)
            elif knwc == 'fix':
                xx, bb = (1, 0, 0, 4), (0, 12, 16, 0)
                cndbb = (True, False, False, True), (False, True, True, False)
        elif type == 'type-2':
            aa = ( (1, 1, 1, 1), (1, 1, 2, 1), (1, 3, 1, 1), (4, 1, 1, 1))
            if knwc == 'xx':
                xx, bb = (1, 2, 3, 4), (0, 0, 0, 0)
                cndxx, cndbb = (True, True, True, True), (False, False, False, False)
            elif knwc == 'bb':
                xx, bb = (0, 0, 0, 0), (10, 12, 16, 22)
                cndxx, cndbb = (False, False, False, False), (True, True, True, True)
            elif knwc == 'fix':
                xx, bb = (0, 2, 0, 4), (0, 13, 0, 13)
                cndxx, cndbb = (False, True, False, True), (False, True, False, True)
    elif rank == '6x6':
        if type == 'type-1':
            aa = ( (1, 1, 1, 1, 1, 1), (1, 2, 1, 1, 1, 1), (1, 1, 3, 1, 1, 1),
                   (1, 1, 1, 4, 1, 1), (1, 1, 1, 1, 5, 1), (1, 1, 1, 1, 1, 6) )
            if knwc == 'xx':
                xx, bb = (1, 2, 3, 4, 5, 6), (0, 0, 0, 0, 0, 0)
                cndxx, cndbb = (True, True, True, True, True, True), (False, False, False, False, False, False)
            elif knwc == 'bb':
                xx, bb = (0, 0, 0, 0, 0, 0), (21, 23, 27, 33, 41, 51)
                cndxx, cndbb = (False, False, False, False, False, False), (True, True, True, True, True, True)
            elif knwc == 'fix':
                xx, bb = (1, 0, 0, 4, 5, 6), (0, 23, 27, 0, 0, 51)
                cndxx, cndbb = (True, False, False, True, True, False), (False, True, True, False, False, True)
        elif type == 'type-2':
            aa = ( (1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 2, 1), (1, 1, 1, 3, 1, 1),
                   (1, 1, 4, 1, 1, 1), (1, 5, 1, 1, 1, 1), (6, 1, 1, 1, 1, 1) )
            if knwc == 'xx':
                xx, bb = (1, 2, 3, 4, 5, 6), (0, 0, 0, 0, 0, 0)
                cndxx, cndbb = (True, True, True, True, True, True), (False, False, False, False, False, False)
            elif knwc == 'bb':
                xx, bb = (0, 0, 0, 0, 0, 0), (21, 26, 29, 30, 29, 26)
                cndxx, cndbb = (False, False, False, False, False, False), (True, True, True, True, True, True)
            elif knwc == 'fix':
                xx, bb = (0, 2, 3, 0, 0, 6), (0, 26, 29, 0, 0, 26)
                cndxx, cndbb = (False, True, True, False, False, True), (False, True, True, False, False, True)

    ## --- section_mb: (GMMatrixEq) creating class instance and solving matrix equation --- ##
    matrixeq = GMMatrixEq(aa=aa, xx=xx, bb=bb, cndxx=cndxx, cndbb=cndbb)
    print(matrixeq.classprop('matrixeq -> '))
    matrixeq.solve()
    print(matrixeq.classprop('matrixeq -> '))

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** class GMMatrixEq: solving matrix equation ***
    ### --- section_module: (GMMatrixEq) importing items from, module --- ###
    ### --- section_class: (GMMatrixEq) declaring class --- ###
    ### --- section_main: (GMMatrixEq) main process --- ###
    (GMMatrixEq): 
        aa = [ [1. 1. 1. 1. 1. 1.] [1. 2. 1. 1. 1. 1.]
               [1. 1. 3. 1. 1. 1.] [1. 1. 1. 4. 1. 1.]
               [1. 1. 1. 1. 5. 1.] [1. 1. 1. 1. 1. 6.] ]
        xx = [1. 2. 3. 4. 5. 6.]
        bb = [21. 23. 27. 33. 41. 51.]
        cndxx = (True, False, False, True, True, False)
        cndbb = (False, True, True, False, False, True)
    '''
