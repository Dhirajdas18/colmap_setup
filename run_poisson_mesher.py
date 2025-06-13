import os
import subprocess
import sys

def run_poisson_mesher(base_dir):
    fused_path = os.path.join(base_dir, "fused.ply")
    output_path = os.path.join(base_dir, "poisson_mesh.ply")  # ✅ must be a .ply file

    if os.path.isfile(fused_path):
        print(f"✅ Found fused.ply in: {base_dir}")
        try:
            subprocess.run([
                "colmap", "poisson_mesher",
                "--input_path", fused_path,
                "--output_path", output_path
            ], check=True)
            print(f"🎉 Poisson meshing completed: {output_path}")
        except subprocess.CalledProcessError as e:
            print("❌ Error running COLMAP poisson_mesher:", e)
    else:
        print(f"⚠️ fused.ply not found in: {base_dir}")
        sys.exit(1)

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    run_poisson_mesher(directory)
