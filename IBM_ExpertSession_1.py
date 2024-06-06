import scipy

n=int(input("Enter the no. of political parties: "))
parties={}
i=0

while i<n:
    party=input("Enter name of the political party: ")
    if party not in parties.keys():
        parties[party]=0
        i+=1
    else:
        print("This political party is already present! Enter a different one")

voters=int(input("Enter no. of voters: "))
for i in range(voters):
    vote=input("Enter your choice: ")
    if vote in parties.keys():
        parties[vote]+=1
    else:
        print("Invalid Party Name!")

max_votes=max(parties.values())
winners=""
c=0
for key,val in parties.items():
    if val==max_votes:
        winners+=key+"-"
        c=1

if c==1:
    print("The winning party on majority votes is: ",winners)
else:
    print("The joint coalition of parties are: ",winners)

