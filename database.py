from sqlalchemy import create_engine, select, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={
                         "ssl": {"ssl_ca": "/etc/ssl/certs/ca-certificates.crt.pem"}
}
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  for row in result.fetchall():
    jobs.append(dict(row._mapping))
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)