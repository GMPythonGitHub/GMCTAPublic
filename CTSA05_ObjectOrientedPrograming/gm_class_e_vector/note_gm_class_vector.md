# **Note on gm_class_e_vector:** ***ベクトルの操作と計算のためのクラス***

## 概要
ここではベクトルを定義し，操作するための４つのクラスを紹介します。
基本的なクラスから始め，これを段階的に更新することによってクラスの機能を強化していきます。
前項のGMNumbersよりは進んだ段階でのクラスの活用法を紹介します。

各クラスの構成は以下のようです。

> [GMVectorA: gm_class_vector_a.py](gm_class_vector_a.py)  :: 基本的なクラス
> クラスの体裁を整えている，基本的なクラスです  
>> インスタンス変数： _\_xx, _\_yy   
> 初期化関数 _\_init\_\_(xx, yy)  
> Setting関数 set_xxyy(), Getting関数 xxyy()  
> 文字列関数 _\_str\_\_()
> インスタンス関数 leng(), dirc(), unitvect()  
> 
> [GMVectorB: gm_class_vector_b.py](gm_class_vector_b.py)  :: 座標変換
> 座標変換をSetting関数とGetting関数で行います。  
>> インスタンス変数： _\_xx, _\_yy  
> 初期化関数 _\_init\_\_(xx, yy, rr, th, deg)
> Setting関数 set_vect()， Getting関数 xxyy(), rrth()  
> 文字列関数 _\_str\_\_()  
> インスタンス関数 leng(), dirc(), unitvect()  
> 
> [GMVectorC: gm_class_vector_c.py](gm_class_vector_c.py)  :: ndarrayの導入
> ndarrayを導入し，数値計算を簡便にします。  
>> インスタンス変数： _\_xxyy; ndarray  
> 初期化関数 _\_init\_\_(xx, yy, rr, th, deg)  
> Setting関数 set_vect()， Getting関数 xxyy(), rrth()
> 文字列関数 _\_str\_\_()
> インスタンス関数 leng(), dirc(), unitvect(), inner(), **outer(), **cross()  
> 
> [GMVectorD: gm_class_vector_d.py](gm_class_vector_d.py)  :: 演算子のオーバーロード
> 演算子のオーバーロードによる，ベクトルの四則演算を可能にします。  
>> インスタンス変数： _\_xxyy; ndarray  
> 初期化関数 _\_init\_\_(xx, yy, rr, th, deg)  
> Setting関数 set_vect( )， Getting関数 xxyy( ), rrth( ), copy( )
> 文字列関数 _\_str\_\_( )
> インスタンス関数 
> leng( ), dirc( ), unitvect( ), inner( ), outer( ), cross( )  
> conv( ), add( ), sub( ), rsub( ), mul( ), div( ), rdiv( )  
> _\_pos\_\_( ), _\_neg\_\_( ), 
> _\_add\_\_( ), _\_radd\_\_( ), _\_sub\_\_( ), _\_rsub\_\_( ), 
> _\_mul\_\_( ), _\_rmul\_\_( ), _\_div\_\_( ), _\_rdiv\_\_( ),
> _\_iadd\_\_( ), _\_isub\_\_( ), _\_imul\_\_( ), _\_itruediv\_\_( )



---

## [GMVectorA: gm_class_vector_a.py](gm_class_vector_a.py)

紹介する最初のクラスGMVecotrAでは，ベクトルの成分がインスタンス変数として所属し，
ベクトルの長さと方位角，単位ベクトルを計算する機能を有しています。


### **[section_module]**  拡張モジュール  
```python
 print('### --- section_module: (GMVectorA) importing items from module --- ###')
 from numpy import(
     square as sq, sqrt as sr, arctan2 as atan2, rad2deg as r2d)
```
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
関数atan2()は座標点の方向角を計算する関数で，
y成分とx成分の両方を引数として渡すことで，全方位の角度を戻り値としてradianで返します。
関数r2d()は角度の単位系をradianからdegreeに，関数d2rはdegreeからradianに変換します。


### **[section_class]**  クラスの定義と記述  
クラスに所属するインスタンス変数とインスタンス関数を定義して，記述しています。  

**[section_ca]**  初期化関数
```python
print('### --- section_class: (GMVectorA) describing class --- ###')
class GMVectorA():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xx: float = 1, yy: float = 1) -> None:
        self.__xx, self.__yy = None, None
        self.set_xxyy(xx=xx, yy=yy)
```
***初期化関数__init__( ) ::*** この関数はクラスGMVectorA型のインスタンスを作成するときに自動的に起動します。
- インスタンス変数は private の属性を有する self.__xx: float と self.__yy: float の２つです。
- self.__xx と self.__yy をひとまず None で初期化することによって，インスタンス内で定義します。
- 引数は２個でデフォルト値を設定しています。
これらをSetting関数 set_xxyy( )に渡すことにより self.__xx と self.__yy を更新します。

**[section_cb]**  Setting関数とGetting関数
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
***Setting関数 set_xxyy() ::***  引数を受取り，インスタンス変数 self.__xx と self.__yy をで更新します。
- 引数はベクトルの成分 xx と yy で，デフォルト値は None です。

引数がデフォルト値 None ではなく，具体的な数値の場合に対応する部分がインスタンス変数が更新されます。
具体的な処理内容は以下のようです。
1. 引数 xx が None でない場合には，self.__xx が更新されます。
2. 引数 yy が None でない場合には，self.__yy が更新されます。

***Getting関数 xxyy( ) ::*** インスタンス変数 self.__xx と self.__yy を参照します。  
self.__xx と self.__yy の値を参照して tuple型で返します。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMVectorA): xx = {self.__xx:g}, yy = {self.__yy:g}'
```
***文字列関数 __str__( ) :: *** インスタンスの属性を記述する文字列を作成して返します。  
この関数は，関数print()でインスタンス名を渡すと自動的に起動します，
インスタンスの属性（クラス名とインスタンス変数などを）を記述する文字列をf-string型で作成して返します。


**[section_cd]**  ベクトルの属性
```python
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
***関数 leng( ) ::*** ベクトルの長さを計算して返します。
ベクトルの長さは，各ベクトル成分の二乗和の平方根として計算します。

***関数 dirc( ) ::*** ベクトルの方向角を返します。
関数atan2( ) を用いて方向角を計算します。
計算結果は角度の単位系 radian で得有れますが，引数 deg が True のときは関数 r2d( ) を用いて degree に単位変換します。

***関数 unitvector( ) ::*** ベクトルと同方向の単位ベクトルを返します。
関数leng( ) が返すベクトルの長さで
ベクトルの各成分 self.__xx と self.__yy を除すことによって，
単位ベクトルを計算しています。


### **[section_main]**  メインセクション

*** [section_ma, section_mb] **  クラスGMVectorBの機能の紹介
```python
print('### --- section_main: (GMVectorB) main process--- ###')
## --- section_ma: vector properties --- ##
vect = GMVectorB(4, 3)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
## --- section_mb: vector properties --- ##
vect.set_vect(xx=5, yy=5)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')
## --- section_mc: vectorcalculating vectors --- ##
vect.set_vect(rr=4, th=30, deg=True)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')
```
クラスの機能を紹介し，パフォーマンスをチェックする目的で，基本的なプログラムを記述しています。

section_ma:
1. GMVectorA型のインスタンスvectを初期値を(xx=4, yy=3)として作成します。
2. 関数print( )と文字列関数を用いてペクトルの属性を表示し，
次いで，関数unitvect( )を用いて単位ベクトルを計算し，表示します。

section_mb:
3. （xx=5, yy=5)でインスタンス変数を更新し，同様な操作を繰返します。


---

## [GMVectorB: gm_class_vector_b.py](gm_class_vector_b.py)

直交座標系のみならず円座標系でもベクトルを記述できるように，先に紹介したクラスGMVecotrAを更新しています。
インスタンス変数を初期化，参照または更新するときに，
必要に応じて直交座標系と円座標系を選択できるようにしています。
インスタンス関数が引数を受取り，戻り値を返すときにも同様に，座標系を選択できます。


### **[section_module]**  拡張モジュール  
```python
print('### --- section_module: (GMVectorB) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
```
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
三角関数 cos() と sin() を追加でimportしています。


### **[section_function]**  グローバル関数  
```python
print("### --- section_function: (GMVectorB) defining global functions --- ###")
def gmsrsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```
クラスで利用する２個のグローバル関数を定義しています。  

***関数 gmsrsq() ::***  ２つの引数の二乗和の平方根を返します。
 
***関数 gmatan2() ::***  べクトルのy成分とx成分を受か取り，方位角を返します。
角度の単位系フラグdegをTrueにすると，単位系をdegreeに指定できます。


### **[section_class]**  クラスの定義と記述

**[section_ca]**  初期化関数
```python
print('### --- section_class: (GMVectorB) describing class --- ###')
class GMVectorB():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xx: float = 1, yy: float = 1,
            rr: float = None, th: float = None, deg: bool = True) -> None:
        self.__xx, self.__yy = None, None  # instance variables
        self.set_vect(xx=xx, yy=yy, rr=rr, th=th, deg=deg)
```
***初期化関数__init__( ) ::*** この関数はクラスGMVectorB型のインスタンスを作成するときに自動的に起動します。
- インスタンス変数は private の属性を有する self.__xx: float と self.__yy: float の２つで，変更はありません。
- self.__xx と self.__yy をひとまず None で初期化することによって，インスタンス内で定義します。
- 引数は５個でデフォルト値を設定しています。
これをSetting関数 set_vect( )に渡すことにより
self.__xx と self.__yy を更新します。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: setting and getting functions --- ##
    ## settinng function
    def set_vect(self,
            xx: float = None, yy: float = None,
            rr: float = None, th: float = None, deg: bool = True) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
        if rr is not None or th is not None:
            if rr is None: rr = gmsrsq(self.__xx,self.__yy)
            if th is None: th = gmatan2(self.__yy,self.__xx,deg=deg)
            else: th = d2r(th) if deg else th
            self.__xx, self.__yy = rr * cos(th), rr * sin(th)
    ## getting functions
    def xxyy(self) -> tuple:
        return self.__xx, self.__yy
    def rrth(self, deg: bool = False) -> tuple:
        return gmsrsq(self.__xx,self.__yy), gmatan2(self.__yy,self.__xx,deg=deg)
```
***Setting関数 set_vect() ::***  引数を受取り，インスタンス変数 self.__xx と self.__yy をで更新します。
- 引数は直交座標系におけるベクトルの成分 xx と yy に， 
座標系におけるベクトルの成分 rr とth，角度の単位系のフラグ deg を加えた５個です。
デフォルト値は deg がTrue であることを除くと None です。

４個の引数がデフォルト値 None ではなく，具体的な数値の場合に対応する部分がインスタンス変数が更新されます。
具体的な処理内容は以下のようです。
1. 引数 xx が None でない場合には，self.__xx が更新されます。
2. 引数 yy が None でない場合には，self.__yy が更新されます。
3. 「引数 rr が None でない，または， 引数 th がNone でない」場合は，
まず，現在の円座標系における成分 rr と th を更新します。
次に，座標系の変換により rr と th から xx, yy を計算し，self.__xx と self.__yy を更新します。
このとき，deg が True の場合は関数d2r( )によって th が degree から radian へ変換されます。

***Getting関数 xxyy( ) ::*** インスタンス変数 self.__xx と self.__yy を参照します。  
self.__xx と self.__yy の値を参照して tuple型で返します。

***Getting関数 rrth( ) ::*** インスタンス変数 self.__xx と self.__yy を参照し，
円座標系におけるベクトルの成分 rr と th を返します。  
直交座標系におけるベクトル成分成分 self.__xx と self.__yy から
円座標系におけるベクトル成分 rr と th をの値を計算してtuple型で返します。
このとき，deg が True の場合は関数red( )によって th が radian から degree へ変換されます。


**[section_cc]**  文字列関数
```python
    ## --- section_cd: string function for print() --- ##
    def __str__(self) -> str:
        rr, th = self.rrth(True)
        return (
            f'(GMVectorB): xx = {self.__xx:g}, yy = {self.__yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
```
ベクトルの属性に，円座標系における成分 rr と th を追加しています。


**[section_cd]**  ベクトルの属性
```python
    ## --- section_ce: functions for properties --- ##
    def leng(self) -> float:
        return self.rrth()[0]  # rr
    def dirc(self, deg: bool = False) -> float:
        return self.rrth(deg=deg)[1]  # th
    def unitvect(self) -> tuple:
        leng = self.leng()
        return self.__xx / leng, self.__yy / leng
```
***関数 leng( ) ::*** ベクトルの長さを計算して返します。
関数rrth( ) が返す円座標系の成分のうち rr を返しています。

***関数 dirc( ) ::*** ベクトルの方向角を返します。
関数rrth( ) が返す円座標系の成分のうち th を返しています。

***関数 unitvector( ) ::*** ベクトルと同方向の単位ベクトルを返します。
関数leng( ) が返すベクトルの長さで
ベクトルの各成分 self.__xx と self.__yy を除すことによって，
単位ベクトルを計算しています。


### **[section_main]**  メインセクション

** [section_ma, section_mb, section_mc] **  クラスGMVectorBの機能の紹介
```python
print('### --- section_main: (GMVectorB) main process--- ###')
## --- section_ma: vector properties --- ##
vect = GMVectorB(4, 3)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
## --- section_mb: vector properties --- ##
vect.set_vect(xx=5, yy=5)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')
## --- section_mc: vectorcalculating vectors --- ##
vect.set_vect(rr=4, th=30, deg=True)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')
```
クラスの機能を紹介し，パフォーマンスをチェックする目的で，基本的なプログラムを記述しています。

section_ma:
1. GMVectorA型のインスタンスvectを初期値を(xx=4, yy=3)として作成します。
2. 関数print( )と文字列関数を用いてペクトルの属性を表示し，
次いで，関数unitvect( )を用いて単位ベクトルを計算し，表示します。

section_mb:
3. （xx=5, yy=5)でインスタンス変数を更新し，同様な操作を繰返します。

section_mb:
3. （rr=4, th=30, deg=True)でインスタンス変数を更新し，同様な操作を繰返します。



---

## [GMVectorC: gm_class_vector_c.py](gm_class_vector_c.py)

拡張モジュールnumpyを導入により数値計算をより効率的に行うために，
先に紹介したクラスGMVecotrBを更新しています。
直交座標系におけるベクトル成分をnumpyが提供するndarray型で表し，
それに対応してクラスに所属するインスタンス関数を変更しています。
さらに，numpyが提供する幾つかの関数を導入してベクトル解析の機能を強化しています。  


### **[section_module]**  モジュール
```python
print('### --- section_module: (GMVectorC) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)
```
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
- 多次元配列を操作することが可能なndarrayを導入するために，ndarray と array をインポートしています。
さらに，ベクトル計算を効率よく行うために，３つの関数をインポートしています。  
- 関数inner()は２つのベクトルの内積（またはドット積）を計算します。
他の関数numpy.dot()は多次元配列（マトリックス）に対しても同様な計算を行うことが可能です。  
- 関数outer()は２つのベクトルの外積（まはたテンソル積）を計算します。
多次元配列を含む計算には他の関数numpy.tenordot()を利用することができます。
用語が乱れていて，高校数学の範囲で用いられる「外積」は次に示す「クロス積」にあたります。  
- 関数numpy.cross()は2つのベクトルのクロス積（ベクトル積）を計算します。


### **[section_function]**  グローバル関数
```python
print('### --- section_function: (GMVectorB) defining global functions --- ###')
def gmsrsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```
グローバル関数に変更はありません。


### **[section_class]**  クラスの定義と記述

**[section_ca]**  初期化関数  
```python
print('### --- section_class: (GMVectorC) describing class --- ###')
class GMVectorC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1, 1), rrth: tuple = None, deg: bool = True) -> None:
        self.__xxyy = None
        self.set_vect(xxyy=xxyy, rrth=rrth, deg=deg)
```
***初期化関数__init__( ) ::*** この関数はクラスGMVectorC型のインスタンスを作成するときに自動的に起動します。
- インスタンス変数は private の属性を有する self.__xxyy: ndarrayです。
- self.__xxyy をひとまず None で初期化することによって，インスタンス内で定義します。
- 引数は３個でデフォルト値を設定しています。
これをSetting関数 set_vect( )に渡すことによりself.__xxyy を更新します。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_vect(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        if xxyy is not None: self.__xxyy = array(xxyy)
        if rrth is not None:
            rr, th = rrth
            if deg: th = d2r(th)
            self.__xxyy = array([rr * cos(th), rr * sin(th)])
    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, deg: bool = False) -> ndarray:
        xx, yy = self.__xxyy
        return array([gmsrsq(xx,yy), gmatan2(yy,xx,deg=deg)])
```
privateであるインスタンス変数の参照と更新を可能にするため，関数を定義しています。
ndarrayに適応した簡潔な表現に変更しています。  

***Setting関数 set_vect( ) ::***  引数を受取り，インスタンス変数 self.__xxyy をで更新します。
- 引数は直交座標系におけるベクトルの成分 xxyy に， 
円座標系におけるベクトルの成分 rrth，角度の単位系のフラグ deg を加えた３個です。
デフォルト値は deg がTrue であることを除くと None です。

４個の引数がデフォルト値 None ではなく，具体的な数値の場合に対応する部分がインスタンス変数が更新されます。
具体的な処理内容は以下のようです。
1. 引数 xxyyt が None でない場合に，self.__xxyy が更新されます。
3. 引数 rrth が None でない場合にも，self.__xxyy が更新されます。
座標系の変換により rr と th から xx, yy を計算し，self.__xxyy を更新します。
このとき，deg が True の場合は関数d2r( )によって th が degree から radian へ変換されます。

***Getting関数 xxyy( ) ::*** インスタンス変数 self.__xxyy を参照します。  
self.__xxyy の値を参照して ndarray型で返します。

***Getting関数 rrth( ) ::*** インスタンス変数 self.__xxyy を参照し，
円座標系におけるベクトルの成分を返します。  
直交座標系におけるベクトル成分 self.__xxyy から
円座標系におけるベクトル成分 rr と th をの値を計算してndarray型で返します。
このとき，deg が True の場合は関数red( )によって th が radian から degree へ変換されます。


**[section_cc]**  文字列関数
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorC): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
```
大きな変更はありませんが，ndarrayに適応した記述に更新しています。


**[section_cd]** ベクトルの属性
```python
    def leng(self) -> float:
        return self.rrth()[0]
    def dirc(self, deg: bool = False) -> float:
        return self.rrth(deg=deg)[1]
    def unitvect(self) -> ndarray:
        return self.__xxyy / self.leng()
```
インスタンス関数に大きに変更はありませんが，ndarrayに適応した簡潔な記述に更新しています。


**[section_ce]**  ベクトルの積
```python
    def inner(self, vect: object) -> float:
        return inner(self.__xxyy, vect.xxyy())
    def outer(self, vect: object) -> ndarray:
        return outer(self.__xxyy, vect.xxyy())
    def cross(self, vect: object) -> float:
        return float(cross(self.__xxyy, vect.xxyy()))
```
numpyが提供する関数を利用して，
与えられるベクトルとの間の積（内積，外積，クロス積）を計算する，
３つのインスタンス関数を用意しています。  
***関数 inner( ) ::*** 与えられるベクトルとの内積を計算して返します。
与えられたベクトル vect: GMVector との間の内積（スカラー積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 outer( ) ::*** 与えられるベクトルとの外積を計算して返します。
与えられたベクトル vect: GMVector との間の外積（テンソル積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。

***関数 cross( ) ::*** 与えられるベクトルとのクロス積を返します。
与えられたベクトル vect: GMVector との間のクロス積（外積）を次式で計算して返します。
長さの単位系をフラグ cnv で指定することが可能です。


### **[section_main]**  メインセクション

**[section_ma, section_mb]**  クラスGMVectorCの機能の紹介
```python
print('### --- section_main: (GMVectorC) main process --- ###')
## --- section_ma: creating instances --- ##
vecta = GMVectorC(xxyy=(3,4))  # creating instance
print('vecta:', vecta)
vectb = GMVectorC(xxyy=(-4,3))  # creating instance
print('vectb:', vectb)
## --- section_mb: calculating vector products --- ##
print(f'{vecta.inner(vectb) = }')
print(f'{vecta.outer(vectb) = }')
print(f'{vecta.cross(vectb) = }')
print(f'{vectb.inner(vecta) = }')
print(f'{vectb.outer(vecta) = }')
print(f'{vectb.cross(vecta) = }')
```
クラスの機能を紹介し，パフォーマンスをチェックする目的で，基本的なプログラムを記述しています。

section_ma:
1. GMVectorC型の２つのインスタンス vecta とvectb を，
それぞれ初期値を (xxyy=(3,4)) と (xxyy=(-4,3)) として作成します。
2. 関数print( )と文字列関数を用いてペクトルの属性を表示します。

section_mb:
3. ３種類のベクトル積を計算して，表示します。



---

## [GMVectorD: gm_class_vector_d.py](gm_class_vector_d.py)

ベクトルの演算をより効果的に行うために，先に紹介したクラスGMVecotrCを変更しています。
具体的には，ベクトルの四則演算を簡潔に実施するために，２つのグループのインスタンス変数を追加しています。
以下では，変更箇所のみを説明します。


### **[section_module]**  
拡張モジュールnumpyからimportする関数に変更はありませんが，
インスタンスを複製するために必要な拡張モジュールcopyを追加してimportしています。  
```python
print('### --- section_module: (GMVectorD) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)
import copy
```


### **[section_function]**
グローバルな関数の定義に変更はありません。
```python
print('### --- section_function: (GMVectorB) defining global functions --- ###')
def gmsrsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```


### **[section_class]**

**[section_ca]**  初期化関数  
初期化関数__init__()に変更はありません。

**[section_cb]**  Setting関数とGetting関数copy()
```python
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_vect(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        if xxyy is not None: self.__xxyy = array(xxyy)
        if rrth is not None:
            rr, th = rrth
            if deg: th = d2r(th)
            self.__xxyy = array([rr * cos(th), rr * sin(th)])
    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, deg: bool = False) -> ndarray:
        xx, yy = self.__xxyy
        return array([gmsrsq(xx,yy), gmatan2(yy,xx,deg=deg)])
    def copy(self) -> object:
        return copy.deepcopy(self)
```
****Getting関数 copy() ::****  インスタンスを複製します。
- 拡張モジュールcopyが提供する関数deepcopy()を利用しています。
これにより，所属する変数を共有しない独立した複製を返します。

**[section_cc]**  文字列関数  :: 変更はありません。

**[section_cd]** ベクトルの属性 :: 変更はありません。

**[section_ce]**  ベクトル積  :: 変更はありません。

**[section_cf]**  ベクトルの四則演算
```python
    ## --- section_cf: functions for vector operation --- ##
    def conv(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVectorD): return vect.xxyy()
        else: return None
    def add(self, vct: object) -> None: self.__xxyy = self.__xxyy + self.conv(vct)
    def sub(self, vct: object) -> None: self.__xxyy = self.__xxyy - self.conv(vct)
    def rsub(self, vct: object) -> None: self.__xxyy = self.conv(vct) - self.__xxyy
    def mul(self, vct: object) -> None: self.__xxyy = self.__xxyy * self.conv(vct)
    def div(self, vct: object) -> None: self.__xxyy = self.__xxyy / self.conv(vct)
    def rdiv(self, vct: object) -> None: self.__xxyy = self.conv(vct) / self.__xxyy
```
四則演算を実行するために，６個のインスタンス関数を用意しています。
演算におけるもう一方の項を引数として渡し，その計算結果に基づいて自身のインスタンス変数を更新します。
数値型，リスト構造型（list型，tuple型）あるいはGMVectorDのインスタンスを引数として渡すことが可能です。
関数conv()は引数の型を調整するために用いられ，これにより多様な多用な引数を受け入れることが可能です。
減算と除算については，演算の順序を入れ替えて実行するrsub()とrdiv()も用意しています。

**[section_cg]**  演算子のオーバーロード
```python
    ## --- section_cf: functions for vector operation --- ##
    def conv(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVectorD): return vect.xxyy()
        else: return None
    def add(self, vct: object) -> None: self.__xxyy = self.__xxyy + self.conv(vct)
    def sub(self, vct: object) -> None: self.__xxyy = self.__xxyy - self.conv(vct)
    def rsub(self, vct: object) -> None: self.__xxyy = self.conv(vct) - self.__xxyy
    def mul(self, vct: object) -> None: self.__xxyy = self.__xxyy * self.conv(vct)
    def div(self, vct: object) -> None: self.__xxyy = self.__xxyy / self.conv(vct)
    def rdiv(self, vct: object) -> None: self.__xxyy = self.conv(vct) / self.__xxyy
```
与えられるベクトルや数値に対して四則演算を行うために，６個の関数を用意しています。  
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
    ## --- section_cg: functions for vector operator --- ##
    # sign operators
    def __pos__(self): return GMVectorD(xxyy=+self.__xxyy)
    def __neg__(self): return GMVectorD(xxyy=-self.__xxyy)
    # arithmetic operators
    def __add__(self, vct): return GMVectorD(xxyy=self.__xxyy+self.conv(vct))
    def __radd__(self, vct): return GMVectorD(xxyy=self.conv(vct)+self.__xxyy)
    def __sub__(self, vct): return GMVectorD(xxyy=self.__xxyy-self.conv(vct))
    def __rsub__(self, vct): return GMVectorD(xxyy=self.conv(vct)-self.__xxyy)
    def __mul__(self, vct): return GMVectorD(xxyy=self.__xxyy*self.conv(vct))
    def __rmul__(self, vct): return GMVectorD(xxyy=self.conv(vct)*self.__xxyy)
    def __truediv__(self, vct): return GMVectorD(xxyy=self.__xxyy/self.conv(vct))
    def __rtruediv__(self, vct): return GMVectorD(xxyy=self.conv(vct)/self.__xxyy)
    # cumulative assignment operaters
    def __iadd__(self, vct): self.__xxyy = self.__xxyy+self.conv(vct); return self
    def __isub__(self, vct): self.__xxyy = self.__xxyy-self.conv(vct); return self
    def __imul__(self, vct): self.__xxyy = self.__xxyy*self.conv(vct); return self
    def __itruediv__(self, vct): self.__xxyy = self.__xxyy/self.conv(vct); return self
```
ベクトルの四則演算をより効果的にするために，演算子をオーバーライドします。
四則演算子について合計１４種類の機能をオーバーライドをしています。

****関数 __pos__( ), __neg__( ) ::**** 正負の符号  
GMVector のインスタンスの直前の符号 '+, -' がある場合に起動します。
ただし，優先度は以下で説明する四則演算より低くなります。
符号の正負に応じてself.__xxyy の符号を変更したものを引数として，
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

**[section_ma, section_mb, section_mb, section_mb]**  クラスGMVectorDの機能の紹介
```python
print('### --- section_main: (GMVectorD) main process --- ###')
## --- section_ma: functions for vector calculations --- ##
vecta = GMVectorD(xxyy=(5,3))  # creating instance
print('vecta:', vecta)
vectb = GMVectorD(xxyy=(2,1))  # creating instance
print('vectb:', vectb)

## --- section_mb: vector arithmetics --- ##
print('  ------  : vect = vecta.copy()')
vect = vecta.copy(); vect.add(2); print('vect.add(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.add((4,4)); print('vect.add((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.add(vectb); print('vect.add(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.sub(2); print('vect.sub(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.sub((4,4)); print('vect.sub((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.sub(vectb); print('vect.sub(vectb2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub(2); print('vect.rsub(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub((4,4)); print('vect.rsub((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub(vectb); print('vect.rsub(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.mul(2); print('vect.mul(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.mul((4,4)); print('vect.mul((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.mul(vectb); print('vect.mul(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.div(2); print('vect.div(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.div((4,4)); print('vect.div((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.div(vectb); print('vect.div(vectb2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv(2); print('vect.rdiv(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv((4,4)); print('vect.rdiv((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv(vectb); print('vect.rdiv(vectb2): ', f'{vect.xxyy() = }')

## --- section_mc: arithmetic operators --- ##
print('\n-- operators')
vect = vecta + 2; print('vect = vecta + 2: ', f'{vect.xxyy() = }')
vect = vecta + (4,4); print('vect = vecta + (4,4): ', f'{vect.xxyy() = }')
vect = vecta + vectb; print('vect = vecta + vectb: ', f'{vect.xxyy() = }')
vect = - vecta + 2; print('vect = - vecta + 2: ', f'{vect.xxyy() = }')
vect = - vecta + (4,4); print('vect = - vecta + (4,4): ', f'{vect.xxyy() = }')
vect = - vecta + vectb; print('vect = - vecta + vectb: ', f'{vect.xxyy() = }')
vect = 2 + vecta; print('vect = 2 + vecta: ', f'{vect.xxyy() = }')
vect = (4,4) + vecta; print('vect = (4,4) + vecta: ', f'{vect.xxyy() = }')
vect = vectb + vecta; print('vect = vectb + vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta - 2; print('vect = vecta - 2: ', f'{vect.xxyy() = }')
vect = vecta - (4,4); print('vect = vecta - (4,4): ', f'{vect.xxyy() = }')
vect = vecta - vectb; print('vect = vecta - vectb: ', f'{vect.xxyy() = }')
vect = - vecta - 2; print('vect = - vecta - 2: ', f'{vect.xxyy() = }')
vect = - vecta - (4,4); print('vect = - vecta - (4,4): ', f'{vect.xxyy() = }')
vect = - vecta - vectb; print('vect = - vecta - vectb: ', f'{vect.xxyy() = }')
vect = 2 - vecta; print('vect = 2 - vecta: ', f'{vect.xxyy() = }')
vect = (4,4) - vecta; print('vect = (4,4) - vecta: ', f'{vect.xxyy() = }')
vect = vectb - vecta; print('vect = vectb - vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta * 2; print('vect = vecta * 2: ', f'{vect.xxyy() = }')
vect = vecta * (4,4); print('vect = vecta * (4,4): ', f'{vect.xxyy() = }')
vect = vecta * vectb; print('vect = vecta * vectb: ', f'{vect.xxyy() = }')
vect = 2 * vecta; print('vect = 2 * vecta: ', f'{vect.xxyy() = }')
vect = (4,4) * vecta; print('vect = (4,4) * vecta: ', f'{vect.xxyy() = }')
vect = vectb * vecta; print('vect = vectb * vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta / 2; print('vect = vecta / 2: ', f'{vect.xxyy() = }')
vect = vecta / (4,4); print('vect = vecta / (4,4): ', f'{vect.xxyy() = }')
vect = vecta / vectb; print('vect = vecta / vectb: ', f'{vect.xxyy() = }')
vect = 2 / vecta; print('vect = 2 / vecta: ', f'{vect.xxyy() = }')
vect = (4,4) / vecta; print('vect = (4,4) / vecta: ', f'{vect.xxyy() = }')
vect = vectb / vecta; print('vect = vectb / vecta: ', f'{vect.xxyy() = }')

## --- section_md: cumulative assigment operators --- ##
print('\n-- cummulative assignment operators')
print('  ------  : vect = vecta.copy()')
vect = vecta.copy(); vect += 2; print('vect += 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect += (4,4); print('vect += (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect += vectb; print('vect += vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= 2; print('vect -= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= (4,4); print('vect -= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= vectb; print('vect -= vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= 2; print('vect *= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= (4,4); print('vect *= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= vectb; print('vect *= vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= 2; print('vect /= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= (4,4); print('vect /= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= vectb; print('vect /= vectb: ', f'{vect.xxyy() = }')
```
section_ma:
1. GMVectorD型の２つのインスタンス vecta と vectb を生成し以下で利用します。
2. 文字列関数を利用して，インスタンスの属性を表示します。

section_mb:  
3. 与えられた数値やベクトルに対して四則演算を行い，計算結果でインスタンス変数を更新します。

section_mc:  
4. オーバーライドした演算子によって四則演算します。
新たに作成されるGMVectorD型のインスタンスとして計算結果を返します。

section_md:  
5. オーバーライドした演算子によって，四則演算の結果を累積代入します。

