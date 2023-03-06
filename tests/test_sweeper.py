from sweeper.sweeper import task_list


def test_task_list():
    outputs = task_list(["sbatch", "batch.sh", "--seed", "[1-3]",
                         "--gpu", "[2,4,8]", "--dataset", "[cifar10,cifar100]"])

    assert outputs[0] == ["sbatch", "batch.sh", "--seed", "1", "--gpu", "2", "--dataset", "cifar10"]
    assert outputs[-1] == ["sbatch", "batch.sh", "--seed", "3", "--gpu", "8", "--dataset", "cifar100"]
