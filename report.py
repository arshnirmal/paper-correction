#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:14:43 2020

@author: bhargavdesai
"""

import nltk
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import TweetTokenizer
from striprtf.striprtf import rtf_to_text
# from absl import logging
import logging
import tensorflow as tf     # Please make sure the version is 2.0.0 or greater
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import time
from fpdf import FPDF
from PIL import Image, ImageChops
import fitz
import string

# Import Spacy and load POS model
import spacy
# from spacy.lang.en import English
# import en_core_web_md
import en_core_web_sm
print('Loading POS Tagger model')
# nlp = en_core_web_md.load()
nlp = en_core_web_sm.load()

# Necessary imports
# Import cosine similarity evaluation metric

# Import nltk
nltk.download('punkt')


# Download Universal Sentence Encoder
module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"

# IF MODEL DOWNLOADED
# model = hub.load(
# '/Users/parthchudasama/Projects/paper-bitbucket/paper-correction/tmp/5')

model = hub.load(module_url)

print("module %s loaded" % module_url)

# Reduce logging output.
# logging.set_verbosity(logging.ERROR)

# # # # Change the path to the folders having S1, S2, S3 here from preprocessing.py
PATH_PAPERS = os.getcwd() + '/preprocessed'

# # # # Change the path to the answer key here
PATH_ANSKEY = os.getcwd() + '/misc_files/master_file.txt'

############ Main functions ############


def process_answer_key(PATH_ANSKEY):

    # RTF support

    rtf = open(PATH_ANSKEY, "r")
    text = rtf_to_text(rtf.read())
    # print(text)

    # Seperate each answer along with its marks from answer key

    indexes = list(find_all(text, '(M:'))
    marks = get_marks_from_anskey(text, indexes)
    reference_answers = get_answers_from_anskey(text, indexes)

    return marks, reference_answers


def process_student_paper(PATH_PAPERS):

    all_student_answers = []
    flag = 0
    folders = os.listdir(PATH_PAPERS)
    if 'PHOTOS' in folders and len(folders) > 1:

        flag = 1
        print('Found PHOTOS folder and student folder(s)...')
        for idx, folder in enumerate(sorted((os.listdir(PATH_PAPERS)))):
            if not folder.startswith('.'):
                for file in os.listdir(os.path.join(PATH_PAPERS, folder)):
                    if file.endswith('.txt'):
                        print(file)
                        f = open(os.path.join(PATH_PAPERS, folder, file), "r")
                        ans = f.read()
                        # print(ans)
                        list_of_lines = strip_headers(ans.rsplit('\n'))
                        q_number, ans = get_answers_from_studentpaper(
                            list_of_lines)
                all_student_answers.append((idx+1, q_number, ans))

    if 'PHOTOS' in folders and len(folders) == 1:

        flag = 2
        print('Found only PHOTOS folder....')
        for idx, folder in enumerate(sorted((os.listdir(PATH_PAPERS)))):
            if not folder.startswith('.'):
                for file in os.listdir(os.path.join(PATH_PAPERS, folder)):
                    if file.endswith('.txt'):
                        # print(file)
                        f = open(os.path.join(PATH_PAPERS, folder, file), "r")
                        ans = f.read()
                        # print(ans)
                        list_of_lines = strip_headers(ans.rsplit('\n'))
                        q_number, ans = get_answers_from_studentpaper(
                            list_of_lines)
                all_student_answers.append((idx+1, q_number, ans))

    if 'PHOTOS' not in folders and len(folders) >= 1:

        flag = 0
        print('No PHOTOS folder found... continuing...')
        for idx, folder in enumerate(sorted((os.listdir(PATH_PAPERS)))):
            for file in os.listdir(os.path.join(PATH_PAPERS, folder)):
                if file.endswith('.txt'):
                    print(file)
                    f = open(os.path.join(PATH_PAPERS, folder, file), "r")
                    ans = f.read()
                    # print(ans)
                    list_of_lines = strip_headers(ans.rsplit('\n'))
                    q_number, ans = get_answers_from_studentpaper(
                        list_of_lines)
            all_student_answers.append((idx+1, q_number, ans))

    if 'PHOTOS' not in folders and len(folders) == 0:
        flag = -1
        print('No valid folders found in the path passed, please check and try again!')

    return all_student_answers, flag


############ Helper Functions Pt. 1 ############


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


def get_marks_from_anskey(text, list_of_indexes):

    marks = []
    for index in list_of_indexes:
        subs = text[int(index):int(index)+10]
        marks.append(subs.split(')')[0][3:])

    return marks


def get_answers_from_anskey(text, list_of_indexes):

    answers = []
    for idx, index in enumerate(list_of_indexes):
        if idx == 0:
            subs = text[:int(index)]
            subs = subs.replace('\n', '')
            subs = subs.replace('\x92', "'")
            subs = subs.replace(subs.split()[0], '')
            answers.append(subs)
        else:
            subs = text[(list_of_indexes[idx-1]):int(index)]
            sub = subs.split()[0]
            if sub in subs:
                subs = subs.replace(sub, '')
                subs = subs.replace('\n', '')
                # unicode encoding support from rtf -> .txt conversion
                subs = subs.replace('\x92', "'")
                subs = subs.replace(subs.split()[0], '')
            answers.append(subs)
    return answers


def get_answers_from_studentpaper(list_of_lines):

    candidates = []
    stu_ans = []
    processed_ans = []
    q_number = []

    for idx, line in enumerate(list_of_lines):
        if line.startswith(('0', 'a', 'Q', 'q', 'O')):
            sub = line.split()[0]
            if len(re.split('\d+', sub)) == 2:
                candidates.append((line, idx))
                continue

            if len(re.findall('[A-Z][^A-Z]', line.split()[1])) != 0:
                if idx != 0 and list_of_lines[idx-1].split()[-1].find('.') != -1:
                    candidates.append((line, idx))

                if idx == 0:
                    candidates.append((line, idx))

    for idx, val in enumerate(candidates):

        if idx != (len(candidates)-1):
            stu_ans.append(list_of_lines[val[1]:candidates[idx+1][1]])
        else:
            stu_ans.append(list_of_lines[val[1]:])

    for ans in stu_ans:

        ans_preprocessed = checks_for_getting_question_number(ans)

        check1 = [int(i) for i in ans_preprocessed if i.isdigit()]

        if len(check1) > 0:
            for idx, val in enumerate(check1):
                if val == 0 and idx == 0:
                    continue
                if val != 0 and idx == 0:
                    q_number.append(val)
                if val != 0 and idx > 0 and (idx+1) != len(check1):
                    q_number.append(int(str(val)+str(check1[idx+1])))
                if val != 0 and idx > 0 and (idx+1) == len(check1):
                    q_number.append(val)

        ans = ' '.join(ans)
        ans = ans.replace(ans.rsplit()[0], '')
        processed_ans.append(ans)

    return q_number, processed_ans


def strip_headers(list_of_lines):

    strip_candidates = []
    for idx, line in enumerate(list_of_lines):
        if not line.startswith(('0', 'a', 'Q', 'q', 'O')):
            strip_candidates.append(line)
            continue
        elif line.startswith(('0', 'a', 'Q', 'q', 'O')):
            sub = line.rsplit()[0]
            for char in sub:
                if char.isdigit() or char == 'l' or char == 'z' or char == 'd' or char == 'I' or char == 'i':
                    break
            break

    for lines in strip_candidates:
        list_of_lines.remove(lines)

    return list_of_lines


def checks_for_getting_question_number(ans):

    check2 = ans[0].rsplit()[0]
    zeros = ['o', 'O']
    ones = ['l', 'i', 'I', 'L', 't', 'T']
    twos = ['z', 'Z']
    sixes = ['b']
    for chars in check2:
        for zero in zeros:
            check2 = check2.replace(zero, '0')
        for one in ones:
            check2 = check2.replace(one, '1')
        for two in twos:
            check2 = check2.replace(two, '2')
        for six in sixes:
            check2 = check2.replace(six, '6')

    return check2


def get_reference_answer_and_total_marks(current_q_number, reference_answers, marks):
    reference_answer = reference_answers[int(current_q_number-1)]
    total_marks = int(marks[int(current_q_number-1)])

    return reference_answer, total_marks


def handle_delimiter_errors(tokenized_text):
    for idx, sentence in enumerate(tokenized_text):
        if sentence.endswith(('!', '.')) and idx+1 != len(tokenized_text):
            next_word = tokenized_text[idx+1].rsplit()[0]
            if next_word[0].isupper():
                continue
            else:
                sentence = sentence.replace('!', '')
                sentence = sentence.replace('.', '')
                comb = sentence + ' ' + tokenized_text[idx+1]
                tokenized_text[idx] = tokenized_text[idx].replace(
                    tokenized_text[idx], comb)
                tokenized_text.remove(tokenized_text[idx+1])

    return tokenized_text


def aware_capitalisation(ans_stu_sent):

    for idx, sent in enumerate(ans_stu_sent):

        candidates = []
        propernouns = []
        print(sent)
        doc = nlp(sent)
        for token in doc:
            if token.tag_ == 'NNP' or token.tag_ == 'NNPS':
                propernouns.append(token.text)

        print(propernouns)

        for word in sent.split():

            if word[0].isupper() and word.translate(str.maketrans('', '', string.punctuation.replace('.', ''))) not in propernouns:
                candidates.append(word)

        count = 0

        print(candidates)
        words = sent.split()
        for idx2, word in enumerate(words):
            if word in candidates:
                if not idx2 == 0:
                    count += 1
                    modify(idx, idx2, ans_stu_sent, count)

    return ' '.join(ans_stu_sent)


def handle_abbreviations(sent):

    # better solution for this to come

    sent = sent.replace('St.', 'St')
    sent = sent.replace('Mr.', 'Mr')
    sent = sent.replace('Mrs.', 'Mrs')
    sent = sent.replace('Dr.', 'Dr')
    sent = sent.replace('Hon.', 'Hon')
    sent = sent.replace('Ave.', 'Avenue')
    sent = sent.replace('appx.', 'approx')
    sent = sent.replace('dept.', 'department')

    return sent


def modify(idx_of_sent, idx_of_word_to_be_replaced, ans_stu_sent, count):

    sent = handle_abbreviations(ans_stu_sent[idx_of_sent]).split()
    word_at_idx_minus_one = sent[idx_of_word_to_be_replaced-1]
    sent.remove(word_at_idx_minus_one)
    sent.insert(idx_of_word_to_be_replaced-1, word_at_idx_minus_one+'.')
    if len(' '.join(sent).split('.')[count-1].split()) >= 4:
        ans_stu_sent[idx_of_sent] = ' '.join(sent)
    else:
        pass

################ End of helper functions Pt.1 ####################


def evaluate(all_student_answers, marks, reference_answers, flag):

    n_papers = len(all_student_answers)
    print('Found %s papers to be checked! Checking them now.....' % n_papers)

    for val in all_student_answers:

        lsm = []
        ssm = []
        nsm = []
        current_paper = val[0]
        attempted_ques = []

        print(current_paper)
        current_student_answers = val[2]

        for idx, current_answer in enumerate(current_student_answers):
            current_q_number = val[1][idx]
            attempted_ques.append(current_q_number)
            print(current_q_number)
            reference_answer, total_marks = get_reference_answer_and_total_marks(
                current_q_number, reference_answers, marks)
            loose_sem_matches, strong_sem_matches, no_sem_matches = compare(reference_answer, current_answer, total_marks,
                                                                            current_paper, current_q_number, flag)
            lsm.append(loose_sem_matches)
            ssm.append(strong_sem_matches)
            nsm.append(no_sem_matches)
        start_time = time.time()
        path_to_gen_pdf = generate_pdf_reports_from_individual_feedbacks(
            PATH_PAPERS, current_paper, attempted_ques, flag)
        highlight(lsm, ssm, nsm, path_to_gen_pdf)
        print('completed generating a report, check folder')
        print('Based on our calculations, it will take the following time to generate reports for the next student:')
        print("--- %s seconds ---" % (time.time() - start_time))


def compare(reference_answer, current_answer, total_marks, current_paper, current_q_number, flag):

    # Split answer key and student answer into sentences.
    start_time = time.time()
    ans_key_sent = convert_answers_to_sentences(reference_answer)
    ans_stu_sent = convert_answers_to_sentences(current_answer)
    ans_stu_sent = delete_erraneous_sentences(ans_stu_sent)
    ans_stu_sent = handle_delimiter_errors(ans_stu_sent)
    ans_stu_sent = convert_answers_to_sentences(
        aware_capitalisation(ans_stu_sent))
    ans_key_sent = delete_erraneous_sentences(ans_key_sent)

    # print(ans_key_sent)
    # print(ans_stu_sent)
    # print(len(ans_key_sent))
    # print(len(ans_stu_sent))

    # Get embeddings for student answer and answer key
    question_paper_embeddings = get_embeddings(ans_stu_sent)
    question_paper_embeddings = convert_eagertensor_to_ndarray(
        question_paper_embeddings)
    answer_key_embeddings = get_embeddings(ans_key_sent)
    answer_key_embeddings = convert_eagertensor_to_ndarray(
        answer_key_embeddings)

    # Get similarity matrix (answer key sentences -> compared with -> student answer sentences)
    sim_mat = get_similarity_matrix(
        question_paper_embeddings, answer_key_embeddings)

    # Get similarity matrix (student answer sentences -> compared with -> answer key sentence)
    sim_mat_trans = sim_mat.transpose()

    print("--- %s seconds ---" % (time.time() - start_time))

    # Get normalised sentences
    ans_stu_main = list(ans_stu_sent)
    ans_stu_sent, ans_key_sent = normalise_sentences(
        ans_key_sent, ans_stu_sent, sim_mat, sim_mat_trans)
    question_paper_embeddings = get_embeddings(ans_stu_sent)
    question_paper_embeddings = convert_eagertensor_to_ndarray(
        question_paper_embeddings)
    answer_key_embeddings = get_embeddings(ans_key_sent)
    answer_key_embeddings = convert_eagertensor_to_ndarray(
        answer_key_embeddings)

    # Get similarity matrix (answer key sentences -> compared with -> student answer sentences)
    sim_mat = get_similarity_matrix(
        question_paper_embeddings, answer_key_embeddings)

    # Get similarity matrix (student answer sentences -> compared with -> answer key sentence)
    sim_mat_trans = sim_mat.transpose()

    assigned_weights, ans_stu_sent, f, loose_sem_matches, strong_sem_matches, no_sem_matches = interpret_sim_mat_and_generate_report(
        sim_mat, sim_mat_trans, ans_key_sent, ans_stu_sent, PATH_PAPERS, current_paper, current_q_number, flag)
    weights = denormalise_sentences(
        ans_stu_sent, ans_stu_main, assigned_weights)

    # To set each column cell to be just as big as it needs to be in order to fully display it's content.
    # pd.set_option('display.max_colwidth', 0)
    pd.options.display.max_colwidth = 50

    marks_per_point = (total_marks)/len(ans_key_sent)

    df = pd.DataFrame(weights.items(), columns=[
                      "Student's Point", 'Associated Weight'])
    df['Marks Awarded'] = df['Associated Weight']
    df['Marks Awarded'] *= marks_per_point
    df["Student's Point"] = df["Student's Point"].str.wrap(50)

    print('Evaluated Score: ', file=f)
    print(str(df['Marks Awarded'].sum()) +
          ' out of ' + str(total_marks), file=f)

    # Close stream to text file
    f.close()

    print('Saved the .txt file')

    plot_assesment_df(df, PATH_PAPERS, current_paper, current_q_number, flag)

    return loose_sem_matches, strong_sem_matches, no_sem_matches


############ Helper Functions Pt. 2 ############

# Embed a sentence to a 512 dimensional vector

def embed(input):
    return model(input)


# Convert the answer into a list of sentences
def convert_answers_to_sentences(text):
    sent_text = nltk.sent_tokenize(text)
    # Return a list of sentences from the passed text
    return sent_text


# Convert the split sentences into a list words.
def convert_sentences_to_words(sent_text):
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized_text)
        print(tagged)

        # tokenizer_words = TweetTokenizer()
        # tokens_sentences = [tokenizer_words.tokenize(t) for t in sent_text]
        # print(tokens_sentences)
        # return tokens_sentences

# Convert the answer into a list sentences with words segmented.


def convert_answers_to_words(text):
    tokenizer_words = TweetTokenizer()
    tokens_sentences = [tokenizer_words.tokenize(
        t) for t in nltk.sent_tokenize(text)]
    print(tokens_sentences)
    return tokens_sentences


# Handling for sentences which have just one word. For eg, "bhargav is awesome. marts."  -> "bhargav is awesome"
def delete_erraneous_sentences(ans_stu_sent):

    for idx, sent in enumerate(ans_stu_sent):
        if len(sent.split()) == 1:
            del (ans_stu_sent[idx])
    return ans_stu_sent


# Calculate embeddings of the sentences in the answer key
def get_embeddings(a_list_of_sentences):
    sentence_embeddings = []
    sentence_embeddings.append(embed(a_list_of_sentences))
    return sentence_embeddings


# Convert tf.EagerTensor to ndarray
def convert_eagertensor_to_ndarray(eagertensor):
    ndarray = np.empty((len(eagertensor[0]), 512))
    for i in range(len(eagertensor[0])):
        ndarray[i, :] = np.asarray(eagertensor[0][i])
    return ndarray


# Calculate similarity matrix
def get_similarity_matrix(question_paper_embeddings, answer_key_embeddings):
    sim_mat = np.empty((len(answer_key_embeddings),
                        len(question_paper_embeddings)))
    for ans_sen_number, anskey_embedding in enumerate(answer_key_embeddings):
        anskey_embedding = anskey_embedding.reshape(1, -1)
        for stu_sen_number, stu_embedding in enumerate(question_paper_embeddings):
            stu_embedding = stu_embedding.reshape(1, -1)
            sim_mat[ans_sen_number, stu_sen_number] = cosine_similarity(
                anskey_embedding, stu_embedding)
    return sim_mat


# Check number of sentences
def check_num_sentences(sentence):
    sent = convert_answers_to_sentences(sentence)
    return (len(sent))


def interpret_sim_mat_and_generate_report(sim_mat, sim_mat_trans, ans_key_sent, ans_stu_sent, PATH_PAPERS, current_paper, current_q_number, flag):

    if flag == 1 and current_paper == 1:
        os.chdir(os.path.join(PATH_PAPERS, 'PHOTOS'))

    elif flag == 2:
        os.chdir(os.path.join(PATH_PAPERS, 'PHOTOS'))

    elif flag == 1 and current_paper > 1:
        os.chdir(os.path.join(PATH_PAPERS, 'S'+str(current_paper-1)))

    else:
        os.chdir(os.path.join(PATH_PAPERS, 'S'+str(current_paper)))

    # Open a file for dumping text
    f = open(str(current_q_number)+'.txt', "a", encoding='utf-8')

    print('The student has written the following answer for this question: \n', file=f)
    print(' '.join(ans_stu_sent)+'\n', file=f)

    # Feedback
    ind = np.argmax(sim_mat, axis=1)
    strong_semantic_match = []
    loose_semantic_match = []
    no_semantic_match = []

    for i in range(len(ind)):
        similarity = sim_mat[i][ind[i]]
        if similarity < 0.35:
            no_semantic_match.append([i, similarity])
        elif similarity > 0.35 and similarity <= 0.65:
            loose_semantic_match.append([i, similarity])
        else:
            strong_semantic_match.append([i, similarity])

    print('Student has not written anything covering the following points: \n', file=f)

    if no_semantic_match != []:
        for i in range(len(no_semantic_match)):
            print(ans_key_sent[no_semantic_match[i][0]], file=f)
    elif no_semantic_match == []:
        print('None. All points were adequately covered \n', file=f)

    print('------------------------------------------------------------------- \n', file=f)

    print('Student has loosely touched upon the following points, but a more adequate coverage was expected: \n', file=f)

    if loose_semantic_match != []:
        for i in range(len(loose_semantic_match)):
            print(ans_key_sent[loose_semantic_match[i][0]], file=f)
    elif loose_semantic_match == []:
        print('None. All points were adequately covered \n', file=f)

    print('------------------------------------------------------------------- \n', file=f)

    print('The student has covered the following points perfectly and as per expectation: \n', file=f)

    if strong_semantic_match != []:
        for i in range(len(strong_semantic_match)):
            print(ans_key_sent[strong_semantic_match[i][0]], file=f)
    elif strong_semantic_match == []:
        print('None of the expected points were adequately covered \n', file=f)

    print('------------------------------------------------------------------- \n', file=f)

    # ------- Student point of view --------- #

    ind = np.argmax(sim_mat_trans, axis=1)
    no_semantic_match = []
    loose_semantic_match = []
    strong_semantic_match = []
    assigned_weights = {}

    for i in range(len(ind)):
        similarity = sim_mat_trans[i][ind[i]]
        if similarity < 0.35:
            no_semantic_match.append([i, similarity])
        elif similarity > 0.35 and similarity <= 0.65:
            loose_semantic_match.append([i, similarity])
        else:
            strong_semantic_match.append([i, similarity])

    # print('------------------------------------------------------------------- \n', file=f)
    # print('The points that loosely matched the answer key were: \n', file=f)
    # print('\n', file=f)

    loose_sem_matches = []
    if loose_semantic_match != []:
        for i in range(len(loose_semantic_match)):
            # print(ans_stu_sent[loose_semantic_match[i][0]], file=f)
            loose_sem_matches.append(ans_stu_sent[loose_semantic_match[i][0]])
            assigned_weights[ans_stu_sent[loose_semantic_match[i]
                                          [0]]] = loose_semantic_match[i][1]
    elif loose_semantic_match == []:
        print('No such sentences \n')

    # print('------------------------------------------------------------------- \n', file=f)
    # print('\n', file=f)

    # print('------------------------------------------------------------------- \n', file=f)
    # print('The points that strongly matched the answer key were: \n', file=f)
    # print('\n', file=f)

    strong_sem_matches = []
    if strong_semantic_match != []:
        for i in range(len(strong_semantic_match)):
            # print(ans_stu_sent[strong_semantic_match[i][0]], file=f)
            strong_sem_matches.append(
                ans_stu_sent[strong_semantic_match[i][0]])
            assigned_weights[ans_stu_sent[strong_semantic_match[i][0]]] = 1.0
    elif strong_semantic_match == []:
        print('No such points \n')

    # print('------------------------------------------------------------------- \n', file=f)
    # print('\n', file=f)

    # print('------------------------------------------------------------------- \n', file=f)
    # print('The sentences that were extra and did not find a match in the the answer key were: \n', file=f)
    # print('\n', file=f)

    no_sem_matches = []
    if no_semantic_match != []:
        for i in range(len(no_semantic_match)):
            # print(ans_stu_sent[no_semantic_match[i][0]], file=f)
            no_sem_matches.append(ans_stu_sent[no_semantic_match[i][0]])
            assigned_weights[ans_stu_sent[no_semantic_match[i][0]]] = 0.0
    elif no_semantic_match == []:
        print('No such sentences \n')

    # print('------------------------------------------------------------------- \n', file=f)
    # print('\n', file=f)
    os.chdir(os.getcwd())
    return assigned_weights, ans_stu_sent, f, loose_sem_matches, strong_sem_matches, no_sem_matches


# Semantically Normalise Sentences

def normalise_sentences(ans_key_sent, ans_stu_sent, sim_mat, sim_mat_trans):

    ############# FOR STUDENT PAPER SIDE OF THINGS ###########

    modifications = []
    thresh = 0.45
    ind = np.argmax(sim_mat, axis=1)
    ind_trans = np.argmax(sim_mat_trans, axis=1)
    print(ind_trans)
    for i in range(len(ind)):
        similarity = sim_mat[i][ind[i]]
        if similarity >= 0.35:
            new_similarity = similarity*thresh
            for idx, j in enumerate(sim_mat[i]):
                if j >= new_similarity and j < similarity:
                    if j == sim_mat_trans[idx][ind_trans[idx]]:
                        modifications.append(
                            [i, idx, j, ind[i], ans_stu_sent[idx], ans_stu_sent[ind[i]]])
        else:
            continue
    # print(modifications)

    if modifications != []:
        for i in modifications:
            comb = i[5] + ' ' + i[4]
            ans_stu_sent[i[3]] = comb
            ans_stu_sent[i[1]] = ''
    else:
        print('No possible combinations found.')

    if modifications != []:
        for idx, sentences in enumerate(ans_stu_sent):
            if sentences == '':
                ans_stu_sent.pop(idx)
    else:
        print('No modifications necessary!')

    ############# FOR ANSWER KEY SIDE OF THINGS ###########

    modifications2 = []
    thresh = 0.45
    ind = np.argmax(sim_mat, axis=1)
    ind_trans = np.argmax(sim_mat_trans, axis=1)
    print(ind_trans)
    for i in range(len(ind_trans)):
        similarity = sim_mat_trans[i][ind_trans[i]]
        if similarity >= 0.35:
            new_similarity = similarity*thresh
            for idx, j in enumerate(sim_mat_trans[i]):
                if j >= new_similarity and j < similarity:
                    if j == sim_mat[idx][ind[idx]]:
                        modifications2.append(
                            [i, idx, j, ind_trans[i], ans_key_sent[idx], ans_key_sent[ind_trans[i]]])
        else:
            continue
    # print(modifications2)

    if modifications2 != []:
        for i in modifications2:
            comb = i[5] + ' ' + i[4]
            ans_key_sent[i[3]] = comb
            ans_key_sent[i[1]] = ''
    else:
        print('No possible combinations found.')

    if modifications2 != []:
        for idx, sentences in enumerate(ans_key_sent):
            if sentences == '':
                ans_key_sent.pop(idx)
    else:
        print('No modifications necessary!')

    return ans_stu_sent, ans_key_sent


# Denormalise Sentences
def denormalise_sentences(ans_stu_sent, ans_stu_main, assigned_weights):
    weights = {}
    for i in range(len(ans_stu_main)):
        for j in range(len(ans_stu_sent)):
            if ans_stu_main[i] in ans_stu_sent[j]:
                if len(ans_stu_main[i]) < len(ans_stu_sent[j]):
                    n = check_num_sentences(ans_stu_sent[j])
                    weights[ans_stu_main[i]] = (
                        assigned_weights[ans_stu_sent[j]])/n
                else:
                    weights[ans_stu_main[i]] = assigned_weights[ans_stu_sent[j]]

    return weights

# Plot breakup of marks for an answer


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def plot_assesment_df(df, path, current_paper, current_q_number, flag):

    fig, ax = plt.subplots(dpi=75, constrained_layout=True)
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText=df.values, colWidths=[
             1.0]*len(df.columns.values), colLabels=df.columns, cellLoc='center').scale(1, 5)
    fig.tight_layout()

    if flag == 1 and current_paper == 1:
        save_path = os.path.join(path, 'PHOTOS', str(current_q_number)+'.png')
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        im = Image.open(save_path)
        im = trim(im)
        im = im.convert('RGB')
        im.save(save_path)
        print('Plotted assesment .png')

    elif flag == 2:
        save_path = os.path.join(path, 'PHOTOS', str(current_q_number)+'.png')
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        im = Image.open(save_path)
        im = trim(im)
        im = im.convert('RGB')
        im.save(save_path)
        print('Plotted assesment .png')

    elif flag == 1 and current_paper > 1:
        save_path = os.path.join(
            path, 'S'+str(current_paper-1), str(current_q_number)+'.png')
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        im = Image.open(save_path)
        im = trim(im)
        im = im.convert('RGB')
        im.save(save_path)
        print('Plotted assesment .png')

    else:
        save_path = os.path.join(
            path, 'S'+str(current_paper), str(current_q_number)+'.png')
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        im = Image.open(save_path)
        im = trim(im)
        im = im.convert('RGB')
        im.save(save_path)
        print('Plotted assesment .png')


####################  PDF GENERATION ####################

title = 'Feedback Report'


class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 16)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def titles(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'For Answer %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def report_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 10)
        # Output justified text
        self.multi_cell(0, 5, txt, border=1, align='J')
        # Line break
        self.ln()
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def report_img(self, num, title, name):

        self.add_page()
        self.titles(num, title)
        self.image(name, h=100, w=190, x=10, y=60, type="png")
        # Line break
        self.ln()

    def print_report(self, num, title, name):
        self.add_page()
        self.titles(num, title)
        self.report_body(name)


def generate_pdf_reports_from_individual_feedbacks(PATH_PAPERS, current_paper, attempted_ques, flag):

    print('Please wait while we generate the feedback PDF for you...... This might take upto 2 minutes!')

    if flag == 1 and current_paper == 1:
        folder = os.path.join(PATH_PAPERS, 'PHOTOS')
        save_name = 'PHOTOS.pdf'

    elif flag == 2:
        folder = os.path.join(PATH_PAPERS, 'PHOTOS')
        save_name = 'PHOTOS.pdf'

    elif flag == 1 and current_paper > 1:
        folder = os.path.join(PATH_PAPERS, 'S'+str(current_paper-1))
        save_name = 'S'+str(current_paper-1)+'.pdf'

    else:
        folder = os.path.join(PATH_PAPERS, 'S'+str(current_paper))
        save_name = 'S'+str(current_paper)+'.pdf'

    # Set variable for PDF report for the current student paper

    title = 'Feedback Report'
    pdf = PDF()
    pdf.set_title(title)
    pdf.set_author('Bhargav Desai')

    for i in attempted_ques:

        # Generation of report
        pdf.print_report(i, 'ANALYSIS', os.path.join(folder, str(i)+'.txt'))
        pdf.report_img(i, "Marks Assignment Breakdown Per Point of the Student's Answer",
                       os.path.join(folder, str(i)+'.png'))
        # Close and save the current PDF for curret student paper
    pdf.output(os.path.join(folder, save_name), 'F')
    return os.path.join(folder, save_name)

#### Experimental Code to highlight the answers, optimisations will be added once functionality is confirmed ####


def highlight(lsm, ssm, nsm, path_to_gen_pdf):

    lists = [lsm, ssm, nsm]
    doc = fitz.open(path_to_gen_pdf)

    for idx, _list in enumerate([lsm, ssm, nsm]):

        if idx == 1:
            colour = (0.467, 0.867, 0.467)  # pastel green
        if idx == 2:
            colour = (1, 0.38, 0.412)  # pastel red
        if idx == 0:
            colour = (0.992, 0.992, 0.558)  # pastel yellow

        for matches in _list:

            if len(matches) != 0:

                for text in matches:

                    text_instances_per_page = []
                    pages = []
                    valid_pages = []

                    for page in doc:
                        pages.append(page)
                        text_instances = page.searchFor(text)
                        text_instances_per_page.append(text_instances)

                    for idx, ele in enumerate(text_instances_per_page):
                        if ele != []:
                            valid_pages.append(idx)

                    text_instances = [
                        x for x in text_instances_per_page if x != []]

                    for inst in text_instances:

                        page = doc[valid_pages[0]]
                        highlight = page.addHighlightAnnot(inst)
                        highlight.setColors(stroke=colour)

                    print('Saved here')
                    doc.can_save_incrementally()
                    doc.saveIncr()

            else:
                continue


# dstore_delete()
# marks, reference_answers = process_answer_key(PATH_ANSKEY)
# all_student_answers, flag = process_student_paper(PATH_PAPERS)
# evaluate(all_student_answers, marks, reference_answers, flag)
