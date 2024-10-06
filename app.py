from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 14,40,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 21,50,000',
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Hyderabad, India',
    },
    {
        'id': 4,
        'title': 'Software Developer',
        'location': 'Remote',
        'salary': '$ 1,55,000',
    },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
