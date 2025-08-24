#!/usr/bin/env python3
"""
Integridai Demo Launcher
Lanzador de Demo para Integridai

This script launches the Integridai Hybrid AI System demo with proper configuration.
Este script lanza el demo del Sistema Híbrido de IA Integridai con configuración adecuada.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    
    required_packages = [
        'streamlit', 'torch', 'transformers', 'openai', 
        'plotly', 'pandas', 'matplotlib', 'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("📦 Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def setup_environment():
    """Setup environment variables and configuration"""
    
    # Create .env file template if it doesn't exist
    env_file = Path(".env")
    if not env_file.exists():
        env_template = """# Integridai AI System Configuration
# Configure your API keys here

# OpenAI Configuration
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-4

# Kimi-K2 (Moonshot AI) Configuration  
KIMI_API_KEY=your_kimi_key_here

# Qwen3 Local Model Configuration
QWEN3_MODEL_PATH=Qwen/Qwen3-8B-Instruct

# Demo Configuration
DEMO_PORT=8501
DEMO_HOST=0.0.0.0
"""
        
        with open(env_file, 'w') as f:
            f.write(env_template)
        
        print("📝 Created .env template file")
        print("🔑 Please configure your API keys in the .env file")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ Environment variables loaded")
    except ImportError:
        print("⚠️  python-dotenv not installed, using system environment")

def launch_demo(port=8501, host="0.0.0.0"):
    """Launch the Streamlit demo"""
    
    print(f"🚀 Launching Integridai Demo at http://{host}:{port}")
    print("=" * 60)
    
    # Streamlit command
    cmd = [
        sys.executable, "-m", "streamlit", "run", 
        "benchmark_demo.py",
        "--server.port", str(port),
        "--server.address", host,
        "--browser.gatherUsageStats", "false",
        "--theme.base", "light"
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching demo: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user")
        return True
    
    return True

def main():
    """Main launcher function"""
    
    parser = argparse.ArgumentParser(description="Integridai Demo Launcher")
    parser.add_argument("--port", type=int, default=8501, help="Port for the demo server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host for the demo server")
    parser.add_argument("--check-only", action="store_true", help="Only check dependencies")
    parser.add_argument("--install", action="store_true", help="Install dependencies automatically")
    
    args = parser.parse_args()
    
    print("🎯 Integridai Hybrid AI System Demo Launcher")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        if args.install:
            print("📦 Installing dependencies...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
                print("✅ Dependencies installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error installing dependencies: {e}")
                return 1
        else:
            print("💡 Use --install flag to install automatically")
            return 1
    
    if args.check_only:
        print("✅ Dependency check completed")
        return 0
    
    # Setup environment
    setup_environment()
    
    # Launch demo
    success = launch_demo(args.port, args.host)
    
    if success:
        print("✅ Demo completed successfully")
        return 0
    else:
        print("❌ Demo failed to launch")
        return 1

if __name__ == "__main__":
    sys.exit(main())