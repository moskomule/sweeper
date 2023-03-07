import dataclasses
import itertools
import re
import subprocess
import sys


@dataclasses.dataclass
class Regex:
    val: str

    def __eq__(self, regex_pattern) -> bool:
        return re.match(regex_pattern, self.val) is not None


def task_list(args: list[str]) -> list[list[str]]:
    """
    args: ["sbatch", "batch.sh", "--seed", "[1-3]", "--dataset", "[cifar10,cifar100,svhn]"]
    output: [["sbatch", "batch.sh", "--seed", "1", "--dataset", "cifar10"], ...]
    """

    fixed_args = []
    variable_args = []
    for arg in args:
        match Regex(arg):
            case r"\[\d\-\d\]":
                # [1-3]
                start, end = re.match(r"\[(\d)\-(\d)\]", arg).groups()
                arg = [str(i) for i in range(int(start), int(end) + 1)]
                variable_args.append(arg)
                fixed_args.append(None)
            case r"\[.+\,.+\]":
                # [1,2,3]
                # [cifar10,cifar100,svhn]
                arg = arg[1:-1].split(",")
                variable_args.append(arg)
                fixed_args.append(None)
            case _:
                variable_args.append([None])
                fixed_args.append(arg)

    outputs = []
    for comb_args in itertools.product(*variable_args):
        outputs.append([f or v for f, v in zip(fixed_args, comb_args)])

    return outputs


def main():
    args = sys.argv  # ['sweeper', 'sbatch', ...] or ['sweeper', '--', 'sbatch', ...]
    launcher_id = 1
    for i, arg in enumerate(args):
        if arg == "--":
            launcher_id = i + 1

    tasks = task_list(args[launcher_id:])
    print(">>> Submitting jobs...")
    for task in tasks:
        print(' '.join(task))
        subprocess.run(task, check=True)

    print(f">>> Submit {len(tasks)} jobs!")


if __name__ == '__main__':
    main()
