import click
import csv
import os
import sqlite_utils

@click.command()
@click.argument(
    "export_file",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
def cli(export_file):
    "Convert exported CSV from Visible app to a SQLite DB"
    db_path = "./visible.db"
    db = sqlite_utils.Database(db_path)
    click.echo('opening csv')
    with open(export_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            click.echo('row')
            click.echo(row)

if __name__ == '__main__':
    cli()