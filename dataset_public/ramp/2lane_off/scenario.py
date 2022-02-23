import os
<<<<<<< HEAD
import random
=======

>>>>>>> f1cbdea80b74be8e93abea99fff8f31e15544f09
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

agent_missions = [
    Mission(Route(begin=("left_in", 1, 20), end=("right_out", (0,), 40))),
    Mission(Route(begin=("left_in", 1, 40), end=("off_ramp", (0,), 40))),
    Mission(Route(begin=("left_in", 0, 20), end=("off_ramp", (0,), 40))),
    Mission(Route(begin=("left_in", 0, 50), end=("right_out", (0,), 40))),
]

gen_missions(scenario, agent_missions, overwrite=True)

gen_traffic(
    scenario,
    Traffic(
        flows=[
            Flow(
<<<<<<< HEAD
                 route=RandomRoute(), rate=3600, actors={TrafficActor(name="car",
                vehicle_type=random.choice(
                        ["coach", "truck"]
                    ),
                ): 1.0},
=======
                route=RandomRoute(), rate=3600, actors={TrafficActor(name="car"): 1.0},
>>>>>>> f1cbdea80b74be8e93abea99fff8f31e15544f09
            )
        ]
    ),
    name="random",
    overwrite=True,
)
