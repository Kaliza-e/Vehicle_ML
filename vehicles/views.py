
import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import (
    manufacturer_frequency_table,
    expensive_cars_table,
    manufacturer_total_price_table,
    manufacturer_transmission_table
)


def dashboard_view(request):
    # Path to the dataset
    dataset_path = (
        settings.BASE_DIR
        / "config"
        / "dummy_data"
        / "vehicles_ml_dataset.csv"
    )

    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Generate the three tables independently
    table_html = manufacturer_frequency_table(df)
    table2_html = expensive_cars_table(df)
    table3_html = manufacturer_total_price_table(df)
    table4_html = manufacturer_transmission_table(df)

    # Render the dashboard template
    return render(request, "vehicles/index.html", {
        "manufacturer_table": table_html,
        "expensive_cars_table": table2_html,
        "manufacturer_totals_table": table3_html,
        "manufacturer_transmission_table": table4_html,
    })
