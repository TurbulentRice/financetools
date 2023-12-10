from financetools import Loan, LoanQueue, LoanQueueCompare
import random

############
#   MAIN
############
if __name__ == "__main__":

	def get_rand_budg():
		return random.uniform(800, 2000)

	def get_rand_loans(n):
		def r_bal():
			return random.uniform(2000, 25000)
		def r_ir():
			return random.uniform(1, 12)
		def r_term():
			return random.randint(12, 360)
		return [Loan(r_bal(), r_ir(), term=r_term()) for i in range(n)]

	##########################################

	# Random example
	my_budget = get_rand_budg()
	my_loans = get_rand_loans(4)

	##########################################

	# Start our primary queue and display
	my_Queue = LoanQueue(my_loans, my_budget, title="My Loans")
	my_Queue.display_info()

	# Get a new paid-off queue for each repayment mehtod, sort
	avalanche = my_Queue.avalanche().prioritize()
	cascade = my_Queue.cascade().prioritize()
	ice_slide = my_Queue.ice_slide().prioritize()
	blizzard = my_Queue.blizzard().prioritize()
	snowball = my_Queue.snowball().prioritize()

	# Get a LoanQueue instance from a single loan, paid-off five different ways
	# Compare how each repayment method payed off a single loan

	# single_loan_queue = LoanQueue([
	# 	avalanche.Q[0], cascade.Q[0], ice_slide.Q[0], blizzard.Q[0], snowball.Q[0]
	# ], my_budget)

	# Get a LoanQueueCompare instance from the paid-off queues, sorted by interest
	# Compare how each repayment method payed off each loan

	# Equivalent to: my_Queue.finish()
	my_LoanQueueCompare = LoanQueueCompare([
		avalanche, cascade, ice_slide, blizzard, snowball
	])
	my_LoanQueueCompare.order_by('interest')
