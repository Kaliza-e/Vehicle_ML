
import pandas as pd


def manufacturer_frequency_table(df):
    manufacturer_counts = (
        df["manufacturer"]
        .value_counts()
        .reset_index()
    )
    manufacturer_counts.columns = ["Manufacturer", "Count"]

    return manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        index=False,
    )


def expensive_cars_table(df):
    expensive_cars = df[df["selling_price"] > 5000]
    return expensive_cars.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        index=False,
    )


def manufacturer_total_price_table(df):
    manufacturer_totals = df.groupby("manufacturer")["selling_price"].sum().to_frame()
    manufacturer_totals.columns = ["Manufacturer", "Total Selling Price"]
    return manufacturer_totals.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        index=False,
        float_format="%.2f",
    )

def manufacturer_transmission_table(df):
    manufacturer_transmission = df.groupby(["manufacturer", "transmission"])["selling_price"].sum().to_frame()

    return manufacturer_transmission.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        float_format="%.2f",
    )
