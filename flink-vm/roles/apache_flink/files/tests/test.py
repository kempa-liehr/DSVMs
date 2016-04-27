from __future__ import print_function
from subprocess import check_call
import unittest


class TestFlink(unittest.TestCase):
  """
  This class contains tests for apache flinks functionality.
  Assumptions:
    (1) Flink is up and running
    (2) pyflink2.sh is in PATH
    (3) the examples used for testing are found in ./examples
    (4) their results will be written back to ./result.txt
  """

  def get_result(self):
    with open('result.txt', 'r') as f:
      result = float(f.read())

  def run_parallel(self):
    check_call('pyflink2.sh examples/local_mae.py', shell=True)
    return self.get_result()

  def run_no_parallel(self):
    check_call('pyflink2.sh examples/local_mae_no_parallel.py', shell=True)
    return self.get_result()

  def test_equal(self):
    """
    Test if the results of running the mae example with parallelism or without are equal
    """
    res_parallel = self.run_parallel()
    res_no_parallel = self.run_no_parallel()
    self.assertEqual(res_no_parallel, res_parallel)


if __name__ == '__main__':
  unittest.main()
