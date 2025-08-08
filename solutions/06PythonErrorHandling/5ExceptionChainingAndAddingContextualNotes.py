configs = [
    {'database': {'host': 'localhost', 'port': 5432}},
    {'database': {'host': 'localhost'}}, # Missing port key
    {'database': {'host': 'localhost', 'port': 'bad_port'}} # Invalid port value
]

class ConfigError(Exception):
    pass

def get_db_port(config: dict):
    port_val = ""
    try: 
        port_val = config['database']['port']
        port_val = int(port_val)
    except KeyError as e:
        raise ConfigError('Configuration key missing') from e
    except ValueError as e:
        e.add_note(f"Invalid port value found: '{port_val}'")
        raise e

for config in configs:
    try:
        get_db_port(config)
    except ConfigError as e:
        print(f"Config Error: {e}")
        print(f"First degree cause {e.__cause__}\n")
    except ValueError as e:
        print(f"Value Error: {e}")
        print(f"Additional notes from traceback {e.__notes__}")