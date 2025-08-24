#!/usr/bin/env python3
"""
Integridai Hybrid AI System - Example Usage
Sistema Híbrido de IA Integridai - Ejemplo de Uso

This file demonstrates how to use the Integridai system for integrity training.
Este archivo demuestra cómo usar el sistema Integridai para entrenamiento en integridad.
"""

import asyncio
import json
from datetime import datetime

from integridai_hybrid_system import (
    IntegrityTrainingAI,
    ConversationContext,
    CharacterPersonality,
    AIProvider
)
from integrity_scenarios import IntegrityScenarios

async def example_conversation_catalina():
    """Example conversation with Catalina (Compliance Expert)"""
    
    print("🏛️ Example: Conversation with Catalina")
    print("=" * 50)
    
    # Initialize AI system (using mock configuration for demo)
    config = {
        'qwen3_model_path': 'Qwen/Qwen3-8B-Instruct',  # Local model
        # 'openai_api_key': 'your_key_here',  # Uncomment for real usage
        # 'kimi_api_key': 'your_key_here',    # Uncomment for real usage
    }
    
    ai_system = IntegrityTrainingAI(config)
    
    # Create conversation context
    context = ConversationContext(
        user_id="employee_001",
        session_id="training_session_001", 
        character=CharacterPersonality.CATALINA,
        scenario="procurement_bribery_scenario"
    )
    
    # Simulate conversation
    user_messages = [
        "Hola Catalina, tengo una situación complicada con un proveedor.",
        "Un proveedor me ofreció un regalo por elegir su propuesta. ¿Qué debo hacer?",
        "Pero su propuesta es realmente buena técnicamente, ¿no cuenta eso?"
    ]
    
    for message in user_messages:
        print(f"\n👤 Usuario: {message}")
        
        try:
            # Generate response (this would work with real API keys)
            response_data = await ai_system.generate_response(context, message)
            
            print(f"🏛️ Catalina: {response_data['response']}")
            print(f"   📊 Provider: {response_data['provider_used']}")
            print(f"   ⚡ Time: {response_data['response_time']:.2f}s")
            print(f"   🎯 Integrity Score: {response_data['integrity_score']}/100")
            print(f"   🏆 Points: {response_data['gamification_points']}")
            
        except Exception as e:
            print(f"❌ Error (expected in demo mode): {e}")
            
            # Fallback demonstration response
            demo_responses = [
                "Hola, soy Catalina. Como especialista en cumplimiento, estoy aquí para ayudarte con situaciones éticas complejas. Por favor, cuéntame más detalles sobre tu situación.",
                "Es importante que rechaces inmediatamente cualquier regalo o beneficio personal. Esto constituye un conflicto de interés y posible soborno. Debes reportar esta situación a tu supervisor y a la oficina de control interno.",
                "Tienes razón en que la calidad técnica es importante, pero el proceso debe ser imparcial. El hecho de que te hayan ofrecido un regalo compromete tu objetividad. Debes apartarte de la evaluación y permitir que otros colegas la realicen objetivamente."
            ]
            
            response_index = min(len(demo_responses) - 1, user_messages.index(message))
            print(f"🏛️ Catalina (Demo): {demo_responses[response_index]}")
            print(f"   📊 Provider: qwen3 (demo mode)")
            print(f"   🎯 Integrity Score: {100 - len(user_messages) * 5}/100")

async def example_benchmark_comparison():
    """Example benchmark comparison across AI providers"""
    
    print("\n📊 Example: AI Provider Benchmark")
    print("=" * 50)
    
    scenarios = IntegrityScenarios()
    
    # Get test scenarios
    test_scenarios = [
        "Un proveedor ofrece un soborno para ganar un contrato gubernamental",
        "Un funcionario debe decidir sobre un contrato donde su hermano es socio",
        "Un empleado descubre irregularidades de su jefe directo"
    ]
    
    print("Test scenarios:")
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"  {i}. {scenario}")
    
    print("\n🤖 Simulated Benchmark Results:")
    
    # Simulate benchmark results (in real usage, this would call actual APIs)
    mock_results = {
        "OpenAI GPT-4": {
            "response_time": 2.3,
            "quality_score": 0.92,
            "cost": 0.045,
            "character_consistency": 0.88,
            "integrity_relevance": 0.94
        },
        "Kimi-K2": {
            "response_time": 1.8,
            "quality_score": 0.89,
            "cost": 0.023,
            "character_consistency": 0.85,
            "integrity_relevance": 0.91
        },
        "Qwen3 Local": {
            "response_time": 0.9,
            "quality_score": 0.87,
            "cost": 0.000,
            "character_consistency": 0.90,
            "integrity_relevance": 0.89
        }
    }
    
    print("\n📈 Results Summary:")
    print(f"{'Provider':<15} {'Time(s)':<8} {'Quality':<8} {'Cost($)':<8} {'Consistency':<12} {'Relevance':<10}")
    print("-" * 70)
    
    for provider, results in mock_results.items():
        print(f"{provider:<15} {results['response_time']:<8.1f} {results['quality_score']:<8.2f} "
              f"{results['cost']:<8.3f} {results['character_consistency']:<12.2f} {results['integrity_relevance']:<10.2f}")
    
    # Analysis
    print("\n🎯 Recommendations:")
    print("• For real-time training: Qwen3 Local (fastest, no cost)")
    print("• For highest quality: OpenAI GPT-4 (best scores)")  
    print("• For cost-effectiveness: Kimi-K2 (balanced performance/cost)")
    print("• For character consistency: Qwen3 Local (best character adherence)")

def example_scenario_analysis():
    """Example integrity scenario analysis"""
    
    print("\n🧪 Example: Scenario Analysis")
    print("=" * 50)
    
    scenarios = IntegrityScenarios()
    
    # Get a sample scenario
    scenario = scenarios.get_scenario("procurement_bribery_01")
    
    if scenario:
        print(f"📋 Scenario: {scenario.title}")
        print(f"Category: {scenario.category.value}")
        print(f"Difficulty: {scenario.difficulty.value}")
        
        print(f"\n📖 Context:")
        print(scenario.context[:200] + "...")
        
        print(f"\n🎭 Stakeholders ({len(scenario.stakeholders)}):")
        for stakeholder in scenario.stakeholders[:3]:
            print(f"  • {stakeholder}")
        if len(scenario.stakeholders) > 3:
            print(f"  • ... and {len(scenario.stakeholders) - 3} more")
        
        print(f"\n⚖️ Ethical Considerations:")
        for consideration in scenario.ethical_considerations[:2]:
            print(f"  • {consideration}")
        
        print(f"\n📚 Learning Objectives:")
        for objective in scenario.learning_objectives[:2]:
            print(f"  • {objective}")
        
        print(f"\n🎯 Correct Action Preview:")
        print(scenario.correct_action[:150] + "...")

def example_gamification_system():
    """Example gamification system demonstration"""
    
    print("\n🎮 Example: Gamification System")
    print("=" * 50)
    
    # Simulate user progress
    user_actions = [
        {"action": "correct_ethical_choice", "points": 100, "description": "Rejected bribe offer"},
        {"action": "ethical_reasoning_improvement", "points": 75, "description": "Showed improved understanding"},
        {"action": "scenario_completion", "points": 25, "description": "Completed procurement scenario"},
        {"action": "corruption_resistance", "points": 300, "description": "Resisted strong temptation"},
        {"action": "consistency_bonus", "points": 150, "description": "Consistent ethical behavior"}
    ]
    
    total_points = 0
    print("🏆 User Progress Simulation:")
    
    for i, action in enumerate(user_actions, 1):
        total_points += action["points"]
        print(f"  Step {i}: {action['description']} (+{action['points']} pts)")
        print(f"          Total: {total_points} points")
        
        # Determine achievement level
        if total_points >= 5000:
            level = "👑 Líder Íntegro"
        elif total_points >= 3000:
            level = "🏆 Maestro de Ética"
        elif total_points >= 1500:
            level = "🥇 Defensor de Principios"
        elif total_points >= 500:
            level = "🥈 Guardián de Integridad"
        else:
            level = "🥉 Principiante Ético"
        
        print(f"          Level: {level}")
        print()

def example_character_personalities():
    """Demonstrate different character personalities"""
    
    print("\n👥 Example: Character Personalities")
    print("=" * 50)
    
    scenario_prompt = "Un empleado me ofreció información confidencial sobre un competidor a cambio de un favor."
    
    characters = {
        "Catalina": {
            "emoji": "🏛️",
            "response": "Como especialista en cumplimiento, debo informarte que recibir información confidencial de un competidor constituye espionaje empresarial y violación de ética. Debes rechazar inmediatamente esta propuesta y reportar el incidente a tu supervisor y al departamento legal."
        },
        "Alexis": {
            "emoji": "😈", 
            "response": "Pero piénsalo... ¿no te daría una ventaja competitiva significativa? El empleado ya tomó la decisión de ofrecértela. Tú no estás robando nada directamente. Además, ¿cómo sabemos que tu competencia no hace lo mismo contigo?"
        },
        "Dr. Mentor": {
            "emoji": "🧙‍♂️",
            "response": "Interesante dilema. Antes de decidir, reflexiona: ¿Qué tipo de líder quieres ser? ¿Cómo te sentirías si alguien hiciera esto con información de tu empresa? ¿Qué principios fundamentales están en juego aquí?"
        },
        "Inspector Rodriguez": {
            "emoji": "👮‍♂️",
            "response": "VIOLACIÓN CLARA: Artículo 308 Código Penal - violación de reserva industrial o comercial. CONSECUENCIAS: Multa y prisión 2-5 años. PROCEDIMIENTO OBLIGATORIO: Reportar inmediatamente. DOCUMENTACIÓN REQUERIDA: Registro escrito del incidente."
        }
    }
    
    print(f"💬 Scenario: '{scenario_prompt}'\n")
    
    for name, char_data in characters.items():
        print(f"{char_data['emoji']} {name}:")
        print(f"   {char_data['response']}")
        print()

async def main():
    """Run all examples"""
    
    print("🎯 INTEGRIDAI HYBRID AI SYSTEM - EXAMPLES")
    print("=" * 60)
    print("Sistema Híbrido de IA para Entrenamiento en Integridad")
    print("Hybrid AI System for Integrity Training")
    print()
    
    # Run examples
    await example_conversation_catalina()
    await example_benchmark_comparison()
    example_scenario_analysis()
    example_gamification_system()
    example_character_personalities()
    
    print("\n" + "=" * 60)
    print("✅ Examples completed!")
    print()
    print("🚀 To run the interactive demo:")
    print("   python run_demo.py")
    print()
    print("📖 To configure API keys:")
    print("   Edit the .env file with your OpenAI and Kimi-K2 keys")
    print()
    print("🔧 System capabilities:")
    print("   • Multi-provider AI integration (OpenAI + Kimi-K2 + Qwen3)")
    print("   • Character-based integrity training (Catalina, Alexis, Mentor, Auditor)")  
    print("   • Gamification and progress tracking")
    print("   • Comprehensive scenario library")
    print("   • Performance benchmarking")
    print("   • Real-time chat interface")

if __name__ == "__main__":
    asyncio.run(main())