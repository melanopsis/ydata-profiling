import pandas as pd

from ydata_profiling.config import Settings
from ydata_profiling.model.missing import missing_bar, missing_heatmap, missing_matrix
from ydata_profiling.visualisation.missing import (
    plot_missing_bar,
    plot_missing_heatmap,
    plot_missing_matrix,
)


@missing_bar.register
def pandas_missing_bar(config: Settings, df: pd.DataFrame) -> str:
    return plot_missing_bar(config, df)


@missing_matrix.register
def pandas_missing_matrix(config: Settings, df: pd.DataFrame) -> str:
    return plot_missing_matrix(config, df)


@missing_heatmap.register
def pandas_missing_heatmap(config: Settings, df: pd.DataFrame) -> str:
    return plot_missing_heatmap(config, df)