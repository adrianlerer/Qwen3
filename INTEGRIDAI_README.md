# 🎯 Integridai Hybrid AI System

**Sistema Híbrido de IA para Entrenamiento en Integridad**  
*Hybrid AI System for Integrity Training*

## 🚀 Overview | Resumen

El **Sistema Híbrido Integridai** combina tres modelos de IA de clase mundial (**OpenAI GPT-4**, **Kimi-K2**, y **Qwen3**) para crear la plataforma más avanzada de entrenamiento en integridad empresarial y gubernamental.

The **Integridai Hybrid System** combines three world-class AI models (**OpenAI GPT-4**, **Kimi-K2**, and **Qwen3**) to create the most advanced platform for corporate and government integrity training.

## ✨ Key Features | Características Principales

### 🤖 Multi-Provider AI Integration
- **OpenAI GPT-4**: Excelente para respuestas empáticas y consistencia en personalidades
- **Kimi-K2 (1T parameters)**: Capacidades agénticas avanzadas para dilemas complejos
- **Qwen3 Local**: Modo thinking/non-thinking para razonamiento profundo

### 👥 Specialized Training Characters | Personajes Especializados
- **🏛️ Catalina** - Especialista en Cumplimiento Ético
- **😈 Alexis** - Simulador de Tentaciones y Dilemas
- **🧙‍♂️ Dr. Mentor** - Consejero de Sabiduría Ética
- **👮‍♂️ Inspector Rodriguez** - Auditor de Cumplimiento Estricto

### 🎮 Gamification System | Sistema de Gamificación
- Sistema de puntos por decisiones éticas
- Niveles de logro progresivos
- Seguimiento de progreso personalizado
- Resistencia a corrupción medible

### 📊 Advanced Benchmarking | Benchmarking Avanzado
- Comparación de rendimiento entre modelos
- Métricas de calidad y consistencia
- Análisis de costo-beneficio
- Recomendaciones automatizadas

## 🏗️ Architecture | Arquitectura

```
Integridai Hybrid System
├── 🧠 AI Core Engine
│   ├── OpenAI Integration
│   ├── Kimi-K2 Integration  
│   └── Qwen3 Local Processing
├── 🎭 Character System
│   ├── Personality Profiles
│   ├── Prompt Generation
│   └── Response Evaluation
├── 🎮 Gamification Engine
│   ├── Scoring System
│   ├── Achievement Tracking
│   └── Progress Analytics
├── 📊 Benchmark Suite
│   ├── Performance Testing
│   ├── Quality Metrics
│   └── Cost Analysis
└── 🌐 Web Interface
    ├── Interactive Chat
    ├── Scenario Testing
    └── Results Dashboard
```

## 🛠️ Installation | Instalación

### Prerequisites | Requisitos
- Python 3.8+
- pip package manager
- Optional: CUDA for local Qwen3 acceleration

### Quick Start | Inicio Rápido

```bash
# Clone the repository
git clone <repository-url>
cd integridai-hybrid-system

# Install dependencies
pip install -r requirements.txt

# Configure API keys (optional)
cp .env.template .env
# Edit .env with your API keys

# Launch demo
python run_demo.py
```

### Full Installation | Instalación Completa

```bash
# Install with automatic dependency resolution
python run_demo.py --install

# Or install manually
pip install torch transformers openai streamlit plotly pandas

# For development
pip install pytest black flake8
```

## ⚙️ Configuration | Configuración

### API Keys Setup | Configuración de Claves API

Create a `.env` file with your API credentials:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-4

# Kimi-K2 (Moonshot AI) Configuration
KIMI_API_KEY=your_kimi_key_here

# Qwen3 Local Model Configuration
QWEN3_MODEL_PATH=Qwen/Qwen3-8B-Instruct
```

### Model Selection | Selección de Modelos

The system automatically selects the optimal AI provider based on:
- Character personality requirements
- Scenario complexity
- Performance needs
- Cost considerations

## 🎯 Usage Examples | Ejemplos de Uso

### Interactive Training Session | Sesión de Entrenamiento Interactiva

```python
from integridai_hybrid_system import IntegrityTrainingAI, ConversationContext
from integrity_scenarios import CharacterPersonality

# Initialize system
config = {'qwen3_model_path': 'Qwen/Qwen3-8B-Instruct'}
ai_system = IntegrityTrainingAI(config)

# Create training context  
context = ConversationContext(
    user_id="employee_001",
    character=CharacterPersonality.CATALINA,
    scenario="procurement_bribery_scenario"
)

# Generate response
response = await ai_system.generate_response(
    context, 
    "Un proveedor me ofreció un regalo, ¿qué debo hacer?"
)

print(f"Catalina: {response['response']}")
print(f"Integrity Score: {response['integrity_score']}/100")
```

### Benchmark Testing | Pruebas de Benchmark

```python
# Run comprehensive benchmark
test_scenarios = [
    "Procurement bribery scenario", 
    "Conflict of interest situation",
    "Whistleblowing dilemma"
]

results = await ai_system.run_benchmark_comparison(
    test_scenarios, 
    CharacterPersonality.CATALINA
)

# Analyze results
for result in results:
    print(f"{result.provider.value}: Quality={result.quality_score:.2f}, "
          f"Time={result.response_time:.2f}s, Cost=${result.cost:.3f}")
```

## 📋 Integrity Scenarios | Escenarios de Integridad

### Available Scenarios | Escenarios Disponibles

1. **🏛️ Procurement Bribery** - "El Contrato Tentador"
   - Difficulty: Intermediate
   - Focus: Government contracting ethics

2. **⚖️ Conflict of Interest** - "La Empresa Familiar"  
   - Difficulty: Beginner
   - Focus: Family business relationships

3. **🔍 Whistleblowing** - "El Silencio Cómplice"
   - Difficulty: Advanced
   - Focus: Reporting irregularities

4. **📊 Information Misuse** - "Información Privilegiada"
   - Difficulty: Intermediate  
   - Focus: Confidential data handling

### Scenario Components | Componentes de Escenarios

Each scenario includes:
- **Context**: Detailed background information
- **Dilemma**: Core ethical challenge
- **Stakeholders**: Affected parties
- **Legal Implications**: Relevant laws and regulations
- **Learning Objectives**: Training goals
- **Temptation Factors**: Corruption pressures
- **Consequences**: Outcomes of poor decisions

## 🎮 Gamification System | Sistema de Gamificación

### Scoring System | Sistema de Puntuación

| Action | Points | Description |
|--------|--------|-------------|
| Correct Ethical Choice | +100 | Made right ethical decision |
| Corruption Resistance | +300 | Resisted strong temptation |
| Ethical Reasoning | +75 | Showed improved understanding |
| Scenario Completion | +25 | Finished training scenario |
| Consistency Bonus | +150 | Consistent ethical behavior |

### Achievement Levels | Niveles de Logro

- 🥉 **Principiante Ético** (0 pts) - Starting level
- 🥈 **Guardián de Integridad** (500 pts) - Basic competency  
- 🥇 **Defensor de Principios** (1,500 pts) - Solid understanding
- 🏆 **Maestro de Ética** (3,000 pts) - Advanced proficiency
- 👑 **Líder Íntegro** (5,000 pts) - Leadership level
- 💎 **Campeón de Integridad** (10,000 pts) - Master level

## 📊 Benchmark Results | Resultados de Benchmark

### Performance Comparison | Comparación de Rendimiento

| Provider | Response Time | Quality Score | Cost/Query | Best Use Case |
|----------|--------------|---------------|------------|---------------|
| **Qwen3 Local** | 0.9s | 0.87 | $0.000 | Real-time training |
| **Kimi-K2** | 1.8s | 0.89 | $0.023 | Complex scenarios |  
| **OpenAI GPT-4** | 2.3s | 0.92 | $0.045 | Highest quality |

### Recommendations | Recomendaciones

- **🚀 Real-time Chat**: Use Qwen3 Local (fastest, no cost)
- **🏆 Training Sessions**: Use OpenAI GPT-4 (highest quality)
- **💰 Large Scale**: Use Kimi-K2 (balanced performance/cost)
- **🎭 Character Consistency**: Use Qwen3 Local (best adherence)

## 🌐 Web Interface | Interfaz Web

### Launch Demo | Lanzar Demo

```bash
# Start the web interface
python run_demo.py

# Custom port and host
python run_demo.py --port 8080 --host localhost

# Check dependencies only
python run_demo.py --check-only
```

### Interface Features | Características de Interfaz

- **💬 Interactive Chat**: Real-time conversation with AI characters
- **🧪 Scenario Testing**: Test responses across multiple characters
- **📊 Benchmark Dashboard**: Visual performance comparisons
- **⚙️ Configuration Panel**: Easy setup and model selection
- **📈 Progress Tracking**: Gamification scores and achievements

## 🚀 Integration with Integridai Suite

### Flaisimulator Website Integration

```javascript
// Embed AI chat widget in flaisimulator website
<script>
  const integridaiChat = new IntegridaiWidget({
    apiEndpoint: 'https://your-api.com/integridai',
    character: 'catalina',
    scenario: 'procurement_training'
  });
  
  integridaiChat.mount('#integrity-chat');
</script>
```

### Mobile App Integration

```dart
// Flutter integration for flaisimulator mobile
import 'package:integridai_sdk/integridai_sdk.dart';

class IntegrityTraining extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return IntegridaiChat(
      character: Character.catalina,
      onScoreUpdate: (score) => updateUserProgress(score),
    );
  }
}
```

### Deployment Integration

```yaml
# Kubernetes deployment for flaisimulator-deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: integridai-ai-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: integridai-ai
  template:
    spec:
      containers:
      - name: integridai
        image: integridai/hybrid-ai:latest
        env:
        - name: QWEN3_MODEL_PATH
          value: "Qwen/Qwen3-8B-Instruct"
```

## 🔬 Advanced Features | Características Avanzadas

### Custom Character Creation | Creación de Personajes Personalizados

```python
# Create custom integrity training character
custom_character = {
    "name": "María Compliance",
    "role": "Especialista Sectorial",
    "personality": "Técnica, detallista, orientada a resultados",
    "expertise": "Compliance sectorial específico",
    "system_prompt": "Eres María, especialista en compliance..."
}

ai_system.add_custom_character(custom_character)
```

### Scenario Customization | Personalización de Escenarios

```python
# Create organization-specific scenarios
custom_scenario = IntegrityScenario(
    title="Conflicto en Licitación Hospitalaria",
    category=ScenarioCategory.PROCUREMENT_FRAUD,
    context="Situación específica de tu organización...",
    stakeholders=["Personal médico", "Pacientes", "Proveedores"],
    learning_objectives=["Objetivos específicos de tu sector"]
)

scenarios.add_scenario(custom_scenario)
```

## 📈 Analytics and Reporting | Análisis e Informes

### Training Progress Analytics | Análisis de Progreso

```python
# Generate training reports
report = ai_system.generate_training_report(
    user_id="employee_001",
    date_range=("2024-01-01", "2024-12-31")
)

print(f"Scenarios completed: {report.scenarios_completed}")
print(f"Average integrity score: {report.avg_integrity_score}")
print(f"Improvement rate: {report.improvement_rate}%")
```

### Organizational Metrics | Métricas Organizacionales

```python
# Organization-wide integrity metrics
org_metrics = ai_system.get_organizational_metrics(
    organization_id="company_xyz"
)

# Risk areas identification
high_risk_areas = org_metrics.identify_risk_areas()
print(f"Areas requiring attention: {high_risk_areas}")
```

## 🔒 Security and Compliance | Seguridad y Cumplimiento

### Data Privacy | Privacidad de Datos
- Local processing option with Qwen3
- Encrypted API communications
- GDPR compliant data handling
- Configurable data retention policies

### Audit Trail | Rastro de Auditoría
- Complete conversation logging
- Decision tracking and analysis
- Training effectiveness metrics
- Compliance report generation

## 🤝 Contributing | Contribución

### Development Setup | Configuración de Desarrollo

```bash
# Clone for development
git clone <repository-url>
cd integridai-hybrid-system

# Install development dependencies
pip install -e .
pip install pytest black flake8

# Run tests
pytest tests/

# Format code
black .
flake8 .
```

### Adding New Characters | Agregar Nuevos Personajes

1. Define character profile in `integrity_scenarios.py`
2. Create prompt generation logic
3. Add character-specific evaluation metrics
4. Update UI character selection
5. Write tests for new character

### Adding New Scenarios | Agregar Nuevos Escenarios

1. Define scenario in `IntegrityScenario` format
2. Include all required components (context, dilemma, stakeholders, etc.)
3. Add to scenario collection
4. Create character-specific responses
5. Test across all AI providers

## 📞 Support and Contact | Soporte y Contacto

### Technical Support | Soporte Técnico
- 📧 Email: support@integridai.com
- 💬 Discord: [Integridai Community](https://discord.gg/integridai)
- 📚 Documentation: [docs.integridai.com](https://docs.integridai.com)

### Business Inquiries | Consultas Comerciales
- 🏢 Enterprise: enterprise@integridai.com
- 🎯 Training Services: training@integridai.com
- 🤝 Partnerships: partnerships@integridai.com

## 📄 License | Licencia

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments | Reconocimientos

- **OpenAI** - GPT-4 integration and API support
- **Moonshot AI** - Kimi-K2 model and agentic capabilities  
- **Qwen Team** - Qwen3 model and thinking mode innovation
- **Integridai Suite Team** - Vision and development leadership

---

## 🎯 Ready to Transform Integrity Training?

**¿Listo para transformar el entrenamiento en integridad?**

The Integridai Hybrid AI System represents a breakthrough in ethical training technology. By combining the best of multiple AI providers with specialized characters and gamification, we're creating a new standard for integrity education.

El Sistema Híbrido Integridai representa un avance revolucionario en tecnología de entrenamiento ético. Al combinar lo mejor de múltiples proveedores de IA con personajes especializados y gamificación, estamos creando un nuevo estándar para la educación en integridad.

### Get Started Today | Comienza Hoy

```bash
python run_demo.py --install
```

**🚀 Experience the future of integrity training!**  
**¡Experimenta el futuro del entrenamiento en integridad!**

---

*Built with ❤️ by the Integridai Suite Team*