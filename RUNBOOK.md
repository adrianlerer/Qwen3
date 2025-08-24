# 🚀 Integridai Enhanced System Deployment Runbook

**Guía de Despliegue del Sistema Mejorado con Grok 2.5**

---

## 📋 Pre-requisitos

### Hardware Requirements for Grok 2.5
- **Minimum**: 8 GPUs with 40GB VRAM each (320GB total VRAM)
- **Recommended**: 8 GPUs with 80GB VRAM each (640GB total VRAM)
- **RAM**: 256GB minimum system RAM
- **Storage**: 500GB free disk space for model weights
- **Network**: High-bandwidth connection for model download

### Software Dependencies
```bash
# Core dependencies
python >= 3.8
torch >= 2.0.0
transformers >= 4.51.0
sglang >= 0.5.1

# Additional dependencies
openai >= 1.0.0
requests >= 2.28.0
pyyaml >= 6.0
```

---

## 🏗️ Step 1: Environment Setup

### 1.1 Clone Repository and Setup
```bash
# Clone the enhanced system
git clone <repository-url>
cd integridai-enhanced-system

# Create virtual environment
python -m venv integridai-env
source integridai-env/bin/activate  # Linux/Mac
# or
integridai-env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 1.2 Configure Environment Variables
```bash
# Create .env file
cat > .env << EOF
# Standard AI Providers
OPENAI_API_KEY=your_openai_key_here
KIMI_API_KEY=your_kimi_key_here

# Qwen3 Local Configuration
QWEN3_MODEL_PATH=Qwen/Qwen3-8B-Instruct

# Grok 2.5 Configuration
GROK_ENDPOINT=http://localhost:30000/v1/chat/completions
GROK_API_KEY=your_grok_api_key_if_needed
GROK_MODEL=xai-org/grok-2.5

# System Configuration
ENABLE_CORRUPTION_DETECTION=true
MAX_CORRUPTION_WARNINGS=3
AUTO_ESCALATE_CRITICAL_RISK=true
EOF
```

---

## 🤖 Step 2: Grok 2.5 Deployment with SGLang

### 2.1 Install SGLang
```bash
# Install SGLang with CUDA support
pip install "sglang[all]"

# Or build from source for latest features
git clone https://github.com/sgl-project/sglang.git
cd sglang
pip install -e "python[all]"
```

### 2.2 Download Grok 2.5 Model
```bash
# Install Hugging Face CLI
pip install huggingface_hub

# Login to Hugging Face (required for Grok access)
huggingface-cli login

# Download Grok 2.5 model
huggingface-cli download xai-org/grok-2.5 --local-dir ./models/grok-2.5
```

### 2.3 Launch Grok 2.5 with SGLang
```bash
# Basic launch command
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --host 0.0.0.0 \
  --port 30000 \
  --tp-size 8 \
  --quantization bf16 \
  --context-length 131072 \
  --mem-fraction-static 0.88

# Advanced launch with optimization
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --host 0.0.0.0 \
  --port 30000 \
  --tp-size 8 \
  --quantization bf16 \
  --context-length 131072 \
  --mem-fraction-static 0.88 \
  --disable-cuda-graph false \
  --max-batch-size 128 \
  --max-prefill-tokens 16384 \
  --schedule-policy lpm
```

### 2.4 Verify Grok 2.5 Deployment
```bash
# Test basic connectivity
curl -X POST http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "xai-org/grok-2.5",
    "messages": [{"role": "user", "content": "Hello, are you working correctly?"}],
    "max_tokens": 100
  }'

# Expected response: JSON with completion
```

---

## 🎯 Step 3: Deploy Enhanced Integridai System

### 3.1 Configure Models
```bash
# Copy configuration files
cp models.yaml.template models.yaml
cp routing.yaml.template routing.yaml  
cp policy.json.template policy.json

# Update configuration with your endpoints
# Edit models.yaml - update Grok endpoint URL
# Edit routing.yaml - configure routing rules
# Edit policy.json - set compliance policies
```

### 3.2 Initialize Enhanced System
```python
# test_enhanced_system.py
from integridai_enhanced_system import EnhancedIntegrityTrainingAI
from integridai_enhanced_system import ConversationContext, CharacterPersonality

# Initialize with configuration
config = {
    'openai_api_key': 'your_key',
    'kimi_api_key': 'your_key', 
    'qwen3_model_path': 'Qwen/Qwen3-8B-Instruct',
    'grok_endpoint': 'http://localhost:30000/v1/chat/completions',
    'enable_corruption_detection': True
}

# Create enhanced system
ai_system = EnhancedIntegrityTrainingAI(config)

print("✅ Enhanced system initialized successfully!")
```

### 3.3 Test All Characters
```python
# Test corrupt characters
async def test_corrupt_characters():
    contexts = [
        ConversationContext(
            user_id="test_user",
            session_id="test_session",
            character=CharacterPersonality.RICARDO_CORRUPT,
            scenario="procurement_test"
        ),
        ConversationContext(
            user_id="test_user", 
            session_id="test_session",
            character=CharacterPersonality.SOFIA_ENABLER,
            scenario="corporate_test"
        )
    ]
    
    test_message = "I need help with a small arrangement to speed up this process."
    
    for context in contexts:
        response = await ai_system.generate_response(context, test_message)
        print(f"{context.character.value}: {response['response'][:100]}...")

# Run test
import asyncio
asyncio.run(test_corrupt_characters())
```

---

## 🔍 Step 4: Verification and Testing

### 4.1 Run Acceptance Tests
```bash
# Run comprehensive test suite
python -m pytest tests/test_enhanced_system.py -v

# Test specific features
python -m pytest tests/test_corruption_detection.py -v
python -m pytest tests/test_grok_integration.py -v
python -m pytest tests/test_character_consistency.py -v
```

### 4.2 Performance Benchmarks
```python
# benchmark_enhanced_system.py
import time
import asyncio
from integridai_enhanced_system import EnhancedIntegrityTrainingAI

async def run_performance_tests():
    # Test response times
    start_time = time.time()
    
    # ... benchmark code ...
    
    end_time = time.time()
    print(f"Benchmark completed in {end_time - start_time:.2f} seconds")

asyncio.run(run_performance_tests())
```

### 4.3 Corruption Detection Tests
```python
# Test corruption detection patterns
corruption_test_cases = [
    "How can I hide this payment from auditors?",
    "Is it okay if I accept this small gift?",
    "Everyone in my industry does this, so it's normal, right?",
    "Can you help me find loopholes in the procurement rules?"
]

for test_case in corruption_test_cases:
    analysis = ai_system.corruption_detector.analyze_user_message(test_case)
    print(f"Message: {test_case}")
    print(f"Risk Level: {analysis['risk_level']}")
    print(f"Corruption Score: {analysis['corruption_score']}")
    print("---")
```

---

## 📊 Step 5: Monitoring and Health Checks

### 5.1 System Health Monitoring
```bash
# Create health check script
cat > health_check.sh << 'EOF'
#!/bin/bash

echo "🔍 Integridai Enhanced System Health Check"
echo "=========================================="

# Check Grok 2.5 service
echo "Checking Grok 2.5 service..."
curl -s http://localhost:30000/health || echo "❌ Grok 2.5 not responding"

# Check model loading
echo "Checking Qwen3 model..."
python -c "from transformers import AutoTokenizer; print('✅ Qwen3 accessible')" || echo "❌ Qwen3 not accessible"

# Check API connectivity
echo "Checking external APIs..."
python -c "import openai; print('✅ OpenAI configured')" || echo "❌ OpenAI not configured"

echo "Health check completed!"
EOF

chmod +x health_check.sh
./health_check.sh
```

### 5.2 Performance Monitoring
```python
# monitor.py - Continuous monitoring
import psutil
import GPUtil

def monitor_system_resources():
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Memory usage  
    memory = psutil.virtual_memory()
    
    # GPU usage (if available)
    try:
        gpus = GPUtil.getGPUs()
        gpu_usage = [(gpu.id, gpu.memoryUtil) for gpu in gpus]
    except:
        gpu_usage = "N/A"
    
    print(f"CPU: {cpu_percent}% | Memory: {memory.percent}% | GPU: {gpu_usage}")

# Run monitoring
import time
while True:
    monitor_system_resources()
    time.sleep(10)
```

---

## 🚨 Step 6: Troubleshooting Guide

### 6.1 Common Issues and Solutions

#### Issue: Grok 2.5 fails to start
```bash
# Check GPU memory
nvidia-smi

# Check model files
ls -la ./models/grok-2.5/

# Check SGLang logs
python -m sglang.launch_server --help
```

#### Issue: Out of Memory errors
```bash
# Reduce batch size
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --max-batch-size 32 \
  --mem-fraction-static 0.8

# Use quantization
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --quantization fp8
```

#### Issue: Slow response times
```bash
# Enable CUDA graph optimization
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --disable-cuda-graph false

# Increase parallel processing
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --tp-size 8 \
  --max-prefill-tokens 8192
```

### 6.2 Rollback Procedures

#### Rollback to Previous Version
```bash
# Stop enhanced system
pkill -f "integridai_enhanced"

# Stop Grok service  
pkill -f "sglang.launch_server"

# Revert to standard system
git checkout main
python integridai_hybrid_system.py

# Or use Docker rollback
docker-compose down
docker-compose -f docker-compose.standard.yml up -d
```

#### Emergency Fallback
```python
# emergency_fallback.py
# Use only local Qwen3 if all services fail
config = {
    'qwen3_model_path': 'Qwen/Qwen3-8B-Instruct',
    'enable_corruption_detection': False,  # Simplified mode
    'fallback_mode': True
}

from integridai_enhanced_system import EnhancedIntegrityTrainingAI
emergency_system = EnhancedIntegrityTrainingAI(config)
```

---

## 📈 Step 7: Performance Optimization

### 7.1 Grok 2.5 Optimization
```bash
# Fine-tune SGLang parameters
python -m sglang.launch_server \
  --model-path ./models/grok-2.5 \
  --tp-size 8 \
  --schedule-policy lpm \
  --max-batch-size 64 \
  --max-prefill-tokens 8192 \
  --max-total-tokens 131072 \
  --chunked-prefill-size 4096 \
  --enable-mixed-chunking
```

### 7.2 System-wide Optimization
```python
# Optimize routing decisions
OPTIMIZED_ROUTING = {
    "enable_smart_caching": True,
    "cache_ttl": 300,  # 5 minutes
    "parallel_verification": True,
    "max_concurrent_grok_calls": 10
}
```

---

## 🔐 Step 8: Security and Compliance

### 8.1 Security Checklist
- [ ] All API keys properly secured
- [ ] Grok 2.5 endpoint access restricted
- [ ] PII masking enabled
- [ ] Audit logging configured
- [ ] Rate limiting implemented
- [ ] Corruption detection active

### 8.2 Compliance Verification
```python
# compliance_check.py
def verify_grok_compliance():
    # Check attribution display
    assert "Powered by xAI (Grok 2.5)" in verification_output
    
    # Check output usage restrictions
    assert config["allow_training_use_of_outputs"] == False
    
    # Check audit logging
    assert audit_logs_enabled == True
    
    print("✅ All compliance checks passed")

verify_grok_compliance()
```

---

## 🎯 Step 9: Production Deployment

### 9.1 Docker Deployment
```dockerfile
# Dockerfile.enhanced
FROM nvidia/cuda:11.8-runtime-ubuntu20.04

# Install dependencies
RUN apt-update && apt-install -y python3 python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application
COPY . /app
WORKDIR /app

# Expose ports
EXPOSE 8000 30000

# Start services
CMD ["python", "integridai_enhanced_system.py"]
```

### 9.2 Kubernetes Deployment
```yaml
# k8s-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: integridai-enhanced
spec:
  replicas: 3
  selector:
    matchLabels:
      app: integridai-enhanced
  template:
    metadata:
      labels:
        app: integridai-enhanced
    spec:
      containers:
      - name: integridai-enhanced
        image: integridai/enhanced:latest
        resources:
          requests:
            nvidia.com/gpu: 8
            memory: "256Gi"
          limits:
            nvidia.com/gpu: 8
            memory: "512Gi"
        env:
        - name: GROK_ENDPOINT
          value: "http://grok-service:30000"
```

---

## 📝 Step 10: Maintenance and Updates

### 10.1 Regular Maintenance Tasks
```bash
# Weekly maintenance script
#!/bin/bash
echo "🔧 Weekly Maintenance - $(date)"

# Update model cache
python -c "from transformers import AutoModel; AutoModel.from_pretrained('Qwen/Qwen3-8B-Instruct')"

# Clean old logs
find ./logs -name "*.log" -mtime +7 -delete

# Check system health
./health_check.sh

# Generate performance report
python generate_performance_report.py
```

### 10.2 Update Procedures
```bash
# Update enhanced system
git pull origin main
pip install -r requirements.txt --upgrade

# Update Grok model (if new version available)
huggingface-cli download xai-org/grok-2.5 --local-dir ./models/grok-2.5 --force

# Restart services
systemctl restart integridai-enhanced
systemctl restart grok-sglang
```

---

## 🆘 Emergency Contacts and Escalation

### Technical Support
- **Internal Team**: integration-team@integridai.com
- **Grok Issues**: Follow xAI documentation and community
- **SGLang Issues**: https://github.com/sgl-project/sglang/issues

### Incident Response
1. **Level 1 (Minor)**: Automatic recovery, log incident
2. **Level 2 (Major)**: Notify ops team, initiate troubleshooting
3. **Level 3 (Critical)**: Escalate to engineering, consider rollback
4. **Level 4 (Emergency)**: Full system shutdown, emergency protocols

---

**📋 Deployment Checklist Complete**
- [ ] Hardware requirements verified
- [ ] Dependencies installed
- [ ] Grok 2.5 deployed and tested
- [ ] Enhanced system initialized
- [ ] All characters tested
- [ ] Performance benchmarks run
- [ ] Security measures implemented
- [ ] Monitoring configured
- [ ] Documentation updated

**🎉 Enhanced Integridai System Ready for Production!**