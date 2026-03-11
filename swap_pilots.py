def swap_on_grouped_board(grouped_leaderboard, logger):
    """
    Swaps the last pilot of a heat with the first pilot of the next heat based on conditions.

    Args:
        grouped_leaderboard (list): An array of arrays representing grouped leaderboard entries.

    Returns:
        list: The updated grouped leaderboard after performing swaps.
    """
    for i in range(len(grouped_leaderboard) - 1):
        current_heat = grouped_leaderboard[i]
        next_heat = grouped_leaderboard[i + 1]

        logger.info(f"Current heat size: {len(current_heat)}")
        logger.info(f"Next heat size: {len(next_heat)}")
        # If any both heats are of 3 pilots only echange last with first
        if len(current_heat) == 3 and len(next_heat) == 3:
            logger.info(f"Will swap last pilot of current heat {current_heat[-1]['callsign']} with first pilot of next heat {next_heat[0]['callsign']}")
            current_heat[-1], next_heat[0] = next_heat[0], current_heat[-1]
        else:
            # If source or destination groups are of more than 3 pilots:
            # Swap with the following logic:
            # Last pilot of current heat is P2 of next heat
            # Second to last pilot of current heat is P1 of next heat
            # First pilot of next heat is second to last of current heat
            # Second pilot of next heat is last of current heat
            logger.info(f"Will swap last pilot of current heat {current_heat[-1]['callsign']} with second pilot of next heat {next_heat[1]['callsign']}")
            logger.info(f"Will swap second to last pilot of current heat {current_heat[-2]['callsign']} with first pilot of next heat {next_heat[0]['callsign']}")
            current_heat[-1], current_heat[-2], next_heat[0], next_heat[1] = next_heat[1], next_heat[0], current_heat[-2], current_heat[-1]

    return grouped_leaderboard
