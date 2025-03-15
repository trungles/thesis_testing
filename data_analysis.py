import os
import json
import bigO
import numpy as np
import pandas as pd
from IPython.display import display

# the implementation in bigO relies on a function object
# this just relies on having the data
def custom_check(data : dict = None, function_name = None, file_name = None):
    # normally, we get this using hashing and function name and whatnot
    # but there's only one function per file
    full_name = list(data.keys())[0]
    tests = data[full_name]['tests']

    # _gather_function_data()
    records = [
        r for r in data[full_name]['observations']
    ]
    lengths = [r['length'] for r in records]
    times = [r['time'] for r in records]
    mems = [r['memory'] for r in records]

    function_data = bigO.FunctionData(
        function_name = function_name,
        file_name = file_name,
        lengths = np.array(lengths),
        times = np.array(times),
        mems = np.array(mems),
    )
    

    # check()
    results = []

    if "mem_bound" in tests or "time_bound" in tests:
        check = bigO.CheckBounds(
            function_data, tests.get("time_bound", None), tests.get("mem_bound", None)
        )
        result = check.run()
        results += [result]

    return results[0]



if __name__ == "__main__":
    # need to read in the JSON data for every file in data
    # change the 'tests' object to the target bound, and then run bigO.check
    # then report the result
    # gather it into a big array and turn it into a table
    # the table will be using a pandas dataframe
    # look into the pandas dataframe before I start storing results

    directory_path = 'data'

    keys = set()
    res_dict = {}

    for entry in os.scandir(directory_path):
        # entry.path gives me the filename
        filename = entry.path
        if '.json' not in filename or 'unanalyzed' in filename:
            continue

        with open(filename) as file:
            data = json.load(file) # data is a dictionary
            full_name = list(data.keys())[0]
            tests = data[full_name]["tests"]
            # run information is stored in the file name
            title = filename[:-5].split('-')
            file_info = {
                "program_filename" : title[0],
                "function_name" : title[1],
                "single_or_batch" : title[2],
                "spacing_type" : title[3],
                "actual_runtime" : title[4],
                "sample_size" : title[5],
                "trial_number" : title[6],
            }

            considered_bounds = ["O(1)", "O(log(n))", "O(n)", "O(n*log(n))", "O(n**2)"]


            for bound in considered_bounds:
                tests.update({"time_bound" : bound})
                
                res = custom_check(data)

                key = f"{file_info['single_or_batch']}-{file_info['spacing_type']}-{file_info['sample_size']}-{file_info['actual_runtime']}-{bound}"

                keys.add(key)

                if res.success:
                    if res_dict.get(key + "successes") == None:
                        res_dict.update({key + "successes" : 1})
                    # increment success counter 
                    else:
                        res_dict.update({key + "successes" : res_dict[key + "successes"] + 1})

                # increment total iterations
                if res_dict.get(key + "attempts") == None: 
                    res_dict.update({key + "attempts" : 1})
                else: 
                    res_dict.update({key + "attempts" : res_dict[key + "attempts"] + 1})
    
    res_dict.update({"keys" : list(keys)})

    with open("data/unanalyzed.json", 'w') as outfile:
        json_object = json.dumps(res_dict)
        outfile.write(json_object)

    
