import os
import subprocess
import time
import matplotlib.pyplot as plt

def create_slurm_script(script_filename="hpc_job.sh"):
    slurm_content = """#!/bin/bash
#SBATCH --job-name=hpc_simulation
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:05:00
#SBATCH --output=hpc_job_%j.log

echo "=== HPC Job Started on Nodes ==="
# Menjalankan simulasi Python pada klaster HPC
python3 -c "
import time
import numpy as np

start = time.time()
# Simulasi perhitungan Floating Point Operations (FLOPS)
a = np.random.rand(2000, 2000).astype(np.float64)
b = np.random.rand(2000, 2000).astype(np.float64)
c = np.dot(a, b)
elapsed = time.time() - start

# Matrix multiplication 2000x2000 ~ 1.6e10 floating point ops
flops = (2 * (2000**3)) / elapsed / 1e9 # GFLOPS
print(f'Calculation finished in {elapsed:.4f}s | Speed: {flops:.2f} GFLOPS')
"
echo "=== HPC Job Completed ==="
"""
    with open(script_filename, "w") as f:
        f.write(slurm_content)
    print(f"[1/3] Created Slurm Batch Script: {script_filename}")

def run_hpc_simulation():
    print("[2/3] Simulating Job Submission & Parallel Execution on HPC Cluster...")
    # Simulasi eksekusi beberapa variasi node/core untuk mengukur performa FLOPS
    nodes_config = [1, 2, 4, 8, 16]
    execution_times = []
    flops_performance = []

    for nodes in nodes_config:
        start_time = time.time()
        
        # Simulasi penurunan waktu komputasi saat jumlah node bertambah (Parallel Computing)
        simulated_calc_time = 5.0 / (nodes ** 0.75) 
        time.sleep(0.2) # Delay simulasi
        
        # Kalkulasi estimasi GFLOPS
        ops = 1.6e10
        gflops = (ops / simulated_calc_time) / 1e9
        
        execution_times.append(simulated_calc_time)
        flops_performance.append(gflops)
        print(f"  -> Nodes Allocated: {nodes:2d} | Exec Time: {simulated_calc_time:.3f}s | Performance: {gflops:.2f} GFLOPS")

    return nodes_config, execution_times, flops_performance

def visualize_hpc_results(nodes, exec_times, gflops):
    print("[3/3] Visualizing Results & Performance Scaling...")
    
    fig, ax1 = plt.subplots(figsize=(8, 5))

    color = 'tab:red'
    ax1.set_xlabel('Number of HPC Nodes')
    ax1.set_ylabel('Execution Time (seconds)', color=color)
    ax1.plot(nodes, exec_times, marker='o', color=color, linewidth=2, label='Execution Time')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Performance (GFLOPS)', color=color)
    ax2.plot(nodes, gflops, marker='s', color=color, linewidth=2, linestyle='--', label='GFLOPS')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('HPC Simulation Performance & Scaling Analysis')
    fig.tight_layout()
    
    output_img = "hpc_performance_result.png"
    plt.savefig(output_img)
    print(f"  -> Performance chart saved as '{output_img}'")
    plt.close()

if __name__ == "__main__":
    print("=== STARTING HPC WORKFLOW IMPLEMENTATION ===")
    
    # Step 1: Buat script Slurm batch
    create_slurm_script()
    
    # Step 2: Simulasikan pengiriman & eksekusi komputasi parallel pada HPC
    nodes, times, gflops = run_hpc_simulation()
    
    # Step 3: Olah & visualisasikan hasil kinerja FLOPS
    visualize_hpc_results(nodes, times, gflops)
    
    print("=== HPC WORKFLOW SUCCESSFULLY COMPLETED ===")