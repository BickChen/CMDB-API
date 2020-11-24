from ..settings import MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION
import pymongo


def insert_one_data(data):
    """
    添加单条数据到mongodb
    data: 必须为一个字典
    return: 返回插入记录在mongo集合中的唯一ID
    """
    myclient = pymongo.MongoClient(MONGO_URL)
    mydb = myclient[MONGO_DATABASE]
    mycol = mydb[MONGO_COLLECTION]

    mydict = data
    record_id = mycol.insert_one(mydict)
    return record_id



