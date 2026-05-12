"""Allow the module to be run as a CLI. I.e.:

.. code-block:: shell-session

    $ python -m cli
"""

if __name__ == "__main__":
    from cli.cli_code import my_cli

    my_cli()
