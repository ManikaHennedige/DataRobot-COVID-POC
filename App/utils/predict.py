import numpy as np

def predict_model(model, x, batch_size=1):

    preds = model.predict(x)
    preds = np.rint(preds).astype("int")
    preds= preds.reshape(batch_size)

    return {'preds': str(preds)}