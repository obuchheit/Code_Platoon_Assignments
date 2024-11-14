import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_sub():
    assert calculator.calculate(10, 5, 'subtract') == 5

def test_multi():
    assert calculator.calculate(2, 10, 'multiply') == 20

def test_divide():
    assert calculator.calculate(10, 2, 'divide') == 5

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == ""

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios

