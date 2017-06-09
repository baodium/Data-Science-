from random import random
sample_size = 0.25
with open("Colors.txt", 'r') as open_file:
    for j, observation in enumerate(open_file):
        if(random() <= sample_size):
            print('Reading Line: '+ str(j) + 'Content: ' + observation)
