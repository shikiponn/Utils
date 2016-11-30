# Utils ユーティリティ
## Time function 関数の実行時間計測

### Usage  
Import timethis.py and put decorater "@timethis" in front of a function you want to time. Or wrap the fuction object with timethis function.  

### 使い方  
timeshis.pyをインポートしたら。"@timethis"というデコレータを関数の前につけてください。もしくは関数をtimethis()に渡してあげてください。

### Example1  
code コード
```python
@timethis
def counter():
    c = 0
    for i in range(10000000):
        c+=1
    print(c)
    
counter()

```

### Example2  
code コード
```python
def counter():
    c = 0
    for i in range(10000000):
        c+=1
    print(c)
    
counter = timethis(counter)
counter()
```

output 出力
>--start wrapper --  
>10000000  
>elapsed_time:elapsed_time:0.915 [sec]
>--end--  
