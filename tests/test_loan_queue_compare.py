import unittest
import random
from financetools import Loan, LoanQueue, LoanQueueCompare

class LoanQueueTest(unittest.TestCase):
  def setUp(self):
    
    self.budget = 750
    self.loans = [
      Loan(3245.65, 4.41, title="2014", term=36),
      Loan(12002.91, 3.61, title="2013", term=120),
      Loan(2481.30, 6.1, title="2012", term=60),
      Loan(5930.42, 6.1, title="2011", term=120)
    ]

    # Start our primary queue and display
    self.loan_queue = LoanQueue(self.loans, self.budget, title="Test Loans")
    # Get a LoanQueueCompare obj
    minimum = 'int'
    self.avalanche, self.cascade, self.blizzard, self.ice_slide, self.snowball = [
      self.loan_queue.avalanche(minimum),
      self.loan_queue.cascade(minimum),
      self.loan_queue.blizzard(minimum),
      self.loan_queue.ice_slide(minimum),
      self.loan_queue.snowball(minimum)
    ]
    self.method_compare = LoanQueueCompare([self.avalanche, self.cascade, self.blizzard, self.ice_slide, self.snowball])

  def test_order_by_interest(self):
    self.method_compare.order_by('interest')
    self.assertLessEqual(self.method_compare.grid[0].get_interest_paid(), self.method_compare.grid[1].get_interest_paid())
    self.assertLessEqual(self.method_compare.grid[1].get_interest_paid(), self.method_compare.grid[2].get_interest_paid())
    self.assertLessEqual(self.method_compare.grid[2].get_interest_paid(), self.method_compare.grid[3].get_interest_paid())
    self.assertLessEqual(self.method_compare.grid[3].get_interest_paid(), self.method_compare.grid[4].get_interest_paid())

  def test_order_by_time(self):
    self.method_compare.order_by('time')
    self.assertLessEqual(self.method_compare.grid[0].get_duration(), self.method_compare.grid[1].get_duration())
    self.assertLessEqual(self.method_compare.grid[1].get_duration(), self.method_compare.grid[2].get_duration())
    self.assertLessEqual(self.method_compare.grid[2].get_duration(), self.method_compare.grid[3].get_duration())
    self.assertLessEqual(self.method_compare.grid[3].get_duration(), self.method_compare.grid[4].get_duration())

  def test_order_by_fewest_payments(self):
    self.method_compare.order_by('num_p')
    self.assertLessEqual(self.method_compare.grid[0].get_num_payments(), self.method_compare.grid[1].get_num_payments())
    self.assertLessEqual(self.method_compare.grid[1].get_num_payments(), self.method_compare.grid[2].get_num_payments())
    self.assertLessEqual(self.method_compare.grid[2].get_num_payments(), self.method_compare.grid[3].get_num_payments())
    self.assertLessEqual(self.method_compare.grid[3].get_num_payments(), self.method_compare.grid[4].get_num_payments())

if __name__ == "main":
  unittest.main()
