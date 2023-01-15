from tox.plugin import impl
from tox.tox_env.python.virtual_env.runner import VirtualEnvRunner
from tox.tox_env.register import ToxEnvRegister


class ExampleVirtualEnvRunner(VirtualEnvRunner):
    @staticmethod
    def id() -> str:
        return "example"

    @property
    def env_name(self):
        name = super().env_name
        print(f"ExampleVirtualEnvRunner: name={name}")


@impl
def tox_register_tox_env(register: ToxEnvRegister) -> None:
    register.add_run_env(ExampleVirtualEnvRunner)

