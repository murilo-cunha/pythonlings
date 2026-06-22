import os
import subprocess as subp
import sys
from abc import ABC, abstractmethod

import i18n
from rich.console import Console

_ = i18n.t

console = Console()


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

    def exercise_metadata(self):
        package = os.path.basename(os.path.dirname(self.fp)).split('_')[1]
        exercise_name = os.path.splitext(os.path.basename(self.fp))[0]
        return package, exercise_name

    def __str__(self) -> str:
        hint = _(f'{self.package}.{self.name}')
        error_msg = f""""{self.fp} [{_('p.error_flag')}]
        {hint}
        {self.output}
        """
        success_msg = f"""{self.fp} [{_('p.success_flag')}]!
        """
        makeitpass_msg = f""""{self.fp} [{_('p.make_it_pass_flag')}]!
        {hint}
        """
        if self.to_do:
            return makeitpass_msg

        return error_msg if self.error else success_msg

    def __bool__(self) -> bool:
        """Bool protocol for class
        Returns:
            bool: True if the exercise pass, False otherwise.
        """
        return not self.error

    def is_not_done(self) -> bool:
        with open(self.fp, "r") as fp:
            self.to_do = "# I AM NOT DONE" in fp.read()
        return self.to_do

    def process(self) -> None:
        if self.is_not_done():
            return
        command = [sys.executable, self.fp]
        r = subp.run(command, stdout=subp.PIPE, stderr=subp.PIPE)
        self.error = bool(r.returncode)
        self.output = r.stderr if self.error else r.stdout
        self.output = self.output.decode()
