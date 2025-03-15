import nanobenchmarks_single
import nanobenchmarks_batch



if __name__ == "__main__":

    num_repetitions = 100

    for i in range(num_repetitions):
        # random spacing tests, single run

        nanobenchmarks_single.main(sample_size = 25, sampling_method = "random_spacing", repetition = i+1)
        nanobenchmarks_single.main(sample_size = 50, sampling_method = "random_spacing", repetition = i+1)
        nanobenchmarks_single.main(sample_size = 75, sampling_method = "random_spacing", repetition = i+1)

        # # linear spacing tests, single run

        nanobenchmarks_single.main(sample_size = 25, sampling_method = "linear_spacing", repetition = i+1)
        nanobenchmarks_single.main(sample_size = 50, sampling_method = "linear_spacing", repetition = i+1)
        nanobenchmarks_single.main(sample_size = 75, sampling_method = "linear_spacing", repetition = i+1)

        # random spacing tests, batch run

        nanobenchmarks_batch.main(sample_size = 25, sampling_method = "random_spacing", repetition = i+1)
        nanobenchmarks_batch.main(sample_size = 50, sampling_method = "random_spacing", repetition = i+1)
        nanobenchmarks_batch.main(sample_size = 75, sampling_method = "random_spacing", repetition = i+1)

        # # linear spacing tests, batch run

        nanobenchmarks_batch.main(sample_size = 25, sampling_method = "linear_spacing", repetition = i+1)
        nanobenchmarks_batch.main(sample_size = 50, sampling_method = "linear_spacing", repetition = i+1)
        nanobenchmarks_batch.main(sample_size = 75, sampling_method = "linear_spacing", repetition = i+1)
