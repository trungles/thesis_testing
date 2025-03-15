import bigO
from functools import wraps
import numpy as np
import time
import random
import json

def experiment_wrapper(length_func = None, time_bound = None, 
                       generate_func = None, sample_size = None,
                       max_input_size = None, sampling_method = None,
                       run_type = None, repetition = None):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            bigO.save_performance_data()

            bigO.set_performance_data_filename(f"data/{func.__module__}-{func.__name__}-{run_type}-{sampling_method}-{time_bound.replace('*','')}-{sample_size}-{repetition}.json")

            # checked_fn = bigO.bounds(length_func, time=time_bound)(func)
            checked_fn = bigO.track(length_func)(func)
            

            lower_bound = 100
            upper_bound = max_input_size

            sample = []

            if sampling_method == "linear_spacing":
                sample = np.linspace(
                    lower_bound,
                    upper_bound - 1,
                    min(sample_size, upper_bound - lower_bound),
                    dtype=int
                )
            
                # if the range is very small and we need to resample from among the small sample
                while len(sample) < sample_size:
                    sample = np.append(sample, sample)
                sample = sample[0:sample_size]

            elif sampling_method == "random_spacing":
                sample = []
                for _ in range(sample_size):
                    sample.append(random.randint(lower_bound, upper_bound - 1))

            for i, num in enumerate(sample):
                if False:
                    print(f"iter: {i} len: {num}")

                args, kwargs = generate_func(num)
                # start = time.perf_counter()
                checked_fn(*args, **kwargs)
                # runtime = time.perf_counter() - start                
                

                # max_used_index = i

            # results = bigO.bigO.check(func)
            # # there are only multiple results when dealing with memory and time
            # # TODO: if testing memory, need to adjust this 
            # for result in results:                    
            #     if not result.success:
            #         write_out(func = func, sampling_method=sampling_method,
            #               max_input_size_used = sample[max_used_index], max_elapsed_time=max_runtime,
            #               specified_bound=time_bound, actual_bound= result.message.split(" ")[-1][:-1], # gets the best bound out of the message
            #               success=result.success, message=result.message, 
            #               details = result.details, warnings = result.warnings)
            #     else:
            #         write_out(func = func, sampling_method=sampling_method,
            #               max_input_size_used = sample[max_used_index], max_elapsed_time=max_runtime,
            #               specified_bound=time_bound, actual_bound=time_bound,
            #               success=result.success, message=result.message, 
            #               details = result.details, warnings = result.warnings)

            return
                
        return wrapper
    return decorator

def write_out(func = None, sampling_method = None,
              max_input_size_used = None, max_elapsed_time = None,
              specified_bound = None, actual_bound = None,
              success = None, message = None, details = None,
              sampling_size = None, warnings = None):
     with open("experiment_data.json") as data:
        info = {
            "function_name" : func.__name__,
            "sampling_method" : sampling_method,
            "sampling_size" : sampling_size,
            "max_input_size_used" : max_input_size_used,
            "max_elapsed_time" : max_elapsed_time, 
            "specified_bound" : specified_bound,
            "actual_bound" : actual_bound,
            "success" : success,
            "message" : message,
            "details" : details,
            "warnings" : warnings
        }
        # make a global array
        # just write to JSON once
        # and load the massive array
        print(info)

# go back to having a maximum size
# put a cap: no test should take more than a certain time
#   if we have an exponential function and it takes forever, then we catch it quickly 
#   and don't waste too much time 
