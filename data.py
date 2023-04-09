import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5433",
    database="mydatabase",
    user="admin",
    password="admin"
)


#get credentials
def getCredentials(username,password):
    cur = conn.cursor()

    cur.execute("SELECT * FROM credential")

    result = cur.fetchone()
    print(result)
    cur.close()

    return str(result)

#gets logs stored, these logs are based on requests sent to the kubernetes control plane
def getLogs():
    cur = conn.cursor()

    cur.execute("SELECT version()")

    result = cur.fetchone()
    print(result)

    cur.close()

def postYamls():
    cur = conn.cursor()

    cur.execute("SELECT version()")

    result = cur.fetchone()
    print(result)

    cur.close()


def getYamls():
    cur = conn.cursor()

    cur.execute("SELECT version()")

    result = cur.fetchone()
    print(result)

    cur.close()

def intialize():
    cur = conn.cursor()
    cur.execute("""create table credential(
    id serial primary key,
    username varchar(20),
    password varchar(20)
    )
    """)

    result = cur.fetchone()
    print(result)

    cur.close()




