# -*- coding: UTF-8 -*-
#-----------------------------#
#Team Name: MacroHard
#Members: Zhenlin Qi
#         Zheyu Shi
#         Yong Mao
#All Rights Reserved
#It's a demo for CWSS
#-----------------------------#

import pickle
import __main__
from math import*
import time

def getlog(x):
    if x == 0:
        return -9999
    else:
        return log(x)


def strH2F(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring


def load():

    """Load HMM model"""
    global transition_matrix
    global confusion_matrix
    global two_char_confusion_matrix
    global pi
    # load matrices
    in_pkl_file = open('log_full_matrix(tra-con-2con)_4f.pkl', 'rb')
    transition_matrix = pickle.load(in_pkl_file)
    confusion_matrix = pickle.load(in_pkl_file)
    two_char_confusion_matrix = pickle.load(in_pkl_file)
    in_pkl_file.close()
    pi = {'B': getlog(0.32),'E': getlog(0),'M': getlog(0),'S': getlog(0.68)}



def find_hidden(sentence):
    print(sentence)
    global transition_matrix
    global confusion_matrix
    global two_char_confusion_matrix
    global pi

    delta = dict()

    length = len(sentence)
    sentence = ' '+sentence

    max_pr = -10**200
    forward_pointer = dict()
    quan_sentence = strH2F(sentence)

    for i in 'BMES':
        if (i, quan_sentence[1]) in confusion_matrix:
            delta[(1, i)] = pi[i] + confusion_matrix[(i, quan_sentence[1])]
            if delta[(1, i)] > max_pr:
                max_pr = delta[(1, i)]
        else:
            delta[1, i] = pi[i]

    for i in range(2, length+1):

        for j in 'BMES':
            max_pr = -10 ** 200
            forward = ''
            for k in 'BMES':
                if ('B', quan_sentence[i-1:i+1]) in two_char_confusion_matrix:  # should be tuple()!!!
                    prob = delta[(i-1, k)] + transition_matrix[(k, j)] + two_char_confusion_matrix[
                        (j, quan_sentence[i-1:i+1])]
                    # confusion_matrix is not necessary when comparing
                elif (j, quan_sentence[i]) in confusion_matrix:
                    prob = delta[(i-1, k)] + transition_matrix[(k, j)] + confusion_matrix[(j, quan_sentence[i])]
                else:
                    prob = delta[(i - 1, k)]
                if prob > max_pr:
                    max_pr = prob
                    forward = k
            delta[(i, j)] = max_pr
            forward_pointer[(i, j)] = forward

    max = -10**200
    last_tag = ''
    for i in 'ES':
        if delta[(length,i)] > max:
            max = delta[(length, i)]
            last_tag = i
    tags = last_tag
    t = length
    while t >= 2:
        last_tag = forward_pointer[(t, last_tag)]
        t -= 1
        tags = last_tag + tags

    return tags


def seg(sentence):
    tags = find_hidden(sentence)
    seged_sentence = ''
    for i in range(len(tags)):
        if tags[i] in 'BM':
            seged_sentence += sentence[i]
        else:
            seged_sentence += sentence[i] + '  '
    return seged_sentence



def check(seged_sentence):
    """To check whether a segmented sentence is serious"""
    tags = find_hidden(''.join(seged_sentence.split(' ')))
    tags_by_hand = ''
    seged_sentence = ' ' + seged_sentence + ' '
    for i in range(1, len(seged_sentence) - 1):
        if seged_sentence[i] != ' ':
            if seged_sentence[i - 1] == ' ' and seged_sentence[i + 1] == ' ':
                tags_by_hand += 'S'
            elif seged_sentence[i - 1] != ' ' and seged_sentence[i + 1] == ' ':
                tags_by_hand += 'E'
            elif seged_sentence[i - 1] == ' ' and seged_sentence[i + 1] != ' ':
                tags_by_hand += 'B'
            else:  # if seged_sentence[i-1] != ' ' and seged_sentence[i+1] != ' '
                tags_by_hand += 'M'
    count = 0
    for i in range(len(tags)):
        if tags_by_hand[i] == tags[i]:
            count +=1
    if count/len(tags) > 0.7:
        return True
    else:
        return False

if __name__ == '__main__':
    load()
    in_file = open('pku_test.utf8', 'r', encoding='utf-8')
    out_file = open('pku_result.utf8' ,'w', encoding='utf-8')
    for line in in_file:
        out_file.write(seg(line[:-1])+'\n')
    in_file.close()
    out_file.close()
