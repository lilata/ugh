import re


def check_password(p: str):
    if len(p) < 6:
        return False
    if re.search(r"[` ~!@#$%^&*()_+{}|?\[\]/\\.,<>;\':-=" + r'"]', p) is None:
        return False
    return True