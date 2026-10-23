from enum import StrEnum


class ConditionalRuleOperator(StrEnum):
    AND = "OPERATOR_AND"
    EQ = "OPERATOR_EQ"
    GT = "OPERATOR_GT"
    GTE = "OPERATOR_GTE"
    IN = "OPERATOR_IN"
    LT = "OPERATOR_LT"
    LTE = "OPERATOR_LTE"
    NE = "OPERATOR_NE"
    NIN = "OPERATOR_NIN"
    NOT = "OPERATOR_NOT"
    OR = "OPERATOR_OR"

    def __str__(self) -> str:
        return str(self.value)
