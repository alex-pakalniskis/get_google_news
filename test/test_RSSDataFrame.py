import pandas as pd
from get_google_news import RSSDataFrame

test_params_1 = ["en","data","US"]
test_params_2 = ["es","data","MX"]
test_params_3 = ["fr","data","CA"]
lists_of_params = [test_params_1, test_params_2, test_params_3]

def test_RSSDataFrame_Type():
    for param in lists_of_params:
        assert type(
            RSSDataFrame(
                param[0],
                param[1],
                param[2]
                ).get()
            ) == type(
            pd.DataFrame()
                )

def test_RSSDataFrame_Columns():
    for param in lists_of_params:
        assert len(
            RSSDataFrame(
                param[0],
                param[1],
                param[2]
                ).get().columns
                ) == 5