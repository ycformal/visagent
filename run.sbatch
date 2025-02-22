#!/bin/bash
#SBATCH -J visagent             # Job name
#SBATCH -N 1                            # Number of nodes
#SBATCH -N1 --gres=gpu:1 -C H100            # Request 1 GPU
#SBATCH --mem=200G                      # Increase memory
#SBATCH -t 60                          # Duration of the job
#SBATCH -o visprog_nlvr_baseline2_mistral-%j.out                # Combined output and error messages file

cd $SLURM_SUBMIT_DIR                    # Correctly change to the submit directory

module load anaconda3
conda activate py39

srun python main_nlvr_baseline2.py --model=mistral