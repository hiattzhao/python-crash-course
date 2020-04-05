class Settings():
  """A class to store all settings"""
  def __init__(self):
    """Initialize the game settings"""
    #screen settings
    self.screen_width = 1000
    self.screen_height = 600
    self.bg_color = (230, 230, 230)

    #ship settings
    self.ship_speed_factor = 1.5
