from flask import Flask, render_template, jsonify
from database import load_job_from_db

app = Flask(__name__)



@app.route("/")
def hello_joy():
    jobs = load_job_from_db()
    return render_template('home.html', jobs=jobs, company_name='Joy')

@app.route('/api/jobs')
def list_jobs():
    jobs = load_job_from_db
    return jsonify(jobs)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
