""""kkk"""# Functions | Assignment-1 - Paying Debt off in a Year
def payingdebtoff_inayear(balance_, annual_interest_rate_, monthly_payment_rate_):
    """kkk"""
    mir_ = annual_interest_rate_ / 12
    i = 0
    for i in range(1, 13):
        mir_ = annual_interest_rate_ / 12
        mmp_ = monthly_payment_rate_ * balance_
        mub_ = balance_ - mmp_
        ubem_ = mub_ + mir_ * mub_
        balance_ = ubem_
    return round(ubem_, 2)
def main():
    """kk"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", payingdebtoff_inayear(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
