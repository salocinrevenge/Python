#!/usr/bin/env python

from os.path import isfile, join, getsize
from os import listdir
import re
import codecs
from subprocess import DEVNULL, PIPE, run, TimeoutExpired


class BaseTask:
    TIME_LIMIT_SECONDS = 5

    def read_file(self, file_name):
        try:
            with codecs.open(file_name, encoding="utf-8", errors="strict") as f:
                return f.read()
        except ValueError:
            raise ValueError(f"Enconding inválido em {file_name}. Por favor, use UTF-8.")
        except:
            return ""

    def has_size(self, file_name, size):
        file_size = getsize(file_name)
        assert file_size >= size, f"{file_name} deve ter pelo menos {size} bytes"

    def count_words(self, text):
        words = text.split()
        number_of_words = len(words)
        return number_of_words

    def has_n_words(self, file_name, n_words):
        try:
            text = self.read_file(file_name)
            assert (
                self.count_words(text) >= n_words
            ), f"{file_name} deve ter pelos menos {n_words} palavras"
        except ValueError:
            raise AssertionError(f"Encoding inválido em {file_name}. Use UTF-8.")

    def compare_stripped(self, left, right):
        return left.strip() == right.strip()

    def compare_files(self, out, res):
        left = self.read_file(out)
        right = self.read_file(res)
        return self.compare_stripped(left, right)

    def test_case(self, script, in_file_name):
        out_file_name = in_file_name.replace(".in", ".out")
        res_file_name = in_file_name.replace(".in", ".res")
        cmd = f"python3 {script} < {in_file_name} > {out_file_name}"
        with open(in_file_name) as i, open(out_file_name, "w") as o:
            try:
                p = run(
                    ["python3", script],
                    stdin=i,
                    stdout=o,
                    stderr=DEVNULL,
                    encoding="utf8",
                    errors="ignore",
                    timeout=self.TIME_LIMIT_SECONDS,
                )
            except TimeoutExpired:
                assert False, f"comando {cmd} excedeu o tempo limite de {self.TIME_LIMIT_SECONDS}s"
        assert p.returncode == 0, f'falha ao executar "{cmd}"'
        assert self.compare_files(
            out_file_name, res_file_name
        ), f'{in_file_name}: arquivos "{out_file_name}" "{res_file_name}" diferem'

    def exists(self, file_name):
        assert isfile(file_name), f"você deve criar um arquivo {file_name}"

    def run(self, all=False):
        for name in sorted(dir(self)):
            if not name.startswith("teste_"):
                continue
            try:
                test = getattr(self, name)
                test()
                print(f"{name}: OK")
            except AssertionError as e:
                print(f"{name}: FALHOU\n  -> {e}")
                if not all:
                    return


class Task(BaseTask):
    def teste_0(self):
        script = "arvore.py"
        self.exists(script)
        self.test_case(script, join("testes", "arvore0.in"))

    def teste_1(self):
        script = "arvore.py"
        self.exists(script)
        self.test_case(script, join("testes", "arvore1.in"))


if __name__ == "__main__":
    Task().run()
