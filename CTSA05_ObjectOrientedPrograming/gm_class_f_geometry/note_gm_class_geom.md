# **Note on gm_class_f_geom:** ***幾何学図形の操作と計算のためのクラス***

## 概要
ここでは幾何学における基本的な図形要素である，ベクトル，座標点，始点を有するベクトル，線分，多角形を取り上げ，
それぞれに対して計５つのクラスを作成し，解説していきます。

オブジェクト指向プログラミング（ＯＯＰ）を支える，
クラスの効果的な利用法としては以下の２つを挙げることができます。
1. クラスの複製： クラス型のインスタンスを作成することです。
インスタンスを大量に作成してlistにまとめることによって，利用法を広げることが可能です。
2. クラスの再利用・継承： 関連するクラスを所定のクラスに取り込むことです。
基準となるクラス（親クラス，基底クラス）を他のクラス（子クラス，派生クラス）で活用（継承）することで，
その機能をす。引継ことが可能です。

これらについても，本稿で適宜説明していきます。

紹介するクラスの構成は以下のようです。

> [GMVector: gm_class_geom_a_vector.py](gm_class_geom_a_vector.py)
> 「ベクトル」の属性有し，関連する幾何学的計算機能を備える，最も基本的な親クラスです。  
>> インスタンス変数： \_\_xxyy: ndarray, \_\_unit: float   
> 初期化関数 \_\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_vector(), set_xxyy()，set_rrth()  
> Getting関数 unit(), xxyy(), rrth(), copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> leng(), dirc(), unitvect()   # vector properties  
> inner_vect(), outer_vect(). cross_vect()  # vector analysis  
> conv(), add(), sub(), rsub(), mul(), div(), rdiv()  # vector arithmetics  
> \_\_pos\_\_(), \_\_neg\_\_(), \_\_add\_\_(), \_\_radd\_\_(), ....  # vector operators  
> \_\_iadd\_\_(), \_\_isub\_\_(), ....  # cumulative assigment operators
 
> [GMPoint: gm_class_geom_b_point.py](gm_class_geom_b_point.py)
> 「点（位置ベクトル）」の属性を有し，関連する幾何学計算機能を備えているクラスです。  
> 親クラス： GMVector
>> インスタンス変数： ....  
> 初期化関数 \_\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_point()  
> Getting関数 copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> vect_p2pint(), dist_p2pint(), dirc_p2pint(), unitvect_p2pint()  # point properties  
> inner_op_vect(), outer_op_vect(), cross_op_vect()  # vector analysis  

> [GMPoint: gm_class_geom_c_point_vector.py](gm_class_geom_c_point_vector.py)
> 「始点を指定するベクトル」の属性を有し，関連する幾何学計算機能を備えているクラスです。  
> 親クラス： GMPoint
>> インスタンス変数： self._vect: GMVector  
> 初期化関数 \_\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_point_vector()  
> Getting関数 copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> inner_op_v(), outer_op_v(), cross_op_v()  # vector analysis  

> [GMSegment: gm_class_geom_d_segment.py](gm_class_geom_d_segment.py)
> 「二端点を有する線分」の属性を有し，関連する幾何学計算機能を備えているクラスです。  
>> インスタンス変数： self._pinta: GMPoint, self._pintb: GMPoint  
> 初期化関数 \_\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_segment()  
> Getting関数 copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> vect_a2b(), vect_b2a(), leng(), dirc_a2b(), dirc_b2a(), unitvect_a2b(), unitvect_b2a()  # properties
> inner_oa_ob(), outer_oa_ob(), outer_ob_oa(), cross_oa_ob(), cross_ob_oa()  # vector analysis 
> projx(), projy()  # projected area

> [GMPolygon: gm_class_geom_e_polygon.py](gm_class_geom_e_polygon.py)
> 「多角形」の属性を有し，関連する幾何学計算機能を備えているクラスです。  
>> インスタンス変数： self._pints: list: GMPoint, self._segms: GMSegment  
> 初期化関数 \_\_init\_\_(points)  
> Setting関数 set_polygon()  
> Getting関数 copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> grav_ctr(), leng(), area_prod(), area_projx(), area_projy()  # properties


---

## [GMVector: gm_class_geom_a_vector.py](gm_class_geom_a_vector.py)

ここで紹介する最初のクラスGMVecotrでは，ベクトルの成分がインスタンス変数として内蔵し，
ベクトルの属性や他のベクトルとの関係を含むベクトル解析の機能を有しています。

### **[section_module]**  
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
```python
print("*** (GMVector) class for vector ***")
# ---------------------------------------------------------
print("### --- section_module: (GMVector) importing items from module --- ###")
from numpy import (
    deg2rad as d2r, rad2deg as r2d, cos, sin, tan, arctan2,
    ndarray, array, inner, outer, cross )
from numpy.linalg import norm
import copy
```
関数atan2()は座標点の方向角を計算する関数で，y成分とx成分の両方を引数として渡すことで，全方位の角度を戻り値としてradianで返します。
また，関数r2d()は角度の単位系をradianからdegreeに，関数d2rはdegreeからradianに変換します。

### **[section_function]**  
クラスが頻繁に利用する三角関数を改良し，
グローバルな関数としてクラスの定義領域の外側で記述しています。  
```python
print("*** (GMVector) class for vector ***")
# ---------------------------------------------------------
print("### --- section_function: (GMVector) defining global functions --- ###")
def gmcos(th: float, deg: bool = False) -> float:
    return cos(d2r(th)) if deg else cos(th)
def gmsin(th: float, deg: bool = False) -> float:
    return sin(d2r(th)) if deg else sin(th)
def gmtan(th: float, deg: bool = False) -> float:
    return tan(d2r(th)) if deg else tan(th)
def gmatan2(yy: float, xx: float, deg=False) -> float:
    return r2d(arctan2(yy, xx)) if deg else arctan2(yy, xx)
```
関数名が 'gm' で始まる４つの関数は引数にフラグ deg を追加し，
角度を受取りまたは返すときの単位系を radian と degree の間で切り替えます。
すなわち，フラグdeg がTrueの場合は角度は度数，Falseの場合はラジアンとなります。

### **[section_class]**
クラスに所属するインスタンス変数とインスタンス関数を記述しています。  

**［section_ca］**  クラスGMVectorでインスタンスを作成するときに起動する，
初期化関数__init__()を記述しています。
```python
print("### --- section_class: (GMVector) describing class --- ###")
class GMVector():
    ## --- section_ca: (GMVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True ):
        self.__xxyy, self.__unit = array([0.,0.]), 1.
        self.set_vector(xxyy, rrth, unit=unit, cnv=cnv, deg=deg)
```
初期化関数の引数は５個です。
- ベクトル成分を直交座標系で設定する場合にはxxyyにベクトルのxとyの２成分を，
円座標系で設定する場合にはrrthにベクトルの長さの方向角を渡します。
このとき，それらの数値はリスト構造（tuple, list または ndarray）で渡します。
- 
ベクトルの長さと方向角の２成分の数値をリスト構造で与えます。
unitは単位系を変換する時に使用する係数です。
ちなみに，クラスの内部では'm'単位でで計算を進めますが，
クラスへの対応する数値を'cm'単位で受け渡しする場合には，unitを0.01と設定します。
cnvは単位変換のフラグで，これをFalseにすると，クラスからの数値の変換を無効にします。
また，deg は角度の単位系のフラグで，True
インスタンス変数self.__xxyyを(1,1)で初期化します。
さらに，単位系を変換する際に使用する係数をself.__unitを1.で初期化します。
その後，セッティング関数set_vector()を用いてインスタンス変数を引数xxとyyでで更新します。  

**［section_cb］**  インスタンス関数の定番である，Setting関数set_xxyy()とGetting関数xxyy()を記述しています。
```python
    ## --- section_cb: setting and getting functions --- ##
    ## setting function
    def set_xxyy(self,
            xx: float = None, yy: float = None) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
    ## getting functions
        def xxyy(self) -> tuple:
            return self.__xx, self.__yy
```
－ Setting関数set_xxyy()では，インスタンス変数self.__xxとself.__yyを引数 xxとyyで更新します。
ここでは，引数xxとyyのデフォルト値をNoneに設定することにより，具体的な数値を渡したインスタンス変数self.__xxとself._yyの両方，
あるいはどちらか一方だけを選択して更新できます。  
－ Getting関数xxyy()では，self.__xxとself.__yyをtuple型で返し，
インスタンス変数を参照できます。

**［section_cc］**  関数print()でインスタンス名を指定すると起動する，文字列関数__str__()を記述しています。
```python
    ## --- section_cd: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMVectorA): xx = {self.__xx:g}, yy = {self.__yy:g}'
```
インスタンスの属性（クラス名とインスタンス変数）を記述する文字列をf-string型で作成して返します。

**［section_cd］**  ベクトルの特性を計算する３つのインスタンス関数を記述しています。
```python
    ## --- section_ce: functions for properties --- ##
    def leng(self) -> float:
        return sr(sq(self.__xx)+sq(self.__yy))
    def dirc(self, deg: bool = True) -> float:
        th = atan2(self.__yy, self.__xx)
        if deg: th = r2d(th)
        return th
    def unitvect(self) -> tuple:
        leng = self.leng()
        return self.__xx / leng, self.__yy / leng
```
－ 関数leng()では，ベクトルの大きさ（長さ）を計算して返します。
－ 関数dirc()では，ベクトルの方位角を計算して出力します。
拡張ライブラリnumpyからインポートした関数atan2()が返す方位角の単位系はradianですが，
デフォルトのbool値がFalseである単位系フラグdegをTrueに変更すると，単位系をdegreeに指定します。
－ 関数unitvector()では，ベクトルの成分をベクトルの大きさで除すことにより単位ベクトルを計算し，tuple型で返します。

### **[section_main]**
クラスのパフォーマンスをチェックする目的で，基本的なプログラムを記述しています。
クラスの記述に続くこの部分は，このファイルを起動したときのみ実行されます。

**［section_ma］**  
```python
print('### --- section_main: (GMVectorA) main process --- ###')
## --- section_ma: calculating vectors --- ##
vect = GMVectorA(xx=4., yy=3.)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
vect.set_xxyy(xx=5., yy=5.)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')
```
最初に，クラスGMVectorAのインスタンスvectを生成し，インスタンス変数の初期値を(4,3)に指定します。
その後，Setting関数set_xxyy()を用いてインスタンス変数を(5,5)に更新します。
それぞれに対して，文字列関数が返すクラス属性と，インスタンス関数unitvect()が単位ベクトルを関数print()で表示します。  

