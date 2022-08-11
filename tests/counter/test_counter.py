from src.counter import count_ocurrences


def test_counter():
    file_path = "src/jobs.csv"

    assert count_ocurrences(file_path, "developer") == 352
    assert count_ocurrences(file_path, "pepino") == 0
    assert count_ocurrences(file_path, "salesforce") == 646
    assert count_ocurrences(file_path, "alface") == 0
