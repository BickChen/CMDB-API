from fastapi import APIRouter, Form
from ....models.mongo_operation import insert_one_data


router = APIRouter()


@router.post("/aliyu/")
def test(*,
         alertName: str = Form(...),
         alertState: str = Form(...),
         curValue: str = Form(...),
         dimensions: str = Form(...),
         instanceName: str = Form(...),
         metricName: str = Form(...),
         ):

    data_dict = {
        "alertname": alertName,
        "start": alertState,
        "curvalue": curValue,
        "instanceid": dimensions,
        "instancename": instanceName,
        "metricname": metricName,
    }

    print(data_dict)
    record_id = insert_one_data(data_dict)
    print(record_id)
    if record_id:
        return {"status": True}
    else:
        return {"status": False, "error": "数据插入失败"}

