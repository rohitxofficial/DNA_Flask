from flask import Flask, render_template, request
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = 'RohitPanchal'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/dna', methods=['POST'])
def dna():
    seq = request.form['seq']

    with open('databases/database.csv') as database:
        reader = list(csv.reader(database))
        dna_seq = reader[0]
        dna_seq.pop(0)

    count = []

    for i in dna_seq:
        counter = 0
        pattern = i
        while pattern in seq:
            counter += 1
            pattern += i
        count.append(counter)

    new_count = []

    for i in count:
        i = str(i)
        new_count.append(i)

    flag = True
    database = csv.reader(open('databases/database.csv'))
    for row in database:
        name = row.pop(0)
        if row == new_count:
            flag = True
            break
        else:
            flag = False

    if flag == True:
        final_name = name
        final_flag = True
    else:
        final_name = "No match"
        final_flag = False

    return render_template('dna.html', name=final_name, flag=final_flag)


if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()