from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.exc import OperationalError

from src.models.item import Item
from src.db.scheme import ItemTable, Base
from src.utils.conf import Postgres
from src.utils.logger import get_logger
from src.utils.err_utils import ApplicationError


logger = get_logger(__name__)
Session = sessionmaker()


class DB:
    def __init__(self):
        self._engine = create_engine(Postgres.ENGINE)
        self._meta = MetaData(self._engine)
        Session.configure(bind=self._engine)
        self.session = Session()

        self._table_item = ItemTable
        Base.metadata.create_all(self._engine, Base.metadata.tables.values(), checkfirst=True)

    def insert_item(self, item: Item):
        try:
            stmt = ItemTable(
                item_id=item.item_id,
                title=item.title,
                category=item.category,
                subcategory=item.subcategory,
                price=item.price,
                city=item.city,
                url=item.url
            )
            self.session.add(stmt)
            logger.info(f'Saving data for {item.item_id} into db')
            self.session.commit()
        except OperationalError as e:
            logger.error(f'Failed to save data for {item.item_id}: {type(e)}')
            raise ApplicationError()
