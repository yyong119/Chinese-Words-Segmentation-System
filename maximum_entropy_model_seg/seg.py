# -*- coding: UTF-8 -*-
import pickle

def seg(sentense):
    in_pkl_file = open('matrix.pkl', 'rb')
    transition_matrix = pickle.load(in_pkl_file)
    confusion_matrix = pickle.load(in_pkl_file)
    in_pkl_file.close()
    #pi maybe more accurate if use 'B'/all and 'S'/all
    pi = {'B':0.5,'E':0,'M':0,'S':0.5}
    delta = dict()

    length = len(sentense)
    sentense = ' '+sentense

    max_pr_list = []
    max_pr = 0
    forward_pointer = dict()
    for i in 'BMES':
        delta[(1,i)] = pi[i]*confusion_matrix[(i,sentense[1])]
        if delta[(1,i)] > max_pr:
            max_pr = delta[(1,i)]

    for i in range(2,length+1):

        for j in 'BMES':
            max_pr = 0
            forward = ''
            for k in 'BMES':
                prob = delta[(i-1,k)]*transition_matrix[(k,j)]*confusion_matrix[(j,sentense[i])] # confusion_matrix is not necessary when comparing
                if prob > max_pr:
                    max_pr = prob
                    forward = k
            delta[(i,j)] = max_pr
            forward_pointer[(i,j)] = forward
    max = 0
    last_tag = ''
    for i in 'ES':
        if delta[(length,i)] > max:
            max = delta[(length,i)]
            last_tag = i
    tags = last_tag
    t = length
    while t>=2:
        last_tag = forward_pointer[(t,last_tag)]
        t -= 1
        tags = last_tag + tags

    for i in range(len(tags)):
        print(sentense[i+1],tags[i])

    seged_sentense = ''
    for i in range(len(tags)):
        if tags[i] in 'BM':
            seged_sentense += sentense[i+1]
        else:
            seged_sentense += sentense[i+1] + ' '
    print(seged_sentense)

