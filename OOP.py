# Creating enterprise solutions
# Building some actions

def off_ac(data):
    print(f"Current temperature is {data}, switching off the AC.")
    
def do_nothing(data):
    print(f"Current temperature is {data}, doing nothing.")
    
def on_ac(data):
    print(f"Current temperature is {data}, switching on the AC.")
    

#Conditions

def cold(data):
    return data < 10


def ideal(data):
    return 20 >= data >= 10


def hot(data):
    return data > 20

#Building Class

class Rule():
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action
        
    def check_condition(self,data):
        return self.condition(data)
    
    def call_action(self,data):
        return self.action(data)
    
class RuleBook():
    def __init__(self):
        self.rules =[]
    
    def add_rule(self,rule):
        self.rules.append(rule)
        
    def engine(self,data):
        for rule in self.rules:
            if rule.check_condition(data):
                rule.call_action(data)

#Defining a rules
inf_engine = RuleBook()
inf_engine.add_rule(Rule('rule1',cold, off_ac))
inf_engine.add_rule(Rule('rule2',ideal, do_nothing))
inf_engine.add_rule(Rule('rule3',hot, on_ac))

#Checking condition for 11
inf_engine.engine(11)