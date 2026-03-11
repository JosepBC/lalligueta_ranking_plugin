import logging
from eventmanager import Evt
from Results import RaceClassRankMethod
from .swap_pilots import swap_on_grouped_board

logger = logging.getLogger(__name__)

def register_handlers(args):
    args['register_fn'](
        RaceClassRankMethod(
            "La Lligueta - Last Heat Position",
            rank_heat_pos_and_time,
            None,
            None
        )
    )

def rank_heat_pos_and_time(rhapi, race_class, _args):
    """
    Processes the heats to generate a ranking based on the last heat positions and lap times.

    Args:
        rhapi: The API object for accessing race data.
        race_class: The race class object containing class information.
        _args: Additional arguments (not used).

    Returns:
        tuple: A ranked list of pilots and metadata for the leaderboard.
    """

    logger.info("Starting ranking process for heats")

    heats = rhapi.db.heats_by_class(race_class.id)
    # Reverse the heats to start from the last heat aka the top pilots
    reversed_heats = list(reversed(heats))

    # Initialize the leaderboard
    leaderboard = []

    # Iterate over all heats in reverse order and generate the leaderboard
    for heat in reversed_heats:
        heat_result = rhapi.db.heat_results(heat)
        if not heat_result: # No heat result available as are pending
            logger.info(f"No heat_result for heat: {heat.display_name}, skipping.")
            continue
        leaderboard_type = heat_result['meta']['primary_leaderboard']
        heat_leaderboard = heat_result[leaderboard_type]

        # Append the heat leaderboard to the consolidated leaderboard
        append_to_leaderboard(leaderboard, heat, heat_leaderboard)

    grouped_leaderboard = group_by_heat(leaderboard)

    # Don't swap pilots for last raceclass
    if rhapi.db.raceclasses[-1].id == race_class.id:
        logger.info("Not swapping pilots as it's last class")
        temp_leaderboard = grouped_leaderboard
    else:
        logger.info("Swapping pilots")
        temp_leaderboard = swap_on_grouped_board(grouped_leaderboard, logger)

    # Flatten the grouped leaderboard back to a single list
    leaderboard = [item for sublist in temp_leaderboard for item in sublist]
    # Correctly assign positions so they make sense
    pos = 1
    for pilot in leaderboard:
        pilot['position'] = pos
        pos += 1

    meta = {
        'rank_fields': [{
            'name': 'heat',
            'label': "Heat"
        },{
            'name': 'heat_rank',
            'label': "Heat Position"
        },{
            'name': 'total_time',
            'label': "Total time"
        },{
            'name': 'laps',
            'label': "Laps"
        }]
    }

    logger.info("Ranking process completed")
    return leaderboard, meta
    
def initialize(rhapi):
    logger.info("Initializing MINIDRONE plugin")
    rhapi.events.on(Evt.CLASS_RANK_INITIALIZE, register_handlers)

def append_to_leaderboard(leaderboard, heat, heat_leaderboard):
    """
    Appends the pilot data to the leaderboard.

    Args:
        leaderboard (list): The leaderboard to append to.
        heat (object): The heat object containing heat information.
        line (dict): The pilot data to append.

    Returns:
        None
    """
    for line in heat_leaderboard:
        rank_pos = heat_leaderboard.index(line) + 1
        leaderboard.append({
            'pilot_id': line['pilot_id'],
            'callsign': line['callsign'],
            'team_name': line['team_name'],
            'heat': heat.display_name,
            'heat_rank': line['position'],
            'position': rank_pos,
            'fastest_lap': line['fastest_lap'],
            'laps': line['laps'],
            'total_time': line['total_time']
        })

def group_by_heat(leaderboard):
    """
    Groups the leaderboard by heat and transforms it into a list of lists.

    Args:
        leaderboard (list): The leaderboard to group.

    Returns:
        list: A list of lists of grouped leaderboard entries.
    """
    grouped = {}

    # Group the leaderboard by heat
    for entry in leaderboard:
        heat_name = entry['heat']
        if heat_name not in grouped:
            grouped[heat_name] = []
        grouped[heat_name].append(entry)

    # Convert grouped dictionary to a list of lists
    result = list(grouped.values())

    return result

