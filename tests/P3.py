import os
import importlib.util
import pytest


def load_module():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'P3', 'enzymes-analyzer.py'))
    spec = importlib.util.spec_from_file_location("enzymes_analyzer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_classify_activity_boundaries():
    m = load_module()
    assert m.classify_activity(39.9) == 'low'
    assert m.classify_activity(40) == 'normal'
    assert m.classify_activity(70) == 'normal'
    assert m.classify_activity(70.1) == 'high'
    assert m.classify_activity(0) == 'low'


def test_analyze_activities_counts_and_stats():
    m = load_module()
    sample = [35, 40, 70, 71, 60]
    res = m.analyze_activities(sample)

    assert res['low_count'] == 1
    assert res['normal_count'] == 3
    assert res['high_count'] == 1

    expected_avg = sum(sample) / len(sample)
    assert res['average_activity'] == pytest.approx(expected_avg)

    assert res['min_activity'] == min(sample)
    assert res['max_activity'] == max(sample)

    # normal values should appear in input order
    assert res['normal_values'] == [40, 70, 60]


def test_analyze_empty_list():
    m = load_module()
    res = m.analyze_activities([])

    assert res['low_count'] == 0
    assert res['normal_count'] == 0
    assert res['high_count'] == 0
    assert res['average_activity'] is None
    assert res['min_activity'] is None
    assert res['max_activity'] is None
    assert res['normal_values'] == []


def test_print_summary_output(capsys):
    m = load_module()
    results = {
        'low_count': 2,
        'normal_count': 3,
        'high_count': 1,
        'average_activity': 55.5,
        'min_activity': 30,
        'max_activity': 80,
        'normal_values': [40, 50, 60]
    }
    m.print_summary(results, total_samples=6)
    captured = capsys.readouterr()
    out = captured.out
    assert 'Enzyme Activity Analysis Summary' in out
    assert 'Total samples: 6' in out
    assert 'Low activity samples: 2' in out
    assert 'Normal activity samples: 3' in out
    assert 'High activity samples: 1' in out
    assert 'Average activity: 55.5 units/mL' in out
    assert 'Highest activity: 80 units/mL' in out
    assert 'Lowest activity: 30 units/mL' in out
    assert 'Normal activity values: [40, 50, 60]' in out


def test_large_repeating_dataset_counts_and_values():
    m = load_module()
    # pattern: low(35), normal(40), normal(70), high(75)
    pattern = [35, 40, 70, 75]
    sample = pattern * 250  # 1000 entries
    res = m.analyze_activities(sample)

    assert res['low_count'] == 250
    assert res['normal_count'] == 500
    assert res['high_count'] == 250
    assert res['min_activity'] == 35
    assert res['max_activity'] == 75
    assert res['normal_values'] == [40, 70] * 250


def test_all_normal_values():
    m = load_module()
    sample = [40, 45, 50, 70, 60]
    res = m.analyze_activities(sample)
    assert res['low_count'] == 0
    assert res['normal_count'] == len(sample)
    assert res['high_count'] == 0
    assert res['min_activity'] == 40
    assert res['max_activity'] == 70


def test_all_low_values():
    m = load_module()
    sample = [0, 10, 39.99, 20]
    res = m.analyze_activities(sample)
    assert res['low_count'] == len(sample)
    assert res['normal_count'] == 0
    assert res['high_count'] == 0
    assert res['average_activity'] == pytest.approx(sum(sample) / len(sample))


def test_all_high_values():
    m = load_module()
    sample = [71, 100, 80]
    res = m.analyze_activities(sample)
    assert res['high_count'] == len(sample)
    assert res['low_count'] == 0
    assert res['normal_count'] == 0


def test_non_integer_and_boundary_floats():
    m = load_module()
    sample = [39.9999, 40.0, 70.0, 70.0001]
    res = m.analyze_activities(sample)
    assert res['low_count'] == 1
    assert res['normal_count'] == 2
    assert res['high_count'] == 1


def test_classify_raises_on_invalid_input():
    m = load_module()
    with pytest.raises(Exception):
        m.classify_activity('not-a-number')

