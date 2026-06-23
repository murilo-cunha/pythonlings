import os
import subprocess as subp
import sys
from abc import ABC, abstractmethod
from enum import Enum, auto

import i18n

_ = i18n.t


class ExerciseKind(Enum):
    NORMAL = auto()
    PYTEST_MODULE = auto()


class BaseExercise(ABC):
    @abstractmethod
    def is_not_done(self):
        ...

    @abstractmethod
    def process(self) -> None:
        ...

    def __str__(self) -> str:
        raise NotImplementedError

    def __bool__(self) -> str:
        raise NotImplementedError


class Exercise:
    def __init__(self, filepath=None) -> None:
        self.fp = filepath
        self.error = False
        self.output = None
        self.to_do = None
        self.is_not_done()
        self.package, self.name = self.exercise_metadata()
        self.test_fp = os.path.join(os.path.dirname(self.fp), "test_" + os.path.basename(self.fp))
        self.kind = ExerciseKind.PYTEST_MODULE if self.package == "pytest" else ExerciseKind.NORMAL

    def exercise_metadata(self):
        package = os.path.basename(os.path.dirname(self.fp)).split('_')[1]
        exercise_name = os.path.splitext(os.path.basename(self.fp))[0]
        return package, exercise_name

    def __bool__(self) -> bool:
        return not self.error

    def is_not_done(self) -> bool:
        with open(self.fp, "r") as fp:
            self.to_do = "# I AM NOT DONE" in fp.read()
        return self.to_do

    def process(self) -> None:
        if self.is_not_done():
            return
        if self.kind == ExerciseKind.PYTEST_MODULE:
            cmd = [sys.executable, "-m", "pytest", self.fp, "-v", "--tb=short", "--no-header"]
        elif os.path.exists(self.test_fp):
            cmd = [sys.executable, "-m", "pytest", self.test_fp, "-v", "--tb=short", "--no-header"]
        else:
            cmd = [sys.executable, self.fp]
        r = subp.run(cmd, stdout=subp.PIPE, stderr=subp.PIPE, cwd=os.path.dirname(self.fp))
        self.error = bool(r.returncode)
        self.output = (r.stdout + r.stderr).decode(errors="replace")
