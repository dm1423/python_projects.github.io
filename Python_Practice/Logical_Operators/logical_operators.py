# if applicant has high income AND good credit
# Eligible for loan

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

#If applicant has good credit AND doesn't have a criminal record, then eligible

good_credit = True
criminal_record = False

if good_credit and not criminal_record:
    print("Eligible for Loan")
else:
    print("Not eligible")


# AND: Both
# OR: at least one
# NOT: both conditions need to be met