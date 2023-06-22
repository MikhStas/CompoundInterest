class CompoundInterest:
    '''
    Represents a compound interest without reinwestments
    and any deposites
    '''
    def __init__(self, initial: float, periods: int, rate_percent: float):
        self.initial = initial
        self.periods = periods
        self.rate = rate_percent / 100
        self.final = None

    def get_final_amount(self):
        self.sub_calc_final()

        return round(self.final, 2)

    def sub_calc_final(self):
        self.final = self.initial * (1 + self.rate*self.periods) 


class ReinvestmentCompoundInterest(CompoundInterest):
    '''
    Represents a compound interest with reinvestments 
    but without deposites
    '''
    def __init__(self, initial: float, periods: int, rate_percent: float, r_times: int):
        super().__init__(initial, periods, rate_percent)
        self.r_times = r_times

    def sub_calc_final(self):
        self.final = self.initial * ((1 + self.rate/self.r_times) ** (self.r_times*self.periods))


class ReinDepCompountInterest(CompoundInterest):
    '''
    Represents a compount interest with reinvestments
    and with deposites
    '''
    pass


if __name__ == '__main__':
    initial_balance = 500_000
    periods = 7
    rate = 10
    
    interest = CompoundInterest(initial_balance, periods, rate)
    final_amount = interest.get_final_amount()
    print(final_amount)

    reinv_times = 12
    reinvestment = ReinvestmentCompoundInterest(
            initial_balance,
            periods,
            rate,
            reinv_times
    )
    reinvestment_amount = reinvestment.get_final_amount()
    print(reinvestment_amount)
