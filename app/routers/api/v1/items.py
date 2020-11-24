from fastapi import APIRouter, Request, Form
from typing import Optional


router = APIRouter()


@router.post("/aliyu/")
def test(*, expression: str = Form(...), metricName: str = Form(...)):
    print(expression)
    print(metricName)

    # return {"status": True}

