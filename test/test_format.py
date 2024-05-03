from subprocess import PIPE, Popen


def _process(command):
    p = Popen(command, stdout=PIPE, stdin=PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        return False
    return True


def test_black():
    assert _process(["black", "--check", "./filtered_ie23_py"])


def test_flake8():
    assert _process(["flake8", "./filtered_ie23_py"])


def test_pydoctstyle():
    assert _process(["pydocstyle", "./filtered_ie23_py"])