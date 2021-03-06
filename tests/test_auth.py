import json

from openfalconclient.client import FalconClient

cli = FalconClient(endpoint="http://116.85.67.78:80/", user='root', password='root')

# 账户密码认证成功
# print(cli)

# /api/portal/self/profile
# auth = {}
print(cli.api.portal.self.profile.get())  # {'err': 'unauthorized'}
print(cli.api.portal.ping.get())  # Get unknow error from falcon:pong
print(cli.api.portal.pid.get())  # 3288
print(cli.api.portal.version.get())  # 1

print(cli.api.portal.collect.get())  # {'err': 'unauthorized'}


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
}
# openfalconclient.exceptions.InternalServerError: Get unknow error from falcon: (HTTP 500) (HTTP 500)
# 用try except进行捕捉
# print(cli.api.portal.stra.put(data=data))  # Internal Server Error (HTTP 500)

print(cli.api.portal.stras.get())
print(cli.api.portal.stras.effective.get())

data = [
  {
    "type": "port",
    "data": {
      "nid": 2,
      "collect_type": "port",
      "name": "service.port",
      "tags": "",
      "port": 90,
      "timeout": 3,
      "step": 20,
      "comment": ""
    }
  },
  {
    "type": "proc",
    "data": {
      "nid": 2,
      "collect_type": "proc",
      "name": "service",
      "collect_method": "cmd",
      "target": "tsdb",
      "tags": "",
      "step": 20,
      "comment": ""
    }
  },
  {
    "type": "log",
    "data": {
      "nid": 2,
      "collect_type": "log",
      "func_type": "FLOW",
      "name": "LOG.aa",
      "func": "cnt",
      "unit": "次数",
      "file_path": "/home/xiaoju/alarm/log/DEBUG.log",
      "time_format": "dd/mmm/yyyy:HH:MM:SS",
      "step": 10,
      "pattern": "flush"
    }
  }
]
print(cli.api.portal.collect.post(data=data))

# api/index
data = {
    "endpoints": ["host1", "host2"],
    "metrics": ["disk.used.percent"],
}
print(cli.api.index.tagkv.post(data=data))

# api/transfer
data = {
  "start": 1562925134,
  "end": 1562925234,
  "series": [
    {
      "endpoints": [
        "127.0.0.1",
        "127.0.0.2"
      ],
      "metric": "proc.num",
      "tagkv": [
        {
          "tagk": "target",
          "tagv": [
            "collector"
          ]
        },
        {
          "tagk": "service",
          "tagv": [
            "n9e-collector"
          ]
        }
      ]
    }
  ]
}
print(cli.api.transfer.data.post(data=data))
print(float(1)==int(1))
