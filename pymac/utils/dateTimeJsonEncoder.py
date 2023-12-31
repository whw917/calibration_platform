# coding:utf-8

import json
import datetime


class DateTimeJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date()):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)