import datetime

from ogame import constants
from ogame import OGame


def queue(ID: int, empire: OGame):
    mines = empire.supply(ID)
    factory = empire.facilities(ID)
    research = empire.research(ID)
    ships = empire.ships(ID)
    resources = empire.resources(ID)
    defences = empire.defences(ID)
    celestial_queue = empire.celestial_queue(ID)

    class Order:
        def __init__(self, build, condition):
            self.build: tuple = build
            self.condition: bool = condition

    return [
        # Supply
        Order(
            build=constants.buildings.solar_plant,
            condition=(
                    resources.energy < 0
                    and mines.solar_plant.level < 30
                    and mines.solar_plant.is_possible
            )
        ),
        Order(
            build=constants.buildings.crystal_mine,
            condition=(
                    mines.crystal_mine.level < 25
                    and mines.crystal_mine.is_possible
            )
        ),
        Order(
            build=constants.buildings.metal_mine,
            condition=(
                    mines.metal_mine.level < 25
                    and mines.metal_mine.is_possible
            )
        ),
        Order(
            build=constants.buildings.deuterium_mine,
            condition=(
                    mines.deuterium_mine.level < 15
                    and mines.deuterium_mine.is_possible
            )
        ),
        Order(
            build=constants.buildings.fusion_plant,
            condition=(
                    resources.energy < 0
                    and mines.fusion_plant.level < 15
                    and mines.fusion_plant.is_possible
            )
        ),
        Order(
            build=constants.buildings.solar_satellite(1),
            condition=(
                    resources.energy < 0
                    and ships.solarSatellite.is_possible
                    and ships.solarSatellite.amount < 100
            )
        ),

        # Facilities
        Order(
            build=constants.buildings.robotics_factory,
            condition=(
                factory.robotics_factory.level <= 15
                and factory.robotics_factory.is_possible
            )
        ),
        Order(
            build=constants.buildings.shipyard,
            condition=(
                factory.shipyard.level < 14
                and factory.shipyard.is_possible
            )
        ),
        Order(
            build=constants.buildings.research_laboratory,
            condition=(
                factory.research_laboratory.level < 14
                and factory.research_laboratory.is_possible
            )
        ),
        Order(
            build=constants.buildings.nanite_factory,
            condition=(
                    factory.nanite_factory.level < 6
                    and factory.nanite_factory.is_possible
            )
        ),
        Order(
            build=constants.buildings.missile_silo,
            condition=(
                    factory.missile_silo.level < 9
                    and factory.missile_silo.is_possible
            )
        ),

        # Research
        Order(
            build=constants.research.espionage,
            condition=(
                    research.espionage.is_possible
                    and research.espionage.level < 8
            )
        ),
        Order(
            build=constants.research.computer,
            condition=(
                    research.computer.is_possible
                    and research.espionage.level < 10
            )
        ),
        Order(
            build=constants.research.weapons,
            condition=(
                    research.weapons.is_possible
                    and research.weapons.level < 3
            )
        ),
        Order(
            build=constants.research.shielding,
            condition=(
                    research.shielding.is_possible
                    and research.shielding.level < 6
            )
        ),
        Order(
            build=constants.research.armor,
            condition=(
                    research.armor.is_possible
                    and research.armor.level < 2
            )
        ),
        Order(
            build=constants.research.energy,
            condition=(
                    research.energy.is_possible
                    and research.energy.level < 12
            )
        ),
        Order(
            build=constants.research.hyperspace,
            condition=(
                    research.hyperspace.is_possible
                    and research.hyperspace.level < 8
            )
        ),
        Order(
            build=constants.research.combustion_drive,
            condition=(
                    research.combustion_drive.is_possible
                    and research.combustion_drive.level < 6
            )
        ),
        Order(
            build=constants.research.impulse_drive,
            condition=(
                    research.impulse_drive.is_possible
                    and research.impulse_drive.level < 17
            )
        ),
        Order(
            build=constants.research.hyperspace_drive,
            condition=(
                    research.hyperspace_drive.is_possible
                    and research.hyperspace_drive.level < 15
            )
        ),
        Order(
            build=constants.research.laser,
            condition=(
                    research.laser.is_possible
                    and research.laser.level < 12
            )
        ),
        Order(
            build=constants.research.ion,
            condition=(
                    research.ion.is_possible
                    and research.ion.level < 5
            )
        ),
        Order(
            build=constants.research.plasma,
            condition=(
                    research.plasma.is_possible
                    and research.plasma.level < 7
            )
        ),
        Order(
            build=constants.research.research_network,
            condition=(
                    research.research_network.is_possible
                    and research.research_network.level < empire.slot_celestial().total
            )
        ),
        Order(
            build=constants.research.astrophysics,
            condition=research.astrophysics.is_possible
        ),
        Order(
            build=constants.research.graviton,
            condition=(
                    research.graviton.is_possible
                    and research.graviton.level < 1
            )
        ),

        # Fleet
        Order(
            build=constants.ships.colonyShip(),
            condition=(
                ships.colonyShip.amount == 0
                and ships.colonyShip.is_possible
                and 0 < empire.slot_celestial().free
            )
        ),

        # Resources
        Order(
            build=constants.buildings.metal_storage,
            condition=(
                    mines.metal_storage.level < 14
                    and mines.metal_storage.is_possible
            )
        ),
        Order(
            build=constants.buildings.crystal_storage,
            condition=(
                    mines.crystal_storage.level < 10
                    and mines.crystal_storage.is_possible
            )
        ),
        Order(
            build=constants.buildings.deuterium_storage,
            condition=(
                    mines.deuterium_storage.level < 11
                    and mines.deuterium_storage.is_possible
            )
        ),

        # Defences
        Order(
            build=constants.buildings.shield_dome_small(),
            condition=defences.shield_dome_small.is_possible
        ),
        Order(
            build=constants.buildings.shield_dome_large(),
            condition=defences.shield_dome_large.is_possible
        ),
        Order(
            build=constants.buildings.rocket_launcher(100),
            condition=(
                defences.rocket_launcher.is_possible
                and 4 < factory.shipyard.level
                and celestial_queue.shipyard < datetime.datetime.now()
                and defences.rocket_launcher.amount < 1000
            )
        ),
        Order(
            build=constants.buildings.laser_cannon_light(100),
            condition=(
                    defences.laser_cannon_light.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 4 < factory.shipyard.level
                    and defences.laser_cannon_light.amount < 1000
            )
        ),
        Order(
            build=constants.buildings.laser_cannon_heavy(100),
            condition=(
                    defences.laser_cannon_heavy.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 4 < factory.shipyard.level
                    and defences.laser_cannon_heavy.amount < 400
            )
        ),
        Order(
            build=constants.buildings.gauss_cannon(10),
            condition=(
                    defences.gauss_cannon.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 8 < factory.shipyard.level
                    and defences.gauss_cannon.amount < 100
            )
        ),
        Order(
            build=constants.buildings.ion_cannon(10),
            condition=(
                    defences.ion_cannon.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 8 < factory.shipyard.level
                    and defences.ion_cannon.amount < 100
            )
        ),
        Order(
            build=constants.buildings.plasma_cannon(5),
            condition=(
                    defences.plasma_cannon.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 10 < factory.shipyard.level
                    and defences.laser_cannon_heavy.amount < 40
            )
        ),
        Order(
            build=constants.buildings.missile_interceptor(5),
            condition=(
                    defences.missile_interceptor.is_possible
                    and celestial_queue.shipyard < datetime.datetime.now()
                    and 1 < factory.shipyard.level
                    and 0 < factory.missile_silo.level
                    and defences.missile_interceptor.amount < 60
            )
        ),
    ]
