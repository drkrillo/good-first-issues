import csv

with open("thistext.txt", "r") as f:
    data = f.read()

# Process the data to remove leading/trailing pipes and split correctly
rows = [line.strip("| ").split(" | ") for line in data.split("\n")]
s = f'''<table>
    <thead>
        <tr><th>Repo</th><th>Title</th><th>Comments</th></tr>
    </thead>
    <tbody>\n'''
for i in rows:
    rpo = i[0]
    titl = i[1]
    cmnt = i[2]
    s2 = f'''        <tr><td>{rpo}</td><td>{titl}</td><td>{cmnt}</td></tr>\n'''
    s += s2
    
s3 = '''
    </tbody>
</table>
'''
s += s3
with open("op.txt", "w") as f2:
    f2.write(s)