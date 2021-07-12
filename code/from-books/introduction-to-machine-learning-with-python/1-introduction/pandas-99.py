import pandas as pd

df = pd.DataFrame([range(40)], columns=['ABCDE%d' % i for i in range(40)])

print(df) # this is with default 'display.width' of 80
