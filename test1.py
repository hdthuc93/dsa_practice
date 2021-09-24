txt = 'ball area read lady'
arr = txt.split(' ')
arr_str = [['']*500 for i in range(500)]

for i, w in enumerate(arr):
    for j, c in enumerate(w):
        arr_str[i][j] = c

print(arr_str[:4][:1])
for i, w in enumerate(arr):
    col_w = ''.join([arr_str[j][i] for j in range(500)])
    print(w, col_w)
    if w != col_w:
        print('False')

print("done")
