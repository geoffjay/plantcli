import click
from rich import print

from plant.utils.messages import highlight, info


@click.command()
@click.option("--id", default="org.plantd.Cli")
@click.option("--broker", default="tcp://localhost:7200")
@click.pass_obj
def client(plant, id, broker):
    if plant.debug:
        print(info("Initializing plantd broker client..."))
    print(f"Attaching client with ID {highlight(id)} to the broker at {broker}")
