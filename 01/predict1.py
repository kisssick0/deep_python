from random import random


class SomeModel:
    def predict(self, message: str) -> float:
        number = random()
        return number


def predict_message_mood(message: str,
                         model: SomeModel,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8,
                         ) -> str:
    if not isinstance(bad_thresholds, float) or not isinstance(good_thresholds, float):
        raise TypeError
    if bad_thresholds > good_thresholds:
        raise ValueError

    prdct = model.predict(message)
    if prdct < bad_thresholds:
        return "неуд"
    if prdct > good_thresholds:
        return "отл"
    return "норм"
