# Utils ユーティリティ
## Time function 関数の実行時間計測

### Usage  
Put decorater "@timethis" in front of the function you want to time.  

### 使い方  
"@timethis"というデコレータを関数の前につけてください。

### Example  
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

output 出力
>--start wrapper --  
>10000000  
>elapsed_time:elapsed_time:0.915 [sec]
>--end--  
