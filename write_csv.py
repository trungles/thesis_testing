import pandas as pd
import json

with open("data/analyzed.json", 'r') as data:
    res_dict = json.load(data)

    df_dict = {
        "single_or_batch" : [],
        "spacing_type" : [],
        "sample_size" : [],
        "actual_bound" : [],
        "specified_bound" : [],
        "reported_match_rate" : []
    }

    for key in res_dict['keys']:

        info = key.split('-')

        df_dict['single_or_batch'].append(info[0])
        df_dict['spacing_type'].append(info[1]) 
        df_dict['sample_size'].append(info[2]) 
        df_dict['actual_bound'].append(info[3]) 
        df_dict['specified_bound'].append(info[4]) 
        df_dict['reported_match_rate'].append(res_dict.get(key + "successes", 0) / res_dict[key + "attempts"])

    df = pd.DataFrame(df_dict)

    df.to_csv('data/res.csv')
