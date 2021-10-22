class Constants:
    # Environment
    water_volume = 200 # liters
    ambient_temperature = 15 # degrees celsius
    start_temperature = 20 # degrees celsius
    environment_interval = 1 # seconds

    # Heater
    heater_delta = 0.14

    # Sensor
    sensor_delta = 0.07

    # Controller
    max_output_power = 1200 # W

    # Topics
    topic_stimuli  = 'stimuli'
    topic_percepts = 'percepts'
    topic_commands = 'commands'
    topic_actions  = 'actions'
    topic_setpoint = 'setpoint'