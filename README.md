# Rule-Based Temperature Control System

This project implements a basic rule-based engine to simulate enterprise-level decision-making for controlling an air conditioner (AC) based on the input temperature. It demonstrates the use of object-oriented programming in Python to define actions, conditions, and rules that trigger appropriate responses.

## 🔧 Features

- Define and bind **actions** to temperature-related **conditions**
- A simple `RuleBook` engine to manage and execute rules
- Modular and extendable design to accommodate more conditions or devices

## 📁 Project Structure

```python
# Actions
def off_ac(data): ...
def do_nothing(data): ...
def on_ac(data): ...

# Conditions
def cold(data): ...
def ideal(data): ...
def hot(data): ...

# Rule and RuleBook Classes
class Rule: ...
class RuleBook: ...

# Rule Engine Setup
inf_engine = RuleBook()
inf_engine.add_rule(...)
...
inf_engine.engine(temperature_data)
