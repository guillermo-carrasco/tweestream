from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from twistream.twitter.models import Base, Status


class SqliteStorageBackend(object):

    def __init__(self, params):
        self.engine = create_engine(f'sqlite:///{params.get("db_path")}')
        self.session = sessionmaker(bind=self.engine)()
        self.create_tables()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def persist_status(self, status):
        s = Status(status.id,
                   status.text,
                   status.created_at,
                   status.user.screen_name,
                   status.user.followers_count)
        self.session.add(s)
        self.session.commit()
