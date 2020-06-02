import json

from openfalconclient.client import FalconClient

cli = FalconClient(endpoint="http://116.85.67.78:80/", user='root', password='root')

# 账户密码认证成功
# print(cli)

# /api/portal/self/profile
auth = {}
print(cli.api.portal.ping.get())
print()
print(cli.api.portal.pid.get())
print(cli.api.portal.version.get())

# PUT
# /api/portal/stra
data = {
    "id": 1,
    "name": "all必触发",
    "nid": 21,
    "excl_nid": None,
    "priority": 3,
    "alert_dur": 60,
    "exprs": [
        {
            "eopt": "!=",
            "func": "all",
            "metric": "cpu.idle",
            "params": [],
            "threshold": 0
        }
    ],
    "tags": [],
    "recovery_dur": 0,
    "recovery_notify": 1,
    "alert_upgrade": {
        "duration": 60,
        "level": 1,
        "users": [],
        "groups": []
    },
    "converge": [3600, 1],
    "notify_group": [],
    "notify_user": [5],
    "callback": "",
    "enable_stime": "00:00",
    "enable_etime": "23:59",
    "enable_days_of_week": [0, 1, 2, 3, 4, 5, 6],
    "need_upgrade": 0,
    "id": 13
}
# openfalconclient.exceptions.InternalServerError: Get unknow error from falcon: (HTTP 500) (HTTP 500)
# 没有这个id
# print(cli.api.portal.stra.put(data=data))
