import os

data_configs = {
    "MNIST_nonoverlaping_balanced_15": {
    "dataset_name" : "mnist",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "MNIST_nonoverlaping_balanced_30": {
    "dataset_name" : "mnist",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "MNIST_nonoverlaping_imbalanced_15": {
    "dataset_name" : "mnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "MNIST_nonoverlaping_imbalanced_30": {
    "dataset_name" : "mnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
   "MNIST_overlaping_balanced_15": {
    "dataset_name" : "mnist",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "MNIST_overlaping_balanced_30": {
    "dataset_name" : "mnist",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "MNIST_overlaping_imbalanced_15":{
    "dataset_name" : "mnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "MNIST_overlaping_imbalanced_30": {
    "dataset_name" : "mnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "FMNIST_nonoverlaping_balanced_15": {
    "dataset_name" : "fmnist",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "FMNIST_nonoverlaping_balanced_30": {
    "dataset_name" : "fmnist",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "FMNIST_nonoverlaping_imbalanced_15": {
    "dataset_name" : "fmnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "FMNIST_nonoverlaping_imbalanced_30": {
    "dataset_name" : "fmnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
   "FMNIST_overlaping_balanced_15": {
    "dataset_name" : "fmnist",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "FMNIST_overlaping_balanced_30": {
    "dataset_name" : "fmnist",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "FMNIST_overlaping_imbalanced_15":{
    "dataset_name" : "fmnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "FMNIST_overlaping_imbalanced_30": {
    "dataset_name" : "fmnist",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "CIFAR10_nonoverlaping_balanced_15": {
    "dataset_name" : "cifar10",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "CIFAR10_nonoverlaping_balanced_30": {
    "dataset_name" : "cifar10",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "CIFAR10_nonoverlaping_imbalanced_15": {
    "dataset_name" : "cifar10",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
    "CIFAR10_nonoverlaping_imbalanced_30": {
    "dataset_name" : "cifar10",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7, 8, 9], # 0, 1, 2, 3 present only
            2: [0, 1, 2, 3, 7, 8, 9], # 4, 5, 6 present only
            3: [0, 1, 2, 3, 4, 5, 6] # 7, 8, 9 present only
        }
    },
   "CIFAR10_overlaping_balanced_15": {
    "dataset_name" : "cifar10",
    "split_type" : "missing_classes_clustered",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4],
            2: [5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "CIFAR10_overlaping_balanced_30": {
    "dataset_name" : "cifar10",
    "split_type" : "missing_classes_clustered",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            3: [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "CIFAR10_overlaping_imbalanced_15":{
    "dataset_name" : "cifar10",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 15,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 15,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2],
            2: [3, 4, 5, 6, 7, 8, 9],
            3: [10, 11, 12, 13, 14]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    },
   "CIFAR10_overlaping_imbalanced_30": {
    "dataset_name" : "cifar10",
    "split_type" : "dirchlet_clusters_nooverlap",
    "shards": 30,
    "local_test_size": 0.3,
    "transformations": {},
    "imbalanced_clients": {},
    "save_dataset": True,
    "save_transformations": True,
    "save_blueprint": True,
    "agents": 30,
    "shuffle": True,
    "alpha": 1,
    "allow_replace": True,
    "save_path": os.getcwd(),
    "agents_cluster_belonging":
        {
            1: [0, 1, 2, 3, 4, 5, 6],
            2: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            3: [21, 22, 23, 24, 25, 26, 27, 28, 29]
        },
    "missing_classes":
        {
            1: [4, 5, 6, 7], # 0, 1, 2, 3, 8, 9 present only
            2: [0, 1, 2, 3], # 4, 5, 6, 7, 8, 9 present only
            3: [6, 7, 8, 9] # 0, 1, 2, 3, 4, 5 present only
        }
    }
}