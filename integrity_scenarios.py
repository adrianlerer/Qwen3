#!/usr/bin/env python3
"""
Integrity Training Scenarios and Character Interactions
Escenarios de Entrenamiento en Integridad e Interacciones de Personajes

Author: Integridai Suite Team
License: MIT
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import json

class ScenarioCategory(Enum):
    """Categories of integrity training scenarios"""
    CORRUPTION = "corruption"
    CONFLICT_OF_INTEREST = "conflict_of_interest"
    WHISTLEBLOWING = "whistleblowing" 
    PROCUREMENT_FRAUD = "procurement_fraud"
    BRIBERY = "bribery"
    INFORMATION_MISUSE = "information_misuse"
    RESOURCE_ABUSE = "resource_abuse"
    DISCRIMINATION = "discrimination"

class DifficultyLevel(Enum):
    """Difficulty levels for scenarios"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

@dataclass
class IntegrityScenario:
    """Represents an integrity training scenario"""
    id: str
    title: str
    category: ScenarioCategory
    difficulty: DifficultyLevel
    description: str
    context: str
    dilemma: str
    stakeholders: List[str]
    ethical_considerations: List[str]
    legal_implications: List[str]
    correct_action: str
    temptation_factors: List[str]
    consequences_of_corruption: List[str]
    learning_objectives: List[str]

class IntegrityScenarios:
    """Collection of integrity training scenarios"""
    
    def __init__(self):
        self.scenarios = self._initialize_scenarios()
    
    def _initialize_scenarios(self) -> Dict[str, IntegrityScenario]:
        """Initialize the complete set of integrity scenarios"""
        
        scenarios = {}
        
        # Scenario 1: Procurement Bribery
        scenarios["procurement_bribery_01"] = IntegrityScenario(
            id="procurement_bribery_01",
            title="El Contrato Tentador - The Tempting Contract",
            category=ScenarioCategory.BRIBERY,
            difficulty=DifficultyLevel.INTERMEDIATE,
            description="Un proveedor ofrece un soborno para ganar un contrato gubernamental importante.",
            context="""
            Eres María González, directora de adquisiciones en una entidad gubernamental. 
            Tu departamento está evaluando propuestas para un contrato de $50 millones 
            para la construcción de un nuevo hospital público. Las propuestas están muy reñidas.
            
            Carlos Mendoza, representante de Constructora Éxito S.A., te invita a almorzar 
            en un restaurante exclusivo. Durante la comida, menciona casualmente que su empresa 
            podría "mostrar su agradecimiento" por una decisión favorable con un "regalo" 
            de $100,000 para "tu desarrollo profesional".
            """,
            dilemma="""
            ¿Cómo respondes a esta situación? El contrato es crucial para la comunidad 
            y Constructora Éxito tiene una propuesta técnicamente sólida, pero no 
            necesariamente la mejor. El dinero ofrecido resolvería tus problemas 
            financieros personales inmediatos.
            """,
            stakeholders=[
                "María González (Directora de Adquisiciones)",
                "Carlos Mendoza (Representante de Constructora Éxito)",
                "Comunidad beneficiaria del hospital",
                "Otros proveedores participantes",
                "Gobierno y contribuyentes",
                "Familia de María (presión financiera)"
            ],
            ethical_considerations=[
                "Imparcialidad en el proceso de selección",
                "Uso apropiado de recursos públicos",
                "Conflicto entre interés personal y público",
                "Integridad del proceso democrático",
                "Justicia para todos los participantes"
            ],
            legal_implications=[
                "Delito de cohecho (Código Penal)",
                "Violación de la Ley de Contratación Estatal",
                "Posible inhabilitación para ejercer cargos públicos",
                "Responsabilidad penal y civil",
                "Nulidad del contrato si hay irregularidades"
            ],
            correct_action="""
            1. Rechazar inmediatamente la oferta de soborno
            2. Documentar el incidente por escrito
            3. Reportar a supervisores y autoridades de control
            4. Retirarse del proceso de evaluación por conflicto de interés
            5. Cooperar con cualquier investigación subsecuente
            """,
            temptation_factors=[
                "Problemas financieros personales urgentes",
                "Propuesta técnicamente competitiva",
                "Presentación 'sutil' de la oferta corrupta",
                "Presión familiar por estabilidad económica",
                "Percepción de que 'todos lo hacen'",
                "Monto significativo del soborno"
            ],
            consequences_of_corruption=[
                "Cárcel de 6-15 años por cohecho",
                "Pérdida permanente del empleo público",
                "Inhabilitación para contratar con el Estado",
                "Daño a la reputación profesional y personal",
                "Perjuicio a la comunidad (hospital subóptimo)",
                "Deterioro de la confianza institucional"
            ],
            learning_objectives=[
                "Reconocer ofertas de soborno en contextos profesionales",
                "Aplicar protocolos de reporte de corrupción",
                "Evaluar consecuencias legales y éticas de decisiones",
                "Desarrollar resistencia a presiones corruptas",
                "Fortalecer compromiso con el servicio público"
            ]
        )
        
        # Scenario 2: Conflict of Interest
        scenarios["conflict_interest_01"] = IntegrityScenario(
            id="conflict_interest_01", 
            title="La Empresa Familiar - The Family Business",
            category=ScenarioCategory.CONFLICT_OF_INTEREST,
            difficulty=DifficultyLevel.BEGINNER,
            description="Un funcionario debe decidir sobre un contrato donde su hermano es socio.",
            context="""
            Eres Pedro Ramírez, coordinador de proyectos en la Alcaldía Municipal.
            Tu oficina está evaluando proveedores para el mantenimiento de parques públicos.
            Entre las propuestas recibidas está "Verde & Jardines Ltda.", empresa donde
            tu hermano Juan es socio mayoritario con 60% de participación.
            
            La propuesta de Verde & Jardines es competitiva: no es la más barata, 
            pero ofrece buena calidad y tu hermano realmente necesita el contrato 
            para mantener su empresa a flote tras la pandemia.
            """,
            dilemma="""
            ¿Participas en la evaluación sabiendo que tu hermano tiene intereses 
            en una de las empresas? ¿Cómo manejas la situación para mantener 
            la transparencia del proceso?
            """,
            stakeholders=[
                "Pedro Ramírez (Coordinador Municipal)",
                "Juan Ramírez (Hermano y empresario)",
                "Otros proveedores participantes", 
                "Ciudadanía (usuarios de parques)",
                "Alcaldía Municipal",
                "Empleados de Verde & Jardines"
            ],
            ethical_considerations=[
                "Transparencia en el proceso de selección",
                "Separación entre intereses familiares y públicos",
                "Equidad para todos los participantes",
                "Confianza ciudadana en las instituciones",
                "Integridad del servidor público"
            ],
            legal_implications=[
                "Conflicto de interés (Ley Anti-corrupción)",
                "Posible nulidad del contrato",
                "Sanciones disciplinarias",
                "Investigación por contraloría",
                "Inhabilitación temporal para contratar"
            ],
            correct_action="""
            1. Declarar inmediatamente el conflicto de interés
            2. Apartarse completamente del proceso de evaluación
            3. Documentar la declaración por escrito
            4. Informar a superiores sobre la situación
            5. Permitir que otros colegas evalúen objetivamente
            """,
            temptation_factors=[
                "Necesidad económica del hermano",
                "Propuesta técnicamente válida",
                "Presión familiar",
                "Percepción de 'no hacer nada malo'",
                "Confianza en la propia objetividad"
            ],
            consequences_of_corruption=[
                "Sanción disciplinaria hasta destitución",
                "Nulidad del contrato celebrado",
                "Pérdida de confianza ciudadana",
                "Investigaciones administrativas",
                "Daño reputacional familiar"
            ],
            learning_objectives=[
                "Identificar conflictos de interés familiares",
                "Aplicar protocolos de declaración",
                "Separar intereses personales de funciones públicas",
                "Mantener transparencia en procesos",
                "Proteger la integridad institucional"
            ]
        )
        
        # Scenario 3: Whistleblowing Dilemma  
        scenarios["whistleblowing_01"] = IntegrityScenario(
            id="whistleblowing_01",
            title="El Silencio Cómplice - Complicit Silence", 
            category=ScenarioCategory.WHISTLEBLOWING,
            difficulty=DifficultyLevel.ADVANCED,
            description="Un empleado descubre irregularidades de su jefe directo y debe decidir si reportarlas.",
            context="""
            Eres Ana Rodríguez, contadora en el Ministerio de Educación. Llevas 8 años
            trabajando bajo la supervisión directa de Roberto Silva, quien siempre ha
            sido un buen jefe y mentor profesional.
            
            Mientras revisas facturas de un proyecto educativo, descubres que Roberto
            ha estado aprobando pagos a una empresa consultora por servicios que
            aparentemente nunca se prestaron. Los montos suman $2 millones en los
            últimos 6 meses. Roberto tiene acceso a tu computador y sabe que
            estás revisando esos documentos.
            """,
            dilemma="""
            ¿Reportas las irregularidades sabiendo que esto destruirá la carrera de
            Roberto y potencialmente la tuya? ¿Hablas primero con él? ¿Qué haces si
            él te pide mantener silencio "por el bien del equipo"?
            """,
            stakeholders=[
                "Ana Rodríguez (Contadora)",
                "Roberto Silva (Jefe directo)",
                "Estudiantes beneficiarios del proyecto",
                "Ministerio de Educación",
                "Empresa consultora involucrada", 
                "Colegas del departamento",
                "Sociedad (recursos públicos desviados)"
            ],
            ethical_considerations=[
                "Deber de proteger recursos públicos",
                "Lealtad vs. integridad profesional",
                "Responsabilidad con la educación pública",
                "Protección de testigos y denunciantes",
                "Daño colateral a personas inocentes"
            ],
            legal_implications=[
                "Obligación legal de reportar irregularidades",
                "Protección legal al denunciante",
                "Responsabilidad penal por omisión", 
                "Malversación de fondos públicos",
                "Fraude contra la administración pública"
            ],
            correct_action="""
            1. Documentar cuidadosamente todas las evidencias
            2. Reportar a la oficina de control interno
            3. Usar canales de denuncia protegida
            4. NO confrontar directamente a Roberto
            5. Preservar la cadena de custodia de documentos
            6. Cooperar con investigaciones oficiales
            """,
            temptation_factors=[
                "Relación personal positiva con Roberto",
                "Miedo a represalias laborales", 
                "Incertidumbre sobre las consecuencias",
                "Presión para 'resolver internamente'",
                "Temor al aislamiento del equipo",
                "Complejidad del proceso de denuncia"
            ],
            consequences_of_corruption=[
                "Continuidad del desvío de recursos educativos",
                "Responsabilidad penal por encubrimiento",
                "Pérdida de confianza institucional",
                "Daño al sistema educativo público",
                "Precedente negativo para otros casos"
            ],
            learning_objectives=[
                "Desarrollar valor para denunciar irregularidades",
                "Conocer protocolos de protección al denunciante",
                "Priorizar el interés público sobre lealtades personales", 
                "Manejar dilemas éticos complejos",
                "Fortalecer cultura de transparencia"
            ]
        )
        
        # Scenario 4: Information Misuse
        scenarios["information_misuse_01"] = IntegrityScenario(
            id="information_misuse_01",
            title="Información Privilegiada - Inside Information",
            category=ScenarioCategory.INFORMATION_MISUSE, 
            difficulty=DifficultyLevel.INTERMEDIATE,
            description="Un funcionario tiene acceso a información que podría beneficiar financieramente a familiares.",
            context="""
            Eres Laura Martínez, asesora en la oficina de planeación urbana de la ciudad.
            Estás trabajando en el plan maestro que incluye la construcción de una nueva
            línea de metro. La información es estrictamente confidencial hasta el anuncio
            oficial en 3 meses.
            
            Tu cuñado Diego es agente inmobiliario y está considerando invertir sus ahorros
            en una propiedad. Casualmente, te pregunta sobre "zonas prometedoras para inversión".
            Una de las zonas que menciona será altamente valorizada por la nueva estación
            de metro, pero él no lo sabe.
            """,
            dilemma="""
            ¿Le das alguna indicación a Diego sobre dónde invertir? ¿Le adviertes que
            evite ciertas zonas sin explicar por qué? ¿Mantienes completo silencio
            aunque su inversión pueda ser un desastre?
            """,
            stakeholders=[
                "Laura Martínez (Funcionaria de planeación)",
                "Diego (Cuñado agente inmobiliario)",
                "Familia (hermana de Laura, esposa de Diego)",
                "Otros inversionistas sin información privilegiada",
                "Ciudadanía en general",
                "Mercado inmobiliario"
            ],
            ethical_considerations=[
                "Confidencialidad de información oficial",
                "Equidad en el acceso a oportunidades",
                "Separación entre funciones públicas e intereses privados",
                "Transparencia en mercados financieros",
                "Integridad en el manejo de información"
            ],
            legal_implications=[
                "Uso indebido de información privilegiada",
                "Violación de reserva de documentos oficiales",
                "Posible investigación disciplinaria",
                "Sanciones por conflicto de interés",
                "Nulidad de decisiones si hay influencia indebida"
            ],
            correct_action="""
            1. Mantener absoluta confidencialidad de la información
            2. NO dar indicaciones directas o indirectas sobre inversiones
            3. Recordar a familiares las restricciones de su cargo
            4. Declarar cualquier conflicto potencial
            5. Separar completamente vida profesional y personal
            """,
            temptation_factors=[
                "Deseo de ayudar económicamente a la familia",
                "Información 'valiosa' disponible",
                "Percepción de que 'no lastima a nadie'",
                "Presión familiar indirecta",
                "Oportunidad única de inversión"
            ],
            consequences_of_corruption=[
                "Pérdida de confianza en instituciones públicas",
                "Ventaja injusta sobre otros inversionistas",
                "Posibles sanciones legales y disciplinarias",
                "Compromiso de procesos de planeación futuros",
                "Daño a la equidad del mercado"
            ],
            learning_objectives=[
                "Proteger confidencialidad de información oficial",
                "Separar intereses familiares de funciones públicas",
                "Reconocer conflictos de interés potenciales",
                "Mantener equidad en acceso a oportunidades",
                "Desarrollar integridad en manejo de información"
            ]
        )
        
        return scenarios
    
    def get_scenario(self, scenario_id: str) -> Optional[IntegrityScenario]:
        """Get a specific scenario by ID"""
        return self.scenarios.get(scenario_id)
    
    def get_scenarios_by_category(self, category: ScenarioCategory) -> List[IntegrityScenario]:
        """Get all scenarios in a specific category"""
        return [s for s in self.scenarios.values() if s.category == category]
    
    def get_scenarios_by_difficulty(self, difficulty: DifficultyLevel) -> List[IntegrityScenario]:
        """Get all scenarios of a specific difficulty level"""  
        return [s for s in self.scenarios.values() if s.difficulty == difficulty]
    
    def get_all_scenarios(self) -> List[IntegrityScenario]:
        """Get all available scenarios"""
        return list(self.scenarios.values())
    
    def get_scenario_for_character_training(self, character_name: str) -> List[IntegrityScenario]:
        """Get scenarios optimized for specific character training"""
        
        character_scenarios = {
            "catalina": [  # Professional, solution-oriented scenarios
                "conflict_interest_01", 
                "information_misuse_01"
            ],
            "alexis": [  # Complex temptation scenarios
                "procurement_bribery_01",
                "whistleblowing_01"  
            ],
            "mentor": [  # Deep ethical reflection scenarios
                "whistleblowing_01",
                "information_misuse_01"
            ],
            "auditor": [  # Clear-cut compliance scenarios
                "procurement_bribery_01", 
                "conflict_interest_01"
            ]
        }
        
        scenario_ids = character_scenarios.get(character_name.lower(), [])
        return [self.scenarios[sid] for sid in scenario_ids if sid in self.scenarios]

class CharacterPromptGenerator:
    """Generates character-specific prompts for integrity scenarios"""
    
    @staticmethod
    def generate_catalina_prompt(scenario: IntegrityScenario, user_response: str) -> str:
        """Generate Catalina's professional, solution-oriented response"""
        return f"""
Como Catalina, especialista en cumplimiento ético, analiza esta situación:

**Escenario:** {scenario.title}
{scenario.dilemma}

**Respuesta del usuario:** {user_response}

Proporciona:
1. Evaluación profesional de la respuesta
2. Aspectos éticos clave a considerar  
3. Soluciones prácticas y procedimentales
4. Recomendaciones para fortalecer la integridad
5. Próximos pasos concretos

Mantén un tono profesional pero accesible, enfocándote en soluciones constructivas.
"""

    @staticmethod  
    def generate_alexis_prompt(scenario: IntegrityScenario, user_response: str) -> str:
        """Generate Alexis's challenging, temptation-focused response"""
        return f"""
Como Alexis, presentador de dilemas éticos, desafía al usuario:

**Escenario:** {scenario.title}  
{scenario.dilemma}

**Respuesta del usuario:** {user_response}

Tu rol es:
1. Identificar debilidades en el razonamiento ético
2. Presentar argumentos tentadores que una persona corrupta usaría
3. Cuestionar la viabilidad práctica de soluciones "ideales"
4. Explorar presiones realistas que enfrentaría la persona
5. Probar la resistencia ética con argumentos convincentes

NO promuevas la corrupción, pero SÍ presenta los desafíos reales que enfrentaría alguien en esta situación.
"""
    
    @staticmethod
    def generate_mentor_prompt(scenario: IntegrityScenario, user_response: str) -> str:
        """Generate Dr. Mentor's reflective, wisdom-based response"""
        return f"""
Como Dr. Mentor, consejero de sabiduría ética, guía la reflexión:

**Escenario:** {scenario.title}
{scenario.dilemma}

**Respuesta del usuario:** {user_response}

Usa tu enfoque socrático para:
1. Hacer preguntas profundas que generen auto-reflexión
2. Conectar la situación con principios éticos universales
3. Ayudar a descubrir motivaciones y valores profundos
4. Guiar hacia el desarrollo del juicio moral personal
5. Compartir sabiduría a través de analogías y reflexiones

No des respuestas directas; mejor haz preguntas que lleven al descubrimiento personal.
"""
    
    @staticmethod
    def generate_auditor_prompt(scenario: IntegrityScenario, user_response: str) -> str:
        """Generate Inspector Rodriguez's strict, compliance-focused response"""
        return f"""
Como Inspector Rodriguez, auditor de cumplimiento estricto, evalúa:

**Escenario:** {scenario.title}
{scenario.dilemma}

**Respuesta del usuario:** {user_response}

Proporciona análisis riguroso:
1. Cumplimiento exacto con regulaciones aplicables
2. Consecuencias legales específicas de cada acción
3. Procedimientos obligatorios que deben seguirse
4. Evaluación binaria: cumple/no cumple estándares
5. Documentación requerida y evidencias necesarias

Mantén criterio inflexible basado en normatividad y procedimientos establecidos.
"""

# Example usage for testing
if __name__ == "__main__":
    
    # Initialize scenarios
    scenarios = IntegrityScenarios()
    
    print("🎯 Integridai Integrity Training Scenarios")
    print("=" * 50)
    
    # Display available scenarios
    all_scenarios = scenarios.get_all_scenarios()
    print(f"Total scenarios available: {len(all_scenarios)}")
    print()
    
    for scenario in all_scenarios:
        print(f"📋 {scenario.title}")
        print(f"   Category: {scenario.category.value}")
        print(f"   Difficulty: {scenario.difficulty.value}")
        print(f"   Stakeholders: {len(scenario.stakeholders)}")
        print(f"   Learning objectives: {len(scenario.learning_objectives)}")
        print()
    
    # Test character-specific scenarios
    print("Character-specific scenario assignments:")
    characters = ["catalina", "alexis", "mentor", "auditor"]
    
    for character in characters:
        char_scenarios = scenarios.get_scenario_for_character_training(character)
        print(f"  {character.title()}: {len(char_scenarios)} scenarios")
        for s in char_scenarios:
            print(f"    - {s.title}")
    
    print("\n✅ Integrity scenarios system ready for training!")