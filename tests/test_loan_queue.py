import unittest
from financetools import Loan, LoanQueue

class LoanQueueTest(unittest.TestCase):
  def setUp(self):

    self.budget = 1200
    self.loans = [
      Loan(2406.65, 4.41, title="2014", term=120),
      Loan(2472.91, 3.61, title="2013", term=120),
      Loan(6282.30, 6.1, title="2012", term=120),
      Loan(5930.42, 6.1, title="2011", term=120)
    ]

    # Start our primary queue and display
    self.loan_queue = LoanQueue(self.loans, self.budget, title="Test Loans")
  
  def test_avalanche(self):
    avalanche = self.loan_queue.avalanche()
    avalanche.display_info()
    self.assertEqual(avalanche.get_duration(), 18)
    self.assertEqual(avalanche.get_num_payments(), 51)
    self.assertEqual(avalanche.get_interest_paid(), Loan.Dec(621.40))
    self.assertEqual(avalanche.get_percent_principal(), Loan.Dec(96.49))
  
  def test_cascade(self):
    cascade = self.loan_queue.cascade()
    cascade.display_info()
    self.assertEqual(cascade.get_duration(), 16)
    self.assertEqual(cascade.get_num_payments(), 53)
    self.assertEqual(cascade.get_interest_paid(), Loan.Dec(645.79))
    self.assertEqual(cascade.get_percent_principal(), Loan.Dec(96.36))

  def test_ice_slide(self):
    ice_slide = self.loan_queue.ice_slide()
    ice_slide.display_info()
    self.assertEqual(ice_slide.get_duration(), 15)
    self.assertEqual(ice_slide.get_num_payments(), 60)
    self.assertEqual(ice_slide.get_interest_paid(), Loan.Dec(613.80))
    self.assertEqual(ice_slide.get_percent_principal(), Loan.Dec(96.53))

  def test_blizzard(self):
    blizzard = self.loan_queue.blizzard()
    blizzard.display_info()
    self.assertEqual(blizzard.get_duration(), 18)
    self.assertEqual(blizzard.get_num_payments(), 66)
    self.assertEqual(blizzard.get_interest_paid(), Loan.Dec(591.13))
    self.assertEqual(blizzard.get_percent_principal(), Loan.Dec(96.66))

  def test_snowball(self):
    snowball = self.loan_queue.snowball()
    snowball.display_info()
    self.assertEqual(snowball.get_duration(), 18)
    self.assertEqual(snowball.get_num_payments(), 39)
    self.assertEqual(snowball.get_interest_paid(), Loan.Dec(808.22))
    self.assertEqual(snowball.get_percent_principal(), Loan.Dec(95.48))

if __name__ == "main":
  unittest.main()
