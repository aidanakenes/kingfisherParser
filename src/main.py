# -*- coding: utf-8 -*-
import uvicorn

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.service.parser import KingfishParser
from src.utils.err_utils import ApplicationError
from src.db.db import DB
from src.service.collector import KingfishCollector

app = FastAPI()


@app.get('/save/items', description='Get item info')
def get():
    try:
        _links = KingfishCollector().get_category_links()
        _items = KingfishParser().get_items(_links)
        if _items:
            my_db = DB()
            for k, v in _items.items():
                for v2 in v:
                    for k3, v3 in v2.items():
                        for v4 in v3:
                            my_db.insert_item(item=v4)
    except ApplicationError as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=jsonable_encoder({'error': e.__dict__})
        )
    return JSONResponse(
        content=jsonable_encoder({'data': _items})
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8081)
