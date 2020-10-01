import click

from neoload_cli_lib import user_data, tools
import logging

@click.command()
def cli():
    """get status of NeoLoad cli Settings"""
    login = user_data.get_user_data(False)
    if login is None:
        print("No settings is stored. Please use \"neoload login\" to start.")
    else:
        print(login)

        environ = {}
        environ["interactive_implied"] = tools.is_user_interactive_implied()
        environ["interactive_environment_set"] = tools.get_user_interactive_value()
        environ["interactive_effective"] = tools.is_user_interactive()
        logging.debug(environ)
