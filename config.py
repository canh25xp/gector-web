BATCH_SIZE = 16
DEFAULT_API = {
        "hostname": "http://localhost",
        "port": 3000,
        "url": "gector",
        "request_key": "text_input_list",
        "response_key": "text_output_list",
    }

combinations = ['ESC', 'MEMT']
selected_combination = 'ESC'

models = {
    "GECToR-Roberta": DEFAULT_API,
    "GECToR-XLNet": DEFAULT_API,
    "GECToR-Bert": DEFAULT_API
}

