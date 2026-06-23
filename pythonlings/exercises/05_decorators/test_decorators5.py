from decorators5 import hello, bold, italic


def test_hello_output():
    assert hello() == "<b><i>hello</i></b>"

def test_bold_wraps_italic():
    @bold
    @italic
    def greet():
        return "hi"
    assert greet() == "<b><i>hi</i></b>"
