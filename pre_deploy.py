import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine



# Connexion à la base de données MS Access
connection_string = (
            "mssql+pyodbc://@DBSQLQCQCRF02/Laboratoire"
            "?trusted_connection=yes&driver=SQL+Server+Native+Client+10.0"
        )
engine = create_engine(connection_string)
    

    # Récupérer les données de la base de données
query = '''
        SELECT NAIS_SAMPLES.SAMPLE_DATE, NAIS_SAMPLES.USER_SAMPLEID, NAIS_RESULTS.TESTID, NAIS_RESULTS.PROPERTYID, NAIS_RESULTS.NUMBER_VALUE
        FROM NAIS_SAMPLES
        INNER JOIN NAIS_RESULTS ON NAIS_SAMPLES.SAMPLE_ID = NAIS_RESULTS.SAMPLE_ID
        WHERE (((NAIS_SAMPLES.USER_SAMPLEID) Like '5069%') AND ((NAIS_RESULTS.NUMBER_VALUE) Is Not Null));
    '''
data = pd.read_sql(query, engine)
data.to_csv('data.csv', index=False)
