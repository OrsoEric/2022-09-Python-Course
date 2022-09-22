#format is called when using : after the variable

class Try:
    def __init__(self):
        self._s_str = "shaka"

    def __format__(self, __format_spec: str) -> str:
        return __format_spec

my = Try()
print(f">>{my:q}<< Shaka")