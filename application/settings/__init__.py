from redis import StrictRedis
import redis

REDIS_HOST = 'tengxunyun'
REDIS_PORT = 6379
class Config(object):
    """项目配置核心类"""
    # 调试模式
    DEBUG = True
    # todo 配置日志
    LOG_LEVEL = "DEBUG"
    # todo 配置日志
    pass

    MYSQL_HOST = 'tengxunyun'
    MYSQL_PORT = 3306

    REDIS_HOST = 'tengxunyun'
    REDIS_PORT = 6379

    # mysql数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:123456@{MYSQL_HOST}:{MYSQL_PORT}/tess?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO= False

    # 配置redis
    # 设置密钥，可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
    SECRET_KEY = "ghhBljAa0uzw2afLqJOXrukORE4BlkTY/1vaMuDh6opQ3uwGYtsDUyxcH62Aw3ju"

    # flask_session的配置信息
    SESSION_TYPE = "redis" # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT,db=1)  # session 放置在db=1
    PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒
    WTF_CSRF_CHECK_DEFAULT = False


pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, db=2)   # 前端传入的数据放在db=2
redis_client = redis.Redis(connection_pool=pool)

# redis_client.set(126, 'a')
# redis_client.set("124", 'b', ex=10)
#
# print(redis_client.keys())
# keys = redis_client.keys("12*")
# print(redis_client.get('126'))
# print(keys)
# # redis_client.getrange()