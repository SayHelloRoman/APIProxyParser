from fastapi import FastAPI
from DateBase.PyDB import DB
from typing import Optional

app = FastAPI()
DateBasePROXY = DB("DateBase/BD.pydb")

@app.get("/proxy_all")
async def proxy_all():
    return [DateBasePROXY.search(i) for i in DateBasePROXY.lists_id]


@app.get("/proxy_settings")
async def read_root(work: Optional[str] = "None", port: Optional[str] = "None", country: Optional[str] = "None"):
    return list(
        filter(
            lambda x: work in (str(x["WORK"]), "None") and port in (str(x["PORT"]), "None") and country in (str(x["COUNTRY"]), "None"),
            (DateBasePROXY.search(i) for i in DateBasePROXY.lists_id)
        )
    )

