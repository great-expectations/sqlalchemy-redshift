from sqlalchemy import create_engine


def test_stub():
    create_engine(
        "redshift+psycopg2://username:password@my-redshift-cluster.abcdef123456.us-west-2.redshift.amazonaws.com:5439/mydatabase"
    )
