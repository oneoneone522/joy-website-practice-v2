from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={
                         "ssl": {"ssl_ca": "/etc/ssl/certs/ca-certificates.crt.pem"}
}
)

def load_job_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  for row in result.fetchall():
    jobs.append(dict(row._mapping))
  return jobs
