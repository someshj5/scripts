import pymysql
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import datetime


class Migration:

    def __init__(self):
        try:
            self.connection = create_engine(
                'mysql+pymysql://{a}:{b}@{c}:{d}/{e}'.format(a='username',
                                                     b='password',
                                                     c='hostname',
                                                     d=3306,
                                                     e='db_name'))
            
            print('connection established successfully!')

        except Exception as e:
            print(e, "\n Cannot connect to the database")
    
    
    def insert(self):
        """

        """
        try:

            df = pd.read_excel('pathto.xlsx')
        

                print('here------------')
             
                # print(df['territory_lube_id'])
                try:
                    print(2)


                    df = df[['columns']]
                    print(3)

                        
                except Exception as e:
                    print(e)
                finally:
                    # self.connection.close()
                    print('connection closed!')

        except Exception as e:
            print(e)
        return True



if __name__ == "__main__":
    c = Migration()
    c.insert()
    # c.update()
    # c.insert_dealer()



