from madlib_cli.madlib import parse

def test_parse():
    actual = parse("A {Adjective} and {Adjective} {Noun}")
    expected = ['Adjective','Adjective','Noun']
    assert actual == expected