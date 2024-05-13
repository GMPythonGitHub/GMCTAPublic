# gm_class_numbers_c.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMNumbersC: operating numbers ***')
print('   *** with encapsulation: setting and getting functions ***')

# =========================================================
print('### --- section_class: (GMNumbersC) describing class --- ###')
class GMNumbersC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self, aa, bb) -> None:
        self.__aa, self.__bb = None, None  # private instance variables
        self.set_aabb(aa, bb)
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_aabb(self, aa: float = None, bb: float = None) -> None:
        if aa is not None: self.__aa = aa
        if bb is not None: self.__bb = bb
    ## getting functions
    def aa(self) -> float: return self.__aa
    def bb(self) -> float: return self.__bb
    ## --- section_cc: functions for arithmetics --- ##
    def calc(self) -> tuple:
        return self.__aa + self.__bb, self.__aa - self.__bb

# =========================================================
print('### --- section_main: (GMMumbersC) main process --- ###')
## --- section_m0: calculating arithmetics --- ##
numbs = GMNumbersC(3, 2)  # creating instance
# print(f'{numbs.__aa = }, {numbs.__bb = }, ')
# AttributeError: 'GMNumbersC' object has no attribute '__aa'
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
# ---------------------------------------------------------
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMNumbersC: operating numbers ***
   *** with encapsulation: setting and getting functions ***
### --- section_class: (GMNumbersC) describing class --- ###
### --- section_main: (GMMumbersC) main process --- ###
numbs.aa() = 3, numbs.bb() = 2
add = 5, sub = 1
numbs.aa() = 7, numbs.bb() = 3
add = 10, sub = 4
'''
