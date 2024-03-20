import Calculate

class TestCalculator:

    def test_addition(self):
        assert 4 == Calculate.add(2, 2)


    def test_addition_secon(self):
        assert 5 == Calculate.add(3, 2)

    def test_subtraction(self):
        assert 2 == Calculate.subtract(4, 2)

    def test_ErrorAddition(self):
        assert 4 == Calculate.add(2, 2)

    def test_subtraction(self):
        assert 2 == Calculate.subtract(4, 2)

