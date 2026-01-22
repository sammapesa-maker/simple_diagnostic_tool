# main.py
from reasoning_engine import ReasoningEngine
import knowledge_base as kb
import re
from ansi import design

class DiagnosticSession:
    """
    Smple Forward-Chaining Diagnostic Session
    Supports multiple patients in a single session.
    Converts user input to snake_case.
    Displays human-readable results.
    """

    def __init__(self):
        self.engine = ReasoningEngine()
        self._width = 60

    def _to_snake_case(self, text):
        return re.sub(r'\s+', '_', text.strip().lower())

    def _to_readable(self, text):
        return text.replace("_", " ").title()

    def _collect_symptoms(self):
        print()
        print(design("Available symptoms:", fg="cyan", styles=["underline", "bold"]))
        symptoms = [self._to_readable(s) for s in kb.symptoms]
        for s in symptoms:
            print(s, end=", ")
        print("\n")
        print(design("Enter symptoms for this patient (type 'q' to finish):", fg="green"))

        symptoms = []
        while True:
            user_input = input("> ").strip()
            if user_input.lower() == "q":
                break
            symptom = self._to_snake_case(user_input)
            if symptom not in kb.symptoms:
                print(design("Invalid symptom. Choose from the list above.", fg="red", styles=["bold"]))
                continue
            if symptom not in symptoms:
                symptoms.append(symptom)
        return symptoms

    def _present_results(self, results):
        if not results:
            print(design("No matching diseases found.", fg="red"))
            return

        title = design(
            "--- DIAGNOSTIC RESULTS ---",
            fg="green",
            styles=["bold", "underline"]
        )
        
        print("\n" + title)
        for item in results[:5]:
            disease = self._to_readable(item["disease"])
            supporting = ", ".join([design(self._to_readable(s), fg="cyan") for s in item["supporting_symptoms"]])
            print(f"• {design(disease, styles=["bold"])}")
            print(f"   Support score: {item['score']}")
            print(f"   Supported by : {supporting}", end="\n\n")

        print()
        if len(results) > 1:
            print(design("Multiple possible diseases detected. \nConsider further testing!", styles=["bold"], fg="red"))
        else:
            print("Single most likely disease identified.")

    def start(self):
        heading = design(
            "FOWARD-CHAINING DIAGNOSTIC ASSISTANT".center(self._width),
            fg="cyan",
            styles=["bold"]
        )
        print("=" * self._width, end="\n\n")
        print(heading, end="\n\n")
        patient_count = 1

        while True:
            print(design(" " * self._width, fg="green", styles=["underline"]))
            title = design(
                f"*** Patient {patient_count} ***".center(self._width),
                fg="green",
                styles=["bold", "underline"]
            )
            
            print(title)
            symptoms = self._collect_symptoms()
            if not symptoms:
                print(design("No symptoms entered. Skipping patient.", fg="red"))
            else:
                results = self.engine.infer_diseases(symptoms)
                self._present_results(results)

            print()
            print("-" * self._width)
            more = input(design("Do you want to diagnose another patient? (y/n): ", fg="cyan")).strip().lower()
            if more != "y":
                print(design("Session ended.", fg="red"))
                print("=" * self._width)
                break
            patient_count += 1

if __name__ == "__main__":
    session = DiagnosticSession()
    session.start()