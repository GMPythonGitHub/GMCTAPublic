# **Note on matrix equation: Type B; vector $B$ is given**

## 行列方程式の解法
ここでは，左辺のベクトル $X$ が未知である，２つの行列方程式を考えます。

![](_img/gm_matrix_equation_type_b1.gif)

![](_img/gm_matrix_equation_type_b2.gif)


「右辺のベクトル $B$ のすべての要素が既知である」という条件で左辺のベクトル $X$ を求めます。  
ここでは，「掃き出し法（ガウスの消去法）」を採用します。
他には，「LU分解法」，逆行列を活用する「クラメルの解法」などが知られています。
必要に応じてピボッティング(行の入れ替え)を行いながら，
行基本変形のみを行うことによって $A$ と $B$ を変換して簡略化し，最終的に $X$ を求めます。
行列方程式における３種類の行基本変形とは以下のようです。

> 1. ある行を c 倍する。
> 2. ある行の c 倍を他の行に加える
> 3. ある２つの行を入れ替える

具体的な解法は以下のようです。

- Type-B1  
行列方程式の初期状態は次のようです。

![](_img/gm_matrix_equation_sol_type_b1a.gif)

【前方消去，行列の左下を消去する】  
「2 行目に 1行目の-1倍を加える」 「3 行目に 1行目の-1倍を加える」 「4 行目から 1行目の-1倍を加える」  
【後方代入， $A$ を対角行列化する】  
「1 行目に 4行目の-1/3倍を加える」 「1行目に 3行目の-1/2倍を加える」 「1行目に 2行目の-1倍を加える」

![](_img/gm_matrix_equation_sol_type_b1b.gif)

【正規化，行列を単位行列化する】  
「3行目を1/2倍する」 「4行目を1/3倍する」

![](_img/gm_matrix_equation_sol_type_b1c.gif)

- Type-B2  
行列方程式の初期状態は次のようです。

![](_img/gm_matrix_equation_sol_type_b2a.gif)

【前方消去，2行目を処理する】  
「2 行目に 1行目の-1倍を加える」 「3 行目に 1行目の-1倍を加える」 「4 行目に 1行目の-4倍を加える」  
【行の入替え，2行2列目がゼロになるのを避け，2列目で絶対値が最大の4行目と2行目を入れ替える】  
「2行目と4行目を入れ替える」

![](_img/gm_matrix_equation_sol_type_b2b.gif)

【前方消去，3行目を処理する】  
「3 行目に 2行目の2/3倍を加える」  
【前方消去，4行目を処理する】  
「4 行目に 3行目の1/2倍を加える」  

![](_img/gm_matrix_equation_sol_type_b2c.gif)

【後方代入， $A$ を対角行列化する】  
「3行目に 4行目の-2倍を加える」 「2行目に 4行目の-3/2倍を加える」 「1行目に 4行目を加える」  
「2行目に 3行目の-3/2倍を加える」 「1行目に 3行目の-1/2倍を加える」  
「1行目に 2行目の1/3倍を加える」  
【正規化・行列を単位行列化する】  
「4行目を-1倍する」 「3行目を-1/2倍する」 「2行目を-1/3倍する」

![](_img/gm_matrix_equation_sol_type_b2d.gif)


---

## プログラミング演習

この演習では，以下に示すでは３つの方針で作成するプログラムを紹介して解説します。

> [gm_matrix_equation_b0_xx_list.py](gm_matrix_equation_b0_xx_list.py)  
> リスト構造（listとtuple）を用いて行列方程式を記述します。
> for-loopを活用した「掃き出し法」による計算で，$B$ を求めます。
> 
> [gm_matrix_equation_b1_xx_array.py](gm_matrix_equation_b1_xx_array.py)  
> 拡張モジュールnumpyが提供するndarrayを用いて行列方程式を記述し，
> for-loopを活用した「掃き出し法」による計算によりベクトル $B$ を求めます。
> リスト構造を用いる場合と比較して，計算過程を簡潔にできます。
> 
> [gm_matrix_equation_b2_xx_array_func.py](gm_matrix_equation_b2_xx_array_func.py)  
> ndarrayを用いて行列方程式を記述し，「掃き出し法」による計算によりベクトル $B$ を求めます。
> nyupyが提供する行列方程式を解くための関数を活用することにより，
> プログラムの記述を簡略にしています。
> 

---

### [gm_matrix_equation_b0_xx_list.py](gm_matrix_equation_b0_xx_list.py)

### **[section_setting]**
マトリックス $aa$と，左辺ベクトル $xx$，右辺ベクトル $bb$ をlistで記述します。
```python
print('\n*** Matrix Equation with list: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
import copy

# =========================================================
print('### --- section_setting --- ###')
aa1 = [ [1, 1, 1, 1], [1, 2, 1, 1],
        [1, 1, 3, 1], [1, 1, 1, 4] ]
bb1 = [10, 12, 16, 22]
aa2 = [ [1, 1, 1, 1], [1, 1, 2, 1],
        [1, 3, 1, 1], [4, 1, 1, 1] ]
bb2 = [10, 13, 14, 13]
xx = [None, None, None, None]

aa, bb = aa1, bb1
rank = len(bb)
```
２つのマトリックス $A$ とベクトル $B$ を用意することによって２種類の行列方程式を扱います。
マトリックスの切り替えは， aa = aa1 の記述を変更することによって可能です。

### **[section_solving]**
「掃き出し法」により，解を求めます。
```python
print('### --- section_solving --- ###')
aa_wk = copy.deepcopy(aa)
bb_wk = copy.deepcopy(bb)
# forward elimination with pivoting
for i in range(rank):
    for j in range(i+1,rank):  # pivoting partial
        if abs(aa_wk[i][i]) < abs(aa_wk[j][i]):
            for k in range(i,rank):
                aa_wk[i][k], aa_wk[j][k] = aa_wk[j][k], aa_wk[i][k]
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank):  # eliminating
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
for i in range(rank):
    xx[i] = bb_wk[i] / aa_wk[i][i]
print(f'{aa = }\n{xx = }\n{bb = }')
```
一連の計算は，順に「前方掃出し」「後方代入」，「正規化」の３過程からなっています。
マトリックス $aa$ とベクトル $bb$ を変形して簡略化し，
最終的にベクトル $xx$ を求めます。

---

### [gm_matrix_equation_a1_bb_array.py](gm_matrix_equation_a1_bb_array.py)

### **[section_setting]**
マトリックス $aa$ と左辺ベクトル $xx$ ，右辺ベクトル $bb$ をndarrayで記述します。
```python
print('\n*** Matrix Equation with array: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import (array, diag)
import copy

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
bb1 = (10, 12, 16, 22)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
bb2 = (10, 13, 14, 13)
xx = [None, None, None, None]

aa = array(aa1, dtype='float64')
xx = array(xx, dtype='float64')
bb = array(bb1, dtype='float64')
rank = len(bb)
```
関数array()はlistやtupleをndarrayへ変換します。

### **[section_solving]**
マトリックス $aa$ とベクトル $xx$ の積（ドット積）を計算しています。
```python
print('### --- section_solving --- ###')
aa_wk = copy.deepcopy(aa)
bb_wk = copy.deepcopy(bb)
# forward elimination with pivoting
for i in range(rank):
    for j in range(i+1,rank):  # pivoting partial
        if abs(aa_wk[i,i]) < abs(aa_wk[j,i]):
            aa_wk[i,i:], aa_wk[j,i:] = aa_wk[j,i:], copy.copy(aa_wk[i,i:])
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank):  # eliminating
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
xx = bb_wk / diag(aa_wk)
print(f'{aa = }\n{xx = }\n{bb = }')
```
前のプログラムと同様に，計算は順に「前方掃出し」「後方代入」，「正規化」の３過程で行います。
マトリックス $aa$ とベクトル $bb$ を変形して簡略化し，
最終的にベクトル $xx$ を求めます。
ndarrayの計算機能を生かし，
listを用いる場合と比べてプログラムをより簡潔に記述できます。

---

### [gm_matrix_equation_b2_xx_array_func.py](gm_matrix_equation_b2_xx_array_func.py)

### **[section_setting]**
前のプログラムと同様に，行列方程式をndarrayで記述しています。
```python
print('\n*** Matrix Equation with array func: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import (array, linalg)

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
bb1 = (10, 12, 16, 22)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
bb2 = (10, 13, 14, 13)
xx = [None, None, None, None]

aa = array(aa1, dtype='float64')
xx = array(xx, dtype='float64')
bb = array(bb1, dtype='float64')
```
関数array()はlistとtupleをndarrayへ変換します。

### **[section_solving]**
マトリックス $aa$ とベクトル $xx$ の積（ドット積）を計算しています。
```python
print('### --- section_solving --- ###')
xx = linalg.solve(aa, bb)  # solving equation
print(f'{aa = }\n{xx = }\n{bb = }')
```
行列方程式を解くのに，numpyが提供する関数linalg.solve()を用います。
















