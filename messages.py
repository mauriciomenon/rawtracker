class UIMessages:

    def __init__(self, lang: str):
        self.msg = {
            "apptitle": {
                "en": "DEV Activities tracker",
                "es": "DEV Registro de actividades",
                "pt": "DEV Registro de atividades"
            },
            "task": {
                "en": "Task",
                "es": "Actividad",
                "pt": "Atividade"
            },
            "planning": {
                "en": "Planning",
                "es": "Planificación",
                "pt": "Planejamento"
            },
            "status": {
                "en": "Status",
                "es": "Estado",
                "pt": "Estado"
            },
            "pending": {
                "en": "Pending",
                "es": "Pendiente",
                "pt": "Pendente"
            },
            "done": {
                "en": "Done",
                "es": "Terminado",
                "pt": "Terminado"
            },
            "cancelled": {
                "en": "Cancelled",
                "es": "Cancelado",
                "pt": "Cancelado"
            },
            "duedate": {
                "en": "Due date",
                "es": "Fecha/hora límite",
                "pt": "Data/hora limite"
            },
            "info": {
                "en": "Additional information",
                "es": "Información adicional",
                "pt": "Informação adicional"
            },
            "parent": {
                "en": "Hierarchical parent",
                "es": "Nivel jerárquico superior",
                "pt": "Nível hierárquico inferior"
            },
            "children": {
                "en": "Hierarchical children",
                "es": "Nivel jerárquico inferior",
                "pt": "Nível hierárquico inferior"
            },
            "inputdoc": {
                "en": "Input document(s)",
                "es": "Documento(s) de entrada",
                "pt": "Documento(s) de entrada"
            },
            "outputdoc": {
                "en": "Output document(s)",
                "es": "Documento(s) de salida",
                "pt": "Documento(s) de saída"
            },
            "choose": {
                "en": "Choose",
                "es": "Elegir",
                "pt": "Escolher"
            },
            "thisfriday": {
                "en": "This Friday",
                "es": "Este viernes",
                "pt": "Sexta-feira"
            },
            "nextweek": {
                "en": "Next week",
                "es": "Próxima semana",
                "pt": "Próxima semana"
            },
            "nextfriday": {
                "en": "Next Friday",
                "es": "Próximo viernes",
                "pt": "Próxima sexta-feira"
            },
            "customdate": {
                "en": "Custom date",
                "es": "Fecha personalizada",
                "pt": "Data personalizada"
            },
            "save": {
                "en": "Save",
                "es": "Guardar",
                "pt": "Salvar"
            },
            "back": {
                "en": "Back",
                "es": "Volver",
                "pt": "Voltar"
            }
        }
        self.lang = lang

    def __getitem__(self, string: str):
        return self.msg[string][self.lang]
