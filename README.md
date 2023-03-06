# sweeper

![pytest](https://github.com/moskomule/sweeper/workflows/pytest/badge.svg)

A simple hyperparameter sweeper written in Python. For example,

```commandline
sweeper -- sbatch batchjob.sh --seed [1-3] --dataset [cifar10,cifar100,svhn]
```

internally runs

```commandline
sbatch batchjob.sh --seed 1 --dataset cifar10
sbatch batchjob.sh --seed 1 --dataset cifar100
...
sbatch batchjob.sh --seed 3 --dataset svhn
```

## Installation

```commandline
pip install -U git+https://github.com/moskomule/sweeper
```

Also installable with `pipx` (recommended).