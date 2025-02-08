votes = {"james": 0, "john": 0, "mary": 0, "peace": 0}
candidates = votes.keys()


def vote(candidate):
    if candidate in candidates:
        print(f"Voted for {candidate}")
        votes[candidate] += 1
    else:
        print("Candidate doesn't exist!")


def result():
    sorted_candidates = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    for candidate, vote_ in sorted_candidates:
        print(f"{candidate} has {vote_} vote(s)")
    max_vote = max(votes.values())
    winners = [candidate for candidate, vote_ in votes.items() if vote_ == max_vote]
    if len(winners) > 1:
        print("It's a tie!")
        print(f'The winners are {", ".join(winners)}')
    else:
        print(f"The winner is {winners[0]} with {max_vote} votes")


vote("james")
vote("james")
vote("john")
vote("john")
vote("mary")
vote("mary")
vote("peace")
vote("peace")
vote("peace")
vote("james")
vote("james")

result()

# print("Welcome to the voting system")
# print("Candidates are: ")
# for sn, candidates in enumerate(votes.keys(), 1):
#     print(f"{sn}. {candidates}")
#
# while True:
#     candidate = input("Enter the candidate you want to vote for (q to quit): ").lower()
#     if candidate == "q":
#         break
#     vote(candidate)

# for candidates in votes.keys():
#     print(f"{candidates} has {votes[candidates]} vote(s)")
