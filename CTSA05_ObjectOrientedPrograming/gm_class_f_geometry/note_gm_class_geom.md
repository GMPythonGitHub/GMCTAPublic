# **Note on gm_class_f_geom:** ***幾何学図形の操作と計算のためのクラス***

## 概要
ここでは幾何学における基本的な図形要素である，ベクトル，座標点，位置ベクトル，線分，多角形を取り上げ，
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
> 「始点を有するベクトル」の属性を有し，関連する幾何学計算機能を備えているクラスです。  
> 親クラス： GMVector
>> インスタンス変数： self._vect: GMVector  
> 初期化関数 \_\_init\_\_(xxyy, rrth, unit, cnv, deg)  
> Setting関数 set_point()  
> Getting関数 copy()  
> 文字列関数 \_\_str\_\_(), classprop()  
> インスタンス関数  
> vect_p2pint(), dist_p2pint(), dirc_p2pint(), unitvect_p2pint()  # point properties  
> inner_op_vect(), outer_op_vect(), cross_op_vect()  # vector analysis  


---

## [GMVectorA: gm_class_vector_a.py](gm_class_vector_a.py)

ここで紹介する最初のクラスGMVecotrAでは，ベクトルの成分をインスタンス変数として内蔵し，
ベクトルの長さと方位角，単位ベクトルを計算する機能を有しています。

### **[section_module]**  
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
```python
 print('### --- section_module: (GMVectorA) importing items from module --- ###')
 from numpy import(
     square as sq, sqrt as sr, arctan2 as atan2, rad2deg as r2d)
```
関数atan2()は座標点の方向角を計算する関数で，y成分とx成分の両方を引数として渡すことで，全方位の角度を戻り値としてradianで返します。
また，関数r2d()は角度の単位系をradianからdegreeに，関数d2rはdegreeからradianに変換します。

### **[section_class]**
クラスが内蔵するインスタンス変数とインスタンス関数を記述しています。  

**［section_ca］**  クラスGMVectorAでインスタンスを作成するときに起動する，初期化関数__init__()を記述しています。
```python
print('### --- section_class: (GMVectorA) describing class --- ###')
class GMVectorA():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
        xx: float = None, yy: float = None) -> None:
        self.__xx, self.__yy = 1, 1
        self.set_xxyy(xx=xx, yy=yy)
```
最初に，インスタンス変数self.__xxとself.__yyを(1,1)で初期化します。
その後，セッティング関数set_xxyy()を用いてインスタンス変数を引数xxとyyでで更新します。  

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

---

## [GMVectorB: gm_class_vector_b.py](gm_class_vector_b.py)

直行座標系のみならず円座標系でもベクトルを記述できるように，先に紹介したクラスGMVecotrAを更新しています。
具体的には，インスタンス変数を初期化，参照または更新するときに，
必要に応じて直交座標系と円座標系を選択できるようにしています。
インスタンス関数が引数を受取り，戻り値を返すときにも同様に，座標系を選択できます。  
以下では，変更箇所を中心に説明します。

### **[section_module]**  
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
```python
print('### --- section_module: (GMVectorB) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
def gmsrsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```
三角関数cos()とsin()を関数atan2()を追加でimportしています。
さらに，クラス関数として２つの関数を新たに定義しています。
－ 関数gmsrsq()は２つの引数の２乗和の平方根を返します。
－ 関数gmatan2()はベクトルのy成分とx成分を受か取り，方位角を返します。
デフォルトのbool値がFalseである単位系フラグdegをTrueに変更すると，単位系をdegreeに指定できます。

### **[section_class]**

**［section_ca］**  初期化関数__init__()を記述しています。
```python
print('### --- section_class: (GMVectorB) describing class --- ###')
class GMVectorB():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xx: float = None, yy: float = None,
            rr: float = None, th: float = None, deg: bool = True) -> None:
        self.__xx, self.__yy = 1, 1  # instance variables
        self.set_vect(xx=xx, yy=yy, rr=rr, th=th, deg=deg)
```
クラスが内蔵するインスタンス変数は直交座標系における２成分で，前のクラスGMVectorAから変更ありません。
ただし，この初期関数__init__()は，直交座標系におけるベクトル成分xxとyyに加えて，
円座標系における半径rrと方位角th，角度の単位系を指定するフラグdegを引数としています。  
最初に，インスタンス変数を(1,1)で初期化し，その後，Setting関数set_vect()を用いて，インスタンス変数を更新します。

**［section_cb］**  インスタンス関数として，Setting関数set_vect()とGetting関数xxyy(), rrth()を記述しています。
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
－ Setting関数set_vect ()では，
直交座標系と円座標系のどちらかを指定してインスタンス変数 self.__xxとself.__yyを変更することが可能です。
デフォルト値がNoneに設定されている４つの引数xxとyy（直交座標系），rrとth（円座標系）から所定のものを選択して数値を渡すことにより，
その引数の種類に応じて直交座標系か円座標系を指定して，インスタンス変数を初期化することができます。
デフォルトのbool値がFalseである単位系フラグdegをTrueに変更すると，単位系をdegreeに指定できます。  
－ Getting関数xxyy()では，
インスタンス変数self.__xxとself.__yyをtuple型で返すことで直交座標系における参照を可能にします。
一方，Getting関数rrth()では，
インスタンス変数から換算した円座標系における半径rrと方位角thをtuple型で返します。
ここでも，単位系フラグdegをTrueに変更することで，単位系をdegreeに指定できます。

**［section_cc］**  ベクトルの属性に，円座標系における成分rrとthを追加しています。
```python
    ## --- section_cd: string function for print() --- ##
    def __str__(self) -> str:
        rr, th = self.rrth(True)
        return (
            f'(GMVectorB): xx = {self.__xx:g}, yy = {self.__yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
```

**［section_cd］**  大きな変更はありませんが，計算過程でGetting関数rrth()を活用しています。
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

### **[section_main]**

**［section_ma］**  
```python
print('### --- section_main: (GMVectorB) main process --- ###')
## --- section_ma: calculating vectors --- ##
vect = GMVectorB(4, 3)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
vect.set_vect(xx=5, yy=5)  # setting instance valuables
print(vect, f'\n{vect.unitvect() = }')
vect.set_vect(rr=4., th=30., deg=True)  # setting instance valuables
print(vect, f'\n{vect.unitvect() = }')
```
最初に，クラスGMVectorBのインスタンスvectを生成し,インスタンス変数の初期値を(4,3)と指定します。
その後，Setting関数set_vect()を用いて，
直交座標系における(xx=5,y=5)と円座標系における(rr=4, th=30, deg=True)にインスタンス変数をと更新します。
それぞれに対して，クラス属性と単位ベクトルを関数print()で表示します。

---

## [GMVectorC: gm_class_vector_c.py](gm_class_vector_c.py)

拡張モジュールnumpyを導入して数値計算をより効率的に行うために，
先に紹介したクラスGMVecotrBを変更しています。
具体的には，インスタンス変数であるベクトル成分をnumpyが提供するndarray型で表し，
それに対応してクラスが内蔵するインスタンス関数を変更しています。
さらに，numpyが提供する関数を導入してベクトル解析の機能を強化しています。  
以下では，変更箇所を中心に説明します。

### **[section_module]**  
クラスが利用する関数を，拡張モジュールnumpyからimportしています。  
```python
print('### --- section_module: (GMVectorC) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)
def gmsrsq(xx, yy) -> float: return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False) -> float:
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```
多次元配列を操作することが可能なndarrayを導入するために，ndarrayとarrayをインポートしています。
さらに，ベクトル計算を効率よく行うために，３つの関数をインポートしています。  
－ 関数inner()は２つのベクトルの内積（またはドット積）を計算します。
他の関数numpy.dot()は多次元配列（マトリックス）に対しても同様な計算を行うことが可能です。  
－ 関数outer()は２つのベクトルの外積（まはたテンソル積）を計算します。
多次元配列を含む計算には他の関数numpy.tenordot()を利用することができます。
用語が乱れていて，高校数学の範囲で用いられる「外積」は次に示す「クロス積」にあたります。  
－ 関数numpy.cross()は2つのベクトルのクロス積（ベクトル積）を計算します。

### **[section_class]**

**［section_ca］**  クラスGMVectorCでインスタンスを作成するときに起動する，初期化関数__init__()を記述しています。
```python
print('### --- section_class: (GMVectorC) describing class --- ###')
class GMVectorC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        self.__xxyy = array([1, 1])
        self.set_vect(xxyy=xxyy, rrth=rrth, deg=deg)
```
クラスが内蔵するインスタンス変数self.__ xxyyは，
直交座標系における２成分（x,y）で構成するndarray型です。
初期化関数__init__()は，引数として直交座標系におけるベクトル成分からなるxxyyと
円座標系におけるベクトル成分からなるrrthをndarray型で受け取ります。
他に，方位角の単位系フラグdegをbool型で受け取ります。  
この関数では，最初にインスタンス変数をndarray([1,1])で初期化し，その後，Setting関数set_vect()を用いてインスタンス変数を更新します。

**［section_cb］**  インスタンス関数として，
Setting関数set_vect()とGetting関数xxyy(), rrth()を定義しています。ndarrayに適応した簡潔な表現に変更しています。
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
－ Setting関数set_vect ()では，返す文字列に変更はありません。
ndarrayに適応した記述にしています。
引数xxyyとrrthの型はndarrayに限定せず，他のリスト構造（list, tuple）でも受け入れ可能です。
－ Getting関数xxyy()では，
インスタンス変数self.__xxyyをndarray型として返します。
一方，Getting関数rrth()では，
インスタンス変数self.__xxyyから換算した円座標系における半径rrと方位角thをndarray型として返します。

**［section_cc］**  文字列関数に大きな変更はありませんが，ndarrayに適応した記述にしています。
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorC): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
```

**［section_cd］** 以下のインスタンス関数には大きに変更はありませんが，ndarrayに適応した簡潔な記述にしています。
```python
    ## --- section_ce: functions for properties --- ##
    def leng(self) -> float:
        return self.rrth()[0]
    def dirc(self, deg: bool = False) -> float:
        return self.rrth(deg=deg)[1]
    def unitvect(self) -> ndarray:
        return self.__xxyy / self.leng()
```

**［section_cd］**  numpyが提供する以下の３つの関数を追加しています。
それぞれ，２つのベクトルの内積，外積，クロス積を計算します。
```python
    ## --- section_ce: functions for vector analysis --- ##
    def inner(self, vect: object) -> float:
        return inner(self.__xxyy, vect.xxyy())
    def outer(self, vect: object) -> ndarray:
        return outer(self.__xxyy, vect.xxyy())
    def cross(self, vect: object) -> float:
        return float(cross(self.__xxyy, vect.xxyy()))
```

### **[section_main]**

**［section_ma］**  
```python
print('### --- section_main: (GMVectorC) main process --- ###')
## --- section_ma: calculating vectors --- ##
vecta = GMVectorC(xxyy=(3.,4.))  # creating instance
print('vecta:', vecta)
vectb = GMVectorC(xxyy=(-4.,3.))  # creating instance
print('vectb:', vectb)
print(f'{vecta.inner(vectb) = }')
print(f'{vecta.outer(vectb) = }')
print(f'{vecta.cross(vectb) = }')
print(f'{vectb.inner(vecta) = }')
print(f'{vectb.outer(vecta) = }')
print(f'{vectb.cross(vecta) = }')
```
最初に，クラスGMVectorCの２つのインスタンスvectaとvectbを生成します。
それら2つのベクトルの内積と外積，クロス積を順に計算して表示します。

---

## [GMVectorD: gm_class_vector_d.py](gm_class_vector_d.py)

ベクトルの演算をより効果的に行うために，先に紹介したクラスGMVecotrCを変更しています。
具体的には，ベクトルの四則演算を簡潔に実施するために，２つのグループのインスタンス変数を追加しています。
以下では，変更箇所のみを説明します。

### **[section_module]**  
拡張モジュールnumpyからimportする関数には変更ありませんが，
インスタンスを複製するために必要な拡張モジュールcopyを追加してimportしています。  
```python
print('### --- section_module: (GMVectorD) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)
import copy
def gmsrsq(xx, yy): return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False):
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht
```

### **[section_class]**

**［section_ca］**  初期化関数__init__()には変更ありません。

**［section_cb］**  Getting関数copy()を追加しています。
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
－ Getting関数copy()では，拡張モジュールcopyが提供する関数deepcopy()を利用しています。
これにより，完全に独立したインスタンスの複製を返します。

**［section_cc］**  文字列関数には変更ありません。

**［section_cd］** ベクトルの特性を返すインスタンス関数には変更ありません。

**［section_ce］**  ベクトル解析の結果を返すインスタンス関数には変更ありません。

**［section_cf］**  ベクトルの四則演算を可能にするインスタンス関数のグループを追加しています。
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

**［section_cd］**  ベクトルの四則演算を可能にするように，演算子を更新している。
```python
    ## --- section_cg: functions for vector operator --- ##
    # sign operators
    def __pos__(self): return GMVectorD(xxyy=+self.__xxyy)
    def __neg__(self): return GMVectorD(xxyy=-self.__xxyy)
    # arismetic operaters
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
最初の２つはインスタン直前に置かれた符号演算子に対応する関数です。
続く８個は四則計算の演算子に対応する関数です。
末尾の４個は累算代入演算子に対応する関数です。

### **[section_main]**

**［section_ma］**  
```python
print('### --- section_main: (GMVectorD) main process --- ###')
## --- section_ma: functions for vector calculations --- ##
vecta = GMVectorD(xxyy=(5,3))  # creating instance
print('vecta:', vecta)
vectb = GMVectorD(xxyy=(2,1))  # creating instance
print('vectb:', vectb)

print('\n-- functions')
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

## --- section_mb: operators for vector calculation --- ##
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

print('\n-- cumulative assigment operator')
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
四則演算のための，２グループのインスタンス関数の利用例を示している。
