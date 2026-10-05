import rooms.lib.creditcard as CC
def run(data):
    return int(data[-1]) == CC.calc_checkdigit(data)