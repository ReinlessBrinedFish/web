# ----------FLASK-WTF扩展库配置--------- #
# 激活跨站点请求伪造保护
CSRF_ENABLED = True
# CSRF被激活时，用于令牌加密，表单验证
# ! **SECRET_KEY参数尽量使用较为复杂的密钥，可以使用os.urandom(16)的方式获取随机密钥。
SECRET_KEY = 'you-will-never-guess'
