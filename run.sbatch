#!/bin/bash
#SBATCH -J visagent             # Job name
#SBATCH -N 1                            # Number of nodes
#SBATCH -N1 --gres=gpu:1 -C H100            # Request 1 GPU
#SBATCH --mem=200G                      # Increase memory
#SBATCH -t 400                          # Duration of the job
#SBATCH -o visprog_baseline2_v2_mistral-%j.out                # Combined output and error messages file

cd $SLURM_SUBMIT_DIR                    # Correctly change to the submit directory

module load anaconda3
conda activate py39

srun python main_baseline2_v2.py --model=mistral