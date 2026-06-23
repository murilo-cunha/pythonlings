import os
from uuid import uuid4

import pytest

from pythonlings import __version__
from pythonlings.display import build_layout
from pythonlings.domain.exercises import Exercise
from pythonlings.services.exercises import get_exercises_root


def _sample_exercise(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_sample_success.py")
    return Exercise(epath)


def test_version():
    assert __version__ == "0.1.0"


def test_get_exercises_root_success():
    get_exercises_root()


def test_get_exercises_root_fail(mocker):
    invalid_dir = uuid4().hex
    mocker.patch("os.getcwd", return_value=invalid_dir)
    with pytest.raises(FileNotFoundError):
        get_exercises_root()


def test_exercise_success(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_sample_success.py")
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is False
    assert exercise.to_do is False
    assert bool(exercise) is True


def test_exercise_to_do(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_sample_to_do.py")
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.to_do is True
    assert bool(exercise) is True


def test_exercise_fail(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_sample_fail.py")
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is True
    assert exercise.to_do is False
    assert bool(exercise) is False


def test_exercise_with_companion_test(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_with_test.py")
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is False
    assert exercise.to_do is False
    assert bool(exercise) is True


def test_exercise_companion_test_fails(fixtures_dir):
    epath = os.path.join(fixtures_dir, "1_examples", "exercise_with_failing_test.py")
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is True
    assert bool(exercise) is False


def test_build_layout_compact_drops_code(fixtures_dir):
    layout = build_layout(_sample_exercise(fixtures_dir), 1, 89, watching=True, height=10)
    names = [c.name for c in layout.children]
    assert "code" not in names
    assert "status" in names
    assert "footer" in names


def test_build_layout_full_includes_code(fixtures_dir):
    layout = build_layout(_sample_exercise(fixtures_dir), 1, 89, watching=True, height=40)
    names = [c.name for c in layout.children]
    assert "code" in names


def test_build_layout_hint_region(fixtures_dir):
    ex = _sample_exercise(fixtures_dir)
    with_hint = build_layout(ex, 1, 89, watching=True, height=40, hint_text="x")
    without_hint = build_layout(ex, 1, 89, watching=True, height=40, hint_text=None)
    assert "hint" in [c.name for c in with_hint.children]
    assert "hint" not in [c.name for c in without_hint.children]
