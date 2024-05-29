import pandas as pd
import os
from sklearn.model_selection import train_test_split
import ndjson

def validation_split(df: pd.DataFrame, col_target: str, val_size: float = 0.2):
    df_train, df_val = train_test_split(df, stratify=df[col_target], test_size=val_size, random_state=43)

def read_data(root_dir: str, pd_file_name:str)->pd.Dataframe:
    return pd.read_csv(os.path.join(root_dir, pd_file_name))

def build_image_detail(row):
    return {
        "format":"png",
        "width": row['Width'],
        "height": row['Height'],
    }

def create_image_json_df(df: pd.DataFrame,datastore_root_dir:str)->pd.DataFrame:
    df["image_url"]=df["Path"].apply(lambda p: datastore_root_dir+p)
    df["label"]=df["ClassId"].astype(pd.StringDtype())
    df["image_details"]=df.apply(build_image_detail,axis=1)
    return df[[ "image_url","image_details", "label"]]

def save_jsonl_df(df_json: pd.DataFrame,path:str):
    json_data=df_json.to_dict('records')
    with open(path, 'w') as f:
        ndjson.dump(json_data, f,ensure_ascii=False)


def build_automl_json_file(df: pd.DataFrame,datastore_root_dir:str, local_path:str):
    json_df=create_image_json_df(df,datastore_root_dir)
    save_jsonl_df(json_df, local_path)











