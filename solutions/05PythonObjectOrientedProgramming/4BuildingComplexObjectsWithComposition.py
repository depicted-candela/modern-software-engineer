class SystemComponent:
    def __init__(self, data: dict):
        self.name = data['name']
        self.__quality_score = 0
        self.quality_score = data['initial_q_score']
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name
    @property
    def quality_score(self):
        return self.__quality_score
    @quality_score.setter
    def quality_score(self, score: float):
        if score < 0.0 or score > 100.0:
            raise ValueError("The value can be higher than 100 or less thadn 0")
        self.__quality_score = score

class SystemBlueprint:
    def __init__(self, name: str):
        self.name = name
        self.components = []
    def add_component(self, component: SystemComponent):
        self.components.append(component)
    def calculate_average_quality(self):
        sum(self.components) / self.components.count
    def __str__(self):
        return f"Name: {self.name}, components: {[component.name for component in self.components]}"
    
db_component = SystemComponent({'name': 'PostgreSQL_DB', 'initial_q_score': 92.0})
api_component = SystemComponent({'name': 'FastAPI_Service', 'initial_q_score': 98.5})
qc_module = SystemComponent({'name': 'QC_Module', 'initial_q_score': 88.0})
    
sysblue1 = SystemBlueprint('Something')
sysblue1.add_component(db_component)
sysblue1.add_component(api_component)
sysblue1.add_component(qc_module)
print(sysblue1)