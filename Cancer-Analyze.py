import random


class SampleData:

    def __init__(self, size=100):
        self.data = [random.randint(1, 100) for _ in range(size)]

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        middle = n // 2

        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def get_mode(self):
        from collections import Counter
        data_counter = Counter(self.data)
        mode_value = data_counter.most_common(1)[0][0]
        return mode_value


class DataAnalyzer:

    def __init__(self, sample_data):
        self.sample_data = sample_data

    def perform_analysis(self):
        mean = self.sample_data.get_mean()
        median = self.sample_data.get_median()
        mode = self.sample_data.get_mode()

        return {'mean': mean, 'median': median, 'mode': mode}


sample_data = SampleData()
data_analyzer = DataAnalyzer(sample_data)

analysis_results = data_analyzer.perform_analysis()
print(analysis_results)
