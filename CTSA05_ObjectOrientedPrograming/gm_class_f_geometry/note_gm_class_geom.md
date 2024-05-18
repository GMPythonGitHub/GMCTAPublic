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
> 「ベクトル」の属性有し，関連する幾何学的計算機能を備えるクラスです。
> 以下で紹介するクラスでは，親クラスとして，
> また，インスタンス変数のクラス型として利用しています。
>> インスタンス変数： _\_xxyy: ndarray, _\_unit: float   
> 初期化関数__init__(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_vector( ), set_xxyy( )，set_rrth( )  
> Getting関数 unit( ), xxyy( ), rrth( ), copy( )  
> 文字列関数__str__( ), classprop( )  
> インスタンス関数  
> leng( ), dirc( ), unitvect( )   # vector properties  
> inner_vect( ), outer_vect( ). cross_vect( )  # vector analysis  
> インスタンス関数 
> conv( ), add( ), sub( ), rsub( ), mul( ), div( ), rdiv( ), 
> _\_pos\_\_( ), _\_neg\_\_( ), 
> _\_add\_\_( ), _\_radd\_\_( ), _\_sub\_\_( ), _\_rsub\_\_( ), 
> _\_mul\_\_( ), _\_rmul\_\_( ), _\_div\_\_( ), _\_rdiv\_\_( ),
> _\_iadd\_\_( ), _\_isub\_\_( ), _\_imul\_\_( ), _\_itruediv\_\_( )
 
> [GMPoint: gm_class_geom_b_point.py](gm_class_geom_b_point.py)
> 「点（位置ベクトル）」の属性を有し，関連する幾何学計算機能を備えているクラスです。
> GMVectorを親クラスとして継承ししている。
> 以下のクラスでは，親クラスとして，また，インスタンス変数のクラス型として利用しています。
>> 親クラス： GMVector
> インスタンス変数： ....  
> 初期化関数 _\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_point( )  
> Getting関数 copy( )  
> 文字列関数 _\_str\_\_( ), classprop( )  
> インスタンス関数  
> vect_p2pint( ), dist_p2pint( ), dirc_p2pint( ), unitvect_p2pint( )  # point properties  
> inner_op_vect( ), outer_op_vect( ), cross_op_vect( )  # vector analysis  

> [GMPoint: gm_class_geom_c_point_vector.py](gm_class_geom_c_point_vector.py)
> 「始点を指定するベクトル」の属性を有し，関連する幾何学計算機能を備えているクラスです。 
> GMVectorを親クラスとして継承し，また，GMVectorのインスタンスをインスタンス変数としている。
>> 親クラス： GMPoint
> インスタンス変数： self._vect: GMVector  
> 初期化関数 _\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_point_vector( )  
> Getting関数 copy( )  
> 文字列関数 _\_str\_\_(), classprop()  
> インスタンス関数  
> inner_op_v( ), outer_op_v( ), cross_op_v( )  # vector analysis  

> [GMSegment: gm_class_geom_d_segment.py](gm_class_geom_d_segment.py)
> 「二端点を有する線分」の属性を有し，関連する幾何学計算機能を備えているクラスです。
> GMPointをインスタンス変数のクラス型として利用しています。
>> インスタンス変数： self._pinta: GMPoint, self._pintb: GMPoint  
> 初期化関数 _\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_segment( )  
> Getting関数 copy( )  
> 文字列関数 _\_str\_\_( ), classprop( )  
> インスタンス関数  
> vect_a2b( ), vect_b2a( ), leng( ), dirc_a2b( ), dirc_b2a( ), unitvect_a2b( ), unitvect_b2a( )  # properties
> inner_oa_ob( ), outer_oa_ob( ), outer_ob_oa( ), cross_oa_ob( ), cross_ob_oa( )  # vector analysis 
> projx( ), projy( )  # projected area

> [GMPolygon: gm_class_geom_e_polygon.py](gm_class_geom_e_polygon.py)
> 「多角形」の属性を有し，関連する幾何学計算機能を備えているクラスです。
> GMPointとGMSegmentをlist要素のクラス型として利用しています。
>> インスタンス変数： self._pints: list: GMPoint, self._segms: list: GMSegment  
> 初期化関数 _\_init\_\_(points)  
> Setting関数 set_polygon( )  
> Getting関数 copy( )  
> 文字列関数 _\_str\_\_( ), classprop( )  
> インスタンス関数  
> grav_ctr( ), leng( ), area_prod( ), area_projx( ), area_projy( )  # properties


---

## [GMVector: gm_class_geom_a_vector.py](gm_class_geom_a_vector.py)

ここで紹介する最初のクラスGMVecotrは，ベクトルの成分がインスタンス変数として所属し，
ベクトルの属性や他のベクトルとの関係を計算する，ベクトル解析の機能を有しています。

### **[section_module]**  拡張モジュール  
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
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
関数norm( )は座標点間の距離を計算して返します。


### **[section_function]**  グロ－バル関数  
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
クラスが頻繁に利用する三角関数を改良し，
グローバルな関数としてクラスの定義領域の外側で記述しています。  
関数名が 'gm' で始まる４つの関数は，
numpyが提供する三角関数 cos( ), sin( ), tan( )と逆関数arctan( )を改良したものです。
引数にフラグとして deg を追加し，
角度を受け渡すときの単位系を radian と degree の間で切り替えます。
フラグ deg がTrueの場合はdegree，Falseの場合はradianとなります。


### **[section_class]**  クラスの定義と記述
クラスに所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数
```python
print("### --- section_class: (GMVector) describing class --- ###")
class GMVector():
    ## --- section_ca: (GMVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True ):
        self.__xxyy, self.__unit = None, None
        self.set_vector(xxyy, rrth, unit=unit, cnv=cnv, deg=deg)
```
***初期化関数__init__( ) ::*** この関数はクラスGMVector型のインスタンスを作成するときに自動的に起動します。
- インスタンス変数は private の属性を有する self.__xxyy: ndarray と self.__unit: float の２つです。
- self.__xxyy と self.__unit をひとまず None で初期化することによって，インスタンスに定義します。
- 引数は５個で，これをSetting関数 set_vector( )に渡すことによって，
self.__xxyy と self.__unit を更新します。

**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: (GMVector) setting and getting functions --- ##
    ## setting functions
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True ) -> None:
        if unit is not None: self.__unit = unit
        if rrth is not None:
            self.set_rrth(rrth, cnv=cnv, deg=deg)
        elif xxyy is not None:
            self.set_xxyy(xxyy, cnv=cnv)
    def set_xxyy(self, xxyy: tuple, cnv: bool = True) -> None:
        self.__xxyy = array(xxyy) * self.__unit if cnv else array(xxyy)
    def set_rrth(self, rrth: tuple, cnv: bool = True, deg: bool = True) -> None:
        rr, th = rrth
        if cnv: rr *= self.__unit
        self.__xxyy = rr * array(
            (gmcos(th,deg=deg), gmsin(th,deg=deg)) )
    ## getting functions
    def unit(self) -> float:
        return self.__unit
    def xxyy(self, cnv: bool = True) -> ndarray:
        if cnv: return self.__xxyy / self.__unit
        else: return self.__xxyy
    def rrth(self, cnv: bool = True, deg: bool = True) -> ndarray:
        rr = norm(self.__xxyy) / self.__unit if cnv else norm(self.__xxyy)
        th = gmatan2(self.__xxyy[1], self.__xxyy[0], deg=deg)
        return array((rr, th))
    def copy(self) -> object:
        return copy.deepcopy(self)
```
***Setting関数 set_vector( ) ::***  引数を受け取り，インスタンス変数self.__xxyyとself.__unitを更新します。  
- 引数 xxyy は直交座標系におけるベクトルの２成分(xx,yy)を受け取ります。
値はリスト構造型（tuple, list または ndarray）でなければなりません。
- 引数 rrth は円座標系におけるベクトルの２成分（長さrrと方位角th）を受け取ります。
同様に，値はリスト構造型でなくてはなりません。
- 引数 unit は長さの単位系を変換するときに使用する係数です。
例えば，クラスの内部では長さを'm'単位で種々の操作や計算を進めますが， 
長さに関連する数値を'cm'単位で受け取る場合には，unitの値を0.01と設定します。
この係数は直交座標系におけるxx, yyと円座標系の rr に影響します。
- 引数 cnv は長さの単位変換のフラグで，値がTrueのときはself.__unitを用いた単位の変換がを有効になりますが，
Falseのときは無効になります。
- クラス内では，角度の単位系をradianで操作や計算を進めますが，
角度を受け渡しするときには，単位系をdegreeにすることを可能にしています。
引数 deg は角度の単位系のフラグで，degがTrueの場合に単位はdegreeに，Falseの場合はradianになります。

引数がデフォルト値 None ではなく，具体的な数値の場合に対応する部分がインスタンス変数が更新されます。
具体的な処理内容は以下のようです。
1. 引数 unit が None でない場合には，インスタンス変数 self.__unit が更新されます。
2. 引数 rrth が None でない場合には，円座標系においてベクトルが指定されます。
引数 rrth と cnv, deg を関数 set_rrth( ) へ 渡して，インスタンス変数 self.__xxyy を更新します。
3. 引数 xxyy が None でない場合には，直交座標系においてベクトルが指定されます。
引数 xxyy と cnv を関数 set_xxyy( ) へ 渡して，インスタンス変数 self.__xxyy を更新します。

***Setting関数 set_xxyy( ) ::*** 引数 xxyy と cnv を受け取り，インスタンス変数 self.__xxyy を更新します。  
引数フラグ cnv は単位変換のフラグで，Trueのときは self.__unit を利用して単位を変換します。
 
***Setting関数 set_rrth( ) ::*** 引数 rrth と cnv, deg を受け取り，インスタンス変数 self.__xxyy を更新します。  
円座標系のベクトル成分 (rr,th) から，
直交座標系におけるベクトル成分を計算します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して rr の単位を変換します。
また，引数 deg は角度の単位変換フラグで，
True のときは th は degree として，False のときは radian として扱われます。 
 
***Getting関数 unit( ) ::*** インスタンス変数 self.__unit を参照します。  
self.__unit の値を参照して float型で返します。

***Getting関数 xxyy( ) ::*** インスタンス変数 self.__xxyy を参照します。  
self.__xxyy の値を参照して ndarray 型で返します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して xx と yy の単位を変換します。

***Getting関数 rrth( ) ::*** インスタンス変数 self.__xxyy を円座標系において参照します。  
self.__xxyy の値を参照して，xx と yy から円座標系のベクトルの長さ rr と方向角 th を計算し，
nadarray型で返します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して rr の単位を変換します。
引数 deg は角度の単位変換のフラグで，
Trueのときはth の値を degree に，Falseのときは radian に変換します。

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を 利用してインスタンスを全体を複製し，返します。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: (GMVector) string function for print() --- ##
    def __str__(self) -> str:
        xxyy = self.xxyy(cnv=True); rrth = self.rrth(cnv=True, deg=True)
        return (
            f'xxyy = {xxyy} : rrth = {rrth} : unit = {self.__unit:g}' )
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMVector ::\n  ' + self.__str__()
```
文字列関数__str__( ) と classprop( ) を記述しています。

***文字列関数 __str__( ) :: *** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
インスタンスの属性（クラス名とインスタンス変数などを）を記述する文字列をf-string型で作成して返します。

***文字列関数 classprop( ) ::*** 親クラスや所属するインスタンスを含めて，
インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型の親インスタンス，および所属するクラスのインスタンスの属性を含めて，
インスタンスの属性を記述する文字列をf-string型で作成して返します。
注) このクラスGMVectorは親クラスを継承せず，そして他のクラスのインスタンスを持たないので，
関数 classprop( ) は 文字列関数__str__( ) とほとんど同じ内容になっています。 


**[section_cd]**  ベクトルの属性
```python
    ## --- section_cd: (GMVector) functions for properties --- ##
    def leng(self, cnv: bool = False) -> float:
        rr, _ = self.rrth(cnv=cnv)
        return rr
    def dirc(self, deg: bool = False) -> float:
        _, th = self.rrth(deg=deg)
        return th
    def unitvect(self) -> tuple:
        dirc = self.dirc(deg=False)
        return cos(dirc), sin(dirc)
```
ベクトルの属性を計算するために，３つの関数を用意しています。  
***関数 leng( ) ::*** ベクトルの長さを計算して返します。
ベクトルの長さは円座標系における rr に相当するので，関数rrth()が返すndarray型の最初の要素を返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 dirc( ) ::*** ベクトルの方向角を返します。
ベクトルの方向角は円座標系における th に相当するので，関数rrth()が返すndarray型の２番目の要素を返します。
角度の単位系をフラグ deg で指定できます。

***関数 unitvector( ) ::*** ベクトルと同方向の単位ベクトルを返します。
ベクトルの２成分を 関数dirc()が返す方向角から余弦と正弦 (cos(),sin()) を計算し，
tuple 型で返します。


**[section_ce]**  ベクトル解析
```python
    ## --- section_ce: (GMVector) functions for analyzing vectors --- ##
    def inner_vect(self, vect: object, cnv: bool = False) -> ndarray:  # inner product
        return inner(self.xxyy(cnv), vect.xxyy(cnv))
    def outer_vect(self, vect: object, cnv: bool = False) -> ndarray:  # outer product
        return outer(self.xxyy(cnv), vect.xxyy(cnv))
    def cross_vect(self, vect: object, cnv: bool = False) -> ndarray:  # cross product
        return cross(self.xxyy(cnv), vect.xxyy(cnv))
```
与えられるベクトルとの間の積（内積，外積，クロス積）を計算する，
３つのインスタンス関数を用意しています。  
***関数 inner_vect( ) ::*** 与えられるベクトルとの内積を計算して返します。
与えられたベクトル vect: GMVector との間の内積（スカラー積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer_vect( ) ::*** 与えられるベクトルとの外積を計算して返します。
与えられたベクトル vect: GMVector との間の外積（テンソル積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross_vect( ) ::*** 与えられるベクトルとのクロス積を返します。
与えられたベクトル vect: GMVector との間のクロス積（外積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。


**[section_cf]**  ベクトルの四則演算
```python
    ## --- section_cf: (GMVector) functions for vector arithmetics --- ##
    def conv(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVector): return vect.xxyy(False)
        else: return None
    def add(self, vct: object) -> None: self.__xxyy += self.conv(vct)
    def sub(self, vct: object) -> None: self.__xxyy -= self.conv(vct)
    def rsub(self, vct: object) -> None: self.__xxyy = self.conv(vct) - self.__xxyy
    def mul(self, vct: object) -> None: self.__xxyy = self.__xxyy * self.conv(vct)
    def div(self, vct: object) -> None: self.__xxyy = self.__xxyy / self.conv(vct)
    def rdiv(self, vct: object) -> None: self.__xxyy = self.conv(vct) / self.__xxyy
```
与えられるベクトルや数値との四則演算を行うために，６個の関数を用意しています。  
****関数 conv( ) ::**** 与えられる引数を型変換して返します。
引数 vect の型に応じて，数値型または ndarray 型へ型変換して返します。
- int型, float型, complex型の引数は，変換せずにそのまま返します。
- tuple型, list型の引数は，ndarray型に変換して返します。
- ndarray型の引数は，変換せずにそのまま返します。
- GMVector型の引数は，インスタンス関数 xxyy( ) が返すndarray型のベクトル成分を返します。

****関数 add( ), sub( ), rsub( ), mul( ), div( ), rdiv( ) ::**** 
与えられるベクトルとの間で四則演算をして，インスタンスを更新します。  
最初に，引数vectを関数conv( )に渡して型変換します。その後四則演算を行い，
その結果でインスタンス変数__xxyyを更新します。
長さの単位系をフラグ cnv で指定することが可能です。


**[section_cg]**  演算子のオーバーライド
```python
    ## --- section_cg: overriding operators for GMVector --- ##
    # sign operators
    def __pos__(self): return GMVector(xxyy=+self.__xxyy, unit=self.__unit, cnv=False)
    def __neg__(self): return GMVector(xxyy=-self.__xxyy, unit=self.__unit, cnv=False)
    # arithmetic operators
    def __add__(self, vct): return GMVector(
        xxyy=self.__xxyy+self.conv(vct), unit=self.__unit, cnv=False )
    def __radd__(self, vct): return GMVector(
        xxyy=self.conv(vct)+self.__xxyy, unit=self.__unit, cnv=False )
    def __sub__(self, vct): return GMVector(
        xxyy=self.__xxyy-self.conv(vct), unit=self.__unit, cnv=False )
    def __rsub__(self, vct): return GMVector(
        xxyy=self.conv(vct)-self.__xxyy, unit=self.__unit, cnv=False )
    def __mul__(self, vct): return GMVector(
        xxyy=self.__xxyy*self.conv(vct), unit=self.__unit, cnv=False )
    def __rmul__(self, vct): return GMVector(
        xxyy=self.conv(vct)*self.__xxyy, unit=self.__unit, cnv=False )
    def __truediv__(self, vct): return GMVector(
        xxyy=self.__xxyy/self.conv(vct), unit=self.__unit, cnv=False )
    def __rtruediv__(self, vct): return GMVector(
        xxyy=self.conv(vct)/self.__xxyy, unit=self.__unit, cnv=False )
    # cumulative assignment operaters
    def __iadd__(self, vct): self.__xxyy += self.conv(vct); return self
    def __isub__(self, vct): self.__xxyy -= self.conv(vct); return self
    def __imul__(self, vct): self.__xxyy *= self.conv(vct); return self
    def __itruediv__(self, vct): self.__xxyy /= self.conv(vct); return self
```
演算子に多様性を持たせて，クラスGMvectorに対応するようにオーバーライドしています。
四則演算子について合計１４種類の機能をオーバーライドをしています。

****関数 __pos__( ), __neg__( ) ::**** 正負の符号  
- GMVector のインスタンスの直前の符号 '+, -' がある場合に起動します。
ただし，優先度は以下で説明する四則演算より低くなります。
- 符号の正負に応じてself.__xxyy の符号を変更したものを引数として，
新たにGMVectorのインスタンスを作成して返します。

****関数 __add__( ), __radd__( ), ... __rtuediv__( ) ::**** 四則演算  
- 関数__add__( )では'+'符号の直後のGMVector型や数値，変数が，
- 関数__radd__( )では'+'符号の直前のものが引数になり，受け取ります。
self.__xxyyとconv( ) で型変換した引数の和を計算をします。
計算結果を引数として渡し，新たにGMVectorのインスタンスを作成して返します。
- このグループの関数も同様に記述しています。

****関数 __iadd__( ), __isub__( ), __imul__( ), __itrudiv__( ) ::**** 累積代入演算子  
- 関数__iadd__() はGMVector型のを累積して加算します。
引数は演算子の直後のGMVector型や数値，変数です。
関数conv( )で型変換した引数を加算して，その結果でself.__xxyyを更新します。
- 減法，乗法，除法の計算と累積についても，他の関数により同様に記述しています。

クラスに関連して演算子をオーバーロードする方法の全体像と詳細な説明は，例えば
[WIKIBOOKS: Python/演算子オーバーロード](https://ja.wikibooks.org/wiki/Python/%E6%BC%94%E7%AE%97%E5%AD%90%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AD%E3%83%BC%E3%83%89)
に譲ります。


### **[section_main]**  メインセクション
クラスの記述に続く，if __name __ == '__main __': で始まるブロックは，
このファイルを直接起動したときのみ実行されます。
他のファイルがクラスGMVectorをインポートしただけでは，実行されません。
このブロックには，クラスの機能を紹介し，
パフォーマンスをチェックするすることを目的として，
基本的なプログラムを記述しています。


**[section_ma, section_ma, section_mc, section_md, section_me]**  クラスGMVectorの機能の紹介
```python
if __name__ == '__main__':
    print("### --- section_main: (GMVector) main process --- ###")
    print()
    ## --- section_ma: (GMVector) creating class instances --- ##
    vecta = GMVector(xxyy=(1.,0.), unit=1.); print(vecta.classprop('vecta -> '))
    vectb = GMVector(xxyy=(0.,1.), unit=1.); print(vectb.classprop('vectb -> '))
    print()
    ## --- section_mb: (GMVector) vector properties --- ##
    print(f'{vecta.leng() = }')
    print(f'{vecta.dirc() = }')
    print(f'{vecta.unitvect() = }')
    print()
    ## --- section_mc: (GMVector) vector products --- ##
    print(f'{vecta.inner_vect(vectb) = }')
    print(f'{vecta.outer_vect(vectb) = }')
    print(f'{vecta.cross_vect(vectb) = }')
    print()
    ## --- section_md: (GMVector) arithmetics operators --- ##
    vecta.add((1.,1.)); print(vecta.classprop('vecta.add(1.,1.) -> '))
    vectb.add((1.,1.)); print(vectb.classprop('vectb.add(1.,1.) -> '))
    print('  ------  : vect = vecta.copy()')
    vectc = vecta + vectb; print('vecta + vectb = ', vectc)
    vectc = vecta - vectb; print('vecta - vectb = ', vectc)
    vectc = vecta * vectb; print('vecta * vectb = ', vectc)
    vectc = vecta / vectb; print('vecta / vectb = ', vectc)
    print()
    ## --- section_me: (GMVector) cumulative assingment operators --- ##
    print('  ------  : vect = vecta.copy()')
    vectc = vecta.copy(); vectc += vectb; print(vectc.classprop('vecta += vectb -> '))
    vectc = vecta.copy(); vectc += - vectb; print(vectc.classprop('vecta += - vectb -> '))
    vectc = vecta.copy(); vectc -= vectb; print(vectc.classprop('vecta -= vectb -> '))
    vectc = vecta.copy(); vectc -= - vectb; print(vectc.classprop('vecta -= - vectb -> '))
    vectc = vecta.copy(); vectc *= vectb; print(vectc.classprop('vecta *= vectb -> '))
    vectc = vecta.copy(); vectc *= - vectb; print(vectc.classprop('vecta *= - vectb -> '))
    vectc = vecta.copy(); vectc /= vectb; print(vectc.classprop('vecta /= vectb -> '))
    vectc = vecta.copy(); vectc /= - vectb; print(vectc.classprop('vecta /= - vectb -> '))
```
section_ma:
1. GMVector型の２つのインスタンス，vecta とvectb を生成し以下で利用します。
2. 文字列関数を利用して，インスタンスの属性を表示します。

section_mb:  
3. 関数を用いて，インスタンスの属性を参照して，表示します。

section_mc:  
4. ベクトル解析により，インスタンス関数inner_vect( ), outer_vect( ), cross_vect( )を用いて，
３種類の積を計算して，結果を表示します。

section_md:  
5. オーバーライドした演算子によって四則演算します。
新たに作成されるGMVectorD型のインスタンスとして計算結果を返します。

section_me:   
6. オーバーライドした演算子によって，四則演算の結果を累積代入します。


