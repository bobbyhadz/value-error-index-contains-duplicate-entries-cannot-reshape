# ValueError: Index contains duplicate entries, cannot reshape

import pandas as pd

df = pd.DataFrame({
    'id': [1, 1, 2, 2, 3, 3],
    'name': ['Alice', 'Alice', 'Bob', 'Bob', 'Carl', 'Carl'],
    'salary': [100, 200, 300, 400, 500, 600]
})

#    id   name  salary
# 0   1  Alice     100
# 1   1  Alice     200
# 2   2    Bob     300
# 3   2    Bob     400
# 4   3   Carl     500
# 5   3   Carl     600
print(df)