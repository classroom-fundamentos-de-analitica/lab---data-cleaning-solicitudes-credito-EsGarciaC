"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop("Unnamed: 0", axis="columns", inplace=True)

    # limpieza de monto de credito, signo, espacios, comas y pasar de float a int por los puntos flotantes
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x: int(float(x.replace("$", "")
                                                            .strip()
                                                            .replace(",", "")
                                                            )))
    # Las fechas varían de formato, hay que poner dayfirst y format mixed
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format='mixed')

    for column in df.columns:
        # no funciona bien if isinstance(df[column][0], str) por algún motivo.
        df[column] = df[column].apply(lambda stri:
                                      stri.lower()
                                      .replace("-", " ")
                                      .replace("_", " ")
                                      if isinstance(stri, str) else stri
                                      )

    # Si se ponen al inicio no funciona
    df.dropna(axis=0, inplace=True)
    df.drop_duplicates(inplace=True)

    return df
