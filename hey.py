import os
import shutil

def replicate(num_copies):
    script_dir = os.path.dirname(__file__)
    script_name = os.path.basename(__file__)
    for i in range(num_copies):
        copy_name = f"{script_name}_{i+1}.py"
        copy_path = os.path.join(script_dir, copy_name)
        shutil.copy(__file__, copy_path)
        print(f"Created copy: {copy_path}")

if __name__ == "__main__":
    c=0

    while (1):
       c+=1
       num_copies=c
       replicate(num_copies)