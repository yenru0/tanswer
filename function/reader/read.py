import re
from typing import List, Dict

from function.reader.exceptions import ReaderWrongException


class Reader:
    def __init__(self, src: str):
        self.src: str = src
        self.src_size: int = len(src)
        self.src_iter: List[str] = []

        self.scope_default = "main"

        self._name: str = None
        self._description: str = ""
        self._variables = {}

        self._stages: Dict[str, list] = {'main': []}

    def read(self):
        self.preprocess()
        self.parse()

        ### post
        for k in list(self._stages.keys()):
            if not self._stages[k]:
                del self._stages[k]

    def preprocess(self) -> None:
        """
        pre-processing (e.g. delete comment, make src_iter)
        :return: Void
        """
        self.preprocess_comment()
        self.src_iter = self.src.split("\n")

    def preprocess_comment(self) -> None:
        """
        process \# escape & delete comment
        :return: Void
        """
        pattern_sharp = re.compile(r"\\#")
        pattern_comment = re.compile(r"###.*")

        self.src = pattern_sharp.sub("%§%SHP%§%", self.src)
        self.src = pattern_comment.sub("", self.src)

        self.src = self.src.replace("%§%SHP%§%", "#")

    def parse(self):
        """
        parse based on src_iter
        :return: Void
        """
        scope = self.scope_default
        for i, s in enumerate(self.src_iter):
            if not s.strip():
                continue

            t = self.parse_stage(s, i)
            if t is not False:
                scope = t
                if scope not in self._stages:
                    self._stages[scope] = []
                continue

            t = self.parse_command(s, i)
            if t is not False:
                continue

            t = self.parse_element(s, i)
            if t is not False:
                self._stages[scope].append(t)
                continue

            raise ReaderWrongException(f"unexpected expression: something wrong")

    def parse_stage(self, s: str, ln: int) -> [str, bool]:
        """
        parse stage starting with '##@'
        :param s: line string
        :param ln: line number
        :return: stage name or False
        """
        pattern_stage = re.compile(r"##@(.*)")
        t = pattern_stage.match(s)
        if not t:
            return False

        if not t.group(1).strip():
            return self.scope_default
        else:
            return t.group(1).strip()

    def parse_command(self, s: str, ln: int):
        """
        parse command starting with '##!'
        :param s: line string
        :param ln: line number
        :return: True or False
        """
        pattern_command = re.compile(r"##!(.*)")
        t = pattern_command.match(s)
        if not t:
            return False
        else:
            return True

    def parse_element(self, s: str, ln: int):
        """
        parse element
        :param s: line string
        :param ln: line number
        :return: recursive List that contains element itself or False
        """
        L1 = s.split(":")
        if len(L1) < 2:
            return False
        elif L1[0] and L1[1]:
            return [[[l.strip() for l in filter(None, l3.split(";"))] for l3 in filter(None, l2.split("|"))] for l2 in
                    L1[:2]]
        else:
            return False

    @property
    def structure(self) -> dict:
        """
        convert information of this reader to dictionary to be processed easily in ADS.
        keys:
        | name
        | description
        | detail_infile
        | cond
        | stages
        :return: dict
        """
        return {
            "stages": self._stages
        }


if __name__ == '__main__':
    r = Reader("""

##@ 결단력S
word: 단어; 바이트
##@ 킹단력K ### 주석
byte: 바이트;
biden: 바이든 주석 각하
##@ 스페시컬<T>

""")

    r.read()
    print(r.src_iter)
    print(r.structure)
