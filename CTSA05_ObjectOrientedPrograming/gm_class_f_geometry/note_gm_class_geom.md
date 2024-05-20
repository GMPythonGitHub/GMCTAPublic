# **Note on gm_class_geom:** ***幾何学図形の操作と計算のためのクラス***

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
（このことは文法的には不要ですが，クラスの構成を整理するために初期化しています。）
- 引数は５個すべてを Setting関数 set_vector( ) に渡すことによって，
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

引数がデフォルト値 None ではなく，具体的な数値の場合に対応するインスタンス変数が更新されます。
具体的な処理内容は以下のようです。
1. 引数 unit が None でない場合には，インスタンス変数 self.__unit が更新されます。
2. 引数 rrth が None でない場合には，円座標系においてベクトルが指定されます。
引数 rrth と cnv, deg を関数 set_rrth( ) へ 渡して，インスタンス変数 self.__xxyy を更新します。
3. 引数 xxyy が None でない場合には，直交座標系においてベクトルが指定されます。
引数 xxyy と cnv を関数 set_xxyy( ) へ 渡して，インスタンス変数 self.__xxyy を更新します。

***Setting関数 set_xxyy( ) ::*** 引数 xxyy と cnv を受け取り，インスタンス変数 self.__xxyy を更新します。  
引数フラグ cnv は単位変換のフラグで，Trueのときは self.__unit を利用して単位を変換します。
 
***Setting関数 set_rrth( ) ::*** 引数 rrth と cnv, deg を受け取り，インスタンス変数 self.__xxyy を更新します。  
円座標系のベクトル成分 (rr,th) から直交座標系におけるベクトル成分を計算します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して rr の単位を変換します。
また，引数 deg は角度の単位変換フラグで，
True のときは th は degree として，False のときは radian として扱われます。 
 
***Getting関数 unit( ) ::*** インスタンス変数 self.__unit を参照します。  
self.__unit の値を float型で返します。

***Getting関数 xxyy( ) ::*** インスタンス変数 self.__xxyy を参照します。  
self.__xxyy の値を ndarray型で返します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して xx と yy の単位を変換します。

***Getting関数 rrth( ) ::*** インスタンス変数 self.__xxyy を円座標系において参照します。  
self.__xxyy の値を参照して，xx と yy から円座標系のベクトルの長さ rr と方向角 th を計算し，
nadarray型で返します。
引数 cnv は長さの単位変換のフラグで，Trueのときは self.__unit を利用して rr の単位を変換します。
引数 deg は角度の単位変換のフラグで，
Trueのときはth の値を degree に，Falseのときは radian に変換します。

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を利用して，
このGMVector型のインスタンス全体を複製して返します。


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

***文字列関数 __str__( ) ::*** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
インスタンスの属性（インスタンス変数など）を記述する文字列を，f-string型で作成して返します。

***文字列関数 classprop( ) ::*** 親クラスや所属するインスタンスを含めて，
インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型の名前に，文字列関数__str__( ) が返す文字列を加えて返します。 


**[section_cd]**  属性の計算
```python
    ## --- section_cd: (GMVector) calculating properties --- ##
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
    ## --- section_ce: (GMVector) analyzing vectors --- ##
    def inner_vect(self, vect: object, cnv: bool = True) -> float:  # inner product
        return inner(self.xxyy(cnv), vect.xxyy(cnv))
    def outer_vect(self, vect: object, cnv: bool = True) -> ndarray:  # outer product
        return outer(self.xxyy(cnv), vect.xxyy(cnv))
    def cross_vect(self, vect: object, cnv: bool = True) -> float:  # cross product
        return cross(self.xxyy(cnv), vect.xxyy(cnv))
```
与えられるベクトルとの間の積（内積，外積，クロス積）を計算します，
３つのインスタンス関数を用意しています。  

***関数 inner_vect( ) ::*** 与えられるベクトルとの内積を計算して返します。
与えられたベクトル vect: GMVector との間の内積（スカラー積）を次式で計算してfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer_vect( ) ::*** 与えられるベクトルとの外積を計算してndarray型で返します。
与えられたベクトル vect: GMVector との間の外積（テンソル積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross_vect( ) ::*** 与えられるベクトルとのクロス積をfloat型で返します。
与えられたベクトル vect: GMVector との間のクロス積（外積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。


**[section_cf]**  四則演算
```python
    ## --- section_cf: (GMVector) arithmetics --- ##
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
    ## --- section_cg: overriding operators --- ##
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



---

## [GMVector: gm_class_geom_b_point.py](gm_class_geom_b_point.py)

ここで紹介するクラスGMPointは，座標点定義して操作します。
GMVectorを親クラスとして継承する属性が，始点の位置ベクトルの属性になります。
座標点や他の座標点の関係を計算する機能をクラスに追加しています。

### **[section_module]**  拡張モジュール  
```python
print("*** (GMPoint) class for point ***")
print("   *** class GMVector is inherited ***")
# ---------------------------------------------------------
print("### --- section_module: (GMPoint) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_a_vector import GMVector
```
クラスが利用する関数を，拡張モジュール numpy と copy からimportしています。  
クラスGMVectorを記述しているファイル gm_class_geom_a_vector.py から GMVectorをインポートしています。


### **[section_class]**  クラスの定義と記述
クラスに所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数
```python
print("### --- section_class: (GMPoint) describing class --- ###")
class GMPoint(GMVector):  # inheriting class GMVector
    ## --- section_ca: (GMPoint) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True ):
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)  # calling parent class
```
***初期化関数__init__( ) ::*** この関数はクラスGMPoint型のインスタンスを作成するときに自動的に起動します。
- クラスの宣言文 class GMPoint(GMVector) で親クラス GMVector を継承しています。
- 座標点の位置ベクトルは継承しているGMVector型になります。
- クラス独自のインスタンス変数はありません。

1. 引数すべてを 親クラスの初期化関数 __init__() に渡します。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: (GMPoint) setting and getting functions --- ##
    ## setting functions
    def set_point(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True) -> None:
        self.set_vector(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
```
***Setting関数 set_point( ) ::***  引数を受け取り，インスタンス変数を更新します。
1. 引数をすべて，親クラスのSetting関数 set_vector() に送ります。  

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を利用して，
このGMPoint型のインスタンスを全体を複製して返します。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: (GMPoint) string function for print() --- ##
    def __str__(self) -> str:
        return '(GMVector) ' + super().__str__()
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMPoint ::\n  ' + self.__str__()
```
文字列関数__str__( ) と classprop( ) を記述しています。

***文字列関数 __str__( ) ::*** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
親クラスの名前を明記するとともに，インスタンスの属性（インスタンス変数など）を記述する文字列をf-string型で作成して返します。

***文字列関数 classprop( ) ::*** 親クラスや所属するインスタンスを含めて，
インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型名を明記するとともに，関数 __str__() が返す文字列とともに返します。 


**[section_cd]**  属性の計算
```python
    ## --- section_cd: (GMPoint) calculating properties --- ##
    def vect_p2pint(self, pint: object) -> GMVector:
        return pint - self
    def dist_p2pint(self, pint: object, cnv: bool = False) -> float:
        vct = self.vect_p2pint(pint)
        return vct.leng(cnv)
    def dirc_p2pint(self, pint: object, deg: bool = False) -> float:
        vct = self.vect_p2pint(pint)
        return vct.dirc(deg)
    def unitvect_p2pint(self, pint: object) -> tuple:
        vct = self.vect_p2pint(pint)
        return vct.unitvect()
```
座標点の属性を計算するために，４つの関数を用意しています。  

***関数 vect_p2pint( ) ::*** 与えれる座標点の相対位置をベクトルで返します。
座標点から見た，与えられた別の座標点の相対位置をGMVector型で返します。

***関数 dist_p2pint( ) ::*** 与えれる座標点までの距離を返します。
関数 vect_p2pint( ) が返すGMVector型の相対ベクトルを用います。
そのインスタンス関数leng( )が返すその相対ベクトル長さをfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 dirc_p2pint( ) ::*** 与えられる座標点の相対方向角を返します。
関数 vect_p2pint( ) が返すGMVector型の相対ベクトルを用います。
そのインスタンス関数direc( )が返すその相対ベクトルの方向角をfloat型で返します。
角度の単位系をフラグ deg で指定できます。

***関数 unitvector( ) ::*** 与えられる座標点の相対方向の単位ベクトルを返します。
関数 vect_p2pint( ) が返すGMVector型の相対ベクトルを用います。
そのインスタンス関数unitvect( )が返す相対ベクトルの単位ベクトルをtuple型で返します。


**[section_ce]**  ベクトル解析
```python
    ## --- section_ce: (GMVector) analyzing vectors --- ##
    def inner_op_vect(self, vect: object, cnv: bool = True) -> float:  # inner product
        return self.inner_vect(vect, cnv=cnv)
    def outer_op_vect(self, vect: object, cnv: bool = True) -> ndarray:  # outer product
        return self.outer_vect(vect, cnv=cnv)
    def cross_op_vect(self, vect: object, cnv: bool = True) -> float:  # cross product
        return self.cross_vect(vect, cnv=cnv)
```
座標点の位置ベクトルと与えられるベクトルとの間の積（内積，外積，クロス積）を計算します，
３つのインスタンス関数を用意しています。  
***関数 inner_op_vect( ) ::*** 位置ベクトルと与えられるベクトルとの内積を計算して返します。
継承されたGMVectorの属性が位置ベクトルの属性になります。
与えられるベクトル vect: GMVector を渡して，インスタンス変数inner( )が返す内積（スカラー積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer_op_vect( ) ::*** 位置ベクトルと与えられるベクトルとの外積を計算して返します。
継承されたGMVectorの属性が位置ベクトルの属性になります。
与えられるベクトル vect: GMVector を渡して，インスタンス変数outer( )が返す外積（テンソル積）をndarray型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross_op_vect( ) ::*** 位置ベクトルと与えられるベクトルとのクロス積を返します。
継承されたGMVectorの属性が位置ベクトルの属性になります。
与えられるベクトル vect: GMVector を渡して，インスタンス変数cross( )が返すクロス積（外積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。



---

## [GMVector: gm_class_geom_c_point_vector.py](gm_class_geom_c_point_vector.py)

ここで紹介するクラスGMPointVectorは，始点を指定するベクトルを定義し操作します。
GMpointを親クラスとして継承する属性が，始点の属性になります。
始点からのベクトルは，GMVectorのインスタンスとしてクラスに所属します。
始点の位置ベクトルと始点からのベクトルとの関係を計算する機能をクラスに追加しています。


### **[section_module]**  拡張モジュール  
```python
print("*** (GMPointVector) class for position vector ***")
print("   *** class GMPoint is inherited; class GMVector is embedded as vect ***")
# ---------------------------------------------------------
print("### --- section_module: (GMPointVector) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_b_point import (GMPoint, GMVector)
```
クラスが利用する関数を，拡張モジュールnumpy と copy からimportしています。  
クラスGMPointを記述しているファイル gm_class_geom_b_point.py から GMPoint と GMVector をインポートしています。


### **[section_class]**  クラスの定義と記述
クラスに所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数
```python
class GMPointVector(GMPoint):  # inheriting GMPoint
    ## --- section_ca: (GMPointVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True,
            vect: GMVector = GMVector(xxyy=(1,0)) ) -> None:
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
        self._vect = None  # vector with initial point: GMVector
        self.set_point_vector(vect=vect)
```
***初期化関数__init__( ) ::*** この関数はクラスGMPointVector型のインスタンスを作成するときに自動的に起動します。
- クラスの宣言文 class GMPointVector(GMPoint) で親クラス GMPoint を継承しています。
- ベクトルの始点継承しているGMPoint型になります。
- このクラス独自のインスタンス変数は self._vect: GMVector です。

1. 前から５個の引数を 親クラスの初期化関数 __init__() に渡します。
2. self._vect はNoneで初期化されます。
3. 引数 vect を Setting関数 set_point_vector( ) に渡します。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: (GMPointVector) setting and getting functions --- ##
    ## setting functions
    def set_point_vector(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True,
            vect: GMVector = None) -> None:
        self.set_point(
            xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg, 
            vect=vect )
        if vect is not None: self._vect = vect
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
```
***Setting関数 set_point_vector( ) ::***  引数を受け取り，インスタンス変数を更新します。
- 引数 vect は，始点からのベクトルの属性を有するGMVector型の変数。 

1. 先頭から５この引数は，親クラスのSetting関数 set_point()に送り，始点の属性を更新ます。
2. 引数 vect が None でなければ，self._vect に vectを代入します。

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を利用して，
このGMPointVector型のインスタンス全体を複製して返します。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: (GMPointVector) string function for print() --- ##
    def __str__(self) -> str:
        return '(GMPoint) ' + super().__str__()
    def classprop(self, idx: str = '') -> str:
        return (
            idx + ':: GMPointVector ::\n'
            + self.__str__() + '\n'
            + '  vect: GMVector: ' + self._vect.__str__() + '' )
```
文字列関数__str__( ) と classprop( ) を記述しています。

***文字列関数 __str__( ) :: *** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
親クラスの名前を明記するとともに，インスタンスの属性（インスタンス変数など）を記述する文字列をf-string型で作成して返します。

***文字列関数 classprop( ) ::*** 親クラスや所属するインスタンスを含めて，
インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型名を明記するとともに，関数 __str__() が返す文字列とともに返します。 
インスタンス変数 self._vect の属性も追加して説明しています。


**[section_cd]**  ベクトル解析
```python
    ## --- section_cd: (GMPointVector) analysing vectors --- ##
    def vect_ot(self) -> GMVector:
        return  self + self._vect
    def inner_op_pt(self, cnv: bool = True) -> float:
        return self.inner_op_vect(self._vect, cnv)
    def outer_op_pt(self, cnv: bool = True) -> ndarray:
        return self.outer_op_vect(self._vect, cnv)
    def cross_op_pt(self, cnv: bool = True) -> float:
        return self.cross_op_vect(self._vect, cnv)
```
座標点の位置ベクトルと与えられるベクトルとの間の積（内積，外積，クロス積）を計算します，
４つのインスタンス関数を用意しています。  
***関数 vect_ot( ) ::*** ベクトルの終点の位置ベクトルをベクトルで返します。
始点の位置ベクトルに，ベクトル self._vect: GMVect を加えることにより，
得られるベクトルをGMVector型で返します。

***関数 inner_op_pt( ) ::*** 始点の位置ベクトルと始点からのベクトルとの内積を計算して返します。
継承されたGMPointの属性が始点の属性になります。
self._vect: GMVector を渡して，インスタンス変数inner( )が返す内積（スカラー積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer_op_pt( ) ::*** 始点の位置ベクトルと始点からのベクトルとの外積を計算して返します。
継承されたGMPointの属性が始点の属性になります。
self._vect: GMVector を渡して，，インスタンス変数outer( )が返す外積（テンソル積）をndarray型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross_op_pt( ) ::*** 始点の位置ベクトルと始点からのベクトルとのクロス積を返します。
継承されたGMPointの属性が始点の属性になります。
self._vect: GMVector を渡して，，インスタンス変数cross( )が返すクロス積（外積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。



---

## [GMVector: gm_class_geom_d_segment.py](gm_class_geom_d_segment.py)

ここで紹介するクラスGMSegmentは，両端に座標点を有する線分を定義し操作します。
継承する親クラスはありません。
両端の座標点は，GMPointのインスタンスとしてクラスに所属します。
線分と両端の座標点の関係を計算する機能をクラスに追加しています。


### **[section_module]**  拡張モジュール  
```python
print("*** (GMSegment) class for segment ***")
print("   *** class GMPoint is embedded as pinta and pintb ***")
# ---------------------------------------------------------
print("### --- section_module: (GMSegment) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_b_point import (GMPoint, GMVector)
```
クラスが利用する関数を，拡張モジュールnumpy と copy からimportしています。  
クラスGMPointを記述しているファイル gm_class_geom_b_point.py から GMPoint と GMVector をインポートしています。


### **[section_class]**  クラスの定義と記述
クラスに所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数
```python
print("### --- section_class: (GMSegment) describing class --- ###")
class GMSegment():
    ## --- section_ca: (GMSegment) initializing class instance --- ##
    def __init__(self,
            pinta: GMPoint = GMPoint(xxyy=(0,0)),
            pintb: GMPoint = GMPoint(xxyy=(1,1)) ):
        self._pinta = None  # end point A: GMPoint
        self._pintb = None  # end point B: GMPoint
        self.set_segment(pinta=pinta, pintb=pintb)
```
***初期化関数__init__( ) ::*** この関数はクラスGMSegment型のインスタンスを作成するときに自動的に起動します。
- インスタンス変数は self._pinta: GMPoint と self._pintb: GMPoint  の２つです。

2. self._pinta と self._pintb はNoneで初期化されます。
1. 引数 pinta と pintb は Setting関数 set_segment( ) に渡されます。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: (GMSegment) setting and getting functions --- ##
    ## setting functions
    def set_segment(self,
            pinta: GMPoint = None, pintb: GMPoint = None) -> None:
        if pinta is not None: self._pinta = pinta
        if pintb is not None: self._pintb = pintb
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
```
***Setting関数 set_point_vector( ) ::***  引数を受け取り，インスタンス変数を更新します。  
- 引数 pinta, pintb は，端点AとBの属性を有するGMPoint型の変数。 

2. 引数 pinta が None でなければ，self._pinta に pinta を代入します。
2. 引数 pintb が None でなければ，self._pintb に pintb を代入します。

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を 利用して，
このGMPolygon型のインスタンス全体を複製して返します。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: (GMSegment) string function for print() --- ##")
    def __str__(self) -> str:
        return (
            + '  pinta: GMPoint: ' + self._pinta.__str__() + '\n'
            + '  pintb: GMPoint: ' + self._pintb.__str__() + '' )
    def classprop(self, idx: str = '') -> str:
        return (
            idx + ':: GMSegment ::\n' + self.__str__() )
```
文字列関数__str__( ) と classprop( ) を記述しています。

***文字列関数 __str__( ) ::*** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
親クラスの名前を明記するとともに，インスタンスの属性（インスタンス変数など）を記述する文字列をf-string型で作成して返します。

***文字列関数 classprop( ) ::*** 引数をインデックスとして，インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型名を明記するとともに，関数 __str__() が返す文字列とともに返します。 


**[section_cd]**  属性の計算
```python
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
```
インスタンスの属性を計算するために，７つの関数を用意しています。  

***関数 vect_a2b( ), vect_b2a( ) ::*** 端点からもう一方の端点へのベクトルを返します。
- vect_a2b( ) は vect._pinta から vect._pintb へのベクトルを返します。
- vect_b2a( ) は vect._pintb から vect._pinta へのベクトルを返します。

1. GMPoint のインスタンス関数 vect_p2pint( ) が返すベクトルを 
GMVector型として返します。 

***関数 leng( ) ::*** 線分の長さを返します。
- 線分の両端点の距離を計算します。

1. GMPoint のインスタンス関数 dist_p2pint( ) が返す距離を 
float型として返します。 

***関数 dirc_a2b( ), dirc_b2a( ) ::*** 端点からもう一方の端点への方向角を返します。
- dirc_a2b( ) は vect._pinta から vect._pintb への方向角を返します。
- dirc_b2a( ) は vect._pintb から vect._pinta への方向角を返します。

1. GMPoint のインスタンス関数 dirc_p2pint( ) が返す方向角を 
float型として返します。 
角度の単位系をフラグ deg で指定できます。

***関数 unitvect_a2b( ), unitvect_b2a( ) ::*** 端点からもう一方の端点への単位ベクトルを返します。
- unitvect_a2b( ) は vect._pinta から vect._pintb への単位ベクトルを返します。
- unitvect_b2a( ) は vect._pintb から vect._pinta への単位ベクトルを返します。

1. GMPoint のインスタンス関数 unitvect_p2pint( ) が返す単位ベクトルを 
tuple型として返します。 


**[section_ce]**  ベクトル解析
```python
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
```
両端点の位置ベクトルの間の積（内積，外積，クロス積）を返します。
また，線分をx-軸またはy-軸へ投影したときの長さを返します。
７つのインスタンス関数を用意しています。  
 
- vect._pinta: GMPoint と vect._pintb: GMPoint の位置ベクトルの属性は，継承している GMVector 属性になります。

***関数 inner_oa_ob( ), inner_ob_oa( ) ::*** 両端点の位置ベクトルの内積を計算して返します。
- inner_oa_ob( ) は vect._pinta の位置ベクトルと vect._pintb の位置ベクトルの間の内積を返します。
- inner_ob_oa( ) は vect._pintb の位置ベクトルと vect._pinta の位置ベクトルの間の内積を返します。

1. GMPoint の関数 inner_op_vect( ) が返す内積（スカラー積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer_oa_ob( ), outer_ob_oa( ) ::*** 両端点の位置ベクトルの外積を計算して返します。
- outer_oa_ob( ) は vect._pinta の位置ベクトルと vect._pintb の位置ベクトルの間の外積を返します。
- outer_ob_oa( ) は vect._pintb の位置ベクトルと vect._pinta の位置ベクトルの間の外積を返します。

1. GMPoint の関数 outer_op_vect( ) が返す外積（テンソル積）をndarray型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross_oa_ob( ), cross_ob_oa( ) ::*** 両端点の位置ベクトルのクロス積を計算して返します。
- cross_oa_ob( ) は vect._pinta の位置ベクトルと vect._pintb の位置ベクトルの間のクロス積を返します。
- cross_ob_oa( ) は vect._pintb の位置ベクトルと vect._pinta の位置ベクトルの間のクロス積を返します。

1. GMPoint の関数 cross_op_vect( ) が返すクロス積（外積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 projx( ), projy( ) ::*** 線分を座標軸に投影するときの面積を計算して返します。
- projx( ) は 線分をx-軸へ投影するときの面積を返します。
- projy( ) は 線分をy-軸へ投影するときの面積を返します。

1. GMPoint の関数 cross_op_vect( ) が返すクロス積（外積）をfloat型で返します。
長さの単位系をフラグ cnv で指定することが可能です。



---

## [GMVector: gm_class_geom_e_polygon.py](gm_class_geom_e_polygon.py)

ここで紹介するクラスGMSegmentは，多角形を定義し操作します。
継承する親クラスはありません。
多角形の頂点は GMPoint のインスタンス，辺は GMSegment のインスタンスです。
頂点のインスタンスのlist と 辺のインスタンスのlist がこのクラスに所属します。
多角形の幾何学特性を計算する機能をクラスに追加しています。


### **[section_module]**  拡張モジュール  
```python
print("*** (GMPolygon) class for segment ***")
print("   *** class GMpoint and GMSegment are embedded as lists ***")
# ---------------------------------------------------------
print("### --- section__: (GMPolygon) importing items from module --- ###")
from numpy import (ndarray, array)
import copy
from gm_class_geom_d_segment import (GMSegment, GMPoint)
```
クラスが利用する関数を，拡張モジュールnumpy と copy からimportしています。  
クラスGMSegmentを記述しているファイル gm_class_geom_d_segment.py から GMSegment と GMPoint をインポートしています。


### **[section_class]**  クラスの定義と記述
クラスに所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数
```python
print("### --- section_class: (GMPolygon) describing class --- ###")
class GMPolygon():
    ## --- section_ca: (GMPolygon) initializing class instance --- ##
    def __init__(self, points: tuple = ((0., 0.),(1., 0.),(1., 1.),(0., 1.),)):
        self._pints = None  # list of polygon points [GMPoint]
        self._segms = None  # list of polygon sides [GMSegment]
        self.set_polygon(points)
```
***初期化関数__init__( ) ::*** この関数はクラスGMpolygon型のインスタンスを作成するときに自動的に起動します。
- 多角形の頂点は GMPoint のインスタンスで，その list が インスタンス変数 self._points です。
- 多角形の辺は GMSegments のインスタンスで，その list が インスタンス変数 self._segms です。
- self._segms の各成分は，両端点として self._pints の成分を共有しています。
- 引数 pints は多角形を構成する頂点座標のリストで，リスト構造（tuple, list, ndarray）でなければなりません。

1. self._pints と self._segms はNoneで初期化されます。
2. 引数 pints は Setting関数 set_polygon( ) に渡されます。


**[section_cb]**  Setting関数とGetting関数
```python
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
```
***Setting関数 set_polygon( ) ::***  引数を受け取り，インスタンス変数を更新します。  
- 引数 pints は，多角形の頂点座標のリストで，リスト構造型で受け取ります。 

1. self._pints は空のlistで初期化され，各頂点のGMPoint型のインスタンスが順に追加されます。
2. self._segms は空のlistで初期化され，辺のGMSegment型のインスタンスが順に追加されます。
辺をインスタンスは self._pints の成分を端点としてして共有しています。

***Getting関数 copy( ) ::*** インスタンスを複製して返します。
拡張モジュール copy が提供する関数 deepcopy( ) を利用して，
このGMPolygon型のインスタンス全体を複製して返します。


**[section_cc]**  文字列関数
```python
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
```
文字列関数__str__( ) と classprop( ) を記述しています。

***文字列関数 __str__( ) ::*** インスタンスの属性を記述する文字列を作成して返します。  
関数print()でインスタンス名を渡すと起動します，
親クラスの名前を明記するとともに，インスタンスの属性（インスタンス変数など）を記述する文字列をf-string型で作成して返します。

***文字列関数 classprop( ) ::*** 引数をインデックスとして，インスタンスの属性を記述する文字列を作成して返します。  
このインスタンスのクラス型名を明記するとともに，関数 __str__() が返す文字列とともに返します。 


**[section_cd]**  属性の計算
```python
    ## --- section_cd: (GMPolygon) calculating properties --- ##
    def grav_ctr(self, cnv: bool = True) -> ndarray:  # gravity center
        grav_ctr = array([0.,0.])
        for pint in self._pints:
            grav_ctr += pint.xxyy(cnv=cnv)
        return grav_ctr / len(self._pints)
    def leng(self, cnv: bool = True) -> float:  # total length of polygon sides
        leng = 0.
        for segm in self._segms:
            leng += segm.leng(cnv=cnv)
        return leng
    def area_prod(self, cnv: bool = True) -> float:  # area of polygon from cross product
        area = 0.
        for segm in self._segms:
            area += segm.cross_oa_ob(cnv=cnv)
        return abs(area) / 2.
    def area_projx(self, cnv: bool = True) -> float:  # area of polygon from projection to x-axis
        area = 0.
        for segm in self._segms:
            area += segm.projx(cnv=cnv)
        return abs(area)
    def area_projy(self, cnv: bool = True) -> float:  # area of polygon from projection to y-axis.
        area = 0.
        for segm in self._segms:
            area += segm.projy(cnv=cnv)
        return abs(area)
```
インスタンスの属性を計算するために，７つの関数を用意しています。  

***関数 grav_ctr( ) ::*** 多角形の重心の座標をを返します。
- 各頂点の座標値から重心座標を求めます。

1. self._pints の各成分（GMPoint のインスタンス）の関数 xxyy( ) が座標値を返します。
2. for-loop で座標値の総和を計算し，頂点数で除すことにより平均値を求め，float型で返します。 
長さの単位系をフラグ cnv で指定できます。

***関数 leng( ) ::*** 多角形の辺長を返します。
- 多角形の辺の長さの総和を計算します。

1. self._segms の各成分（GMSegment のインスタンス）の関数 leng( ) が辺長を返します。
2. for-loop で辺長を総和を計算し，float型で返します。 
長さの単位系をフラグ cnv で指定できます。

***関数 area_prod( ) ::*** 多角形の面積を返します。
- 多角形の各辺と原点が作る三角形の面積の総和を返します。

1. self._segms の各成分（GMSegment のインスタンス）の
関数 cross_oa_ob( ) が各辺と原点が作る三角形の面積を返します。
2. for-loop で面積の総和を計算し，その絶対値をfloat型で返します。 
長さの単位系をフラグ cnv で指定できます。

***関数 area_projx( ), area_projy( ) ::*** 多角形の面積を返します。
1. self._segms の各成分（GMSegment のインスタンス）の
関数 projx( ) または projx( ) が各辺を座標軸（x-軸またはy-軸）に投影するときの台形の面積を返します。
2. for-loop で面積の総和を計算し，その絶対値をfloat型で返します。 
長さの単位系をフラグ cnv で指定できます。







