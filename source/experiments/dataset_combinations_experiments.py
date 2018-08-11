import argparse
import pandas as pd
import sys
sys.path.append('../modeling/')
from svm_constructiveness_classification import ConstructivenessClassifier

def get_arguments():
    parser = argparse.ArgumentParser(description='Classify constructive comments')
    parser.add_argument('--train_dataset_path', '-tr', type=str, dest='train_dataset_path', action='store',
                        #default= '/Users/vkolhatk/Data/Constructiveness/data/train/features.csv',
                        #default='/Users/vkolhatk/Data/Constructiveness/data/train/gnm_features.csv',
                        #default = '/Users/vkolhatk/Data/Constructiveness/data/train/gnm_nyt_ync_features.csv',
                        default='/Users/vkolhatk/Data/Constructiveness/data/train/SOCC_nyt_ync_features.csv',
                        help="The input CSV containing features")

    parser.add_argument('--model_path', '-m', type=str, dest='model_file_path', action='store',
                        default= '/Users/vkolhatk/Data/Constructiveness/intermediate_output/models/svm_model.pkl',
                        #default='/home/vkolhatk/data/Constructiveness/data/train/features.csv',
                        help="the path of the file to save the model")

    parser.add_argument('--test_dataset_path', '-te', type=str, dest='test_dataset_path', action='store',
                        default='/Users/vkolhatk/Data/Constructiveness/data/test/features.csv',
                        #default='/home/vkolhatk/data/Constructiveness/data/test/features.csv',
                        help="The test dataset path for constructive and non-constructive comments")

    parser.add_argument('--features', '-f', type=list, dest='features', action='store',
                        default=(['Has_conjunction_or_connectives',
                                  'Has_stance_adverbials',
                                  'Has_reasoning_verbs', 'Has_modals'
                                  'Has_shell_nouns',
                                  'Len',
                                  'Average_word_length',
                                  'Redability',
                                  'PersonalEXP',
                                  'Named_entity_count',
                                  'nSents',
                                  'Avg_words_per_sent']),

                        help="The features to use for classification")

    args = parser.parse_args()
    return args

def run_cross_validation_experiments(training_feats_df, data_sources = ['SOCC'], n = 10):

    # Subset the feature vector based on the data sources
    subset_df = training_feats_df[training_feats_df['source'].isin(data_sources)]
    svm_classifier = ConstructivenessClassifier(subset_df)
    svm_classifier.run_nfold_cross_validation(n)

if __name__ == "__main__":
    args = get_arguments()
    print(args)

    # Training data with features csv
    #svm_classifier = ConstructivenessClassifier(args.train_dataset_path, args.test_dataset_path, args.features)
    training_feats_df = pd.read_csv(args.train_dataset_path)
    run_cross_validation_experiments(training_feats_df)

    #svm_classifier = ConstructivenessClassifier(args.train_dataset_path, args.test_dataset_path, args.features)
    #svm_classifier.run_nfold_cross_validation(training_feats_df, n=10)
    #svm_classifier.grid_search()
    #svm_classifier.train_classifier(args.model_file_path)
    #svm_classifier.test_classifier()
    #svm_classifier.run_svm_cross_validation()
    #svm_classifier.run_svm_with_csv_features()
    #Results with word count features
    #print('Results with word features:')
    #svm_classifier.run_svm_with_word_count_features()