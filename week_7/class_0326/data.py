

login_info = [
    ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "get", {"mobilephone": 18688773467, "pwd": 123456},
     "登录成功"],

    ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "post", {"mobilephone": 18688773467, "pwd": 123456},
     "登录成功"],

    ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "get", {"mobilephone": 18688773467, "pwd": 111111},
     "用户名或密码错误"],

    ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "post", {"mobilephone": 18688773466, "pwd": 123456},
     "用户名或密码错误"]
]

# login_info = [
#      {"url":"http://47.107.168.87:8080/futureloan/mvc/api/member/login","method":"get","data":{"mobilephone": 18688773467, "pwd": 123456},
#      "exp_data":""登录成功"},
#
#     ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "post", {"mobilephone": 18688773467, "pwd": 123456},
#      "登录成功"],
#
#     ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "get", {"mobilephone": 18688773467, "pwd": 111111},
#      "用户名或密码错误"],
#
#     ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "post", {"mobilephone": 18688773466, "pwd": 123456},
#      "用户名或密码错误"]
# ]

# section, option, value
# [section]
# 配置

# login_info = [
#     {'name':{'name':'yuze'}}
# ]


