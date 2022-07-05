import geopandas as gp
import psycopg2 as pg2


def main():
    try:
        con = pg2.connect(
            host = "ec2-3-222-74-92.compute-1.amazonaws.com",
            database = "ddkqm651ptq41g",
            user = "knxfxnexhnvtqx",
            password = "fd99404f7a0e7a8c5fe119ab7ab20ef7a0bea0b3c7fe2bb262b0c0e8b6341076",
            port = "5432"
        )

        cursor = con.cursor()
        sql = """SELECT * FROM pan_adm0;"""
        df = gp.GeoDataFrame.from_postgis(sql, con, geom_col='geom')
        df.plot()
        cursor.close()
        con.close()

    except Exception as error:
        print(error.args)


if __name__ == "__main__":
    main()

