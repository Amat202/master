from time import perf_counter as pfc     #as dc dung nhu ham thay the
start_time=pfc()                         # thay the perf_counter=pfc
input('Moi nhap bat ki:')
elapsed=pfc()-start_time
print('Tgian ban dung:',elapsed,'giay')
