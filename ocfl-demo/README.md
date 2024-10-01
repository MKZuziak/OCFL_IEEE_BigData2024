# One Shot Clustered Federated Learning - Code Repository and Numerical Results
This repository contains all the numerical results in the paper '''One-Shot Clustering for Federated Learning''' by M.K.Zuziak, R.Pellungrini and S.Rinzivillo. The repository is split into two parts:
    -numerical results
    -ocfl-demo
The first contains all the data recorded during the experiments. The second allows for the re-creation of the numerical results.

## Numerical Results Section
Numerical results contain all the values recorded during the experiments. To re-create graphs and tables included in the paper, open '''IEEE_BigData2024.ipynb''' notebook and run all the cells. The notebook is split into sections and is well-annotated.
The numerical results are divided into three different categories: **experiments**, **elbow_experiments** and **temperature_experiments**. The first contains all the baseline experimentation with the algorithms included in the paper. The second contains all the experimentation on OCFL-KMeans with different numbers of clusters. The last contained experiments on the behaviour of the temperature function.

## OCFL-Demo Section
The repository allows for an easy re-creation of the experiments included in the paper using an external library also published as a part of the submission. It was configured using Poetry [https://python-poetry.org/](https://python-poetry.org/), and it requires it for proper execution.

To do so, navigate into ocfl-demo and run command:

```
poetry install
```

This will install all the dependencies in addition to a dedicated virtual environment. 
Enter the poetry shell executing the command:

```
poetry shell
```

and generate the splits using commands:

```
cd ocfl/demo/datasets
python datasets_generation.py
```

dataset generation can take several minutes depending, on the machine. Navigate to the main repository and launch scripts using commands:

```
cd ..
python baseline_experiments.py
```

This should generate all the 336 baseline experiments included in the original paper. Please note that due to the number of experiments included, we provide all the numerical results in a separate directory titled ```numerical_results```. However, execution of this code should allow for the re-creation of all the experiments if needed.
Please note that due to an inherent randomness of the process, some numerical results may be slightly different upon execution of the code. Although we have fixed seeds in many places, some elements are not entirely deterministic - e.g., the [PyTorch library may offer varied reproducibility.](https://pytorch.org/docs/stable/notes/randomness.html).
