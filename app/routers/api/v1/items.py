from fastapi import APIRouter, Form


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
    # return {"status": True}

