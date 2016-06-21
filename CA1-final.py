import sys


def computepay(hours, rate, ot, tax):  # we must define a function to compute our pay

    try:
        hours = float(hours)
        rate = float(rate)
        ot = float(ot)
        tax = float(tax)

    except ValueError:
        print "please enter a valid input"
        sys.exit(1)

    if float(tax) >= 1: # To prevent greater than 100% tax
        print "Tax rate not found, try again"

    if hours > 40:
        overtime_hours = hours - 40  # hours over 40
        hours -= overtime_hours  # regular rate hours
        overtime_pay = overtime_hours * ot
        gross_pay = (hours * rate) + overtime_pay
        net_pay = gross_pay * tax
        deduction = gross_pay - net_pay
        return [gross_pay, net_pay, deduction]  # Returns a list of the variables needed

    else:    # This condition is for calculating pay if there are no overtime hours
        gross_pay = hours * rate
        net_pay = gross_pay * tax
        deduction = gross_pay - net_pay

        return [gross_pay,net_pay, deduction]


if __name__ == "__main__":  # This line allows the function to be imported into another project without raw inputs
    Name = raw_input('Please enter your Name: ')
    hours = raw_input("Enter Hours: ")
    rate = raw_input("Enter Rate: ")
    OVERTIME_RATE = raw_input('Please enter overtime rate: ')
    tax = raw_input('Please enter your tax rate: ')
    answer = computepay(hours, rate, OVERTIME_RATE, tax)

    print "Name: %s \n Gross Pay: %s \n Deduction:%s \n Net Pay:%s \n" % (Name, answer[0], answer[1], answer[2])

