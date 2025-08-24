#!/usr/bin/env python3
"""
Integridai Benchmark Demo System
Sistema de Demo y Benchmark para Integridai

Author: Integridai Suite Team  
License: MIT
"""

import asyncio
import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from integridai_hybrid_system import (
    IntegrityTrainingAI, 
    ConversationContext, 
    CharacterPersonality, 
    AIProvider,
    BenchmarkResult
)
from integrity_scenarios import IntegrityScenarios, CharacterPromptGenerator

class BenchmarkDemo:
    """
    Demonstration and benchmarking system for Integridai AI models
    Sistema de demostración y benchmarking para modelos IA de Integridai
    """
    
    def __init__(self):
        self.ai_system = None
        self.scenarios = IntegrityScenarios()
        self.benchmark_results = []
        
    def initialize_ai_system(self, config: Dict) -> bool:
        """Initialize the AI system with configuration"""
        try:
            self.ai_system = IntegrityTrainingAI(config)
            return True
        except Exception as e:
            st.error(f"Error initializing AI system: {e}")
            return False
    
    def create_streamlit_interface(self):
        """Create the main Streamlit interface"""
        
        st.set_page_config(
            page_title="Integridai Hybrid AI System",
            page_icon="🎯",
            layout="wide"
        )
        
        # Main header
        st.title("🎯 Integridai Hybrid AI System")
        st.markdown("**Sistema Híbrido de IA para Entrenamiento en Integridad**")
        st.markdown("*OpenAI + Kimi-K2 + Qwen3 Comparison & Benchmarking*")
        
        # Sidebar for configuration
        with st.sidebar:
            st.header("⚙️ Configuration")
            
            # API Keys configuration
            st.subheader("API Keys")
            openai_key = st.text_input("OpenAI API Key", type="password")
            kimi_key = st.text_input("Kimi-K2 API Key", type="password") 
            
            # Model selection
            st.subheader("Models")
            use_qwen3 = st.checkbox("Use Qwen3 Local", value=True)
            qwen3_model = st.selectbox(
                "Qwen3 Model", 
                ["Qwen/Qwen3-8B-Instruct", "Qwen/Qwen3-4B-Instruct", "Qwen/Qwen3-30B-A3B-Instruct-2507"]
            )
            
            # Test configuration
            st.subheader("Test Configuration")
            test_mode = st.selectbox(
                "Mode", 
                ["Interactive Chat", "Benchmark Comparison", "Scenario Testing"]
            )
            
            config = {
                'openai_api_key': openai_key if openai_key else None,
                'kimi_api_key': kimi_key if kimi_key else None,
                'qwen3_model_path': qwen3_model if use_qwen3 else None,
            }
            
            if st.button("Initialize System"):
                if self.initialize_ai_system(config):
                    st.success("✅ System initialized!")
                    st.session_state['system_ready'] = True
                else:
                    st.error("❌ System initialization failed")
        
        # Main content area
        if st.session_state.get('system_ready', False):
            
            if test_mode == "Interactive Chat":
                self._create_interactive_chat()
            elif test_mode == "Benchmark Comparison":
                self._create_benchmark_interface()
            elif test_mode == "Scenario Testing":
                self._create_scenario_testing()
        else:
            self._create_welcome_screen()
    
    def _create_welcome_screen(self):
        """Create the welcome screen with system overview"""
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.header("🤖 AI Models")
            st.markdown("""
            **OpenAI GPT-4**
            - Excelente para respuestas empáticas
            - Consistencia en personalidades
            - Ideal para Catalina (compliance)
            
            **Kimi-K2 (1T parameters)**  
            - Capacidades agénticas avanzadas
            - Razonamiento complejo
            - Ideal para Alexis (dilemas)
            
            **Qwen3 (Local)**
            - Modo thinking/non-thinking
            - Control completo de datos
            - Ideal para Mentor (reflexión)
            """)
        
        with col2:
            st.header("👥 Characters")
            st.markdown("""
            **Catalina** 🏛️
            *Especialista en Cumplimiento*
            - Profesional y empática
            - Soluciones prácticas
            - Enfoque en compliance
            
            **Alexis** 😈  
            *Simulador de Tentaciones*
            - Presenta dilemas realistas
            - Argumentos convincentes
            - Prueba resistencia ética
            
            **Dr. Mentor** 🧙‍♂️
            *Consejero Sabio*
            - Preguntas socráticas
            - Reflexión profunda
            - Desarrollo del juicio moral
            
            **Inspector Rodriguez** 👮‍♂️
            *Auditor Estricto*
            - Criterio inflexible
            - Cumplimiento exacto
            - Consecuencias legales
            """)
        
        with col3:
            st.header("🎮 Gamification")
            st.markdown("""
            **Sistema de Puntos:**
            - Decisiones éticas: +100 pts
            - Resistencia a corrupción: +300 pts
            - Razonamiento mejorado: +75 pts
            
            **Niveles de Logro:**
            - 🥉 Principiante Ético (0 pts)
            - 🥈 Guardián Integridad (500 pts)  
            - 🥇 Defensor Principios (1,500 pts)
            - 🏆 Maestro Ética (3,000 pts)
            - 👑 Líder Íntegro (5,000 pts)
            - 💎 Campeón Integridad (10,000 pts)
            """)
        
        st.markdown("---")
        st.info("👆 Configure your API keys in the sidebar and click 'Initialize System' to begin!")
    
    def _create_interactive_chat(self):
        """Create interactive chat interface"""
        
        st.header("💬 Interactive Integrity Training")
        
        col1, col2 = st.columns([2, 1])
        
        with col2:
            # Character selection
            character = st.selectbox(
                "Select Character",
                ["Catalina", "Alexis", "Dr. Mentor", "Inspector Rodriguez"]
            )
            
            character_map = {
                "Catalina": CharacterPersonality.CATALINA,
                "Alexis": CharacterPersonality.ALEXIS, 
                "Dr. Mentor": CharacterPersonality.MENTOR,
                "Inspector Rodriguez": CharacterPersonality.AUDITOR
            }
            
            selected_character = character_map[character]
            
            # Scenario selection
            scenario_options = self.scenarios.get_all_scenarios()
            scenario_titles = [s.title for s in scenario_options]
            selected_scenario_title = st.selectbox("Select Scenario", scenario_titles)
            
            selected_scenario = next(s for s in scenario_options if s.title == selected_scenario_title)
            
            # AI Provider selection
            provider = st.selectbox(
                "AI Provider", 
                ["Auto-Select", "OpenAI", "Kimi-K2", "Qwen3"]
            )
            
            provider_map = {
                "OpenAI": AIProvider.OPENAI,
                "Kimi-K2": AIProvider.KIMI_K2,
                "Qwen3": AIProvider.QWEN3
            }
        
        with col1:
            # Scenario display
            st.subheader(f"📋 {selected_scenario.title}")
            st.markdown(f"**Category:** {selected_scenario.category.value}")
            st.markdown(f"**Difficulty:** {selected_scenario.difficulty.value}")
            
            with st.expander("Scenario Details"):
                st.markdown("**Context:**")
                st.write(selected_scenario.context)
                st.markdown("**Dilemma:**") 
                st.write(selected_scenario.dilemma)
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("**Stakeholders:**")
                    for stakeholder in selected_scenario.stakeholders:
                        st.write(f"• {stakeholder}")
                
                with col_b:
                    st.markdown("**Learning Objectives:**")
                    for objective in selected_scenario.learning_objectives:
                        st.write(f"• {objective}")
        
        # Chat interface
        st.markdown("---")
        
        # Initialize conversation context
        if 'conversation_context' not in st.session_state:
            st.session_state.conversation_context = ConversationContext(
                user_id="demo_user",
                session_id=f"session_{int(time.time())}",
                character=selected_character,
                scenario=selected_scenario.description
            )
        
        # Chat history display
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if message["role"] == "assistant" and "metadata" in message:
                    metadata = message["metadata"]
                    st.caption(f"Provider: {metadata.get('provider', 'Unknown')} | "
                              f"Response time: {metadata.get('response_time', 0):.2f}s | "
                              f"Integrity score: {metadata.get('integrity_score', 0)}")
        
        # User input
        user_message = st.chat_input("Type your response to the integrity scenario...")
        
        if user_message:
            # Add user message to history
            st.session_state.chat_history.append({
                "role": "user", 
                "content": user_message
            })
            
            # Generate AI response
            with st.spinner("Generating response..."):
                try:
                    selected_provider = provider_map.get(provider) if provider != "Auto-Select" else None
                    
                    response_data = asyncio.run(
                        self.ai_system.generate_response(
                            st.session_state.conversation_context,
                            user_message,
                            preferred_provider=selected_provider
                        )
                    )
                    
                    # Add AI response to history
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response_data["response"],
                        "metadata": {
                            "provider": response_data["provider_used"],
                            "response_time": response_data["response_time"],
                            "integrity_score": response_data["integrity_score"],
                            "gamification_points": response_data["gamification_points"]
                        }
                    })
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error generating response: {e}")
    
    def _create_benchmark_interface(self):
        """Create benchmark comparison interface"""
        
        st.header("📊 AI Model Benchmark Comparison")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Benchmark Configuration")
            
            # Test scenarios selection
            test_scenarios = st.multiselect(
                "Select test scenarios",
                [s.title for s in self.scenarios.get_all_scenarios()],
                default=[s.title for s in self.scenarios.get_all_scenarios()[:2]]
            )
            
            # Character for testing
            test_character = st.selectbox(
                "Character for testing",
                ["Catalina", "Alexis", "Dr. Mentor", "Inspector Rodriguez"]
            )
            
            character_map = {
                "Catalina": CharacterPersonality.CATALINA,
                "Alexis": CharacterPersonality.ALEXIS,
                "Dr. Mentor": CharacterPersonality.MENTOR, 
                "Inspector Rodriguez": CharacterPersonality.AUDITOR
            }
            
            if st.button("🚀 Run Benchmark"):
                if test_scenarios:
                    with st.spinner("Running benchmark tests..."):
                        # Convert scenario titles to descriptions
                        scenario_descriptions = []
                        for title in test_scenarios:
                            scenario = next(s for s in self.scenarios.get_all_scenarios() if s.title == title)
                            scenario_descriptions.append(scenario.description)
                        
                        try:
                            results = asyncio.run(
                                self.ai_system.run_benchmark_comparison(
                                    scenario_descriptions,
                                    character_map[test_character]
                                )
                            )
                            
                            st.session_state.benchmark_results = results
                            st.success("✅ Benchmark completed!")
                            
                        except Exception as e:
                            st.error(f"Benchmark failed: {e}")
        
        with col2:
            # Display benchmark results
            if st.session_state.get('benchmark_results'):
                self._display_benchmark_results(st.session_state.benchmark_results)
    
    def _display_benchmark_results(self, results: List[BenchmarkResult]):
        """Display benchmark results with charts"""
        
        st.subheader("📈 Benchmark Results")
        
        # Convert results to DataFrame for easier plotting
        data = []
        for result in results:
            data.append({
                'Provider': result.provider.value,
                'Response Time (s)': result.response_time,
                'Quality Score': result.quality_score,
                'Cost ($)': result.cost,
                'Character Consistency': result.character_consistency,
                'Integrity Relevance': result.integrity_relevance
            })
        
        df = pd.DataFrame(data)
        
        if not df.empty:
            # Performance comparison chart
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=['Response Time', 'Quality Score', 'Cost Analysis', 'Overall Performance'],
                specs=[[{"secondary_y": False}, {"secondary_y": False}],
                       [{"secondary_y": False}, {"secondary_y": False}]]
            )
            
            # Response Time
            fig.add_trace(
                go.Bar(x=df['Provider'], y=df['Response Time (s)'], name='Response Time'),
                row=1, col=1
            )
            
            # Quality Score  
            fig.add_trace(
                go.Bar(x=df['Provider'], y=df['Quality Score'], name='Quality Score'),
                row=1, col=2
            )
            
            # Cost Analysis
            fig.add_trace(
                go.Bar(x=df['Provider'], y=df['Cost ($)'], name='Cost'),
                row=2, col=1
            )
            
            # Overall Performance (radar-like)
            fig.add_trace(
                go.Scatter(
                    x=df['Provider'], 
                    y=df['Character Consistency'], 
                    mode='markers+lines',
                    name='Character Consistency',
                    marker=dict(size=10)
                ),
                row=2, col=2
            )
            
            fig.add_trace(
                go.Scatter(
                    x=df['Provider'],
                    y=df['Integrity Relevance'], 
                    mode='markers+lines',
                    name='Integrity Relevance',
                    marker=dict(size=10)
                ),
                row=2, col=2
            )
            
            fig.update_layout(height=800, title_text="AI Model Performance Comparison")
            st.plotly_chart(fig, use_container_width=True)
            
            # Detailed results table
            st.subheader("📋 Detailed Results")
            st.dataframe(df, use_container_width=True)
            
            # Recommendations
            st.subheader("🎯 Recommendations")
            
            # Find best performer in each category
            fastest = df.loc[df['Response Time (s)'].idxmin(), 'Provider']
            highest_quality = df.loc[df['Quality Score'].idxmax(), 'Provider'] 
            most_cost_effective = df.loc[df['Cost ($)'].idxmin(), 'Provider']
            best_consistency = df.loc[df['Character Consistency'].idxmax(), 'Provider']
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown(f"""
                **Performance Leaders:**
                - 🚀 **Fastest Response:** {fastest}
                - 🏆 **Highest Quality:** {highest_quality}
                - 💰 **Most Cost-Effective:** {most_cost_effective}
                - 🎭 **Best Character Consistency:** {best_consistency}
                """)
            
            with col_b:
                st.markdown("""
                **Recommended Usage:**
                - **Real-time Chat:** Use fastest provider
                - **Training Sessions:** Use highest quality 
                - **Large Scale:** Use most cost-effective
                - **Character Play:** Use best consistency
                """)
    
    def _create_scenario_testing(self):
        """Create scenario testing interface"""
        
        st.header("🧪 Scenario Testing Laboratory") 
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Test Configuration")
            
            # Scenario selection
            all_scenarios = self.scenarios.get_all_scenarios()
            selected_scenario = st.selectbox(
                "Select Scenario",
                all_scenarios,
                format_func=lambda x: f"{x.title} ({x.difficulty.value})"
            )
            
            # Multiple character testing
            test_characters = st.multiselect(
                "Test with Characters",
                ["Catalina", "Alexis", "Dr. Mentor", "Inspector Rodriguez"],
                default=["Catalina", "Alexis"]
            )
            
            # Test message
            test_message = st.text_area(
                "Test Message",
                "Creo que en esta situación lo más importante es seguir los procedimientos establecidos y reportar cualquier irregularidad."
            )
        
        with col2:
            st.subheader("Scenario Details")
            
            if selected_scenario:
                st.markdown(f"**{selected_scenario.title}**")
                st.write(selected_scenario.description)
                
                with st.expander("Full Context"):
                    st.write(selected_scenario.context)
                    st.write("---")
                    st.write(selected_scenario.dilemma)
        
        if st.button("🔬 Run Character Tests"):
            if test_characters and test_message:
                
                character_map = {
                    "Catalina": CharacterPersonality.CATALINA,
                    "Alexis": CharacterPersonality.ALEXIS,
                    "Dr. Mentor": CharacterPersonality.MENTOR,
                    "Inspector Rodriguez": CharacterPersonality.AUDITOR
                }
                
                st.markdown("---")
                st.subheader("🎭 Character Responses")
                
                for character_name in test_characters:
                    character = character_map[character_name]
                    
                    with st.expander(f"💬 {character_name} Response", expanded=True):
                        
                        context = ConversationContext(
                            user_id="test_user",
                            session_id="test_session",
                            character=character,
                            scenario=selected_scenario.description
                        )
                        
                        try:
                            with st.spinner(f"Generating {character_name}'s response..."):
                                response_data = asyncio.run(
                                    self.ai_system.generate_response(
                                        context,
                                        test_message
                                    )
                                )
                            
                            st.write(response_data["response"])
                            
                            # Response metadata
                            col_meta1, col_meta2, col_meta3 = st.columns(3)
                            with col_meta1:
                                st.metric("Provider", response_data["provider_used"])
                            with col_meta2: 
                                st.metric("Response Time", f"{response_data['response_time']:.2f}s")
                            with col_meta3:
                                st.metric("Integrity Score", f"{response_data['integrity_score']}/100")
                            
                        except Exception as e:
                            st.error(f"Error generating {character_name}'s response: {e}")

def main():
    """Main function to run the Streamlit app"""
    
    # Initialize demo system
    demo = BenchmarkDemo()
    
    # Create Streamlit interface
    demo.create_streamlit_interface()

if __name__ == "__main__":
    main()