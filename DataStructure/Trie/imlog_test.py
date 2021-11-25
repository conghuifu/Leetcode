import os
import tensorflow as tf
from transformers import AutoTokenizer, TFBertForSequenceClassification
import pandas as pd
import numpy as np
###############

SEQ_LEN = 30
num_classes = 3
# initialize model and tokenizer
model = TFBertForSequenceClassification.from_pretrained(
    "./bert_based",
    local_files_only=True,
    from_pt=True,
    num_labels=num_classes)
tokenizer = AutoTokenizer.from_pretrained("./bert_based")
checkpoint_filepath = 'bert_model/bert_model.h5'
model.load_weights(checkpoint_filepath)

test_ori = pd.read_excel('test_sent_mini.xlsx', index_col=None, engine='openpyxl')
test_ori.drop_duplicates(inplace=True)
# Report the number of sentences.
print('Number of test sentences: {:,}\n'.format(test_ori.shape[0]))
size = len(test_ori)
test_pred_df = pd.DataFrame()
for i in range(0, size, 10000):
    print(i, i + 10000)
    tmp = test_ori.loc[(test_ori.index >= i) & (test_ori.index < i+10000)]
    print(tmp.shape)

    test_input_ids = []
    test_attention_masks = []
    for sent in tmp.text:
        bert_inp = tokenizer.encode_plus(
            sent,
            add_special_tokens = True,
            max_length = SEQ_LEN,
            pad_to_max_length = True,
            truncation=True,
            return_attention_mask = True)
        test_input_ids.append(bert_inp['input_ids'])
        test_attention_masks.append(bert_inp['attention_mask'])

    test_inp = np.asarray(test_input_ids)
    test_mask = np.array(test_attention_masks)

    print('prediction begin......')
    test_pred_res = model.predict([test_inp, test_mask])
    test_pred_res = pd.DataFrame(test_pred_res[0])
    test_pred_res.columns = ['prob0', 'prob1', 'prob2']
    test_pred_res['prob0'] = test_pred_res.apply(lambda x: np.exp(x[0]) / (np.exp(x[0]) + np.exp(x[1]) + np.exp(x[2])), axis=1)
    test_pred_res['prob1'] = test_pred_res.apply(lambda x: np.exp(x[1]) / (np.exp(x[0]) + np.exp(x[1]) + np.exp(x[2])), axis=1)
    test_pred_res['prob2'] = test_pred_res.apply(lambda x: np.exp(x[2]) / (np.exp(x[0]) + np.exp(x[1]) + np.exp(x[2])), axis=1)

    tmp.reset_index(drop=True, inplace=True)
    tmp1 = pd.concat([tmp, test_pred_res], axis=1)

    test_pred_df = pd.concat([test_pred_df, tmp1], axis=0, ignore_index=True)
    print('total df shape', test_pred_df.shape)

test_pred_df.to_csv('tf_test_res.csv', index=None)
