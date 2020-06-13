import json
import numpy as np

def main(event, context):

    event_body = json.loads(event['body'])

    arr = np.array([4, -8, 7 ])     
    out_arr = np.array_str(arr) 

    body = {
        "message": "Lol beef",
        "np": out_arr,
        "event": event_body
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

if __name__ == "__main__":
    main('', '')