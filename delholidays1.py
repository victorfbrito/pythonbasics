import numpy as np
import pandas as pd
import holidays
import datetime
from datetime import datetime

for date in holidays.Argentina(years=datetime.now().year).items():
  print(date)