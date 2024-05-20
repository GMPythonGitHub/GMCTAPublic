# gm_class_geom_d_segment.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMSegment) class for segment ***")
print("   *** class GMPoint is embedded as pinta and pintb ***")
# ---------------------------------------------------------
print("### --- section_module: (GMSegment) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_b_point import (GMPoint, GMVector)

# =========================================================
print("### --- section_class: (GMSegment) describing class --- ###")
class GMSegment():
    ## --- section_ca: (GMSegment) initializing class instance --- ##
    def __init__(self,
            pinta: GMPoint = GMPoint(xxyy=(0,0)),
            pintb: GMPoint = GMPoint(xxyy=(1,1)) ):
        self._pinta = None  # end point A: GMPoint
        self._pintb = None  # end point B: GMPoint
        self.set_segment(pinta=pinta, pintb=pintb)
    ## --- section_cb: (GMSegment) setting and getting functions --- ##
    ## setting functions
    def set_segment(self,
            pinta: GMPoint = None, pintb: GMPoint = None) -> None:
        if pinta is not None: self._pinta = pinta
        if pintb is not None: self._pintb = pintb
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: (GMSegment) string function for print() --- ##")
    def __str__(self) -> str:
        return (
              '  pinta: GMPoint: ' + self._pinta.__str__() + '\n'
            + '  pintb: GMPoint: ' + self._pintb.__str__() + '' )

    def classprop(self, idx: str = '') -> str:
        return (
            idx + ':: GMSegment ::\n' + self.__str__() )
    ## --- section_cd: (GMSegment) calculating properties --- ##
    def vect_a2b(self) -> GMVector:  # vector from pinta to pintb
        return self._pinta.vect_p2pint(self._pintb)
    def vect_b2a(self) -> GMVector:  # vector from pintb to pinta
        return self._pintb.vect_p2pint(self._pinta)
    def leng(self, cnv: bool = True) -> float:  # length (m)
        return self._pinta.dist_p2pint(self._pintb, cnv=cnv)
    def dirc_a2b(self, deg: bool = True) -> float:  # direction from pinta to pintb
        return self._pinta.dirc_p2pint(self._pintb, deg=False)
    def dirc_b2a(self, deg: bool = True) -> float:  # direction from pintb to pinta
        return self._pintb.dirc_p2pint(self._pinta, deg=False)
    def unitvect_a2b(self) -> tuple:  # unit vector from pinta to pintb
        return self._pinta.unitvect_p2pint(self._pintb)
    def unitvect_b2a(self) -> tuple:  # unit vector from pintb to pinta
        return self._pintb.unitvect_p2pint(self._pinta)
    ## --- section_ce: (GMSegment) analysing vectors --- ##
    def inner_oa_ob(self, cnv: bool = True) -> float:  # inner product between vectoa and vectob
        return self._pinta.inner_op_vect(self._pintb, cnv=cnv)
    def inner_ob_oa(self, cnv: bool = True) -> float:  # inner product between vectoa and vectob
        return self._pintb.inner_op_vect(self._pinta, cnv=cnv)
    def outer_oa_ob(self, cnv: bool = True) -> ndarray:  # outer product form vectoa to vectob
        return self._pinta.outer_op_vect(self._pintb, cnv=cnv)
    def outer_ob_oa(self, cnv: bool = True) -> ndarray:  # outer product form vectob to vectoa
        return self._pintb.outer_op_vect(self._pinta, cnv=cnv)
    def cross_oa_ob(self, cnv: bool = True) -> float:  # cross product form vectoa to vectob
        return self._pinta.cross_op_vect(self._pintb, cnv=cnv)
    def cross_ob_oa(self, cnv: bool = True) -> float:  # cross product form vectob to vectoa
        return self._pintb.cross_op_vect(self._pinta, cnv=cnv)
    def projx(self, cnv: bool = True) -> float:  # projection area to x-axis
        axx, ayy = self._pinta.xxyy(cnv=cnv)
        bxx, byy = self._pintb.xxyy(cnv=cnv)
        return (bxx - axx) * (ayy + byy) / 2
    def projy(self, cnv: bool = True) -> float:  # projection area to y-axis
        axx, ayy = self._pinta.xxyy(cnv=cnv)
        bxx, byy = self._pintb.xxyy(cnv=cnv)
        return (byy - ayy) * (axx + bxx) / 2

# =============================================================================
# =============================================================================
if __name__ == '__main__':
    print("### --- section_main: (GMSegment) main process --- ###")
    print()
    ## --- section_ma: (GMSegment) creating class instances --- ##
    pinta = GMPoint(xxyy=(1., 2.), unit=1.); print(pinta.classprop('pinta -> '))
    pintb = GMPoint(xxyy=(2., 1.), unit=1.); print(pintb.classprop('pintb -> '))
    segm = GMSegment(pinta=pinta, pintb=pintb); print(segm.classprop('segm -> '))
    print()
    ## --- section_mb: (GMSegment) calculating vector properties --- ##
    print(segm.vect_a2b().classprop('segm.vect_a2b() -> '))
    print(segm.vect_b2a().classprop('segm.vect_b2a() -> '))
    print(f'{segm.leng() = }')
    print(f'{segm.dirc_a2b() = }, {segm.dirc_b2a() = }')
    print(f'{segm.unitvect_a2b() = }'); print(f'{segm.unitvect_b2a() = }')
    print()
    ## --- section_mc: (GMSegment) calculating vector products --- ##
    print(f'{segm.inner_oa_ob() = }')
    print(f'{segm.outer_oa_ob() = }')
    print(f'{segm.outer_ob_oa() = }')
    print(f'{segm.cross_oa_ob() = }, {segm.cross_ob_oa() = }')
    print(f'{segm.projx() = }, {segm.projy() = }')

    # =============================================================================
    # terminal log / terminal log / terminal log /
    '''
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
    ### --- section_main: (GMSegment) main process --- ###
    
    pinta -> :: GMPoint ::
      (GMVector) xxyy = [1. 2.] : rrth = [ 2.23606798 63.43494882] : unit = 1
    pintb -> :: GMPoint ::
      (GMVector) xxyy = [2. 1.] : rrth = [ 2.23606798 26.56505118] : unit = 1
    segm -> :: GMSegment ::
      pinta: GMPoint: (GMVector) xxyy = [1. 2.] : rrth = [ 2.23606798 63.43494882] : unit = 1
      pintb: GMPoint: (GMVector) xxyy = [2. 1.] : rrth = [ 2.23606798 26.56505118] : unit = 1
    
    segm.vect_a2b() -> :: GMVector ::
      xxyy = [ 1. -1.] : rrth = [  1.41421356 -45.        ] : unit = 1
    segm.vect_b2a() -> :: GMVector ::
      xxyy = [-1.  1.] : rrth = [  1.41421356 135.        ] : unit = 1
    segm.leng() = 1.4142135623730951
    segm.dirc_a2b() = -0.7853981633974483, segm.dirc_b2a() = 2.356194490192345
    segm.unitvect_a2b() = array([ 0.70710678, -0.70710678])
    segm.unitvect_b2a() = array([-0.70710678,  0.70710678])
    
    segm.inner_oa_ob() = 4.0
    segm.outer_oa_ob() = array([[2., 1.], [4., 2.]])
    segm.outer_ob_oa() = array([[2., 4.], [1., 2.]])
    segm.cross_oa_ob() = array(-3.), segm.cross_ob_oa() = array(3.)
    segm.projx() = 1.5, segm.projy() = -1.5
    '''
