from experiment_wrapper import experiment_wrapper
import math
# python does not optimize nothing loops

batch_run_number = 10

# @experiment_wrapper(length_func= lambda n: int(n), time_bound="O(1)", 
#                     generate_func= lambda n: ([n], {}), sample_size=25, 
#                     max_input_size= 100000, sampling_method="single-run")
def constant(n):
    for _ in range(batch_run_number):
        x = 1
    return


# @experiment_wrapper(length_func= lambda n: int(n), time_bound="O(log(n))", 
#                     generate_func= lambda n: ([n], {}), sample_size=25, 
#                     max_input_size= 100000, sampling_method="single-run")
def logn(n):
    for _ in range(batch_run_number):
        for _ in range(math.ceil(math.log(n))):
            x = 1
    return


# @experiment_wrapper(length_func= lambda n: int(n), time_bound="O(log(n))", 
#                     generate_func= lambda n: ([n], {}), sample_size=25, 
#                     max_input_size= 100000, sampling_method="single-run")
def linear(n):
    for _ in range(batch_run_number):
        for _ in range(n):
            x = 1
    return


# @experiment_wrapper(length_func= lambda n: int(n), time_bound="O(n*log(n))", 
#                     generate_func= lambda n: ([n], {}), sample_size=25, 
#                     max_input_size= 100000, sampling_method="single-run")
def nlogn(n):
    for _ in range(batch_run_number):
        for _ in range(math.ceil(n * math.log(n))):
            x = 1
    return


# @experiment_wrapper(length_func= lambda n: int(n), time_bound="O(n**2)", 
#                     generate_func= lambda n: ([n], {}), sample_size=75, 
#                     max_input_size= 100000, sampling_method="single-run")
def n2(n):
    for _ in range(batch_run_number):
        for _ in range(n**2):
            x = 1
        return
    
def main(sample_size = None, sampling_method = None, repetition = None):

    constant_wrapped = experiment_wrapper(length_func= lambda n: int(n), time_bound="O(1)", 
                    generate_func= lambda n: ([n], {}), sample_size=sample_size, 
                    max_input_size= 5000, sampling_method=sampling_method, run_type = "batch_run",
                    repetition=repetition)(constant)
    
    logn_wrapped = experiment_wrapper(length_func= lambda n: int(n), time_bound="O(log(n))", 
                    generate_func= lambda n: ([n], {}), sample_size=sample_size, 
                    max_input_size= 5000, sampling_method=sampling_method, run_type = "batch_run",
                    repetition=repetition)(logn)
    
    n_wrapped = experiment_wrapper(length_func= lambda n: int(n), time_bound="O(n)", 
                    generate_func= lambda n: ([n], {}), sample_size=sample_size, 
                    max_input_size= 5000, sampling_method=sampling_method, run_type = "batch_run",
                    repetition=repetition)(linear)
    
    nlogn_wrapped = experiment_wrapper(length_func= lambda n: int(n), time_bound="O(n*log(n))", 
                    generate_func= lambda n: ([n], {}), sample_size=sample_size, 
                    max_input_size= 5000, sampling_method=sampling_method, run_type = "batch_run",
                    repetition=repetition)(nlogn)
    
    n2_wrapped = experiment_wrapper(length_func= lambda n: int(n), time_bound="O(n**2)", 
                    generate_func= lambda n: ([n], {}), sample_size=sample_size, 
                    max_input_size= 5000, sampling_method=sampling_method, run_type = "batch_run",
                    repetition=repetition)(n2)

    constant_wrapped()
    logn_wrapped()
    n_wrapped()
    nlogn_wrapped()
    n2_wrapped()
    

if __name__ == "__main__":
    constant()
    logn()
    linear()
    nlogn()
    n2()
