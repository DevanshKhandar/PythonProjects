import Blind_auction_project_art
print(Blind_auction_project_art.logo)

def highest_bidder(bidding_dictionary):
    highest = 0
    winner = ""

    for bidder in bidding_dictionary:
        amount = bidding_dictionary[bidder]
        if amount > highest:
            highest = amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest}.")


x = True
auction = {}
while x is True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    n = input("Are there any other bidders? type 'yes' or 'no'. ").lower()
    if n == "no":
        x = False
        highest_bidder(auction)
    elif n == "yes":
        print("\n" * 100)






