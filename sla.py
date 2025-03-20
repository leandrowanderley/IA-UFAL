class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def forward_chaining(self):
        new_facts = True
        while new_facts:
            new_facts = False
            for condition, result in self.rules:
                if all(c in self.facts for c in condition) and result not in self.facts:
                    self.facts.add(result)
                    new_facts = True

    def backward_chaining(self, goal, explanation=None):
        if explanation is None:
            explanation = []
        if goal in self.facts:
            return True, explanation
        for condition, result in self.rules:
            if result == goal:
                explanation.append(f"Para provar {goal}, precisamos provar {condition}.")
                if all(self.backward_chaining(c, explanation)[0] for c in condition):
                    explanation.append(f"{goal} foi inferido porque {condition} são verdadeiros.")
                    return True, explanation
        return False, explanation

    def explain(self, goal):
        success, explanation = self.backward_chaining(goal)
        if success:
            return "\n".join(explanation)
        return f"Não foi possível provar {goal}."

class KnowledgeAgent:
    def __init__(self):
        self.kb = KnowledgeBase()

    def add_fact(self, fact):
        self.kb.add_fact(fact)

    def add_rule(self, condition, result):
        self.kb.add_rule(condition, result)

    def infer(self, goal=None):
        if goal:
            success, explanation = self.kb.backward_chaining(goal)
            if success:
                print(f"Objetivo alcançado: {goal} é verdadeiro.")
                print("Explicação:")
                print(self.kb.explain(goal))
            else:
                print(f"Objetivo não alcançado: {goal} não pode ser provado.")
        else:
            self.kb.forward_chaining()
            print("Fatos inferidos:", self.kb.facts)

    def interactive_dialogue(self):
        print("Bem-vindo ao sistema de diálogo do agente baseado em conhecimento!")
        print("""
    Este sistema utiliza duas estratégias de inferência:
    1. **Encadeamento para frente (Forward Chaining)**: Parte dos fatos conhecidos e aplica regras para inferir novos fatos.
    2. **Encadeamento para trás (Backward Chaining)**: Parte de um objetivo e verifica quais fatos e regras são necessários para alcançá-lo.

    Você pode:
    - Adicionar fatos (ex: A)
    - Adicionar regras (ex: SE A & B ENTÃO C)
    - Realizar inferências (encadeamento para frente ou para trás)
    - Solicitar explicações sobre como um fato foi inferido.
    """)
        while True:
            user_input = input("O que você gostaria de fazer? (adicionar fato, adicionar regra, inferir, explicar, sair): ").strip().lower()
            if user_input == "sair":
                break
            elif user_input == "adicionar fato":
                fact = input("Digite o fato (ex: A): ").strip()
                self.add_fact(fact)
                print(f"Fato '{fact}' adicionado.")
            elif user_input == "adicionar regra":
                condition = input("Digite a condição (ex: A & B): ").strip().split(" & ")
                result = input("Digite o resultado (ex: C): ").strip()
                self.add_rule(condition, result)
                print(f"Regra 'SE {' & '.join(condition)} ENTÃO {result}' adicionada.")
            elif user_input == "inferir":
                goal = input("Digite o objetivo para inferência (ou deixe em branco para encadeamento para frente): ").strip()
                if goal:
                    self.infer(goal)
                else:
                    self.infer()
            elif user_input == "explicar":
                goal = input("Digite o objetivo para explicação (ex: C): ").strip()
                print(self.kb.explain(goal))
            else:
                print("Comando não reconhecido. Tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    agent = KnowledgeAgent()

    # Adicionando fatos e regras manualmente (ou via interface)
    """
    agent.add_fact("A")
    agent.add_fact("B")
    agent.add_fact("E")
    agent.add_rule(["A", "B"], "C")
    agent.add_rule(["C"], "D")
    agent.add_rule(["D", "E"], "F")
    
    """
    # Iniciando o diálogo interativo
    agent.interactive_dialogue()