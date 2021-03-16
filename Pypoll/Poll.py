import os, csv
from pathlib import Path
file = Path("election_data.csv")
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes= 0
TotalVotes = 0
with open(file,newline="", encoding="utf-8") as elections:
    reader = csv.reader(elections,delimiter=",")
    header = next(reader)
    for row in reader:
        TotalVotes +=1
        if row[2] == "Khan":
            KhanVotes +=1
        elif row[2] == "Correy":
            CorreyVotes +=1
        elif row[2] == "Li":
            LiVotes +=1
        elif row[2] == "O'Tooley":
            OtooleyVotes+=1
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [KhanVotes, CorreyVotes,LiVotes,OtooleyVotes]
CandidatesVotes = dict(zip(candidates,votes))
key = max(CandidatesVotes, key=CandidatesVotes.get)
KhanPercent = (KhanVotes/TotalVotes) *100
CorreyPercent = (CorreyVotes/TotalVotes) * 100
LiPercent = (LiVotes/TotalVotes)* 100
OtooleyPercent = (OtooleyVotes/TotalVotes) * 100
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"----------------------------")
print(f"Khan: {KhanPercent:.3f}% ({KhanVotes})")
print(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes})")
print(f"Li: {LiPercent:.3f}% ({LiVotes})")
print(f"O'Tooley: {OtooleyPercent:.3f}% ({OtooleyVotes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")



output_file = Path("ElectionResultsSummary.txt")

with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {TotalVotes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {KhanPercent:.3f}% ({KhanVotes})")
    file.write("\n")
    file.write(f"Correy: {CorreyPercent:.3f}% ({CorreyVotes})")
    file.write("\n")
    file.write(f"Li: {LiPercent:.3f}% ({LiVotes})")
    file.write("\n")
    file.write(f"O'Tooley: {OtooleyPercent:.3f}% ({OtooleyVotes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
    