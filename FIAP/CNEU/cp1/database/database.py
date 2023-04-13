

from sqlalchemy import text
from database.connection import create_session
import pandas as pd


# def save_predict(pred):
#     session = create_session()
#     create_table(session)
#     pred.to_sql('weather_data', con=session.bind, if_exists='append', index=False)
    





def create_table(session):
    session.execute(
        text(
            '''
            CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            Wind_Direction INTEGER,
            Wind_Speed FLOAT,
            Humidity INTEGER,
            Pressure FLOAT,
            Power_Level FLOAT,
            Light_Intensity INTEGER,
            prediction_label INTEGER
            );
            '''
        )
    )
    
session = create_session()
create_table(session)

# def get_predicts_in_db():
#     session = create_session()
#     query = session.execute(text("SELECT * FROM weather_data;"))

#     return pd.DataFrame(query.fetchall())