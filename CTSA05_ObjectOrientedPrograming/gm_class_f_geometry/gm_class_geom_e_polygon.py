# gm_class_geom_e_polygon.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMPolygon) class for segment ***")
print("   *** class GMpoint and GMSegment are embedded as lists ***")
# ---------------------------------------------------------
print("### --- section__: (GMPolygon) importing items from module --- ###")
from numpy import (ndarray, array)
import copy
from gm_class_geom_d_segment import (GMSegment, GMPoint)

# =========================================================
print("### --- section_class: (GMPolygon) describing class --- ###")
class GMPolygon():
    ## --- section_ca: (GMPolygon) initializing class instance --- ##
    def __init__(self, points: tuple = ((0., 0.),(1., 0.),(1., 1.),(0., 1.),)):
        self._pints, self._segms = [], []
        self.set_polygon(points)
    ## --- section_cb: (GMPolygon) setting and getting functions --- ##
    ## setting functions
    def set_polygon(self, points: tuple = None):
        self._pints, self._segms = [], []
        for point in points:
            self._pints.append(GMPoint(xxyy=point))
        for ipint in range(len(self._pints)):
            self._segms.append(GMSegment(
                pinta=self._pints[ipint-1], pintb=self._pints[ipint]) )
    ## getting functions
    def copy(self):
        return copy.deepcopy(self)
    ## --- section_cc: (GMPolygon) string function for print() --- ##
    def __str__(self) -> str:
        return ''
    def classprop(self, idx: str = '') -> str:
        st = idx + ':: GMPolygon ::'
        st += f'\npints[{len(self._pints)}]: GMPoint:'
        for i, pint in enumerate(self._pints):
            st += '\n' + pint.classprop(f'**[{i:02d}]')
        st += f'\nsegms[{len(self._segms)}]: GMSegment:'
        for i, segm in enumerate(self._segms):
            st += '\n' + segm.classprop(f'**[{i:02d}]')
        return st
    ## --- section_cd: (GMPolygon) functions for properties --- ##
    def grav_ctr(self) -> ndarray:
        grav_ctr = array([0.,0.])
        for pint in self._pints:
            grav_ctr += pint.xxyy()
        return grav_ctr / len(self._pints)
    def leng(self) -> float:
        leng = 0.
        for segm in self._segms:
            leng += segm.leng()
        return leng
    def area_prod(self) -> float:  # area from cross product
        area = 0.
        for segm in self._segms:
            area += segm.cross_oa_ob()
        return abs(area) / 2.
    def area_projx(self) -> float:  # area from projection to x-axis
        area = 0.
        for segm in self._segms:
            area += segm.projx()
        return abs(area)
    def area_projy(self) -> float:  # area from projection in y-dir.
        area = 0.
        for segm in self._segms:
            area += segm.projy()
        return abs(area)

# =========================================================
if __name__ == '__main__':
    print("### --- section_m: main process --- ###")
    print()
    ## --- section_ma: (GMPolygon) creating class instance --- ##
    points = ((1., 3.),(4., 4.),(3., 1.),(0., 0.),)  # tuple of points
    print(f'{points = }')
    polg = GMPolygon(points)
    print(polg.classprop('polg -> '))
    print()
    ## --- section_mb: (GMPolygon) calculating polygon properties --- ##
    print(f'{polg.grav_ctr() = }')
    print(f'{polg.leng() = }')
    print(f'{polg.area_prod() = }')
    print(f'{polg.area_projx() = }')
    print(f'{polg.area_projy() = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPolygon) class for segment ***
       *** class GMpoint and GMSegment are embedded as lists ***
    ### --- section__: (GMPolygon) importing items from module --- ###
    *** (GMSegment) class for segment ***
       *** class GMPoint is embedded as pinta and pintb ***
    ### --- section_module: (GMSegment) importing items from module --- ###
    *** (GMPoint) class for point ***
       *** class GMVector is inherited ***
    ### --- section_module: (GMPoint) importing items from module --- ###
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_function: (GMVector) defining global functions --- ###
    ### --- section_class: (GMVector) describing class --- ###
    ### --- section_class: (GMPoint) describing class --- ###
    ### --- section_class: (GMSegment) describing class --- ###
    ### --- section_class: (GMPolygon) describing class --- ###
    ### --- section_m: main process --- ###
    
    points = ((1.0, 3.0), (4.0, 4.0), (3.0, 1.0), (0.0, 0.0))
    polg -> :: GMPolygon ::
    pints[4]: GMPoint:
    **[00]:: GMPoint ::
      (GMVector) xxyy = [1. 3.] : rrth = [ 3.16227766 71.56505118] : unit = 1
    **[01]:: GMPoint ::
      (GMVector) xxyy = [4. 4.] : rrth = [ 5.65685425 45.        ] : unit = 1
    **[02]:: GMPoint ::
      (GMVector) xxyy = [3. 1.] : rrth = [ 3.16227766 18.43494882] : unit = 1
    **[03]:: GMPoint ::
      (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
    segms[4]: GMSegment:
    **[00]:: GMSegment ::
      pinta: GMPoint: (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
      pintb: GMPoint: (GMVector) xxyy = [1. 3.] : rrth = [ 3.16227766 71.56505118] : unit = 1
    **[01]:: GMSegment ::
      pinta: GMPoint: (GMVector) xxyy = [1. 3.] : rrth = [ 3.16227766 71.56505118] : unit = 1
      pintb: GMPoint: (GMVector) xxyy = [4. 4.] : rrth = [ 5.65685425 45.        ] : unit = 1
    **[02]:: GMSegment ::
      pinta: GMPoint: (GMVector) xxyy = [4. 4.] : rrth = [ 5.65685425 45.        ] : unit = 1
      pintb: GMPoint: (GMVector) xxyy = [3. 1.] : rrth = [ 3.16227766 18.43494882] : unit = 1
    **[03]:: GMSegment ::
      pinta: GMPoint: (GMVector) xxyy = [3. 1.] : rrth = [ 3.16227766 18.43494882] : unit = 1
      pintb: GMPoint: (GMVector) xxyy = [0. 0.] : rrth = [0. 0.] : unit = 1
    
    polg.grav_ctr() = array([2., 2.])
    polg.leng() = 12.649110640673518
    polg.area_prod() = 8.0
    polg.area_projx() = 8.0
    polg.area_projy() = 8.0
    '''
