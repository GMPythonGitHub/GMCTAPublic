# **Note on gm_class_d_numbers:** ***２変数の操作と計算のためのクラス***

## 概要
ここでは２つの数値型の変数を有するクラスを紹介します。
基本的なクラスから始め，これを段階的に更新することによってクラスの機能を強化していきます。

各クラスの構成は以下のようです。

> [GMNumbersA: gm_class_numbers_a.py](gm_class_numbers_a.py)  :: インスタンス変数  
> インスタンス変数と初期化関数だけが所属する，基本的なクラスです  
>> インスタンス変数： aa, bb   
> 初期化関数 _\_init\_\_( )  
> 
> [GMNumbersB: gm_class_numbers_b.py](gm_class_numbers_b.py)  :: インスタンス関数  
> インスタンス変数に加えて，幾つかのインスタンス関数も所属するクラスです。  
>> インスタンス変数： aa, bb  
> 初期化関数 _\_init\_\_( )  
> インスタンス関数 add( ), sub( ), calc( )  
> 
> [GMNumbersC: gm_class_numbers_c.py](gm_class_numbers_c.py) :: privateなインスタンス変数  
> インスタンス変数を prive に設定し，Setting関数とGettinng関数を導入しています。  
>> インスタンス変数： _\_aa, _\_bb  
> 初期化関数 _\_init\_\_(aa, bb)  
> Setting関数 set_aabb( )， Getting関数 aa( ), bb( )  
> インスタンス関数 calc( )  
> 
> [GMNumbersD: gm_class_numbers_d.py](gm_class_numbers_d.py)  :: 文字列関数  
> 文字列関数を導入し，関数print( )でクラスの属性を表示できるようにしています。  
>> インスタンス変数： _\_aa, _\_bb  
> 初期化関数 _\_init\_\_(aa, bb) 
> Setting関数 set_aabb( )， Getting関数 aa( ), bb( )  
> 文字列関数 _\_str\_\_( ) 
> インスタンス関数 calc( )  


---

## [GMNumbersA: gm_class_numbers_a.py](gm_class_numbers_a.py)

紹介するクラスGMNumbersAは基本的なもので，
2つの数値型変数がインスタンス変数として所属しています。初期化関数を導入しています。

### **[section_class]**  クラスの定義と記述
クラスが所属するインスタンス変数とインスタンス関数を定義し，記述しています。  

**[section_ca]**  初期化関数  
```python
print('### --- section_class: (GMNumbersA) describing class --- ###')
class GMNumbersA():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables
```
****初期化関数 __init__( ) ::**** クラスGMVectorA型のインスタンスを作成するときに
自動的に起動します。
インスタンス変数 self.aa と self.bb をNoneで初期化します。
これによって，２つのインスタンス変数が定義され，
インスタンスに所属することになります。

### **[section_main]**  メインセクション
クラスの機能を紹介し，パフォーマンスをチェックすることを目的として，
基本的なプログラムを記述しています。

**[section_ma, section_mb]**  クラスGMVectorAの機能の紹介
```python
print('### --- section_main: (GMMumbersA) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersA()  # creating instance
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.aa, numbs.bb = 7, 3  # setting instance variables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = (  # using instance variables
    numbs.aa + numbs.bb, numbs.aa - numbs.bb )
print(f'{add = }, {sub = }\n')
```
section_ma:  
1. クラスGMVectorAのインスタンスnumbsを生成します。
2. インスタンス変数 self.aa と self.bb を数値(aa=3, bb=4)に更新し，表示します。
3. インスタンス関数culc( )が返す self.aa と self.bb の和と差を表示します。  
 
section_mb:  
4. self.aa と self.bb を(aa=7, bb=3)に変更し，同様な操作を繰返します。

インスタンス変数を更新または参照するときは，
インスタンス名に続けて，ピリオドと変数名を記述します。  


---

## [GMNumbersB: gm_class_numbers_b.py](gm_class_numbers_b.py)

先に紹介したクラスGMNumbersAを更新し，クラスに演算する機能を追加しています。
そのために，３つのインスタンス変数を用意しています。

### **[section_class]**  クラスの定義と記述

**[section_ca]**  初期化関数
```python
print('### --- section_class: (GMNumbersB) describing class --- ###')
class GMNumbersB():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self) -> None:
        self.aa, self.bb = None, None  # instance variables
```
****初期化関数 __init__( ) ::****  変更はありません。

**[section_cb]**  四則演算
```python
    ## --- section_cb: functions for arithmetics --- ##
    def add(self) -> float: return self.aa + self.bb
    def sub(self) -> float: return self.aa - self.bb
    def calc(self) -> tuple:
        return self.add(), self.sub()
```
２数の四則演算をするために，３つの関数を用意しています。  
****関数 add( ) ::**** self.aaとself.bbの和を計算して返します。  
****関数 sub( ) ::**** self.aaとself.bbの差を計算して返します。  
****関数 calc( ) ::**** 関数add( )と関数sub( )を利用して，
self.aa と self.bb の和と差を一緒にtuple型で返します。


### **[section_main]**  メインセクション
クラス内で演算を行えるように機能を強化したので，クラスの新たな機能を紹介します。

**[section_ma, section_mb]**  クラスの機能の紹介
```python
print('### --- section_main: (GMMumbersB) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersB()  # creating instance
numbs.aa, numbs.bb = 3, 2
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.aa, numbs.bb = 7, 3  # setting instance valuables
print(f'{numbs.aa = }, {numbs.bb = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
section_ma:  
1. クラスGMVectorBのインスタンスnumbsを生成します。
2. インスタンス変数 self.aa と self.bb を数値(aa=3, bb=4)に更新し，表示します。
3. インスタンス関数culc( )が返す self.aa と self.bb の和と差を表示します。  

section_mb:  
4. self.aa と self.bb を(aa=7, bb=3)に変更し，同様な操作を繰返します。


---

## [GMNumbersC: gm_class_numbers_c.py](gm_class_numbers_c.py)

クラスにおけるカプセル化を実現するために，先に紹介したクラスGMNumbersBを変更しています。
インスタンス変数の特性をprivateに変更することで，
インスタンスの参照と変更といったアクセスを厳密に制御します。  
以下では，変更箇所を中心に説明します。


### **[section_class]**  クラスの定義と記述

**[section_ca]**  初期化関数
```python
class GMNumbersC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self, aa, bb) -> None:
        self.__aa, self.__bb = None, None  # private instance variables
        self.set_aabb(aa, bb)
```
****初期化関数 __init__( ) ::**** privateになったインスタンス変数に適用するように更新しています。
初期化関数が２つの引数aaとbbを受け取るように更新しています。
1. インスタンス関数は名前を変更して self.__aa と self.__bb とします。
名前の前にアンダースコアを２つ付けることにより，変数の特性がprivateになります。
これにより，クラスの外からは変数を参照することも更新することも直接にはできません。
2. self.__aa と self.__bb をNoneで初期化します。
3. 次で説明するSetting関数set_aabb( )に引数 aa, bb を渡すことにより，
self.__aa と self.__bb を更新します。


**[section_cb]**  Setting関数とGetting関数
```python
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_aabb(self, aa: float = None, bb: float = None) -> None:
        if aa is not None: self.__aa = aa
        if bb is not None: self.__bb = bb
    ## getting functions
    def aa(self) -> float: return self.__aa
    def bb(self) -> float: return self.__bb
```
****Setting関数 set_aabb( ) ::****  引数 aaとbbで，インスタンス変数self.__aaとself.__bbを更新します。
ここでは，引数aaとbbのデフォルト値をNoneに設定しています。
具体的な数値を渡すことにより，インスタンス変数 self.__aa と self.__bb の両方，
あるいはどちらか一方選択して更新します。
この関数を介してのみ，privateなインスタンス変数を更新できます。

****Getting関数 aa( ), bb( ) ::****  関数aa( )とbb( )がそれぞれ self.__aa と self.__bb を返します。
これらの関数を用いてのみ，privateなインスタンス変数を参照できます。


**[section_cc]** 四則演算
```python
    ## --- section_cc: functions for arithmetics --- ##
    def calc(self) -> tuple:
        return self.__aa + self.__bb, self.__aa - self.__bb
```
２数の四則演算をするために関数を用意しています。  
****関数 calc( ) ::****  インスタンス変数 self.__aa と self.__bb の和と差を計算し，
tuple型で返します。


### **[section_main]**  クラスGMNumbersCの機能の紹介
```python
print('### --- section_main: (GMMumbersC) main process --- ###')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersC(3, 2)  # creating instance
# print(f'{numbs.__aa = }, {numbs.__bb = }, ')
# AttributeError: 'GMNumbersC' object has no attribute '__aa'
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(f'{numbs.aa() = }, {numbs.bb() = }')
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
section_ma:
1. 初期値を(aa=3, bb=2)としてクラスGMVectorAのインスタンスnumbsを生成します。
2. インスタンス変数 self.__aa と self.__bb を直接参照することはできません
（エラーになります）。参照するにはGetting関数aa( )とbb( )を利用します。
3. インスタンス関数culc( )が返す self.__aa と self.__bb の和と差を表示します。

section_mb:
4. Setting関数 set_aabb( )を用いて
self.__aa と self.__bb を(aa=7, bb=3)に変更し，同様な操作を繰返します。



---

## [GMNumbersD: gm_class_numbers_d.py](gm_class_numbers_d.py)

クラスインスタンスの属性の表示を簡潔にするために，
文字列関数を導入してGMNumbersを変更しています。
以下では，変更箇所のみを説明します。


### **[section_class]**  クラスの定義と記述

**[section_ca]**  初期化関数  :: 変更はありません。


**[section_cb]**  Setting関数とGetting関数  :: 変更はありません


**[section_cc]**  文字列関数  
```python
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMNumbersD): aa = {self.__aa:g}, bb = {self.__bb:g}'
```
****文字列関数 __str__( ) ::****  インスタンスの属性を記述する文字列を作成して返します。  
この関数は，関数print()でインスタンス名を渡すと自動的に起動します，
インスタンスの属性（クラス名とインスタンス変数などを）を記述する文字列をf-string型で作成して返します。


**[section_cd]**  四則演算  :: 変更はありません 


### **[section_main]**  メインセクション

**[section_ma, section_mb]**  クラスGMNumbersDの機能の紹介
```python
print('## --- section_main: (GMMumbersD) main process --- ##')
## --- section_ma: calculating arithmetics --- ##
numbs = GMNumbersD(3, 2)  # creating instance
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }')
## --- section_mb: calculating arithmetics --- ##
numbs.set_aabb(aa=7, bb=3)  # setting instance variables
print(numbs)
add, sub = numbs.calc()  # using instance functions
print(f'{add = }, {sub = }\n')
```
section_ma:  
1. クラスGMVectorAのインスタンスnumbsを生成します。
2. インスタンス変数 self.__aa と self.__bb を数値(aa=3, bb=4)に更新します。
self.__aa と self.__bb を直接参照，変更することはできません（エラーになります）。
参照するにはインスタンス関数aa( )とbb( )を利用します。
3. インスタンス関数culc( )が返す self.__aa と self.__bb の和と差を表示します。  

section_mb:  
4. インスタンス関数 set_aabb( )を用いて
self.__aa と self.__bb を(aa=7, bb=3)に変更し，同様な操作を繰返します。

