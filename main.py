from plant.cli import cli


def patched_main():
    cli()


if __name__ == "__main__":
    patched_main()
