# RotorHazard Minidrone Plugin

This repository contains the ranking plugin for [La Lligueta](http://lalligueta.com/). The plugin introduces a custom ranking method based on the last heat positions.

## Installation

To install the La Lligueta Plugin in RotorHazard, follow these steps:

1. **Clone the Repository**:
   Ensure you have the RotorHazard repository cloned on your system. Navigate to the `plugins` directory within the RotorHazard source folder.

   ```bash
   cd /path/to/RotorHazard/src/server/plugins
   ```

2. **Copy the Plugin**:
   Clone the repo into the `plugins` directory.

   ```bash
   git clone https://github.com/JosepBC/lalligueta_ranking_plugin.git
   ```

3. **Restart RotorHazard**:
   Restart the RotorHazard server to load the new plugin.

   ```bash
   cd /path/to/RotorHazard/src/server
   python server.py
   ```

4. **Verify Installation**:
   Check the RotorHazard logs to ensure the plugin is initialized correctly. You should see a log entry similar to:

   ```
   Loaded plugin 'lalligueta_heatgenerator_balanced_ranking'
   ```

## Usage

The Minidrone Plugin introduces a custom ranking method called **"Class Ranking—La Lligueta - Last Heat Position"**. This ranking method processes heats to generate a leaderboard based on the following logic:

1. **Reverse Heat Order**:
   The heats are processed in reverse order, starting from the last heat (top pilots).

2. **Generate Leaderboard**:
   The plugin consolidates the results of all heats into a single leaderboard.

3. **Group by Heat**:
   The leaderboard is grouped by heat to facilitate comparisons between pilots in adjacent heats.

4. **Pilot Swapping**:
   Pilot swapping happens on all race classes but last one. As race classification is based on result of last class.
   Pilots are swapped between heats based on the following conditions:
   - If current and next heat are of 3 pilots exchange last pilot of current heat with first of next heat.
   - Otherwise, swap last pilot of current heat with P2 of next heat and second to last pilot of current heat is P1 of next heat

5. **Flatten Leaderboard**:
   The grouped leaderboard is flattened back into a single list for final ranking.

### Steps to Use the Plugin

1. **Enable the Ranking Method**:
   In the RotorHazard interface, select the race class you want to apply the ranking method to.

2. **Run a Race**:
   Conduct races as usual. The plugin will automatically process the results using the custom ranking method.

3. **View Results**:
   The leaderboard will display the rankings based on the logic described above.

### Additional Logging Details

The plugin now logs the following during the ranking process:
- If it's going to swap or not pilots
- Pilot swaps, including callsigns and reasons for swapping

## Logging

The plugin logs detailed information during the ranking process, including:
- Heat results
- Leaderboard transformations
- Pilot swaps

Logs can be found in the RotorHazard log files, typically located in the `logs/` directory.

## Contributing

Contributions to the La Lligueta Plugin are welcome! Feel free to submit issues or pull requests to improve the functionality or add new features.

## License

This plugin is licensed under the MIT License. See the `LICENSE` file for details.
