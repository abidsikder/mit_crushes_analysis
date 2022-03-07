import pandas as pd

data = pd.read_csv("anonymized_crushes.csv")

# indegree
kerb_in = {}
# outdegree
kerb_out = {}

for row in range(0, data.shape[0]):
    # filter out all the NaNs
    person_info = list(filter(lambda x: not (pd.isna(x)), data.iloc[row]))
    kerb = person_info[0]
    crushes = list(person_info[1:])
    # remove duplicates
    crushes = list(set(crushes))

    # make sure this entry exists in both dictionaries
    if kerb not in kerb_in:
        kerb_in[kerb] = 0
    if kerb not in kerb_out:
        kerb_out[kerb] = 0

    # make sure all crushes exist in the indegree
    for crush in crushes:
        if crush not in kerb_in:
            kerb_in[crush] = 0

    # indegree
    for crush in crushes:
        kerb_in[crush] = kerb_in[crush] + 1

    # outdegree
    outdegree = len(crushes)
    kerb_out[kerb] = outdegree

output = []
for kerb in kerb_out:
    indegree = kerb_in[kerb]
    outdegree = kerb_out[kerb]
    output.append([kerb, indegree, outdegree])

csv_out = pd.DataFrame(output, columns=["kerb", "indegree", "outdegree"])

csv_out.to_csv("InOutDegrees.csv", index=False)
