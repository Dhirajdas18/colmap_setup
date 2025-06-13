import os
import subprocess

# Define input and output paths
dense_dir = "/home/dhiraj/skull-cameramoves-flash-no-background/dense"
fused_path = os.path.join(dense_dir, "fused.ply")
output_path = os.path.join(dense_dir, "mesh_poisson.ply")

# Check if fused.ply exists
if os.path.isfile(fused_path):
    print(f"✅ Found fused.ply in: {fused_path}")
    
    try:
        # Run Poisson meshing with enhancements
        subprocess.run([
            "colmap", "poisson_mesher",
            "--input_path", fused_path,
            "--output_path", output_path,
            "--PoissonMeshing.trim", "10"
        ], check=True)

        print(f"✅ Poisson mesh created at: {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error running COLMAP poisson_mesher:\n{e}")

else:
    print(f"❌ fused.ply not found at {fused_path}")
