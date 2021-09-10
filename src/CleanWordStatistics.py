## make src dir avlb for cmd operation
import sys
from pathlib import Path
src_dir_location = Path(__file__).parents[1]
sys.path.append(str(src_dir_location))
from src.Model.WordStatistics import WordStatistics

ws = WordStatistics.WordStatistics('DEFAULT')
ws.empty_statistics()