import pickle
from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / 'initial_dataset1.csv'
MODEL_PATH = BASE_DIR / 'br1.pkl'
class modelpredictor:  
    def __init__(self):
        with open(MODEL_PATH, 'rb') as model_file:
            self.model = pickle.load(model_file)
        self.dataset = pd.read_csv(DATASET_PATH)
        self.dataset['combined'] = self.dataset[['Title', 'Author', 'Main Genre', 'Sub Genre', 'Rating', 'Price', 'URLs']].values.tolist()

    def test(self, value):
        predicted_genre = self.model.predict([value])[0]
        filtered_data = self.dataset[self.dataset['Main Genre'] == predicted_genre]['combined'].tolist()
        suggestions = sorted(filtered_data, key=lambda x: x[4], reverse=True)[:10]

        return {
            'input': {"prompt": value, "predicted_genre": predicted_genre},
            'suggestions': suggestions
        }
