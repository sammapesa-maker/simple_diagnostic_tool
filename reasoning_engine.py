# reasoning_engine.py
from collections import defaultdict
import knowledge_base as kb
import re

class ReasoningEngine:
    """
    Forward-Chaining Reasoning Engine
    """

    def _to_snake_case(self, text):
        """
        Converts text to snake_case to match knowledge base
        """
        return re.sub(r'\s+', '_', text.strip().lower())

    def infer_diseases(self, reported_symptoms):
        """
        Input: list of symptoms in snake_case
        Output: list of dictionaries with disease, score, supporting symptoms
        """
        disease_scores = defaultdict(int)
        disease_support = defaultdict(set)

        for symptom in reported_symptoms:
            # Find associated findings
            symptom_findings = kb.findings.get(symptom, [])
            for finding in symptom_findings:
                # Find associated conditions
                finding_conditions = kb.conditions.get(finding, [])
                for condition in finding_conditions:
                    # Find associated diseases
                    condition_diseases = kb.diseases.get(condition, [])
                    for disease in condition_diseases:
                        disease_scores[disease] += 1
                        disease_support[disease].add(symptom)

        # Build result list sorted by score descending
        results = []
        for disease, score in disease_scores.items():
            results.append({
                "disease": disease,
                "score": score,
                "supporting_symptoms": sorted(disease_support[disease])
            })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results