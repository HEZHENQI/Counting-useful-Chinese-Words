# Counting-useful-Chinese-Words
It is based on Baidu Lac model to count useful chinese words and characters in text documents
基于百度LAC模型计算中文文本有效词组数量

## Introduction
It is for analysising the useful chinese words or characters in text documents, which is usually applied in reply quality measurements.
Baidu Lac(https://github.com/baidu/lac) is used for word segmentation.
The useful chinese words here refer to nouns, adjectives, verbs and adverbs. The LAC model is firstly used to split text into words, and stop words from the stop words dictionary(Baidu stop words dictionary is used here) are excluded.
此文档应用于计算中文有效词组或字，通常运用在计算问卷调查回复的质量计算。
我先运用百度的LAC模型（https://github.com/baidu/lac）进行分词，之后使用百度停止词库剔除停止词后计算文本中的名词，形容词，动词和副词的数量。


## Installation & Usage
Details of Installation of lac is in https://github.com/baidu/lac

Edit paths name in main.sh and simply run the command main.sh
    -stop_words_path refer to where stop_words.txt is stored
    -csv_path: path of the csv file which stored all texts and all texts texts are stored in the column named "text" in the csv file
    -save_path: path of saving output csv file


