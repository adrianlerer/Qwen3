#!/usr/bin/env python3
"""
Integridai Hybrid AI System - Simple Demo (No Dependencies)
Sistema Híbrido de IA Integridai - Demo Simplificado (Sin Dependencias)

This demo shows the system architecture and capabilities without requiring external APIs.
Esta demo muestra la arquitectura del sistema y capacidades sin requerir APIs externas.
"""

import json
import time
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

class AIProvider(Enum):
    """AI Model Providers"""
    OPENAI = "openai"
    KIMI_K2 = "kimi_k2" 
    QWEN3 = "qwen3"

class CharacterPersonality(Enum):
    """Character personalities for integrity training"""
    CATALINA = "catalina"  # Ethical compliance expert
    ALEXIS = "alexis"      # Corruption temptation scenarios
    MENTOR = "mentor"      # Wise guidance counselor
    AUDITOR = "auditor"    # Strict compliance checker

@dataclass
class ConversationContext:
    """Context for maintaining conversation state"""
    user_id: str
    session_id: str
    character: CharacterPersonality
    scenario: str
    integrity_score: int = 100
    gamification_points: int = 0

class MockIntegrityTrainingAI:
    """
    Mock version of the Integrity Training AI for demonstration
    Versión simulada del AI de Entrenamiento en Integridad para demostración
    """
    
    def __init__(self):
        self.character_profiles = {
            CharacterPersonality.CATALINA: {
                "name": "Catalina",
                "role": "Especialista en Cumplimiento Ético",
                "responses": [
                    "Como especialista en cumplimiento, debo informarte que esta situación requiere seguir protocolos estrictos de ética empresarial.",
                    "Es fundamental mantener la transparencia y reportar cualquier conflicto de interés inmediatamente.",
                    "La integridad no se negocia. Debes priorizar el interés público sobre cualquier beneficio personal."
                ]
            },
            CharacterPersonality.ALEXIS: {
                "name": "Alexis", 
                "role": "Simulador de Tentaciones",
                "responses": [
                    "Pero considera las ventajas... nadie se enteraría y realmente necesitas esos recursos adicionales.",
                    "¿No crees que estás siendo demasiado rígido? Todos en la industria hacen este tipo de arreglos.",
                    "Piénsalo pragmáticamente: el resultado final beneficia a todos, ¿realmente importa cómo se logre?"
                ]
            },
            CharacterPersonality.MENTOR: {
                "name": "Dr. Mentor",
                "role": "Consejero de Sabiduría",
                "responses": [
                    "Reflexiona profundamente: ¿Qué tipo de líder quieres ser? ¿Cómo se alinea esta decisión con tus valores fundamentales?",
                    "La verdadera prueba del carácter no está en las decisiones fáciles, sino en cómo actuamos bajo presión.",
                    "¿Has considerado todas las perspectivas? ¿Qué consejo darías a alguien más en esta misma situación?"
                ]
            },
            CharacterPersonality.AUDITOR: {
                "name": "Inspector Rodriguez",
                "role": "Auditor Estricto",
                "responses": [
                    "INCUMPLIMIENTO DETECTADO: Artículo 6 del Código de Ética. ACCIÓN REQUERIDA: Reporte inmediato a supervisores.",
                    "PROCEDIMIENTO OBLIGATORIO: Declaración de conflicto de interés según normativa interna vigente.",
                    "CONSECUENCIAS LEGALES: Posible sanción disciplinaria y inhabilitación temporal según gravedad del caso."
                ]
            }
        }
        
        self.scenarios = {
            "procurement_bribery": {
                "title": "El Contrato Tentador - The Tempting Contract",
                "description": "Un proveedor ofrece un soborno para ganar un contrato gubernamental importante.",
                "difficulty": "Intermediate"
            },
            "conflict_interest": {
                "title": "La Empresa Familiar - The Family Business", 
                "description": "Un funcionario debe decidir sobre un contrato donde su hermano es socio.",
                "difficulty": "Beginner"
            },
            "whistleblowing": {
                "title": "El Silencio Cómplice - Complicit Silence",
                "description": "Un empleado descubre irregularidades de su jefe directo y debe decidir si reportarlas.",
                "difficulty": "Advanced"
            }
        }
        
        self.gamification_rules = {
            "correct_ethical_choice": 100,
            "ethical_reasoning_improvement": 75,
            "corruption_resistance": 300,
            "scenario_completion": 25
        }
    
    def generate_response(self, context: ConversationContext, user_message: str) -> Dict:
        """Generate mock response based on character and context"""
        
        character_data = self.character_profiles[context.character]
        
        # Simple response selection based on message content
        response_index = len(user_message) % len(character_data["responses"])
        response = character_data["responses"][response_index]
        
        # Calculate integrity score change
        score_change = 0
        if any(word in user_message.lower() for word in ["ética", "integridad", "reportar", "correcto"]):
            score_change = 10
            context.gamification_points += self.gamification_rules["correct_ethical_choice"]
        elif any(word in user_message.lower() for word in ["aceptar", "ignorar", "silencio"]):
            score_change = -15
        
        context.integrity_score = max(0, min(100, context.integrity_score + score_change))
        
        return {
            "response": response,
            "provider_used": "qwen3_demo",
            "response_time": 0.8 + (len(response) / 200),  # Simulated response time
            "character": context.character.value,
            "integrity_score": context.integrity_score,
            "gamification_points": context.gamification_points,
            "score_change": score_change
        }
    
    def run_benchmark_comparison(self) -> List[Dict]:
        """Run mock benchmark comparison"""
        
        return [
            {
                "provider": "OpenAI GPT-4",
                "response_time": 2.3,
                "quality_score": 0.92,
                "cost": 0.045,
                "character_consistency": 0.88,
                "integrity_relevance": 0.94,
                "best_for": "Highest quality responses"
            },
            {
                "provider": "Kimi-K2",
                "response_time": 1.8, 
                "quality_score": 0.89,
                "cost": 0.023,
                "character_consistency": 0.85,
                "integrity_relevance": 0.91,
                "best_for": "Complex agentic scenarios"
            },
            {
                "provider": "Qwen3 Local",
                "response_time": 0.9,
                "quality_score": 0.87,
                "cost": 0.000,
                "character_consistency": 0.90,
                "integrity_relevance": 0.89,
                "best_for": "Real-time training, no cost"
            }
        ]

def demonstration_conversation():
    """Demonstrate a complete integrity training conversation"""
    
    print("🎯 INTEGRIDAI HYBRID AI SYSTEM - DEMONSTRATION")
    print("=" * 60)
    print("Sistema Híbrido de IA para Entrenamiento en Integridad")
    print()
    
    # Initialize system
    ai_system = MockIntegrityTrainingAI()
    
    # Create conversation context
    context = ConversationContext(
        user_id="demo_employee_001",
        session_id=f"demo_session_{int(time.time())}",
        character=CharacterPersonality.CATALINA,
        scenario="procurement_bribery"
    )
    
    print("📋 Scenario: El Contrato Tentador")
    print("Un proveedor te ofrece un 'regalo' de $100,000 para elegir su propuesta en una licitación pública.")
    print()
    
    # Simulate conversation
    user_messages = [
        "Hola Catalina, un proveedor me ofreció dinero para elegir su propuesta. ¿Qué hago?",
        "Pero su propuesta es técnicamente buena, y realmente necesito ese dinero para mi familia.",
        "Tienes razón, voy a rechazar la oferta y reportar este incidente a mi supervisor."
    ]
    
    print("💬 Conversación de Entrenamiento:")
    print("-" * 40)
    
    for i, message in enumerate(user_messages, 1):
        print(f"\n👤 Usuario: {message}")
        
        response_data = ai_system.generate_response(context, message)
        
        print(f"🏛️ Catalina: {response_data['response']}")
        print(f"   📊 Proveedor: {response_data['provider_used']}")
        print(f"   ⚡ Tiempo: {response_data['response_time']:.2f}s")
        print(f"   🎯 Puntuación Integridad: {response_data['integrity_score']}/100", end="")
        if response_data['score_change'] != 0:
            change_symbol = "+" if response_data['score_change'] > 0 else ""
            print(f" ({change_symbol}{response_data['score_change']})")
        else:
            print()
        print(f"   🏆 Puntos Gamificación: {response_data['gamification_points']}")
        
        # Show achievement level
        points = response_data['gamification_points']
        if points >= 5000:
            level = "👑 Líder Íntegro"
        elif points >= 3000:
            level = "🏆 Maestro de Ética"
        elif points >= 1500:
            level = "🥇 Defensor de Principios"
        elif points >= 500:
            level = "🥈 Guardián de Integridad"
        else:
            level = "🥉 Principiante Ético"
        
        print(f"   🎖️ Nivel: {level}")

def demonstration_character_comparison():
    """Demonstrate different character responses to same scenario"""
    
    print("\n\n👥 COMPARACIÓN DE PERSONAJES")
    print("=" * 50)
    
    ai_system = MockIntegrityTrainingAI()
    
    scenario_prompt = "Un colega me pidió que falsifique unos documentos para 'acelerar' un proceso administrativo."
    
    characters = [
        (CharacterPersonality.CATALINA, "🏛️"),
        (CharacterPersonality.ALEXIS, "😈"),
        (CharacterPersonality.MENTOR, "🧙‍♂️"),
        (CharacterPersonality.AUDITOR, "👮‍♂️")
    ]
    
    print(f"💬 Escenario: '{scenario_prompt}'\n")
    
    for character, emoji in characters:
        context = ConversationContext(
            user_id="demo_user",
            session_id="comparison_session",
            character=character,
            scenario="document_falsification"
        )
        
        response_data = ai_system.generate_response(context, scenario_prompt)
        character_name = ai_system.character_profiles[character]["name"]
        
        print(f"{emoji} {character_name}:")
        print(f"   {response_data['response']}")
        print()

def demonstration_benchmark():
    """Demonstrate AI provider benchmark comparison"""
    
    print("\n📊 BENCHMARK DE PROVEEDORES DE IA")
    print("=" * 50)
    
    ai_system = MockIntegrityTrainingAI()
    results = ai_system.run_benchmark_comparison()
    
    print("Comparación de rendimiento entre modelos de IA:\n")
    
    print(f"{'Proveedor':<15} {'Tiempo(s)':<10} {'Calidad':<8} {'Costo($)':<10} {'Consistencia':<12} {'Relevancia':<10}")
    print("-" * 75)
    
    for result in results:
        print(f"{result['provider']:<15} {result['response_time']:<10.1f} {result['quality_score']:<8.2f} "
              f"{result['cost']:<10.3f} {result['character_consistency']:<12.2f} {result['integrity_relevance']:<10.2f}")
    
    print("\n🎯 Recomendaciones de Uso:")
    for result in results:
        print(f"• {result['provider']}: {result['best_for']}")

def demonstration_gamification():
    """Demonstrate gamification system"""
    
    print("\n\n🎮 SISTEMA DE GAMIFICACIÓN")
    print("=" * 50)
    
    # Simulate user progress through multiple scenarios
    user_progress = [
        {"action": "Rechazar soborno", "points": 100, "description": "Decisión ética correcta"},
        {"action": "Reportar irregularidades", "points": 300, "description": "Resistencia a corrupción"},
        {"action": "Mejorar razonamiento", "points": 75, "description": "Comprensión ética mejorada"},
        {"action": "Completar escenario", "points": 25, "description": "Escenario de compras completado"},
        {"action": "Bonus consistencia", "points": 150, "description": "Comportamiento ético consistente"}
    ]
    
    total_points = 0
    print("🏆 Progreso del Usuario - Simulación de Entrenamiento:\n")
    
    for i, action in enumerate(user_progress, 1):
        total_points += action["points"]
        print(f"Paso {i}: {action['action']} (+{action['points']} puntos)")
        print(f"        {action['description']}")
        print(f"        Total acumulado: {total_points} puntos")
        
        # Determine achievement level
        if total_points >= 10000:
            level = "💎 Campeón de Integridad"
        elif total_points >= 5000:
            level = "👑 Líder Íntegro"
        elif total_points >= 3000:
            level = "🏆 Maestro de Ética"
        elif total_points >= 1500:
            level = "🥇 Defensor de Principios"
        elif total_points >= 500:
            level = "🥈 Guardián de Integridad"
        else:
            level = "🥉 Principiante Ético"
        
        print(f"        Nivel actual: {level}")
        print()

def demonstration_scenarios():
    """Demonstrate available training scenarios"""
    
    print("\n📋 ESCENARIOS DE ENTRENAMIENTO")
    print("=" * 50)
    
    ai_system = MockIntegrityTrainingAI()
    
    print("Biblioteca de escenarios para entrenamiento en integridad:\n")
    
    for scenario_id, scenario_data in ai_system.scenarios.items():
        print(f"📖 {scenario_data['title']}")
        print(f"   Dificultad: {scenario_data['difficulty']}")
        print(f"   Descripción: {scenario_data['description']}")
        print(f"   ID: {scenario_id}")
        print()

def main():
    """Run the complete demonstration"""
    
    print("🚀 Iniciando demostración del Sistema Híbrido Integridai...")
    print()
    
    try:
        # Run all demonstrations
        demonstration_conversation()
        demonstration_character_comparison()  
        demonstration_benchmark()
        demonstration_gamification()
        demonstration_scenarios()
        
        print("\n" + "=" * 60)
        print("✅ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 60)
        print()
        print("🎯 Capacidades Demostradas:")
        print("✓ Conversaciones interactivas de entrenamiento")
        print("✓ Múltiples personalidades de IA especializadas")
        print("✓ Sistema de benchmarking comparativo")
        print("✓ Gamificación y seguimiento de progreso")
        print("✓ Biblioteca completa de escenarios")
        print()
        print("🚀 Para usar el sistema completo:")
        print("   1. Instalar dependencias: pip install -r requirements.txt")
        print("   2. Configurar claves API en archivo .env")
        print("   3. Lanzar interfaz web: python run_demo.py")
        print()
        print("📖 Para más información, ver: INTEGRIDAI_README.md")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en la demostración: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)