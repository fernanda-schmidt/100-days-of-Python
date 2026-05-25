# Day 09: Silent Auction
def highest_bidder(bid_dict):
    winner = ""
    highest_bid = 0
    for bidder in bid_dict:
        amount = bid_dict[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")
            
            
        
            
    
print("=============================")
print("Welcome to the Silent Auction")
print("=============================")


bids = {}
continue_auction = True

while continue_auction:
    name = input("Enter a name: \n").title()
    price = float(input("How much would you like to bid?\n"))

    bids[name] = price

    more_bids = input("Are thre more people to bid? Enter 'yes' or 'no'\n").lower()
    if more_bids == 'no':
        highest_bidder(bids)
        continue_auction = False
    elif more_bids == 'yes':
        print('\n'*20)
    else:
        print("ERROR: Invalid Input - Please try again.")