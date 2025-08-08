# A dictionary representing a system component with sensitive quality metrics
component_data = {'name': 'PostgreSQL_DB', 'initial_q_score': 95.5}

class SystemComponent:
    def __init__(self, data: dict):
        self.name = data['name']
        self.quality_score = data['initial_q_score']
    @property
    def quality_score(self):
        return self.__quality_score
    @quality_score.setter
    def quality_score(self, score: float):
        if score < 0.0 or score > 100.0:
            raise ValueError("The value can be higher than 100 or less thadn 0")
        self.__quality_score = score

entity = SystemComponent(component_data)
print(entity.quality_score)
entity.quality_score = 98.8
print(entity.quality_score)
try:
    entity.quality_score = 101.0
    print(entity.quality_score)
except Exception as e:
    print(f"The exception as {e} arised")