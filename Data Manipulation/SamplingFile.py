n = 2
with open('Colors.txt','r') as open_file:
    for j, observation in enumerate(open_file):
        if j%n ==0:
            print('Reading Line: '+ str(j) + 'Content: '+ observation)
