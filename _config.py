import os
basedir=os.path.abspath(os.path.dirname(__file__))
DATABASE="flasktaskr.db"
USERNAME="admin"
PASSWORD="admin"
WTF_CSRF_ENABLED=True
SECRET_KEY="b'~\x8e!p\xffJ\x93\xfa\xaf\xaf\xc45{\x01\xe0a\xf8\x8f\x02\xf20\x99\xf7G'"
DATABASE_PATH=os.path.join(basedir,DATABASE)