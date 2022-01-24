import click
import gi
from rich import print

from plant.utils.messages import highlight, info

gi.require_version("Pd", "1.0")

from gi.repository import Pd


@click.group()
@click.option("--broker", "-b", default="tcp://localhost:7200", show_default=True)
@click.pass_obj
def client(plant, broker):
    if plant.debug:
        print(info("Initializing plantd broker client..."))
    print(f"Attaching client to the broker at {broker}")
    plant.client = Pd.Client.new(broker)
    plant.broker_endpoint = broker


@client.command()
@click.option("--module-id", "-m", default="org.plantd.Cli", show_default=True)
@click.option("--job-id", required=True)
@click.option("--job-value", default="")
@click.option("--job-properties", multiple=True, default=[], help="List of properties in the form key=value.")
@click.pass_obj
def submit_job(plant, module_id, job_id, job_value, job_properties):
    if plant.client and plant.debug:
        print(info("client is valid"))
    request = Pd.JobRequest()
    request.set_id(module_id)
    request.set_job_id(job_id)
    request.set_job_value(job_value)
    for property in job_properties:
        try:
            key, value = property.split("=")
        except ValueError:
            raise Exception("job properties were provided incorrectly")
        request.add(Pd.Property.new(key, value))
    plant.client.send_request(module_id, "submit-job", request.serialize())
    print(plant.client.recv_response())
