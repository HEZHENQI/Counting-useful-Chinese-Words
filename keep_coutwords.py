from LAC import LAC
import pandas as pd
import argparse

def get_stop_words(stop_words_path):
  with open(stop_words_path,"r") as f:
    stop_words = f.readlines()
  stop_words = [i.replace("\n","") for i in stop_words]
  return stop_words

def count_useful_char(stop_words,text):
  for stop_word in stop_words:
    text = text.replace(stop_word,"")
  return len(text)
  
### example:
## python keep_countwords.py --stop_words_path=xxx --csv_path=xxx --save_path=xxx
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stop_words_path",dest = "stop_words_path",required = True)
    parser.add_argument("--csv_path",dest = "csv_path",required = True)
    parser.add_argument("--save_path",dest = "save_path",required = True)
    args = parser.parse_args
    stop_words_path = args.stop_words_path
    csv_path = args.csv_path
    save_path = args.save_path

    stop_words = get_stop_words(stop_words_path)
    lac = LAC(mode='lac')
    need_words_type = ["n","PER","LOC","ORG","a","f","s","nw","nz","v","vd","vb","vd","vn","TIME"]
    df = pd.read_csv(csv_path)
    text_lists = df["text"].to_list()
    for i,text in enumerate(text_lists):
        lac_result = lac.run(text)
        num_useful_words = 0
        useful_words = ""
    
        for n in range(len(lac_result[0])):
            if n in stop_words or lac_result[1][n] not in need_words_type:
                continue
            else:
                useful_words += lac_result[0][n] + " "
                num_useful_words += 1
        df.loc[i,"num_useful_char"] = len(useful_words.replace(" ",""))
        df.loc[i,"num_useful_words"] = num_useful_words
        df.loc[i,"useful_words"] = useful_words
  df.to_csv(save_path,index=False)

if __name__ == "__main__":
    main()

