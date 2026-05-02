import subprocess
import sys

def run_script(script_name):
    print(f"\n🚀 Running {script_name}...")
    subprocess.run([sys.executable, f"src/{script_name}"], check=True)
    print(f"✅ {script_name} completed!")

if __name__ == "__main__":
    print("🎵 Starting Spotify ML Project Pipeline...")
    
    run_script("data_exploration.py")
    run_script("preprocessing.py")
    run_script("visualization.py")
    run_script("model.py")
    run_script("evaluation.py")
    
    print("\n🎉 Pipeline completed successfully!")