import os

from smarts.sstudio import gen_traffic, gen_missions
from smarts.sstudio.types import (
    Traffic,
    Flow,
    Route,
    RandomRoute,
    TrafficActor,
    Mission,
)

scenario = os.path.dirname(os.path.realpath(__file__))
<<<<<<< HEAD
'''
    Mission(Route(begin=("edge-north-NS", 0, 10), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-west-WE", 0, 10), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 20), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 40), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 30), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 60), end=("edge-south-NS", (0,), 10))), '''
agent_missions = [
    
    Mission(Route(begin=("edge-north-NS", 0, 11), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-north-NS", 0, 4), end=("edge-west-EW", (0,), 5))),
    Mission(Route(begin=("edge-east-EN", 0, 60), end=("edge-west-EW", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 50), end=("edge-south-NS", (0,), 14))),
    Mission(Route(begin=("edge-east-EN", 0, 10), end=("edge-north-SN", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 20), end=("edge-west-EW", (0,), 14))),

=======

agent_missions = [
    Mission(Route(begin=("edge-north-NS", 0, 10), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-west-WE", 0, 10), end=("edge-south-NS", (0,), 10))),
    Mission(Route(begin=("edge-east-EN", 0, 20), end=("edge-south-NS", (0,), 10))),
>>>>>>> f1cbdea80b74be8e93abea99fff8f31e15544f09
]

gen_missions(scenario, agent_missions, overwrite=True)

gen_traffic(
    scenario,
    Traffic(
        flows=[
            Flow(
                route=RandomRoute(), rate=3600, actors={TrafficActor(name="car"): 1.0},
            )
        ]
    ),
    name="random",
    overwrite=True,
)
