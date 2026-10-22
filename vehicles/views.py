import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import frequency_table


def dashboard_view(request):
    dataset_path = settings.BASE_DIR / "config" / "dummy_data" / "vehicles_ml_dataset.csv"
    df = pd.read_csv(dataset_path)
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df)
    })