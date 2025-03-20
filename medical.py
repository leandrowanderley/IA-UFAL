class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, fact, certainty=1.0):
        self.facts[fact] = certainty

    def add_rule(self, condition, result, certainty):
        self.rules.append((condition, result, certainty))

    def backward_chaining(self, goal, explanation=None):
        if explanation is None:
            explanation = []
        
        if goal in self.facts:
            return self.facts[goal], explanation
        
        best_certainty = 0.0
        for condition, result, rule_certainty in self.rules:
            if result == goal:
                explanation.append(f"Para provar {goal}, precisamos verificar {condition}.")
                sub_certainties = []
                for c in condition:
                    certainty, _ = self.backward_chaining(c, explanation)
                    sub_certainties.append(certainty)
                
                rule_result_certainty = rule_certainty * min(sub_certainties)
                best_certainty = max(best_certainty, rule_result_certainty)
                explanation.append(f"{goal} inferido com certeza {best_certainty:.2f} porque {condition} foram atendidos.")
        
        return best_certainty, explanation

    def explain(self, goal):
        certainty, explanation = self.backward_chaining(goal)
        if certainty > 0:
            return f"Certeza de {goal}: {certainty:.2f}\n" + "\n".join(explanation)
        return f"Não foi possível provar {goal}."


class MedicalDiagnosisSystem:
    def __init__(self):
        self.kb = KnowledgeBase()
    
    def add_symptom(self, symptom, certainty=1.0):
        self.kb.add_fact(symptom, certainty)
    
    def add_diagnosis_rule(self, symptoms, diagnosis, certainty):
        self.kb.add_rule(symptoms, diagnosis, certainty)
    
    def diagnose(self, disease):
        certainty, explanation = self.kb.backward_chaining(disease)
        if certainty > 0:
            print(f"Possível diagnóstico: {disease} com certeza {certainty:.2f}")
            print("Explicação:")
            print(self.kb.explain(disease))
        else:
            print(f"Não há evidências suficientes para diagnosticar {disease}.")
    
    def interactive_diagnosis(self):
        print("Bem-vindo ao Sistema de Diagnóstico Médico!")
        while True:
            user_input = input("Digite um sintoma ou 'diagnosticar' para avaliar: ").strip().lower()
            if user_input == "diagnosticar":
                disease = input("Digite a doença que deseja verificar: ").strip()
                self.diagnose(disease)
            elif user_input == "sair":
                break
            else:
                certainty = float(input("Digite um grau de certeza (0 a 1): "))
                self.add_symptom(user_input, certainty)
                print(f"Sintoma '{user_input}' registrado com certeza {certainty}.")


if __name__ == "__main__":
    system = MedicalDiagnosisSystem()
    
    system.add_diagnosis_rule(["febre", "tosse"], "gripe", 0.7)
    system.add_diagnosis_rule(["febre", "dificuldade para respirar"], "pneumonia", 0.8)
    system.add_diagnosis_rule(["dor de garganta", "febre"], "faringite", 0.6)
    system.add_diagnosis_rule(["espirros", "coriza"], "resfriado", 0.7)
    system.add_diagnosis_rule(["dores no corpo", "febre alta"], "dengue", 0.9)
    system.add_diagnosis_rule(["dores no corpo", "manchas vermelhas na pele"], "dengue hemorrágica", 0.85)
    system.add_diagnosis_rule(["náusea", "vômito"], "gastroenterite", 0.8)
    system.add_diagnosis_rule(["dor de cabeça", "sensibilidade à luz"], "meningite", 0.75)
    system.add_diagnosis_rule(["perda de olfato", "perda de paladar"], "covid-19", 0.9)
    system.add_diagnosis_rule(["febre", "suor noturno"], "tuberculose", 0.7)
    system.add_diagnosis_rule(["pressão no peito", "dificuldade para respirar"], "ataque cardíaco", 0.95)
    system.add_diagnosis_rule(["dor abdominal intensa", "náusea"], "apendicite", 0.85)
    
    system.interactive_diagnosis()