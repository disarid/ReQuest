#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 2019

@author: disarideb
"""

from relation_extraction_2 import RelationExtractionModel

class ReQuest(RelationExtractionModel):
    
    '''
    The constructor can be used if needed
    def __init__(self, constructor_param1):
        self.constructor_param1 = constructor_param1
    '''
    
    '''
    All functions declared in the abstract class to be written here too, even if you're not using it
    '''

    def read_dataset(self, input_file, *args, **kwargs):
        '''

        input - path to the input file train.json, test.json, qa.json

        output - raw data (train, test and qa)
        
        '''
        return raw data
		
    def data_preprocess(self,input_data, *args, **kwargs):

        '''

        input - train.json, qa.json

        steps -
        Step 1 Generate Features
        
        feature_generation.py
            pruning_heuristics.py
            ner_feature.py
                mention_reader.py
                    mention.py
            nlp_parse.py

        output - train_new.json, text_new.json
        
        '''


	return processed data

    def tokenize(self, input_data ,ngram_size=None, *args, **kwargs): 
        '''

        input - data from data_preprocess

        steps - 
        Start the Stanford corenlp server for the python wrapper.
        java -mx4g -cp "code/DataProcessor/stanford-corenlp-full-2016-10-31/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer

        output - tokenized data
        
        '''
        return tokenized data

    def train(self, train_data, *args, **kwargs):  
        '''

        input - train.json

        steps -
        Step 2 Train ReQuest on Relation Classification
        run cpp code - code/Model/request/request -data $Data -mode m -size 50 -negative 4 -threads 20 -alpha 0.0001 -samples 1 -iters 500 -lr 0.025 -qaMFWeight 0.3 -qaMMWeight 0.3
        request.cpp 
	- hplelib.h
	
        output - model.tf (optional) / saved locally
        
        '''

        return model

    def predict(self, test_data, entity_1 = None, entity_2= None,  trained_model = None, *args, **kwargs):   
        '''

        input - test.json

        output - predicted relation type (entity 1 entity 2 relation type)
        
        '''
	return predict 

    def evaluate(self, input_data, trained_model = None, *args, **kwargs):
        # Script to predict and evaluate in a pipeline



        '''

        input - test input , model.tf (loaded locally)

        steps -
        Step 3 Evaluate ReQuest on Relation Classification
        python code/Evaluation/emb_test.py $Data request cosine 0.0
        python code/Evaluation/tune_threshold.py $Data emb request cosine
		
        emb_test.py
        -	evaluation.py
        -	emb_prediction.py
                o	DataIO.py
        tune_threshold.py
        -	evaluation.py
        -	emb_prediction.py
                o	DataIO.py

        output - Precision, Recall, F-1


        
        '''
	return evaluation tuple
    
    
    '''
    Extra individual functions

    def own_function(self):
        return 1
    '''


'''    
User Input
my_obj = ReBran()

print(my_obj.data_preprocess())

print(my_obj.data_tokenize()) ----- optional

print(my_obj.train())

print(my_obj.evaluate())

        
''' 
