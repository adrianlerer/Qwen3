#!/usr/bin/env python3
"""
Integridai Hybrid AI System for Integrity Training
Sistema Híbrido de IA para Entrenamiento en Integridad

Combines OpenAI, Kimi-K2, and Qwen3 for optimal performance
Combina OpenAI, Kimi-K2 y Qwen3 para rendimiento óptimo

Author: Integridai Suite Team
License: MIT
"""

import asyncio
import json
import logging
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union, Any
import openai
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    conversation_history: List[Dict] = None
    gamification_points: int = 0
    
    def __post_init__(self):
        if self.conversation_history is None:
            self.conversation_history = []

@dataclass 
class BenchmarkResult:
    """Results from AI model benchmarking"""
    provider: AIProvider
    response_time: float
    quality_score: float
    cost: float
    character_consistency: float
    integrity_relevance: float

class IntegrityTrainingAI:
    """
    Hybrid AI system for integrity training using multiple providers
    Sistema híbrido de IA para entrenamiento en integridad
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.openai_client = None
        self.kimi_client = None
        self.qwen3_model = None
        self.qwen3_tokenizer = None
        
        self._initialize_providers()
        self._load_character_profiles()
        self._initialize_gamification_engine()
    
    def _initialize_providers(self):
        """Initialize all AI providers"""
        logger.info("Initializing AI providers...")
        
        # OpenAI Setup
        if self.config.get('openai_api_key'):
            openai.api_key = self.config['openai_api_key']
            self.openai_client = openai
            logger.info("✅ OpenAI initialized")
        
        # Kimi-K2 Setup (Moonshot AI API)
        if self.config.get('kimi_api_key'):
            self.kimi_client = {
                'api_key': self.config['kimi_api_key'],
                'base_url': 'https://api.moonshot.cn/v1',
                'headers': {
                    'Authorization': f"Bearer {self.config['kimi_api_key']}",
                    'Content-Type': 'application/json'
                }
            }
            logger.info("✅ Kimi-K2 initialized")
        
        # Qwen3 Local Setup
        if self.config.get('qwen3_model_path'):
            try:
                logger.info("Loading Qwen3 model locally...")
                self.qwen3_tokenizer = AutoTokenizer.from_pretrained(
                    self.config['qwen3_model_path']
                )
                self.qwen3_model = AutoModelForCausalLM.from_pretrained(
                    self.config['qwen3_model_path'],
                    torch_dtype="auto",
                    device_map="auto" if torch.cuda.is_available() else None
                )
                logger.info("✅ Qwen3 loaded successfully")
            except Exception as e:
                logger.error(f"❌ Error loading Qwen3: {e}")
                self.qwen3_model = None
    
    def _load_character_profiles(self):
        """Load character personality profiles"""
        self.character_profiles = {
            CharacterPersonality.CATALINA: {
                "name": "Catalina",
                "role": "Especialista en Cumplimiento Ético",
                "personality": "Profesional, empática, orientada a soluciones",
                "expertise": "Códigos de ética empresarial, dilemas morales, compliance",
                "speaking_style": "Formal pero accesible, usa ejemplos prácticos",
                "system_prompt": """Eres Catalina, una especialista en cumplimiento ético con 15 años de experiencia. 
                Tu misión es ayudar a los empleados a entender y aplicar principios de integridad en situaciones complejas.
                Siempre buscas educar sin juzgar, usando casos reales y soluciones prácticas.
                Hablas en español de manera profesional pero cercana."""
            },
            
            CharacterPersonality.ALEXIS: {
                "name": "Alexis",
                "role": "Simulador de Tentaciones y Dilemas",
                "personality": "Persuasivo, desafiante, realista",
                "expertise": "Escenarios de corrupción, presión empresarial, dilemas éticos",
                "speaking_style": "Directo, convincente, presenta argumentos tentadores",
                "system_prompt": """Eres Alexis, un personaje que presenta escenarios desafiantes de integridad.
                Tu rol es crear dilemas éticos realistas que pongan a prueba los principios morales del usuario.
                No promuevas la corrupción, pero sí presenta argumentos convincentes que una persona corrupta usaría.
                El objetivo es entrenar la resistencia ética a través de la práctica."""
            },
            
            CharacterPersonality.MENTOR: {
                "name": "Dr. Mentor",
                "role": "Consejero de Sabiduría Ética", 
                "personality": "Sabio, paciente, reflexivo",
                "expertise": "Filosofía moral, desarrollo del carácter, liderazgo ético",
                "speaking_style": "Pausado, reflexivo, usa preguntas socráticas",
                "system_prompt": """Eres el Dr. Mentor, un consejero ético con décadas de experiencia.
                Tu enfoque es ayudar a las personas a desarrollar su propio juicio moral a través de preguntas reflexivas.
                No das respuestas directas, sino que guías el descubrimiento personal de principios éticos sólidos.
                Usas historias, metáforas y preguntas profundas para generar reflexión."""
            },
            
            CharacterPersonality.AUDITOR: {
                "name": "Inspector Rodriguez",
                "role": "Auditor de Cumplimiento Estricto",
                "personality": "Riguroso, detallista, inflexible",
                "expertise": "Regulaciones, procedimientos, consecuencias legales",
                "speaking_style": "Técnico, preciso, sin ambigüedades",
                "system_prompt": """Eres el Inspector Rodriguez, un auditor de cumplimiento con criterio estricto.
                Tu misión es evaluar comportamientos según regulaciones exactas y procedimientos establecidos.
                No hay zonas grises en tu análisis - algo cumple o no cumple con los estándares.
                Proporcionas feedback directo sobre consecuencias legales y reglamentarias."""
            }
        }
    
    def _initialize_gamification_engine(self):
        """Initialize gamification scoring system"""
        self.gamification_rules = {
            "correct_ethical_choice": 100,
            "partial_ethical_understanding": 50,
            "ethical_reasoning_improvement": 75,
            "scenario_completion": 25,
            "consistency_bonus": 150,
            "integrity_challenge_passed": 200,
            "corruption_resistance": 300,
        }
        
        self.achievement_levels = {
            "Principiante Ético": 0,
            "Guardián de Integridad": 500, 
            "Defensor de Principios": 1500,
            "Maestro de Ética": 3000,
            "Líder Íntegro": 5000,
            "Campeón de Integridad": 10000
        }
    
    async def generate_response(
        self, 
        context: ConversationContext,
        user_message: str,
        preferred_provider: Optional[AIProvider] = None
    ) -> Dict[str, Any]:
        """
        Generate response using the best AI provider for the context
        Genera respuesta usando el mejor proveedor de IA para el contexto
        """
        
        # Determine best provider if not specified
        if not preferred_provider:
            preferred_provider = self._select_optimal_provider(context)
        
        character_profile = self.character_profiles[context.character]
        
        # Build conversation prompt
        prompt = self._build_character_prompt(character_profile, context, user_message)
        
        # Generate response based on provider
        start_time = time.time()
        
        try:
            if preferred_provider == AIProvider.OPENAI:
                response = await self._generate_openai_response(prompt, context)
            elif preferred_provider == AIProvider.KIMI_K2:
                response = await self._generate_kimi_response(prompt, context)
            elif preferred_provider == AIProvider.QWEN3:
                response = await self._generate_qwen3_response(prompt, context)
            else:
                raise ValueError(f"Unsupported provider: {preferred_provider}")
            
            response_time = time.time() - start_time
            
            # Update context and gamification
            self._update_conversation_context(context, user_message, response)
            gamification_update = self._calculate_gamification_points(context, response)
            
            return {
                "response": response,
                "provider_used": preferred_provider.value,
                "response_time": response_time,
                "character": context.character.value,
                "integrity_score": context.integrity_score,
                "gamification_points": context.gamification_points,
                "gamification_update": gamification_update,
                "achievement_level": self._get_achievement_level(context.gamification_points)
            }
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            # Fallback to alternative provider
            return await self._fallback_response(context, user_message, preferred_provider)
    
    def _select_optimal_provider(self, context: ConversationContext) -> AIProvider:
        """
        Select the optimal AI provider based on context and requirements
        Selecciona el proveedor óptimo de IA basado en contexto y requisitos
        """
        
        # Logic for provider selection based on:
        # - Character personality requirements
        # - Scenario complexity 
        # - Performance needs
        # - Cost considerations
        
        character = context.character
        
        if character == CharacterPersonality.CATALINA:
            # Catalina needs empathetic, professional responses - OpenAI excels here
            return AIProvider.OPENAI if self.openai_client else AIProvider.QWEN3
        
        elif character == CharacterPersonality.ALEXIS:
            # Alexis needs creative, challenging scenarios - Kimi-K2's agentic capabilities
            return AIProvider.KIMI_K2 if self.kimi_client else AIProvider.QWEN3
        
        elif character == CharacterPersonality.MENTOR:
            # Mentor needs deep reasoning - Qwen3 thinking mode
            return AIProvider.QWEN3 if self.qwen3_model else AIProvider.OPENAI
        
        elif character == CharacterPersonality.AUDITOR:
            # Auditor needs precise, structured responses - OpenAI's consistency
            return AIProvider.OPENAI if self.openai_client else AIProvider.QWEN3
        
        # Default fallback
        return AIProvider.QWEN3 if self.qwen3_model else AIProvider.OPENAI
    
    def _build_character_prompt(
        self, 
        character_profile: Dict, 
        context: ConversationContext, 
        user_message: str
    ) -> str:
        """Build character-specific prompt"""
        
        base_prompt = character_profile["system_prompt"]
        
        scenario_context = f"\n\nEscenario actual: {context.scenario}"
        history_context = self._format_conversation_history(context.conversation_history[-3:])  # Last 3 messages
        
        prompt = f"""
{base_prompt}

{scenario_context}

Historial reciente:
{history_context}

Puntuación actual de integridad del usuario: {context.integrity_score}/100
Puntos de gamificación: {context.gamification_points}

Mensaje del usuario: {user_message}

Responde como {character_profile['name']}, manteniendo tu personalidad y expertise. 
Evalúa la respuesta del usuario en términos de integridad y proporciona feedback constructivo.
Considera el impacto en la puntuación de integridad y sugiere próximos pasos en el entrenamiento.
"""
        
        return prompt
    
    async def _generate_openai_response(self, prompt: str, context: ConversationContext) -> str:
        """Generate response using OpenAI API"""
        if not self.openai_client:
            raise ValueError("OpenAI client not initialized")
        
        try:
            response = await self.openai_client.ChatCompletion.acreate(
                model=self.config.get('openai_model', 'gpt-4'),
                messages=[{"role": "system", "content": prompt}],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    async def _generate_kimi_response(self, prompt: str, context: ConversationContext) -> str:
        """Generate response using Kimi-K2 API"""
        if not self.kimi_client:
            raise ValueError("Kimi-K2 client not initialized")
        
        try:
            payload = {
                "model": "moonshot-v1-128k",  # Kimi-K2 model
                "messages": [{"role": "system", "content": prompt}],
                "temperature": 0.6,  # Kimi recommended temperature
                "max_tokens": 1500
            }
            
            response = requests.post(
                f"{self.kimi_client['base_url']}/chat/completions",
                headers=self.kimi_client['headers'],
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except Exception as e:
            logger.error(f"Kimi-K2 API error: {e}")
            raise
    
    async def _generate_qwen3_response(self, prompt: str, context: ConversationContext) -> str:
        """Generate response using local Qwen3 model"""
        if not self.qwen3_model:
            raise ValueError("Qwen3 model not loaded")
        
        try:
            messages = [{"role": "user", "content": prompt}]
            
            text = self.qwen3_tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            model_inputs = self.qwen3_tokenizer([text], return_tensors="pt")
            if torch.cuda.is_available():
                model_inputs = model_inputs.to(self.qwen3_model.device)
            
            # Use thinking mode for complex scenarios
            enable_thinking = context.character in [CharacterPersonality.MENTOR, CharacterPersonality.AUDITOR]
            
            generated_ids = self.qwen3_model.generate(
                **model_inputs,
                max_new_tokens=1500,
                temperature=0.7,
                do_sample=True
            )
            
            response_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
            response = self.qwen3_tokenizer.decode(response_ids, skip_special_tokens=True)
            
            return response
            
        except Exception as e:
            logger.error(f"Qwen3 generation error: {e}")
            raise
    
    async def _fallback_response(
        self, 
        context: ConversationContext, 
        user_message: str, 
        failed_provider: AIProvider
    ) -> Dict[str, Any]:
        """Fallback to alternative provider when primary fails"""
        
        providers = [AIProvider.QWEN3, AIProvider.OPENAI, AIProvider.KIMI_K2]
        providers.remove(failed_provider)
        
        for provider in providers:
            try:
                if provider == AIProvider.OPENAI and self.openai_client:
                    return await self.generate_response(context, user_message, provider)
                elif provider == AIProvider.KIMI_K2 and self.kimi_client:
                    return await self.generate_response(context, user_message, provider)
                elif provider == AIProvider.QWEN3 and self.qwen3_model:
                    return await self.generate_response(context, user_message, provider)
            except Exception as e:
                logger.warning(f"Fallback provider {provider.value} also failed: {e}")
                continue
        
        # Emergency fallback
        return {
            "response": "Lo siento, estoy experimentando dificultades técnicas. Por favor, intenta nuevamente en unos momentos.",
            "provider_used": "fallback",
            "response_time": 0,
            "character": context.character.value,
            "integrity_score": context.integrity_score,
            "gamification_points": context.gamification_points,
            "error": "All providers failed"
        }
    
    def _format_conversation_history(self, history: List[Dict]) -> str:
        """Format conversation history for context"""
        if not history:
            return "Sin historial previo."
        
        formatted = []
        for entry in history:
            role = "Usuario" if entry.get('role') == 'user' else "Asistente"
            formatted.append(f"{role}: {entry.get('content', '')}")
        
        return "\n".join(formatted)
    
    def _update_conversation_context(
        self, 
        context: ConversationContext, 
        user_message: str, 
        ai_response: str
    ):
        """Update conversation context with new exchange"""
        context.conversation_history.extend([
            {"role": "user", "content": user_message, "timestamp": time.time()},
            {"role": "assistant", "content": ai_response, "timestamp": time.time()}
        ])
        
        # Keep only last 20 messages to prevent context explosion
        if len(context.conversation_history) > 20:
            context.conversation_history = context.conversation_history[-20:]
    
    def _calculate_gamification_points(
        self, 
        context: ConversationContext, 
        response: str
    ) -> Dict[str, Any]:
        """Calculate gamification points based on interaction"""
        
        points_earned = 0
        achievements = []
        
        # Analyze response for ethical indicators (simplified logic)
        # In production, this would use NLP analysis
        
        if "ética" in response.lower() or "integridad" in response.lower():
            points_earned += self.gamification_rules["ethical_reasoning_improvement"]
            achievements.append("Pensamiento Ético Demostrado")
        
        points_earned += self.gamification_rules["scenario_completion"]
        
        context.gamification_points += points_earned
        
        return {
            "points_earned": points_earned,
            "total_points": context.gamification_points,
            "achievements": achievements,
            "level": self._get_achievement_level(context.gamification_points)
        }
    
    def _get_achievement_level(self, points: int) -> str:
        """Get current achievement level based on points"""
        for level, threshold in reversed(list(self.achievement_levels.items())):
            if points >= threshold:
                return level
        return "Principiante Ético"
    
    async def run_benchmark_comparison(
        self, 
        test_scenarios: List[str], 
        character: CharacterPersonality
    ) -> List[BenchmarkResult]:
        """
        Run benchmark comparison across all available providers
        Ejecuta comparación de benchmark entre todos los proveedores disponibles
        """
        
        results = []
        
        for provider in AIProvider:
            if not self._is_provider_available(provider):
                continue
            
            provider_results = []
            
            for scenario in test_scenarios:
                context = ConversationContext(
                    user_id="benchmark_user",
                    session_id="benchmark_session",
                    character=character,
                    scenario=scenario
                )
                
                try:
                    start_time = time.time()
                    response_data = await self.generate_response(
                        context, 
                        "Explícame cómo manejarías esta situación desde el punto de vista ético.",
                        preferred_provider=provider
                    )
                    end_time = time.time()
                    
                    # Calculate quality metrics (simplified)
                    quality_score = self._evaluate_response_quality(
                        response_data["response"], 
                        scenario, 
                        character
                    )
                    
                    result = BenchmarkResult(
                        provider=provider,
                        response_time=end_time - start_time,
                        quality_score=quality_score,
                        cost=self._estimate_cost(provider, response_data["response"]),
                        character_consistency=self._evaluate_character_consistency(
                            response_data["response"], 
                            character
                        ),
                        integrity_relevance=self._evaluate_integrity_relevance(
                            response_data["response"]
                        )
                    )
                    
                    provider_results.append(result)
                    
                except Exception as e:
                    logger.error(f"Benchmark failed for {provider.value}: {e}")
            
            if provider_results:
                # Average the results for this provider
                avg_result = self._average_benchmark_results(provider_results)
                results.append(avg_result)
        
        return results
    
    def _is_provider_available(self, provider: AIProvider) -> bool:
        """Check if provider is available and configured"""
        if provider == AIProvider.OPENAI:
            return self.openai_client is not None
        elif provider == AIProvider.KIMI_K2:
            return self.kimi_client is not None
        elif provider == AIProvider.QWEN3:
            return self.qwen3_model is not None
        return False
    
    def _evaluate_response_quality(
        self, 
        response: str, 
        scenario: str, 
        character: CharacterPersonality
    ) -> float:
        """Evaluate response quality (simplified scoring)"""
        
        score = 0.5  # Base score
        
        # Length appropriateness
        if 100 <= len(response) <= 800:
            score += 0.1
        
        # Character-specific keywords
        character_keywords = {
            CharacterPersonality.CATALINA: ["cumplimiento", "ética", "profesional", "solución"],
            CharacterPersonality.ALEXIS: ["dilema", "tentación", "presión", "decisión"],
            CharacterPersonality.MENTOR: ["reflexiona", "considera", "pregunta", "sabiduría"],
            CharacterPersonality.AUDITOR: ["regulación", "procedimiento", "cumple", "infracción"]
        }
        
        keywords = character_keywords.get(character, [])
        for keyword in keywords:
            if keyword in response.lower():
                score += 0.05
        
        # Integrity-related content
        integrity_terms = ["integridad", "ética", "moral", "principios", "valores"]
        for term in integrity_terms:
            if term in response.lower():
                score += 0.03
        
        return min(score, 1.0)
    
    def _evaluate_character_consistency(self, response: str, character: CharacterPersonality) -> float:
        """Evaluate how well the response matches character personality"""
        # Simplified implementation - in production would use more sophisticated NLP
        
        character_traits = {
            CharacterPersonality.CATALINA: ["profesional", "empática", "práctica"],
            CharacterPersonality.ALEXIS: ["desafiante", "persuasivo", "realista"],
            CharacterPersonality.MENTOR: ["reflexivo", "sabio", "pregunta"],
            CharacterPersonality.AUDITOR: ["riguroso", "preciso", "estricto"]
        }
        
        traits = character_traits.get(character, [])
        score = 0.5
        
        for trait in traits:
            if trait in response.lower():
                score += 0.15
        
        return min(score, 1.0)
    
    def _evaluate_integrity_relevance(self, response: str) -> float:
        """Evaluate how relevant the response is to integrity training"""
        
        integrity_indicators = [
            "integridad", "ética", "moral", "principios", "valores", "cumplimiento",
            "transparencia", "honestidad", "responsabilidad", "accountability"
        ]
        
        score = 0.3  # Base score
        for indicator in integrity_indicators:
            if indicator in response.lower():
                score += 0.07
        
        return min(score, 1.0)
    
    def _estimate_cost(self, provider: AIProvider, response: str) -> float:
        """Estimate cost for the API call (simplified)"""
        
        # Rough cost estimates per 1000 tokens
        cost_per_1k_tokens = {
            AIProvider.OPENAI: 0.03,  # GPT-4 pricing
            AIProvider.KIMI_K2: 0.015,  # Estimated based on similar services
            AIProvider.QWEN3: 0.0  # Local model, only compute cost
        }
        
        estimated_tokens = len(response.split()) * 1.3  # Rough token estimation
        cost_per_token = cost_per_1k_tokens.get(provider, 0.02) / 1000
        
        return estimated_tokens * cost_per_token
    
    def _average_benchmark_results(self, results: List[BenchmarkResult]) -> BenchmarkResult:
        """Average multiple benchmark results for a provider"""
        
        if not results:
            return None
        
        return BenchmarkResult(
            provider=results[0].provider,
            response_time=sum(r.response_time for r in results) / len(results),
            quality_score=sum(r.quality_score for r in results) / len(results),
            cost=sum(r.cost for r in results) / len(results),
            character_consistency=sum(r.character_consistency for r in results) / len(results),
            integrity_relevance=sum(r.integrity_relevance for r in results) / len(results)
        )

# Example usage and testing
if __name__ == "__main__":
    
    # Configuration example
    config = {
        'openai_api_key': 'your-openai-key-here',
        'openai_model': 'gpt-4',
        'kimi_api_key': 'your-kimi-key-here', 
        'qwen3_model_path': 'Qwen/Qwen3-8B-Instruct',
    }
    
    print("🚀 Integridai Hybrid AI System for Integrity Training")
    print("=" * 60)
    print("Sistema Híbrido de IA para Entrenamiento en Integridad")
    print()
    print("Características:")
    print("✅ Soporte para OpenAI, Kimi-K2 y Qwen3")
    print("✅ Personajes especializados (Catalina, Alexis, Mentor, Auditor)")
    print("✅ Sistema de gamificación integrado")
    print("✅ Benchmarking automático de proveedores")
    print("✅ Selección inteligente de modelo según contexto")
    print("✅ Sistema de puntuación de integridad")
    print()
    
    # Initialize system
    ai_system = IntegrityTrainingAI(config)
    
    print("Sistema inicializado. Listo para entrenamiento en integridad! 🎯")