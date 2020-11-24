from fastapi import APIRouter
from typing import Optional


router = APIRouter()


@router.post("aliyu/")
def alarm_callback(
    alertName: Optional[str] = None,
    alertState: Optional[str] = None,
    curValue: Optional[str] = None,
    dimensions: Optional[str] = None,
    expression: Optional[str] = None,
    instanceName: Optional[str] = None,
    metricName: Optional[str] = None,
    metricProject: Optional[str] = None,
    namespace: Optional[str] = None,
    preTriggerLevel: Optional[str] = None,
    ruleId: Optional[str] = None,
    timestamp: Optional[str] = None,
    triggerLevel: Optional[str] = None,
    userId: Optional[str] = None,
):
    data_dict = {
        "alertName": alertName,
        "alertState": alertState,
        "curValue": curValue,
        "dimensions": dimensions,
        "expression": expression,
        "instanceName": instanceName,
        "metricName": metricName,
        "metricProject": metricProject,
        "namespace": namespace,
        "preTriggerLevel": preTriggerLevel,
        "ruleId": ruleId,
        "timestamp": timestamp,
        "triggerLevel": triggerLevel,
        "userId": userId
    }
    return data_dict
