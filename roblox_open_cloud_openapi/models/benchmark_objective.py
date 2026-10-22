from enum import StrEnum


class BenchmarkObjective(StrEnum):
    BENCHMARK_OBJECTIVE_INVALID = "BENCHMARK_OBJECTIVE_INVALID"
    BENCHMARK_OBJECTIVE_MAXIMIZE = "BENCHMARK_OBJECTIVE_MAXIMIZE"
    BENCHMARK_OBJECTIVE_MINIMIZE = "BENCHMARK_OBJECTIVE_MINIMIZE"

    def __str__(self) -> str:
        return str(self.value)
