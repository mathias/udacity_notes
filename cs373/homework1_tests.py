import unittest

class HomeworkOneTesting(unittest.TestCase):
  # def runTest(self):
    # assert p = expected_p, 'results do not match'

  def testExample1(self):
    # Setup -should probably be a fixture
    colors = [['green', 'green', 'green'],
              ['green', 'red', 'green'],
              ['green', 'green', 'green']]

    measurements = ['red']

    motions=[[0,0]]

    sensor_right = 1.0
    p_move = 1.0

    expected_p = [[0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0]]

    # actually run our code:
    p = run_probabilities()

    assert p = expected_p, 'p does not match expected'

  def testExample2(self):

    expected_p = [[0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0]]

    # actually run our code:
    p = run_probabilities()

    assert p = expected_p, 'p does not match expected'

  def testExample3(self):

    expected_p = [[0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0]]

    # actually run our code:
    p = run_probabilities()

    assert p = expected_p, 'p does not match expected'

  def testExample4(self):

    expected_p = [[0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0]]

    # actually run our code:
    p = run_probabilities()

    assert p = expected_p, 'p does not match expected'

  def testExample5(self):

    expected_p = [[0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0]]

    # actually run our code:
    p = run_probabilities()

    assert p = expected_p, 'p does not match expected'


