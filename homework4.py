immutable_var = (1, 34, 3.5, 'YES', 'no', True, False)
print(immutable_var)
# immutable_var[2] = 'cool' # кортеж не поддерживает изменении он используется как неизменяемое хранилище
mutable_list = [24, 0.7, "God", 'war', True, False]
print(mutable_list)
mutable_list[-2]= False
mutable_list[2]= 'Good'
print(mutable_list)