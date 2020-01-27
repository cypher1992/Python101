# Flow Control with If/ElIf/Else


industry = 'automobile'
jp = 'Japan'
usa = 'United States'
legacy = 'Legacy'

honda = 'Honda'
toyota = 'Toyota'
ford = 'Ford'
pontiac = 'Pontiac'

input = ['automobile','United States']

if input[0] == 'automobile':
    if input[1] == 'Japan':
        output = [honda,toyota]
    elif input[1] == 'United States':
        output = [ford]
    else:
        output = [pontiac]


print(output)